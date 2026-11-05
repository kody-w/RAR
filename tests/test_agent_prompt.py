"""Homepage AI discovery and the modal's primary Copilot hot-load action."""

import json
from pathlib import Path
import shutil
import subprocess

import pytest

from tests.test_install_prompt import InstallParser
from tools.build_agent_pages import agent_page_contents, copilot_prompt


ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
SOURCE_CAPTURE = next(
    agent for agent in json.loads((ROOT / "registry.json").read_text())["agents"]
    if agent["name"] == "@kody-w/source_capture_agent"
)


def parse(html):
    parser = InstallParser()
    parser.feed(html)
    return parser


def test_ai_discovery_is_static_but_below_browsing():
    static = HTML.split("<body>", 1)[1].split("<script", 1)[0]
    parser = parse(static)
    assert static.index('id="search"') < static.index('id="grid"') < static.index('id="for-ais-title"')
    assert 'href="a/@kody-w/source_capture_agent/agent.md"' in static
    assert 'href="llms.txt"' in static
    assert 'href="LAYERS.md"' in static
    assert "No JavaScript is needed." in parser.elements["for-ais-title"]["parents"][-1][2]["text"]
    container_content = static.split('<div class="container">', 1)[1]
    # Pages are human first: only the plain-language hero may sit above search; no AI text there.
    head = container_content.split('<div class="search-box">', 1)[0]
    assert head.strip() == "" or head.lstrip().startswith('<section class="home-hero"')
    assert "llms.txt" not in head and ".md" not in head and "http" not in head


@pytest.fixture
def render_modal():
    if not shutil.which("node"):
        pytest.skip("Node.js is required to exercise the storefront JavaScript")
    functions = "function openAgent(name) {" + HTML.split(
        "function openAgent(name) {", 1
    )[1].split("// On page load", 1)[0]

    def render(agent, name=None, blocked=False):
        setup = """
const agent = JSON.parse(process.argv[1]);
const name = process.argv[2];
const blocked = process.argv[3] === 'true';
const allAgents = [agent], RAW = 'https://raw.githubusercontent.com/kody-w/RAR/main';
const OWNER = 'kody-w', REPO_NAME = 'RAR', LOCK_SVG = '';
const esc = value => String(value).replace(/[&<>"']/g, c =>
  ({'&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;'}[c]));
const metricsSection = () => '<div id="metrics">Metrics</div>';
const reviewsSection = () => '<div id="reviews">Reviews</div>';
let clipboard = null, selected = false, focused = false, route = null;
const elements = {
  'modal-content': {innerHTML: ''},
  modal: {classList: {add() {}, remove() {}}},
  'agent-prompt-status': {textContent: ''},
  'agent-prompt': {value: '', focus() {focused = true;}, select() {selected = true;}}
};
const document = {getElementById: id => elements[id], body: {style: {}}};
const navigator = {clipboard: {async writeText(text) {
  if (blocked) throw new Error('Permission denied');
  clipboard = text;
}}};
const history = {replaceState(a, b, value) {route = value;}};
"""
        exercise = """
openAgent(name);
const html = elements['modal-content'].innerHTML;
const match = html.match(/<textarea[^>]*>([\\s\\S]*?)<\\/textarea>/);
if (match) {
  elements['agent-prompt'].value = match[1].replace(/&#39;/g, "'")
    .replace(/&quot;/g, '"').replace(/&gt;/g, '>').replace(/&lt;/g, '<').replace(/&amp;/g, '&');
  await copyAgentPrompt();
}
console.log(JSON.stringify({html, clipboard, selected, focused, route,
  status: elements['agent-prompt-status'].textContent}));
"""
        result = subprocess.run(
            ["node", "--input-type=module", "-e", setup + functions + exercise,
             json.dumps(agent), name or agent["name"], str(blocked).lower()],
            capture_output=True, text=True, check=True, timeout=15,
        )
        return json.loads(result.stdout)

    return render


def test_source_capture_prompt_and_clipboard(render_modal):
    result = render_modal(SOURCE_CAPTURE, "@kody-w/source_capture")
    parser = parse(result["html"])
    elements = parser.elements
    expected = (
        "Follow https://kody-w.github.io/grail-layers/skills/rar-easy-mode/SKILL.md "
        "to hot-load this agent into my local Brainstem: "
        f"https://kody-w.github.io/RAR/{SOURCE_CAPTURE['_file']}. "
        "If I don't have a Brainstem yet, install it first the same way. "
        "When it's loaded, send the Brainstem one message that uses the agent "
        "and show me the reply."
    )
    assert elements["agent-prompt"]["text"] == expected
    assert result["clipboard"] == expected
    assert "readonly" in elements["agent-prompt"]["attrs"]
    assert elements["copy-agent-prompt"]["attrs"]["onclick"] == "copyAgentPrompt()"
    assert elements["agent-prompt-status"]["attrs"]["role"] == "status"
    assert result["route"] == "#agent/%40kody-w%2Fsource_capture"
    assert "Prompt copied." in result["status"]
    assert result["html"].index('class="desc"') < result["html"].index('class="copilot-agent"')
    assert result["html"].index('class="copilot-agent"') < result["html"].index("<details")
    assert 'href="https://code.visualstudio.com/download"' in result["html"]
    assert f'href="a/{SOURCE_CAPTURE["name"]}/agent.md"' in result["html"]
    assert not any(parent[0] == "details" for parent in elements["metrics"]["parents"])
    assert not any(parent[0] == "details" for parent in elements["reviews"]["parents"])
    folded = result["html"].split('<details class="agent-alternatives">', 1)[1].split("</details>", 1)[0]
    assert "Other ways to get it" in folded
    for text in ("Copy Link", "Agent ticket and load steps", SOURCE_CAPTURE["_file"],
                 "Download agent.py", "Environment Variables", "None required", "View source"):
        assert text in folded


def test_required_env_is_warned_above_prompt_and_escaped(render_modal):
    result = render_modal({**SOURCE_CAPTURE, "requires_env": ["TOKEN", "<SECRET>"]})
    assert result["html"].index("Requires environment variables: TOKEN, &lt;SECRET&gt;") < result["html"].index("<textarea")
    assert "<SECRET>" not in result["html"]


def test_blocked_clipboard_reports_failure_and_selects_prompt(render_modal):
    result = render_modal(SOURCE_CAPTURE, blocked=True)
    assert result["clipboard"] is None
    assert result["focused"] and result["selected"]
    assert "Could not copy prompt." in result["status"]
    assert "Permission denied" in result["status"]


def test_gated_agent_keeps_access_instructions_without_public_hotload(render_modal):
    result = render_modal({
        **SOURCE_CAPTURE, "type": "stub",
        "_source": {"repo": "publisher/private", "path": "agent.py"},
    })
    assert "Gated agent" in result["html"] and "Request access" in result["html"]
    assert "agent-prompt-title" not in result["html"]
    assert "Download agent.py" not in result["html"]
    assert result["html"].index("Request access") < result["html"].index("<details")


def test_canonical_agent_route_still_opens(render_modal):
    assert render_modal(SOURCE_CAPTURE)["clipboard"] is not None


@pytest.mark.parametrize("agent", json.loads((ROOT / "registry.json").read_text())["agents"],
                         ids=lambda a: a["name"])
def test_ticket_prompt_matches_modal_exactly(render_modal, agent):
    modal = render_modal(agent)
    page = parse(agent_page_contents(agent)["index.html"])
    assert page.elements["manual-ticket"]["text"] == agent_page_contents(agent)["agent.md"]
    assert "open" not in page.elements["advanced-ticket"]["attrs"]
    if agent.get("type") == "stub":
        assert copilot_prompt(agent) == ""
        assert "copy-source" not in page.elements
        assert modal["clipboard"] is None
    else:
        assert page.elements["copy-source"]["text"] == modal["clipboard"] == copilot_prompt(agent)
        assert page.elements["copy-source"]["attrs"]["readonly"] is None
