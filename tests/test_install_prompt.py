"""The primary install prompt and advanced command remain readable without JS."""

from html.parser import HTMLParser
from pathlib import Path


class InstallParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.elements = {}
        self.body_children = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if self.stack and self.stack[-1][0] == "body":
            self.body_children.append((tag, attrs.get("id"), attrs.get("class")))
        element = {"tag": tag, "attrs": attrs, "parents": self.stack[:], "text": ""}
        if "id" in attrs:
            assert attrs["id"] not in self.elements
            self.elements[attrs["id"]] = element
        if tag not in {"meta", "link", "br", "hr", "input", "img"}:
            self.stack.append((tag, attrs.get("id"), element))

    def handle_data(self, data):
        for _, _, element in self.stack:
            element["text"] += data

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                del self.stack[index:]
                break


def test_install_prompt_is_primary_and_terminal_is_folded():
    html = (Path(__file__).resolve().parents[1] / "install.html").read_text(encoding="utf-8")
    parser = InstallParser()
    parser.feed(html)
    elements = parser.elements
    nav_index = next(i for i, child in enumerate(parser.body_children)
                     if child[1] == "rar-nav")
    assert parser.body_children[nav_index + 1] == ("section", None, "copilot-install")
    assert elements["copilot-install-title"]["text"] == "Install with GitHub Copilot in VS Code"
    prompt = elements["install-prompt"]["text"]
    assert prompt.startswith("Install the RAPP Brainstem on this computer and get it running.")
    assert "https://kody-w.github.io/grail-layers/skills/rar-easy-mode/SKILL.md exactly." in prompt
    assert "show me the GitHub code" in prompt
    assert "test message to the Brainstem and showing me the reply" in prompt
    assert "http://localhost:<port>/" in prompt
    assert "typing and sending a chat message with browser tools" in prompt
    assert "If those tools are unavailable" in prompt
    assert elements["copy-prompt"]["tag"] == "button"
    assert elements["copy-prompt"]["attrs"]["onclick"] == "copyPrompt()"
    assert elements["copy-prompt-status"]["attrs"]["role"] == "status"
    assert 'href="https://code.visualstudio.com/download"' in html
    assert 'href="https://code.visualstudio.com/docs/copilot/setup"' in html
    advanced = elements["advanced-install"]
    assert advanced["tag"] == "details" and "open" not in advanced["attrs"]
    assert "Advanced: install from a terminal" in advanced["text"]
    assert elements["install-cmd"]["text"] == (
        "curl -fsSL https://raw.githubusercontent.com/kody-w/RAR/main/scripts/install.sh | bash"
    )
    for element_id in ("ai-toggle", "install-widget", "install-cmd", "copy-icon",
                       "os-label", "install-comment", "install-hint"):
        assert any(parent[1] == "advanced-install"
                   for parent in elements[element_id]["parents"])
    assert 'data-tab="one-liner"' in html and 'data-tab="manual"' in html
    for tier in ("ollama", "brainstem", "hippocampus", "nervous-system"):
        assert not any(parent[1] == "advanced-install"
                       for parent in elements[tier]["parents"])
