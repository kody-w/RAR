# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/private/example_private_agent.py.stub -o ~/.brainstem/src/rapp_brainstem/agents/example_private_agent.py.stub
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/example_private/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Example gated stub — the actual agent.py lives in a private repo.

This file is metadata only. Public RAR lists it so the agent is
discoverable; the brainstem resolves __source__ at install time using
the user's own GitHub credentials. If the user can read the private
repo, they get the bytes. If not, they get a clean access-denied
message.

Stubs may contain ONLY:
  - a module docstring (this block)
  - __manifest__ = { ... }
  - __source__   = { ... }

Anything else (functions, classes, imports, executable code) is
rejected by build_registry.py — stubs are pure metadata.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/example_private",
    "version": "1.0.2",
    "display_name": "ExamplePrivate",
    "description": "Demonstrates the RAR private-agent stub layer \u2014 metadata only, with source resolved from a private GitHub repo at install time.",
    "author": "Kody Wildfeuer",
    "tags": ["example", "private", "stub"],
    "category": "productivity",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

__source__ = {
    "schema": "rapp-source/1.0",
    "type": "github_private",
    "repo": "kody-w/example-private-rar",
    "ref": "main",
    "path": "agents/@kody-w/example_private_agent.py",
}
