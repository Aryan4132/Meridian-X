"""Data-driven lazy skill packs (Phase 4: 12 primitives + lazy Skills).

Skill packs live in ``plugins/skills/<skill>/`` as ``SKILL.md`` (YAML
front-matter: name, version, description, keywords) plus ``tools.yaml``
(tool name/tier/description entries referencing TOOL_REGISTRY tools).

The loader is deliberately decoupled from the tool registry: validation
takes a registry mapping as a parameter, so importing this module can
never create an import cycle. ``generate_tools_doc`` prefers skill packs
and falls back to its hardcoded maps if packs are missing or invalid —
prompt generation can never break because of a skill file.
"""

import logging
import os
import re
from typing import Any, Dict, List, Optional

logger = logging.getLogger("meridian_skills")

_FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)

_skill_packs_cache: Optional[Dict[str, Dict[str, Any]]] = None


def find_skills_dir() -> str:
    """Locate <workspace>/plugins/skills without depending on other modules."""
    try:
        from src.core.history_manager import find_workspace_root
        return os.path.join(find_workspace_root(), "plugins", "skills")
    except Exception:
        backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        root_dir = os.path.dirname(backend_dir)
        return os.path.join(root_dir, "plugins", "skills")


def _parse_skill_manifest(skill_dir: str) -> Optional[Dict[str, Any]]:
    """Parse SKILL.md front-matter + tools.yaml into a skill dict."""
    import yaml

    manifest_path = os.path.join(skill_dir, "SKILL.md")
    tools_path = os.path.join(skill_dir, "tools.yaml")
    if not (os.path.isfile(manifest_path) and os.path.isfile(tools_path)):
        return None

    with open(manifest_path, "r", encoding="utf-8") as f:
        content = f.read()
    m = _FRONT_MATTER_RE.match(content)
    if not m:
        logger.warning("[Skills] %s missing YAML front-matter; skipped.", manifest_path)
        return None
    meta = yaml.safe_load(m.group(1)) or {}

    with open(tools_path, "r", encoding="utf-8") as f:
        tools_doc = yaml.safe_load(f) or {}
    tools = tools_doc.get("tools", []) or []
    if not isinstance(tools, list):
        logger.warning("[Skills] %s 'tools' is not a list; skipped.", tools_path)
        return None

    name = str(meta.get("name") or os.path.basename(skill_dir))
    keywords = [str(k).lower() for k in (meta.get("keywords") or [])]
    clean_tools = []
    for t in tools:
        if not isinstance(t, dict) or not t.get("name"):
            continue
        clean_tools.append({
            "name": str(t["name"]),
            "tier": int(t.get("tier", 1)),
            "description": str(t.get("description", "")),
        })
    return {
        "name": name,
        "version": str(meta.get("version", "0.0.0")),
        "description": str(meta.get("description", "")),
        "keywords": keywords,
        "tools": clean_tools,
    }


def load_skill_packs(skills_dir: Optional[str] = None, force_reload: bool = False) -> Dict[str, Dict[str, Any]]:
    """Load all skill packs from disk (cached). Never raises on bad files."""
    global _skill_packs_cache
    if _skill_packs_cache is not None and not force_reload:
        return _skill_packs_cache
    packs: Dict[str, Dict[str, Any]] = {}
    base = skills_dir or find_skills_dir()
    try:
        entries = sorted(os.listdir(base))
    except Exception:
        entries = []
    for entry in entries:
        skill_dir = os.path.join(base, entry)
        if not os.path.isdir(skill_dir):
            continue
        try:
            pack = _parse_skill_manifest(skill_dir)
        except Exception as e:
            logger.warning("[Skills] Failed parsing pack '%s': %s", entry, e)
            continue
        if pack:
            packs[pack["name"]] = pack
    _skill_packs_cache = packs
    return packs


def validate_skill_packs(packs: Dict[str, Dict[str, Any]], registry: Dict[str, Dict[str, Any]]) -> List[str]:
    """Return human-readable warnings for skill tools missing from the registry or tier mismatches."""
    warnings: List[str] = []
    for pack_name, pack in packs.items():
        for t in pack.get("tools", []):
            info = registry.get(t["name"])
            if info is None:
                warnings.append(f"skill '{pack_name}' references unknown tool '{t['name']}'")
            elif info.get("tier") != t["tier"]:
                warnings.append(
                    f"skill '{pack_name}' tool '{t['name']}' tier {t['tier']} "
                    f"!= registry tier {info.get('tier')}"
                )
    return warnings


def match_skills_for_prompt(prompt: str, packs: Dict[str, Dict[str, Any]]) -> List[str]:
    """Return tool names from skill packs whose keywords hit the prompt."""
    p_lower = (prompt or "").lower()
    matched: List[str] = []
    for pack in packs.values():
        if any(kw and kw in p_lower for kw in pack.get("keywords", [])):
            matched.extend(t["name"] for t in pack.get("tools", []))
    return matched
