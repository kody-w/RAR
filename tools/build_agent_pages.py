"""Deterministic, JavaScript-free ticket pages derived from registry agents."""

from __future__ import annotations

from html import escape
from pathlib import Path
from urllib.parse import quote

from tools.stamp_ticket import SITE, agent_path, page_url, ticket_text


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


def build_agent_pages(agents: list[dict], root: Path = Path(".")) -> int:
    changed = 0
    for agent in agents:
        agent_path(agent)
        directory = root / "a" / agent["name"]
        markdown = agent_markdown(agent)
        html = (
            '<!doctype html>\n<html lang="en">\n<head>\n'
            '<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f"<title>{escape(agent['display_name'])} - RAPP agent ticket</title>\n"
            f'<meta name="description" content="{escape(agent["description"], quote=True)}">\n'
            f'<link rel="canonical" href="{escape(page_url(agent), quote=True)}">\n'
            '</head>\n<body>\n<main>\n'
            f"<h1>{escape(agent['display_name'])}</h1>\n"
            f"<p>{escape(agent['description'])}</p>\n"
            '<h2>Load this agent in three steps</h2>\n'
            f'<pre style="white-space:pre-wrap">{escape(markdown)}</pre>\n'
            f'<p><a href="{escape(SITE + "/" + quote(str(agent_path(agent)), safe="@/"), quote=True)}">Raw file</a> | '
            f'<a href="{escape(SITE + "/#agent/" + quote(agent["name"], safe="@/"), quote=True)}">Browse in RAR</a> | '
            '<a href="agent.md">Plain text for AIs</a></p>\n'
            '</main>\n</body>\n</html>\n'
        )
        directory.mkdir(parents=True, exist_ok=True)
        for filename, content in (("agent.md", markdown), ("index.html", html)):
            path = directory / filename
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                path.write_text(content, encoding="utf-8")
                changed += 1
    return changed
