"""Deterministic, human-first ticket pages with a plain-text AI counterpart.

Regenerate with build_agent_pages(json.loads(Path("registry.json").read_text())["agents"]).
The prompt mirrors index.html's agent modal; tests enforce byte-for-byte parity.
"""

from __future__ import annotations

from html import escape
from pathlib import Path
import re
from urllib.parse import quote

from tools.stamp_ticket import SITE, agent_path, page_url, ticket_text


SKILL_URL = "https://kody-w.github.io/grail-layers/skills/rar-easy-mode/SKILL.md"
PROMPT_END = (
    "If I don't have a Brainstem yet, install it first the same way. "
    "When it's loaded, send the Brainstem one message that uses the agent "
    "and show me the reply."
)
PAGE_STYLE = """
:root{--bg:#f7f5f0;--card:#fff;--ink:#1c1f23;--muted:#5b636b;--line:#e4e0d6;--accent:#0f766e;--soft:#0f766e14}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:18px/1.6 ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif}
main{max-width:720px;margin:0 auto;padding:56px 16px 80px}
h1{font-size:clamp(34px,7vw,52px);line-height:1.1;margin:0 0 20px;letter-spacing:-.02em;overflow-wrap:anywhere}
.promises{list-style:none;padding:0;margin:0 0 36px}
.promises li{padding:10px 0;border-bottom:1px solid var(--line);overflow-wrap:anywhere}
.start{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:22px}
.start p{margin:0 0 16px}
.start p:last-child{margin-bottom:0}
button{font:600 16px/1.5 ui-sans-serif,system-ui,sans-serif;background:var(--accent);color:#fff;border:0;border-radius:10px;padding:10px 18px;cursor:pointer}
button:focus-visible,a:focus-visible,summary:focus-visible{outline:3px solid var(--accent);outline-offset:4px}
.start .copy-status{font-size:14px;color:var(--muted);margin:12px 0 0}
.copy-status:empty{display:none}
.next{margin:16px 0 28px;font-size:16px;color:var(--muted)}
ol.hour{padding:0;margin:0;list-style:none;counter-reset:s}
ol.hour li{counter-increment:s;position:relative;padding:14px 0 14px 56px;border-bottom:1px solid var(--line)}
ol.hour li::before{content:counter(s);position:absolute;left:0;top:14px;width:38px;height:38px;border-radius:50%;background:var(--soft);color:var(--accent);font-weight:700;display:grid;place-items:center}
main details{margin-top:48px;border-top:1px solid var(--line);padding-top:16px;color:var(--muted);font-size:16px}
summary{cursor:pointer;font-weight:600;color:var(--ink)}
pre{white-space:pre-wrap;overflow-wrap:anywhere;font:14px/1.6 ui-monospace,SFMono-Regular,Menlo,monospace}
a{color:var(--accent)}
footer{margin-top:32px;font-size:14px;color:var(--muted)}
@media(max-width:640px){main{padding-top:32px}.start{padding:18px}}
"""
COPY_SCRIPT = """
document.getElementById('copy-prompt')?.addEventListener('click', async () => {
  const prompt = document.getElementById('copy-source');
  const status = document.getElementById('copy-status');
  try {
    await navigator.clipboard.writeText(prompt.value);
    status.textContent = 'Copied. Paste into Copilot Chat in Agent mode.';
  } catch (error) {
    prompt.hidden = false;
    prompt.focus();
    prompt.select();
    try {
      if (!document.execCommand('copy')) throw new Error('Copy was blocked');
      prompt.hidden = true;
      status.textContent = 'Copied. Paste into Copilot Chat in Agent mode.';
    } catch (fallbackError) {
      status.textContent = 'Could not copy. Copy the selected prompt manually. ' + fallbackError.message;
    }
  }
});
"""


def copilot_prompt(agent: dict) -> str:
    if agent.get("type") == "stub":
        return ""
    return (
        f"Follow {SKILL_URL} to hot-load this agent into my local Brainstem: "
        f"{SITE}/{agent_path(agent)}. {PROMPT_END}"
    )


def agent_markdown(agent: dict) -> str:
    path = agent_path(agent)
    raw_url = f"{SITE}/{quote(str(path), safe='@/')}"
    spa_url = f"{SITE}/#agent/{quote(agent['name'], safe='@/')}"
    title = f"{agent['display_name']} ({agent['name']})"
    text = f"# {title}\n\n{agent['description']}\n\n"
    if agent.get("type") == "stub":
        source = agent["_source"]
        text += (
            "GATED LISTING: this public file is metadata, NOT executable agent code.\n"
            "Do not copy the .py.stub into the agents folder. Your person needs read "
            f"access to {source['repo']} and their own GitHub credentials.\n\n"
            "1. Brainstem: if http://localhost:7071/health does not answer, run:\n"
            "   curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash\n"
            "2. In your paired Brainstem chat, ask:\n"
            f"   rar install {agent['name']}\n"
            "   It resolves the private source using your own gh auth access. "
            "No restart is needed.\n"
            '3. Open http://localhost:7071, or POST /chat {"user_input": "..."}; '
            'the reply is in "response".\n\n'
            "Can't run commands (a web chat AI)? Give your person these steps.\n"
        )
    else:
        lines = ticket_text(agent).splitlines()[1:-1]
        text += "\n".join(line.removeprefix("# ") for line in lines) + "\n"
        if path.name.endswith(".py.card"):
            text += (
                "\nThis download is a Python .py.card package. Before chatting, "
                f"rename {path.name} to {path.name.removesuffix('.card')} "
                "in the agents folder so the Python loader discovers it.\n"
            )
        elif not path.name.endswith("_agent.py"):
            filename = agent.get("_install_filename") or f"{path.stem}_agent.py"
            text += (
                f"\nBefore chatting, rename {path.name} to {filename} in the "
                "agents folder so the Python loader discovers its _agent.py suffix.\n"
            )
    text += (
        "\nOnly load code you trust. If that filename already exists, keep a backup "
        "and inspect it before replacing it. Configure any required environment "
        "variables and dependencies before use.\n"
    )
    env = agent.get("requires_env") or []
    deps = agent.get("dependencies") or []
    if env:
        text += f"Required environment variables: {', '.join(env)}\n"
    if deps:
        text += f"Dependencies: {', '.join(deps)}\n"
    return (
        text + f"\nRaw file: {raw_url}\n"
        f"Browse in RAR: {spa_url}\n"
        f"Page: {page_url(agent)}\n"
        f"Plain text for AIs: {page_url(agent)}agent.md\n"
    )


def agent_page_contents(agent: dict) -> dict[str, str]:
    """Render the two owned filenames without writing or creating directories."""
    agent_path(agent)
    markdown = agent_markdown(agent)
    benefit_lines = re.split(r"(?<=[.!?])\s+(?=[A-Z])", agent["description"], maxsplit=2)
    benefits = "".join(f"<li>{escape(line)}</li>" for line in benefit_lines)
    raw_url = f"{SITE}/{quote(str(agent_path(agent)), safe='@/')}"
    spa_url = f"{SITE}/#agent/{quote(agent['name'], safe='@/')}"
    root = "../../../"
    destinations = (
        ("Browse", "index.html"), ("Distros", "distros.html"),
        ("Skills", "skills.html"), ("Install", "install.html"),
        ("Front page", "front.html"), ("Advanced", "store.html"),
        ("For AIs", "llms.txt"),
    )
    fallback = "".join(
        f'<a href="{root}{target}">{label}</a>' for label, target in destinations
    )
    if agent.get("type") == "stub":
        start = (
            '<section class="start" aria-label="Private agent access">\n'
            '<p>This agent has private source. You need read access and your own '
            'GitHub credentials before installing it.</p>\n'
            f'<a href="{escape(spa_url, quote=True)}">Request access in RAR</a>\n'
            '</section>\n'
        )
    else:
        start = (
            '<section class="start" aria-label="Copilot prompt">\n'
            f'<p>Follow <a href="{SKILL_URL}">the Brainstem setup skill</a> to hot-load '
            'this agent into my local Brainstem: '
            f'<a href="{escape(raw_url, quote=True)}">this agent</a>. '
            f'{escape(PROMPT_END)}</p>\n'
            '<textarea id="copy-source" aria-label="Copilot prompt" readonly hidden '
            f'style="width:100%;min-height:16em">{escape(copilot_prompt(agent))}</textarea>\n'
            '<button id="copy-prompt" type="button">Copy</button>\n'
            '<p id="copy-status" class="copy-status" role="status" aria-live="polite"></p>\n'
            '</section>\n'
            '<p class="next">Open VS Code, open Copilot Chat in Agent mode, paste, '
            'press Enter. No VS Code? <a href="https://code.visualstudio.com/download">'
            'Get it.</a></p>\n'
            '<ol class="hour" aria-label="How to use this agent">\n'
            '<li>Paste the prompt into Copilot.</li>\n'
            "<li>Copilot sets up your Brainstem if you don't have one, then loads this agent.</li>\n"
            '<li>Copilot sends it one message and shows you the reply.</li>\n'
            '</ol>\n'
        )
    html = (
        '<!doctype html>\n<html lang="en">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"<title>{escape(agent['display_name'])} - RAPP agent ticket</title>\n"
        f'<meta name="description" content="{escape(agent["description"], quote=True)}">\n'
        f'<link rel="canonical" href="{escape(page_url(agent), quote=True)}">\n'
        f'<link rel="stylesheet" href="{root}nav.css">\n'
        f'<style>{PAGE_STYLE}</style>\n'
        f'<script src="{root}nav.js" defer></script>\n'
        '</head>\n<body>\n'
        f'<nav id="rar-nav" aria-label="Primary" data-root="{root}">\n'
        f'<a class="rar-brand" href="{root}index.html"><span class="rar-brand-mark">R</span>'
        'RAPP Agent Repository</a>\n'
        '<span class="rar-primary"><noscript><span class="rar-nav-fallback">'
        f'{fallback}</span></noscript></span>\n'
        '<details class="rar-more"><summary>More</summary><div class="rar-more-content">\n'
        f'<a href="{root}virtual-brainstem.html">Get Started</a>\n'
        f'<a href="{root}discover.html">For Work</a>\n'
        f'<a href="{root}metrics.html">Metrics</a>\n'
        f'<a href="{root}submit.html">Submit</a>\n'
        f'<a href="{root}admin.html">Admin</a>\n'
        '</div></details>\n</nav>\n<main>\n'
        f"<h1>{escape(agent['display_name'])}</h1>\n"
        f'<ul class="promises">{benefits}</ul>\n'
        f'{start}'
        '<details id="advanced-ticket"><summary>Advanced: do it by hand</summary>\n'
        f'<pre id="manual-ticket">{escape(markdown)}</pre>\n</details>\n'
        f'<footer><a href="{escape(raw_url, quote=True)}">Raw file</a> | '
        f'<a href="{escape(spa_url, quote=True)}">Browse in RAR</a> | '
        '<a href="agent.md">Plain text for AIs</a></footer>\n'
        f'</main>\n<script>{COPY_SCRIPT}</script>\n</body>\n</html>\n'
    )
    return {"agent.md": markdown, "index.html": html}


def build_agent_pages(agents: list[dict], root: Path = Path(".")) -> int:
    changed = 0
    for agent in agents:
        contents = agent_page_contents(agent)
        directory = root / "a" / agent["name"]
        directory.mkdir(parents=True, exist_ok=True)
        for filename, content in contents.items():
            path = directory / filename
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                path.write_text(content, encoding="utf-8")
                changed += 1
    return changed
