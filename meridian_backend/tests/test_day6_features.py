"""
test_day6_features.py — Unit Test Suite for Day 6 Features:
- DEV-05: Offline Codebase AST Graph, Symbol Search, Call Tracing & Impact Analysis
- JARVIS-09: Subconscious Codebase Memory & Neural RAG Synthesizer
- DEV-04: 3-Stage Paper-to-Code (PaperCoder) Generator
"""

import os
import pytest
from src.core.code_graph import (
    parse_python_ast,
    search_codebase_symbols,
    trace_symbol_callers,
    trace_symbol_callees,
    analyze_change_impact
)
from src.core.neural_rag import NeuralRAGSynthesizer
from src.tools.papercoder import PaperCoderEngine, generate_paper2code


def test_ast_symbol_parsing(tmp_path):
    sample_file = tmp_path / "sample_module.py"
    sample_file.write_text('''"""Sample Module Docstring"""

class TestModel:
    """Class docstring"""
    def forward(self, x):
        """Method docstring"""
        return compute_logits(x)

def compute_logits(data):
    """Function docstring"""
    return len(data)
''', encoding="utf-8")

    ast_data = parse_python_ast(str(sample_file))
    symbols = ast_data["symbols"]
    calls = ast_data["calls"]

    names = [s["name"] for s in symbols]
    assert "TestModel" in names
    assert "TestModel.forward" in names
    assert "compute_logits" in names

    call_names = [c["name"] for c in calls]
    assert "compute_logits" in call_names


def test_codebase_symbol_search():
    results = search_codebase_symbols("parse_python_ast")
    assert isinstance(results, list)
    assert len(results) > 0
    assert any("parse_python_ast" in r["name"] for r in results)


def test_symbol_tracing_and_impact():
    callers = trace_symbol_callers("parse_python_ast")
    assert isinstance(callers, list)

    impact = analyze_change_impact("parse_python_ast")
    assert isinstance(impact, dict)
    assert "impact_score" in impact
    assert "affected_files" in impact


def test_neural_rag_synthesizer(tmp_path):
    synthesizer = NeuralRAGSynthesizer(workspace_dir=str(tmp_path))

    file1 = tmp_path / "engine.py"
    file1.write_text("def run_neural_engine(): pass", encoding="utf-8")

    graph = synthesizer.build_intent_graph()
    assert graph["status"] == "success"
    assert graph["nodes_count"] > 0

    intents = synthesizer.query_intent("neural engine")
    assert len(intents) > 0
    assert intents[0]["name"] == "run_neural_engine"


def test_papercoder_3stage_pipeline(tmp_path):
    paper_input = """Title: Attention Is All You Need (Transformer)
Abstract: We propose the Transformer model architecture based on self-attention mechanisms.
ArXiv: 1706.03762
"""
    engine = PaperCoderEngine(output_base_dir=str(tmp_path))

    # Stage 1
    spec = engine.parse_paper_spec(paper_input)
    assert spec["spec_parsed"] is True
    assert spec["title"] == "Attention Is All You Need (Transformer)"

    # Stage 2
    arch = engine.design_architecture(spec)
    assert arch["architecture_designed"] is True
    assert len(arch["files_plan"]) == 5

    # Stage 3
    result = engine.generate_repository(arch)
    assert result["status"] == "success"
    assert result["created_files_count"] == 5
    assert os.path.exists(os.path.join(result["repo_dir"], "trainer.py"))

    # Tool wrapper JSON test
    tool_json = generate_paper2code(paper_input)
    assert "runnable paper codebase" in tool_json
