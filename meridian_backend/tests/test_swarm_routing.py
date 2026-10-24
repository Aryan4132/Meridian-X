import pytest
from src.core.swarm import resolve_role_model_and_provider, SwarmAgent

def test_resolve_role_model_and_provider_defaults():
    # Test default model and provider assignment for researcher
    model, provider, source = resolve_role_model_and_provider("researcher")
    assert model is not None
    assert provider in ("gemini", "ollama", "openai", "anthropic", "deepseek", "groq")
    assert source in ("gemini", "ollama", "openai", "anthropic", "deepseek", "groq")

    # Test auditor resolution
    model_aud, provider_aud, source_aud = resolve_role_model_and_provider("auditor")
    assert "coder" in model_aud.lower() or "deepseek" in model_aud.lower() or "claude" in model_aud.lower() or "qwen" in model_aud.lower()

def test_resolve_role_model_and_provider_override():
    # Explicit custom override takes precedence
    model, provider, source = resolve_role_model_and_provider("planner", custom_model="claude-3-7-sonnet")
    assert model == "claude-3-7-sonnet"
    assert provider == "anthropic"
    assert source == "anthropic"

def test_swarm_agent_initialization_with_heterogeneous_config():
    agent = SwarmAgent(role="auditor")
    assert agent.role == "auditor"
    assert agent.model is not None
    assert hasattr(agent, "provider")
    assert hasattr(agent, "model_source")
