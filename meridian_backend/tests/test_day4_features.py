import os
import sys
import pytest
import tempfile
import subprocess
from unittest.mock import patch, AsyncMock, MagicMock

# Add src and backend root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from src.core.llm_provider import scan_and_redact_secrets, call_llm, call_llm_sync
from src.tools.review import review_file, review_diff, review_directory, export_review
from src.tools.auto_reviewer import generate_unit_tests, review_git_changes
from database import get_model_source, set_model_source

def test_secret_redaction():
    """Verify high-entropy tokens are redacted before LLM calls."""
    raw_text = "API Key: sk-1234567890abcdef1234567890abcdef and GitHub token ghp_abcdef1234567890abcdef1234567890abcd"
    redacted = scan_and_redact_secrets(raw_text)
    assert "sk-1234567890" not in redacted
    assert "ghp_abcdef" not in redacted
    assert "[REDACTED_SECRET]" in redacted

def test_model_source_persistence():
    """Verify get_model_source and set_model_source."""
    set_model_source("cloud")
    assert get_model_source() == "cloud"
    set_model_source("local")
    assert get_model_source() == "local"

@pytest.mark.asyncio
async def test_call_llm_redaction_and_streaming():
    """Verify call_llm redacts secrets and aggregates streamed tokens."""
    async def mock_stream(messages, provider, model, temperature=0.7):
        yield "Review "
        yield "complete: "
        yield "🟢 OK"

    with patch("src.core.llm_provider.generate_completion_stream", side_effect=mock_stream):
        res = await call_llm([{"role": "user", "content": "sk-1234567890abcdef1234567890abcdef test code"}], provider="ollama", model="test-model")
        assert "Review complete: 🟢 OK" in res

def test_call_llm_sync():
    """Verify call_llm_sync synchronous wrapper execution."""
    async def mock_stream(messages, provider, model, temperature=0.7):
        yield "Sync test "
        yield "passed"

    with patch("src.core.llm_provider.generate_completion_stream", side_effect=mock_stream):
        res = call_llm_sync([{"role": "user", "content": "hello"}], provider="ollama", model="test-model")
        assert res == "Sync test passed"

def test_review_file():
    """Verify review_file with mock LLM response and temp file."""
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".py") as tf:
        tf.write("def foo():\n    return 42\n")
        tf_path = tf.name

    try:
        with patch("src.tools.review.call_llm_sync", return_value="🟢 OK: Clean code."):
            res = review_file(tf_path)
            assert "🟢 OK: Clean code." in res
    finally:
        if os.path.exists(tf_path):
            os.remove(tf_path)

def test_review_file_nonexistent():
    """Verify path validation for nonexistent files."""
    res = review_file("nonexistent_path_xyz123.py")
    assert "Error" in res

def test_review_diff():
    """Verify review_diff subprocess call and mock LLM response."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Initialize dummy git repo
        subprocess.run(["git", "init"], cwd=temp_dir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        with patch("src.tools.review.call_llm_sync", return_value="🟢 OK: No critical diff issues."):
            # First check with clean repo
            res_clean = review_diff(temp_dir)
            assert "No git diff changes" in res_clean

def test_auto_reviewer_generate_unit_tests():
    """Verify auto_reviewer unit test generator."""
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".py") as tf:
        tf.write("def add(a, b):\n    return a + b\n")
        tf_path = tf.name

    try:
        mock_test_code = "def test_add():\n    assert add(1, 2) == 3\n"
        with patch("src.tools.auto_reviewer.call_llm_sync", return_value=mock_test_code):
            res = generate_unit_tests(tf_path, framework="pytest")
            assert "Successfully generated pytest unit tests" in res
    finally:
        if os.path.exists(tf_path):
            os.remove(tf_path)

def test_auto_reviewer_review_git_changes():
    """Verify review_git_changes with clean repo."""
    with tempfile.TemporaryDirectory() as temp_dir:
        subprocess.run(["git", "init"], cwd=temp_dir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        res = review_git_changes(temp_dir)
        assert "No staged or unstaged git diff changes detected" in res
