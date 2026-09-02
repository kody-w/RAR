from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
AGENT = ROOT / "agents/@kody-w/copilot_studio_parity_deploy_agent.py"


def test_copilot_studio_architect_uses_golden_copilot_harness():
    source = AGENT.read_text(encoding="utf-8")
    assert '"version": "1.0.3"' in source
    assert 'SUBAGENT_MODEL = "gpt-5.6-sol-fast"' in source
    assert 'SUBAGENT_CONTEXT = "long_context"' in source
    assert 'SUBAGENT_EFFORT = "max"' in source
    assert '"--context",' in source
    assert "SUBAGENT_CONTEXT" in source
    assert '["--effort", effort]' in source
    assert "RAPP_COPILOT_STUDIO_EFFORT must be" in source
