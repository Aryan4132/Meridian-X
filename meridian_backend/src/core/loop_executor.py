"""
loop_executor.py — Tool execution auditing, syntax critique & healing, and history pruning.
"""

import re
import ast
import json
import time
import inspect
from typing import Dict, Any, List, Tuple, Optional
import ollama

from src.tools.registry import call_tool, TOOL_REGISTRY
from database import add_to_task_log, get_auditor_model, ingest_into_knowledge_base
from src.core.bus import event_bus


def clean_final_text(text: str) -> str:
    """Safely extracts the final message and removes XML-like agent loop tags."""
    text = re.sub(r"<thought>.*?</thought>", "", text, flags=re.DOTALL)
    text = re.sub(r"<call:\w+>.*?</call:\w+>", "", text, flags=re.DOTALL)
    text = re.sub(r"</?thought>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"</?finish>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"</?call:\w+>", "", text, flags=re.IGNORECASE)
    return text.strip()


def critique_and_correct_tool_call(tool_name: str, args_str: str, client: ollama.Client, model_source: str = "local") -> Tuple[bool, str, str]:
    """Inspects tool signature and code blocks locally/cloud to auto-correct errors."""
    try:
        if tool_name not in TOOL_REGISTRY:
            return False, args_str, f"Unknown tool '{tool_name}' requested."
            
        tool_meta = TOOL_REGISTRY[tool_name]
        func = tool_meta["func"]
        
        try:
            args = json.loads(args_str) if args_str.strip() else {}
        except Exception as e:
            prompt = (
                f"You are a syntax recovery engine. Correct the following invalid JSON arguments for tool '{tool_name}' so it is well-formed.\n"
                f"Invalid JSON:\n{args_str}\n\n"
                f"Output ONLY the corrected JSON string. Do not include markdown code block syntax."
            )
            try:
                from src.core.llm_provider import call_llm_sync
                corrected = call_llm_sync([{"role": "user", "content": prompt}], model=get_auditor_model()).strip()
                if corrected.startswith("```"):
                    corrected = corrected.strip("`").replace("json\n", "").strip()
                json.loads(corrected)
                return True, corrected, "Auto-corrected malformed JSON arguments."
            except Exception:
                return False, args_str, f"Malformed JSON arguments for tool '{tool_name}': {e}"

        # 1. Tool Signature Verification
        try:
            sig = inspect.signature(func)
            has_var_positional = any(p.kind == inspect.Parameter.VAR_POSITIONAL for p in sig.parameters.values())
            has_var_keyword = any(p.kind == inspect.Parameter.VAR_KEYWORD for p in sig.parameters.values())

            required_params = []
            valid_params = set()

            for param_name, param in sig.parameters.items():
                if param.kind in (inspect.Parameter.POSITIONAL_OR_KEYWORD, inspect.Parameter.KEYWORD_ONLY):
                    valid_params.add(param_name)
                    if param.default == inspect.Parameter.empty:
                        required_params.append(param_name)

            PARAM_ALIASES = {
                "filepath": "path", "file_path": "path", "filename": "path", "TargetFile": "path",
                "command_str": "command", "cmd": "command",
                "query_str": "query", "search_term": "query",
                "content_str": "content", "CodeContent": "content"
            }
            remapped = False
            for p in list(args.keys()):
                if p not in valid_params and p in PARAM_ALIASES:
                    canonical = PARAM_ALIASES[p]
                    if canonical in valid_params and canonical not in args:
                        args[canonical] = args.pop(p)
                        remapped = True
                        break

            if remapped:
                args_str = json.dumps(args)

            missing = [p for p in required_params if p not in args]
            unexpected = [p for p in args if p not in valid_params] if not has_var_keyword else []

            if missing or unexpected:
                sig_err_msg = ""
                if missing:
                    sig_err_msg += f"Missing required parameter(s): {', '.join(missing)}. "
                if unexpected:
                    sig_err_msg += f"Unexpected parameter(s): {', '.join(unexpected)}."

                prompt = (
                    f"You are a signature matching assistant. The tool '{tool_name}' has the following expected parameter signature:\n"
                    f"Signature: {str(sig)}\n"
                    f"The provided arguments were:\n{json.dumps(args)}\n"
                    f"Validation Error: {sig_err_msg}\n\n"
                    f"Correct or map the keys in the arguments to match the expected signature. Output ONLY the corrected JSON string. Do not include markdown code block syntax."
                )
                try:
                    from src.core.llm_provider import call_llm_sync
                    corrected = call_llm_sync([{"role": "user", "content": prompt}], model=get_auditor_model()).strip()
                    if corrected.startswith("```"):
                        corrected = corrected.strip("`").replace("json\n", "").strip()

                    corrected_args = json.loads(corrected)
                    missing_corr = [p for p in required_params if p not in corrected_args]
                    unexpected_corr = [p for p in corrected_args if p not in valid_params] if not has_var_keyword else []
                    if not missing_corr and not unexpected_corr:
                        return True, json.dumps(corrected_args), f"Auto-corrected parameter signature: {sig_err_msg}"
                except Exception:
                    pass

                return False, args_str, f"Signature validation failed: {sig_err_msg} Expected: {str(sig)}"
        except ValueError:
            pass

        # 2. Code Syntax Verification & LLM Linting
        code_to_validate = None
        code_type = None
        
        if tool_name in ["run_python", "create_dynamic_tool"]:
            code_to_validate = args.get("code", "")
            code_type = "python"
        elif tool_name == "write_file":
            path = args.get("path", "") or args.get("filepath", "") or args.get("TargetFile", "")
            content = args.get("content", "") or args.get("CodeContent", "")
            if path.endswith(".py"):
                code_to_validate = content
                code_type = "python"
            elif path.endswith(".json"):
                code_to_validate = content
                code_type = "json"

        if code_to_validate:
            if code_type == "python":
                try:
                    ast.parse(code_to_validate)
                except SyntaxError as se:
                    prompt = (
                        f"You are a code-healing assistant. The following Python code contains a syntax error:\n"
                        f"Error: {se}\n\n"
                        f"Code:\n```python\n{code_to_validate}\n```\n\n"
                        f"Rewrite the code to fix the syntax error. Output ONLY the raw corrected Python code, no explanation, no markdown blocks."
                    )
                    try:
                        from src.core.llm_provider import call_llm_sync
                        corrected_code = call_llm_sync([{"role": "user", "content": prompt}], model=get_auditor_model()).strip()
                        if corrected_code.startswith("```"):
                            corrected_code = corrected_code.strip("`").replace("python\n", "").strip()
                        
                        ast.parse(corrected_code)
                        if tool_name in ["run_python", "create_dynamic_tool"]:
                            args["code"] = corrected_code
                        elif tool_name == "write_file":
                            if "content" in args:
                                args["content"] = corrected_code
                            elif "CodeContent" in args:
                                args["CodeContent"] = corrected_code
                        return True, json.dumps(args), f"Auto-healed Python code syntax error on line {se.lineno}."
                    except Exception as se2:
                        return False, args_str, f"Python syntax check failed: {se} (Auto-healing also failed: {se2})"

                lint_prompt = (
                    f"You are a Python code linter. Analyze the following Python code for any logic errors, undefined names, incorrect method calls, or compiler warnings.\n"
                    f"Code:\n```python\n{code_to_validate}\n```\n\n"
                    f"If you find any critical compiler warnings or errors, list them clearly. If the code is perfect and contains no issues, respond with ONLY 'OK'. Do not explain if there are no errors."
                )
                try:
                    from src.core.llm_provider import call_llm_sync
                    lint_resp = call_llm_sync([{"role": "user", "content": lint_prompt}], model=get_auditor_model()).strip()
                    if "OK" not in lint_resp.upper() and len(lint_resp) > 5:
                        return False, args_str, f"Python Lint Warning: Compiler warning or logic error detected in code block:\n{lint_resp}"
                except Exception:
                    pass

            elif code_type == "json":
                try:
                    json.loads(code_to_validate)
                except Exception as e:
                    prompt = (
                        f"You are a syntax recovery engine. Correct the following invalid JSON content to make it well-formed.\n"
                        f"Invalid JSON:\n{code_to_validate}\n\n"
                        f"Output ONLY the corrected JSON string. Do not include markdown code block syntax."
                    )
                    try:
                        from src.core.llm_provider import call_llm_sync
                        corrected_code = call_llm_sync([{"role": "user", "content": prompt}], model=get_auditor_model()).strip()
                        if corrected_code.startswith("```"):
                            corrected_code = corrected_code.strip("`").replace("json\n", "").strip()

                        json.loads(corrected_code)
                        if "content" in args:
                            args["content"] = corrected_code
                        elif "CodeContent" in args:
                            args["CodeContent"] = corrected_code
                        return True, json.dumps(args), "Auto-corrected malformed JSON file content."
                    except Exception as e2:
                        return False, args_str, f"JSON syntax check failed: {e} (Auto-healing failed: {e2})"

        return True, args_str, ""
    except Exception as e:
        return False, args_str, f"Critique verification failed: {e}"


async def prune_and_compress_history(history: List[Dict[str, str]], client: ollama.Client, model_source: str = "local") -> List[Dict[str, str]]:
    """Prunes history if too long, summarizes older turns, and saves raw history to Turbovec RAG."""
    if len(history) <= 9:
        return history
        
    print(f"[Context Governor] Active history has {len(history)} turns. Compressing old segments...")
    
    compress_turns = history[1:-4]
    keep_turns = history[-4:]
    
    log_text = ""
    for idx, turn in enumerate(compress_turns):
        role_label = "Assistant" if turn["role"] == "assistant" else "User"
        log_text += f"{role_label}: {turn['content']}\n"
        
    prompt = (
        "You are an executive memory compressor. Synthesize the following sequence of assistant actions, "
        "commands executed, decisions, and observations into a concise bulleted summary of key facts and progress.\n\n"
        f"Sequence:\n{log_text}"
    )
    try:
        from src.core.llm_provider import call_llm
        summary = await call_llm([{"role": "user", "content": prompt}], model=get_auditor_model())
        summary = (summary or "").strip()
    except Exception:
        summary = "Older context consolidated by System."
        
    try:
        ingest_into_knowledge_base("archived_history", log_text, {"timestamp": time.time()})
        print(f"[Context Governor] Archived context segments ingested into Turbovec RAG.")
    except Exception as e:
        print(f"[Context Governor] RAG ingestion failed: {e}")
        
    new_history = [history[0]]
    new_history.append({"role": "user", "content": f"[SYSTEM — Context Archive]:\n{summary}"})
    new_history.extend(keep_turns)
    
    return new_history


def check_llm_tool_output_anomaly(tool_name: str, args: dict) -> Tuple[bool, str]:
    """Detects system directory targeting and dangerous execution anomalies before execution (SEC-26)."""
    args_str = json.dumps(args).lower().replace("\\\\", "/").replace("\\", "/")
    dangerous_targets = ["c:/windows", "/etc/shadow", "/etc/passwd", "/boot", "rm -rf /", "del /f /s /q c:"]
    for target in dangerous_targets:
        if target in args_str:
            from src.core.audit_logger import log_sensitive_action
            log_sensitive_action("SECURITY_VIOLATION", "llm_anomaly_blocked", {"tool_name": tool_name, "args": args}, "FAILED")
            return True, f"Error: Tool execution targeting sensitive system path or pattern '{target}' was blocked by Anomaly Detector (SEC-26)."
    return False, ""


async def execute_single_tool_async(
    tool_name: str, 
    args: dict, 
    tier: int, 
    client: ollama.Client, 
    active_model: str,
    model_source: str = "local"
) -> Tuple[str, str, str]:
    """Helper to run security auditor checks and execute tool asynchronously."""
    is_anomaly, anomaly_err = check_llm_tool_output_anomaly(tool_name, args)
    if is_anomaly:
        return anomaly_err, "REJECTED", f"Anomaly Detector blocked {tool_name}"

    args_str = json.dumps(args)
    
    if tier >= 2:
        auditor_model = get_auditor_model()
        await event_bus.publish("agent_thoughts", {
            "agent": "Security Auditor", 
            "thought": f"Auditing '{tool_name}' execution with arguments: {args_str}"
        })
        
        audit_prompt = (
            f"You are the Meridian Security Auditor. Assess if the following tool execution is safe and does not contain vulnerabilities, dangerous deletions, shell injects, or system risks.\n"
            f"Tool: {tool_name}\n"
            f"Arguments: {args_str}\n\n"
            f"Respond ONLY in this exact format:\n"
            f"REASONING: <brief analysis of the arguments>\n"
            f"DECISION: <APPROVED or REJECTED>"
        )
        
        try:
            from src.core.llm_provider import call_llm
            audit_text = await call_llm([{"role": "user", "content": audit_prompt}], model=auditor_model)
        except Exception:
            try:
                from src.core.llm_provider import call_llm
                audit_text = await call_llm([{"role": "user", "content": audit_prompt}], model=active_model)
            except Exception:
                audit_text = "REASONING: Auditor model unreachable. Failing secure.\nDECISION: REJECTED_UNREACHABLE"
        
        decision = "APPROVED"
        reasoning = ""
        for line in audit_text.split("\n"):
            if line.upper().startswith("DECISION:"):
                decision = line.split(":", 1)[1].strip().upper()
            elif line.upper().startswith("REASONING:"):
                reasoning = line.split(":", 1)[1].strip()
                
        await event_bus.publish("agent_thoughts", {
            "agent": "Security Auditor", 
            "thought": f"Audit Result for '{tool_name}': {decision}. Reasoning: {reasoning}"
        })
        
        if "REJECTED" in decision:
            if "UNREACHABLE" in decision:
                return tool_name, f"Blocked: Security Auditor unreachable for Tier {tier} tool.", "blocked_unreachable"
            else:
                return tool_name, f"Blocked by Security Auditor: {reasoning}", "blocked"

    try:
        result = await call_tool(tool_name, args)
        add_to_task_log(tool_name, tier, "success")
        return tool_name, result, "success"
    except Exception as e:
        err_txt = str(e)
        add_to_task_log(tool_name, tier, "failed", err_txt)
        return tool_name, f"Error: {err_txt}", "failed"
