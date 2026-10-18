"""LearnNew's template source is configurable (RAPP_LEARN_REGISTRY_URL and friends) and unchanged when unset."""
import hashlib
import json
import os
import subprocess
import sys
import textwrap
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
AGENT = REPO_ROOT / "agents" / "@rapp" / "learn_new_agent.py"
TEMPLATES = REPO_ROOT / "agents" / "@aibast-agents-library" / "templates"

LOAD = textwrap.dedent("""
    import importlib.util, json, sys
    sys.path.insert(0, %(templates)r)
    spec = importlib.util.spec_from_file_location("learn_new_agent", %(agent)r)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
""")

TEMPLATE_AGENT = '''"""Counts the words in a text."""
try:
    from agents.basic_agent import BasicAgent
except ImportError:
    from basic_agent import BasicAgent

__manifest__ = {"schema": "rapp-agent/1.0", "name": "@lib/word_counter", "version": "1.0.0",
                "display_name": "WordCounter", "description": "Counts the words in a text.", "author": "lib",
                "tags": ["text", "count", "words"], "category": "productivity"}


class WordCounterAgent(BasicAgent):
    def __init__(self):
        self.name = "WordCounter"
        self.metadata = {"name": self.name, "description": "Counts words.",
                         "parameters": {"type": "object", "properties": {"text": {"type": "string"}}, "required": []}}
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        return str(len(str(kwargs.get("text", "")).split()))
'''


def _run(code, env):
    full = dict(os.environ, **env)
    for k in [k for k in full if k.startswith("RAPP_LEARN_") and k not in env]:
        del full[k]
    r = subprocess.run([sys.executable, "-c", LOAD % {"templates": str(TEMPLATES), "agent": str(AGENT)} + code],
                       capture_output=True, text=True, env=full, timeout=120)
    assert r.returncode == 0, r.stderr
    return r.stdout


def test_default_source_unchanged(tmp_path):
    out = json.loads(_run("print(json.dumps([m.TEMPLATE_REPO, m.TEMPLATE_REGISTRY_URL, m.TEMPLATE_RAW_BASE]))",
                          {"RAPP_LEARN_CACHE_DIR": str(tmp_path)}))
    assert out == ["microsoft/aibast-agents-library",
                   "https://raw.githubusercontent.com/microsoft/aibast-agents-library/main/registry.json",
                   "https://raw.githubusercontent.com/microsoft/aibast-agents-library/main/"]


def test_local_library_is_adapted_with_its_own_provenance(tmp_path):
    lib = tmp_path / "lib"
    (lib / "agents").mkdir(parents=True)
    body = TEMPLATE_AGENT.encode()
    (lib / "agents" / "word_counter_agent.py").write_bytes(body)
    (lib / "registry.json").write_text(json.dumps({"agents": [{
        "name": "@lib/word_counter", "display_name": "WordCounter", "description": "Counts the words in a text.",
        "tags": ["text", "count", "words"], "category": "productivity",
        "_file": "agents/word_counter_agent.py", "_sha256": hashlib.sha256(body).hexdigest()}]}))
    cache, out_dir = tmp_path / "cache", tmp_path / "out"
    out_dir.mkdir()
    env = {"RAPP_LEARN_CACHE_DIR": str(cache), "RAPP_LEARN_NO_LLM": "1",
           "RAPP_LEARN_REGISTRY_URL": (lib / "registry.json").as_uri(), "RAPP_LEARN_TEMPLATE_BASE": lib.as_uri() + "/",
           "RAPP_LEARN_TEMPLATE_REPO": "example/lib", "RAPP_LEARN_TEMPLATE_REPO_URL": "https://example.invalid/lib",
           "RAPP_LEARN_TEMPLATE_LICENSE": "MIT License, Copyright (c) Example"}
    r = json.loads(_run(textwrap.dedent("""
        a = m.LearnNewAgent()
        print(a.perform(action="create", description="counts the words in a customer's note",
                        name="NoteWords", template="@lib/word_counter", output_dir=%r))
    """) % str(out_dir), env))
    written = list(out_dir.glob("*.py"))
    assert len(written) == 1, r
    text = written[0].read_text()
    assert "https://example.invalid/lib" in text and "Copyright (c) Example" in text
    assert "Microsoft" not in text
    assert "def perform" in text and "len(str(kwargs.get(\"text\", \"\")).split())" in text   # body kept: adapted, not regenerated
    assert not (cache / "aibast-registry.json").exists()
    assert list(cache.glob("registry-*.json"))


def test_tampered_local_template_is_refused(tmp_path):
    lib = tmp_path / "lib"
    (lib / "agents").mkdir(parents=True)
    (lib / "agents" / "word_counter_agent.py").write_text(TEMPLATE_AGENT + "\n# changed after publishing\n")
    (lib / "registry.json").write_text(json.dumps({"agents": [{
        "name": "@lib/word_counter", "display_name": "WordCounter", "description": "Counts the words in a text.",
        "tags": ["text"], "category": "productivity", "_file": "agents/word_counter_agent.py",
        "_sha256": hashlib.sha256(TEMPLATE_AGENT.encode()).hexdigest()}]}))
    out_dir = tmp_path / "out"
    out_dir.mkdir()
    env = {"RAPP_LEARN_CACHE_DIR": str(tmp_path / "cache"), "RAPP_LEARN_NO_LLM": "1",
           "RAPP_LEARN_REGISTRY_URL": (lib / "registry.json").as_uri(), "RAPP_LEARN_TEMPLATE_BASE": lib.as_uri() + "/"}
    _run(textwrap.dedent("""
        a = m.LearnNewAgent()
        print(a.perform(action="create", description="counts words", name="NoteWords", template="@lib/word_counter",
                        output_dir=%r))
    """) % str(out_dir), env)
    assert not any("word_counter" in p.read_text() for p in out_dir.glob("*.py"))
