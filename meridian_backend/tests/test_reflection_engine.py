import os
import tempfile
import pytest
from unittest.mock import patch
from src.core.reflection_engine import (
    detect_user_correction,
    ReflectionEngine
)
from src.core.cognitive_graph import UnifiedCognitiveGraph
from src.core.loop_planning import enrich_system_prompt


@pytest.fixture
def temp_reflection_engine():
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp_dir:
        db_path = os.path.join(tmp_dir, "test_cognitive.db")
        cg = UnifiedCognitiveGraph(db_path=db_path)
        engine = ReflectionEngine(cg=cg)
        yield engine


def test_detect_user_correction():
    # Explicit correction cues
    assert detect_user_correction("No, don't use npm, use bun instead.") is not None
    assert "use bun" in detect_user_correction("No, don't use npm, use bun instead.")

    assert detect_user_correction("In this project, always use Python 3.10 syntax") is not None
    assert detect_user_correction("Stop, never delete test files without asking") is not None
    assert detect_user_correction("Remember that in this repo, always format before committing") is not None

    # Normal queries should not trigger correction
    assert detect_user_correction("How can I build this component?") is None
    assert detect_user_correction("Check git status and summarize diffs.") is None
    assert detect_user_correction("") is None


def test_record_and_retrieve_learned_lessons(temp_reflection_engine):
    engine = temp_reflection_engine

    # Record lessons
    engine.record_learned_lesson("Always use forward slashes in pytest commands on Windows", category="correction")
    engine.record_learned_lesson("Do not edit package-lock.json manually", category="correction")

    lessons = engine.get_relevant_lessons("run pytest suite", limit=2)
    assert len(lessons) >= 1
    assert any("pytest commands" in l for l in lessons)


def test_record_and_retrieve_task_experiences(temp_reflection_engine):
    engine = temp_reflection_engine

    engine.record_task_experience(
        goal="Audit git repository and summarize modified files",
        tools_used=["workspace_quick_audit", "git_status"],
        outcome="Successfully generated git health audit and commit message proposal."
    )

    exps = engine.get_relevant_experiences("audit git repository", limit=1)
    assert len(exps) == 1
    assert "workspace_quick_audit" in exps[0]["tools"]
    assert "Audit git repository" in exps[0]["goal"]


def test_enrich_system_prompt_with_reflections(temp_reflection_engine):
    engine = temp_reflection_engine
    engine.record_learned_lesson("In this repo, use ruff for linting", category="correction")
    engine.record_task_experience("Lint files", ["lint_file"], "All files cleanly formatted.")

    with patch("src.core.reflection_engine.get_reflection_engine", return_value=engine):
        base_prompt = "You are Meridian."
        enriched = enrich_system_prompt(base_prompt, prompt="Lint and check files with ruff", session_id="test_session")
        assert "[🧠 LEARNED LESSONS & USER CONSTRAINTS]" in enriched
        assert "ruff for linting" in enriched
        assert "[PROVEN PAST TRAJECTORIES (FEW-SHOT)]" in enriched
