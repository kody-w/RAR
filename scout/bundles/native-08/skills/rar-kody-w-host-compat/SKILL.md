---
name: "rar-kody-w-host-compat"
description: "Bridge to everything agent-host-shaped on this machine, across Claude Code, GitHub Copilot CLI and the open Agent Skills layout: skills (SKILL.md), plugins, slash commands / prompts, subagent personas, hooks, MCP servers, instruction files (CLAUDE.md, AGENTS.md, copilot-instructions.md) and local session transcripts. action='list' shows what exists; 'load' pulls a skill/command/persona's instructions into the conversation before doing that kind of work; 'read' returns a bundled file; 'run' executes a skill's bundled script; 'mcp_tools'/'mcp_call' use an MCP server; 'install' adds a plugin from a path or git URL; 'promote' compiles a skill into a native Brainstem agent; 'export' turns an agent into a SKILL.md; 'hook' fires a hook; 'instructions' returns the project's instruction files; 'transcripts' searches the user's own past CODING-ASSISTANT CHAT HISTORY \u2014 Claude Code and GitHub Copilot CLI session logs on this machine \u2014 across both hosts at once (query=...; this is the tool for 'what did I ask Claude/Copilot about X', 'find my earlier session where...', NOT for meeting or call transcripts); 'transcript' reads one session by id; 'index' backfills the session index; 'doctor' is a health report."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/host_compat_agent", "rar_sha256": "284c111aa88d5588b9873c97f04d44676223ea37a80240a5e7b884bbdc7170c8", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "kody-w", "tags": ["skills", "plugins", "claude-code", "copilot-cli", "agent-skills", "mcp", "hooks", "transcripts", "interop", "compat"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/host_compat_agent`. The original RAPP
agent is preserved byte-for-byte in `host_compat_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

HostCompat -- make the Brainstem speak every agent-host dialect (Claude Code,
GitHub Copilot CLI, and the open Agent Skills layout) from ONE agent file,
without teaching the kernel any of it.

Why an agent and not a kernel feature: the kernel stays "engine, not experience".
Everything host-shaped (skills, plugins, slash commands / prompts, subagent
personas, hooks, MCP servers, instruction files, session transcripts) is a
cartridge you can drop in, delete, or replace.

Hosts are data, not code: each adapter below is a table of where that host keeps
things. Adding a host is adding an entry (or a JSON file via HOST_COMPAT_HOSTS).

What it does better than the originals:
  * One catalog across hosts. A skill installed for Copilot CLI is usable from a
    Brainstem chat, and vice versa. Duplicates (same folder reachable from two
    hosts) are collapsed.
  * Progressive disclosure that fits: a capped, cached catalog goes into the
    system prompt each turn so skills auto-trigger; bodies load on demand; the
    catalog degrades (full -> short -> names-only) before it drops anything.
  * Skills are first-class tools: action="promote" compiles any SKILL.md into a
    native <slug>_agent.py; action="export" turns any agent into a SKILL.md
    folder every host can read.
  * MCP servers from every host config are callable directly (stdio and
    streamable-HTTP), no host process required.
  * Local transcript search across BOTH hosts' session history (Claude Code
    ~/.claude/projects/*.jsonl, Copilot CLI ~/.copilot/session-state/*/events.jsonl)
    through an incremental SQLite FTS index -- "what did I tell Copilot about X
    last week" answered from the Brainstem.

Everything is stdlib-only. Every subprocess has a timeout. Paths handed in by the
model are confined to the skill/plugin directory they belong to.

Environment (all optional):
  HOST_COMPAT_CLAUDE_HOME     default ~/.claude
  HOST_COMPAT_COPILOT_HOME    default ~/.copilot
  HOST_COMPAT_PROJECT         project dir scanned for .claude/ .github/ .agents/ (default cwd)
  HOST_COMPAT_ROOTS           extra colon-separated dirs containing */SKILL.md
  HOST_COMPAT_HOSTS           JSON file with extra/override host adapters
  HOST_COMPAT_STORE           installed plugins + transcript index (default ~/.brainstem/host_compat)
  HOST_COMPAT_CONTEXT_CHARS   cap on the per-turn catalog (default 6000; 0 disables)
  HOST_COMPAT_TIMEOUT         default subprocess timeout seconds (default 120)
  HOST_COMPAT_TRANSCRIPT_DAYS how far back transcripts are indexed (default 30)
  HOST_COMPAT_INDEX_BUDGET    seconds of indexing a search call may spend (default 15)

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "What to do.",
      "enum": [
        "list",
        "load",
        "read",
        "run",
        "hook",
        "mcp_tools",
        "mcp_call",
        "install",
        "uninstall",
        "promote",
        "export",
        "instructions",
        "transcripts",
        "transcript",
        "index",
        "doctor",
        "refresh"
      ],
      "type": "string"
    },
    "args": {
      "description": "For load ($ARGUMENTS), run (script args), or hook (matcher / tool name).",
      "type": "string"
    },
    "arguments": {
      "description": "For mcp_call: the tool's arguments object.",
      "type": "object"
    },
    "cwd": {
      "description": "For transcripts: only sessions whose working directory contains this text.",
      "type": "string"
    },
    "days": {
      "description": "For transcripts/index: how many days back to index (default 30).",
      "type": "integer"
    },
    "host": {
      "description": "Restrict to one host's catalog or transcripts (default all).",
      "enum": [
        "all",
        "claude-code",
        "copilot-cli",
        "agent-skills"
      ],
      "type": "string"
    },
    "kind": {
      "description": "For list: which catalog to show (default all).",
      "enum": [
        "all",
        "skills",
        "plugins",
        "commands",
        "agents",
        "hooks",
        "mcp",
        "instructions"
      ],
      "type": "string"
    },
    "limit": {
      "description": "For transcripts/transcript: max results (default 20 / 200).",
      "type": "integer"
    },
    "name": {
      "description": "Skill / command / persona / plugin / MCP server / agent / session id (plugin-qualified 'plugin:name' allowed).",
      "type": "string"
    },
    "path": {
      "description": "For read/run: file path relative to the skill or plugin directory. For export: output directory.",
      "type": "string"
    },
    "query": {
      "description": "For list: substring filter. For transcripts: the search terms (all must match).",
      "type": "string"
    },
    "role": {
      "description": "For transcripts: only messages from this role.",
      "enum": [
        "user",
        "assistant"
      ],
      "type": "string"
    },
    "source": {
      "description": "For install: local directory path or git URL of a plugin (or a bare skill folder).",
      "type": "string"
    },
    "stdin": {
      "description": "For run/hook: text (usually JSON) sent on stdin.",
      "type": "string"
    },
    "timeout": {
      "description": "Seconds to allow a script/hook/MCP call or an index pass (default 120).",
      "type": "integer"
    },
    "tool": {
      "description": "For mcp_call: the MCP tool name.",
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `host_compat_agent.py` and embedded as the fenced Python below (sha256 284c111aa88d5588…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `host_compat_agent.py` first:

```bash
python3 host_compat_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 host_compat_agent.py   # or on stdin
python3 host_compat_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/host_compat_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/host_compat_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/host_compat_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""HostCompat -- make the Brainstem speak every agent-host dialect (Claude Code,
GitHub Copilot CLI, and the open Agent Skills layout) from ONE agent file,
without teaching the kernel any of it.

Why an agent and not a kernel feature: the kernel stays "engine, not experience".
Everything host-shaped (skills, plugins, slash commands / prompts, subagent
personas, hooks, MCP servers, instruction files, session transcripts) is a
cartridge you can drop in, delete, or replace.

Hosts are data, not code: each adapter below is a table of where that host keeps
things. Adding a host is adding an entry (or a JSON file via HOST_COMPAT_HOSTS).

What it does better than the originals:
  * One catalog across hosts. A skill installed for Copilot CLI is usable from a
    Brainstem chat, and vice versa. Duplicates (same folder reachable from two
    hosts) are collapsed.
  * Progressive disclosure that fits: a capped, cached catalog goes into the
    system prompt each turn so skills auto-trigger; bodies load on demand; the
    catalog degrades (full -> short -> names-only) before it drops anything.
  * Skills are first-class tools: action="promote" compiles any SKILL.md into a
    native <slug>_agent.py; action="export" turns any agent into a SKILL.md
    folder every host can read.
  * MCP servers from every host config are callable directly (stdio and
    streamable-HTTP), no host process required.
  * Local transcript search across BOTH hosts' session history (Claude Code
    ~/.claude/projects/*.jsonl, Copilot CLI ~/.copilot/session-state/*/events.jsonl)
    through an incremental SQLite FTS index -- "what did I tell Copilot about X
    last week" answered from the Brainstem.

Everything is stdlib-only. Every subprocess has a timeout. Paths handed in by the
model are confined to the skill/plugin directory they belong to.

Environment (all optional):
  HOST_COMPAT_CLAUDE_HOME     default ~/.claude
  HOST_COMPAT_COPILOT_HOME    default ~/.copilot
  HOST_COMPAT_PROJECT         project dir scanned for .claude/ .github/ .agents/ (default cwd)
  HOST_COMPAT_ROOTS           extra colon-separated dirs containing */SKILL.md
  HOST_COMPAT_HOSTS           JSON file with extra/override host adapters
  HOST_COMPAT_STORE           installed plugins + transcript index (default ~/.brainstem/host_compat)
  HOST_COMPAT_CONTEXT_CHARS   cap on the per-turn catalog (default 6000; 0 disables)
  HOST_COMPAT_TIMEOUT         default subprocess timeout seconds (default 120)
  HOST_COMPAT_TRANSCRIPT_DAYS how far back transcripts are indexed (default 30)
  HOST_COMPAT_INDEX_BUDGET    seconds of indexing a search call may spend (default 15)
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/host_compat_agent",
    "version": "1.0.1",
    "display_name": "Host Compat",
    "description": "Makes a Brainstem speak every agent-host dialect from one file: Claude Code, GitHub Copilot CLI and open Agent Skills — skills, plugins, slash commands/prompts, subagent personas, hooks, MCP servers, instruction files — plus cross-host search of your local Claude Code and Copilot CLI session transcripts.",
    "author": "kody-w",
    "tags": ["skills", "plugins", "claude-code", "copilot-cli", "agent-skills", "mcp", "hooks", "transcripts", "interop", "compat"],
    "category": "devtools",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

import ast
import glob
import hashlib
import json
import os
import re
import shlex
import shutil
import sqlite3
import subprocess
import sys
import threading
import time
import urllib.request

try:
    from agents.basic_agent import BasicAgent
except ImportError:  # pragma: no cover - standalone / registry contract use
    try:
        from basic_agent import BasicAgent
    except ImportError:
        class BasicAgent:
            def __init__(self, name=None, metadata=None):
                self.name = getattr(self, "name", name or "BasicAgent")
                self.metadata = getattr(self, "metadata", metadata or {})

            def perform(self, **kwargs):
                return "Not implemented."

            def system_context(self):
                return None

            def to_tool(self):
                return {"type": "function", "function": {"name": self.name,
                        "description": self.metadata.get("description", ""),
                        "parameters": self.metadata.get("parameters", {"type": "object", "properties": {}})}}

# ── configuration ───────────────────────────────────────────────────────────

def _env(name, default):
    v = os.getenv(name)
    return v if v not in (None, "") else default


def _int_env(name, default):
    try:
        return int(_env(name, str(default)))
    except ValueError:
        return default


def _project_dir():
    return os.path.abspath(_env("HOST_COMPAT_PROJECT", os.getcwd()))


def _store_dir():
    return os.path.expanduser(_env("HOST_COMPAT_STORE", "~/.brainstem/host_compat"))


# ── host adapters (data, not code) ─────────────────────────────────────────
# Path templates use {home} (that host's home) and {project}. Globs allowed.

HOSTS = {
    "claude-code": {
        "display": "Claude Code",
        "home_env": "HOST_COMPAT_CLAUDE_HOME", "home": "~/.claude",
        "skills": ["{project}/.claude/skills", "{home}/skills"],
        "commands": [{"dir": "{project}/.claude/commands", "suffix": ".md"},
                     {"dir": "{home}/commands", "suffix": ".md"}],
        "agents": [{"dir": "{project}/.claude/agents", "suffix": ".md"},
                   {"dir": "{home}/agents", "suffix": ".md"}],
        "plugins": {"installed_json": "{home}/plugins/installed_plugins.json",
                    "dirs": ["{home}/plugins/cache/*/*/*"],
                    "manifests": [".claude-plugin/plugin.json", "plugin.json"],
                    "skills_subdir": "skills", "commands_subdir": "commands", "agents_subdir": "agents",
                    "hooks_files": ["hooks/hooks.json", "hooks.json"], "mcp_file": ".mcp.json"},
        "hooks": ["{project}/.claude/settings.json", "{project}/.claude/settings.local.json"],
        "mcp": [{"file": "{project}/.mcp.json", "key": "mcpServers"},
                {"file": "{home}/../.claude.json", "key": "mcpServers"}],
        "instructions": ["{project}/CLAUDE.md", "{project}/.claude/CLAUDE.md", "{home}/CLAUDE.md"],
        "transcripts": {"glob": "{home}/projects/*/*.jsonl", "format": "claude-jsonl"},
    },
    "copilot-cli": {
        "display": "GitHub Copilot CLI",
        "home_env": "HOST_COMPAT_COPILOT_HOME", "home": "~/.copilot",
        "skills": ["{project}/.github/skills", "{home}/skills"],
        "commands": [{"dir": "{project}/.github/prompts", "suffix": ".prompt.md"}],
        "agents": [{"dir": "{project}/.github/agents", "suffix": ".agent.md"},
                   {"dir": "{project}/.github/agents", "suffix": ".md"},
                   {"dir": "{home}/agents", "suffix": ".md"}],
        "plugins": {"installed_json": None,
                    "dirs": ["{home}/installed-plugins/*/*", "{home}/installed-plugins/_direct/*"],
                    "manifests": ["plugin.json", ".claude-plugin/plugin.json"],
                    "skills_subdir": "skills", "commands_subdir": "prompts", "agents_subdir": "agents",
                    "hooks_files": ["hooks/hooks.json", "hooks.json"], "mcp_file": ".mcp.json"},
        "hooks": ["{project}/.github/hooks/*.json", "{home}/hooks/*.json"],
        "mcp": [{"file": "{home}/mcp-config.json", "key": "mcpServers"},
                {"file": "{project}/.copilot/mcp-config.json", "key": "mcpServers"},
                {"file": "{project}/.vscode/mcp.json", "key": "servers"}],
        "instructions": ["{project}/AGENTS.md", "{project}/.github/copilot-instructions.md",
                         "{project}/.github/instructions/*.instructions.md"],
        "transcripts": {"glob": "{home}/session-state/*/events.jsonl", "format": "copilot-events"},
    },
    "agent-skills": {
        "display": "Open Agent Skills layout",
        "home_env": "HOST_COMPAT_AGENTS_HOME", "home": "~/.agents",
        "skills": ["{project}/.agents/skills", "{home}/skills"],
        "commands": [], "agents": [], "plugins": None, "hooks": [], "mcp": [],
        "instructions": ["{project}/AGENTS.md"], "transcripts": None,
    },
}


def _hosts():
    hosts = {k: dict(v) for k, v in HOSTS.items()}
    extra = _env("HOST_COMPAT_HOSTS", "")
    if extra and os.path.isfile(os.path.expanduser(extra)):
        try:
            for k, v in json.loads(_safe_read(os.path.expanduser(extra))).items():
                hosts.setdefault(k, {}).update(v)
        except ValueError:
            pass
    return hosts


def _host_home(host):
    return os.path.expanduser(_env(host.get("home_env", ""), host.get("home", "")))


def _fill(tpl, host):
    return os.path.normpath(os.path.expanduser(tpl.replace("{home}", _host_home(host)).replace("{project}", _project_dir())))


def _expand_paths(tpl, host):
    p = _fill(tpl, host)
    return sorted(glob.glob(p)) if any(ch in p for ch in "*?[") else [p]


# ── tiny YAML-subset frontmatter parser (no PyYAML dependency) ──────────────

_FM_RE = re.compile(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*\r?\n?", re.S)


def _unquote(s):
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        inner = s[1:-1]
        if s[0] == '"':
            inner = inner.replace('\\"', '"').replace("\\n", "\n")
        return inner
    if s in ("true", "True"):
        return True
    if s in ("false", "False"):
        return False
    if s in ("null", "~", ""):
        return None
    if s.startswith("[") and s.endswith("]"):
        return [_unquote(x) for x in s[1:-1].split(",") if x.strip()]
    return s


def _parse_frontmatter(text):
    """Return (meta_dict, body). Scalars, one-level nested maps, block lists and
    folded/literal strings -- enough for SKILL.md, prompts, agents and commands."""
    m = _FM_RE.match(text)
    if not m:
        return {}, text
    block, body = m.group(1), text[m.end():]
    meta = {}
    lines = block.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        km = re.match(r"^([A-Za-z0-9_\-\.]+)\s*:\s*(.*)$", line)
        if not km:
            i += 1
            continue
        key, rest = km.group(1), km.group(2)
        if rest in (">", "|", ">-", "|-"):
            buf = []
            i += 1
            while i < len(lines) and (lines[i].startswith(" ") or not lines[i].strip()):
                buf.append(lines[i].strip())
                i += 1
            meta[key] = (" " if rest.startswith(">") else "\n").join(buf).strip()
            continue
        if rest == "":
            sub, lst = {}, []
            i += 1
            while i < len(lines) and (lines[i].startswith(" ") or lines[i].startswith("\t")):
                s = lines[i].strip()
                if s.startswith("- "):
                    lst.append(_unquote(s[2:]))
                else:
                    sm = re.match(r"^([A-Za-z0-9_\-\.]+)\s*:\s*(.*)$", s)
                    if sm:
                        sub[sm.group(1)] = _unquote(sm.group(2))
                i += 1
            meta[key] = lst if lst else sub
            continue
        meta[key] = _unquote(rest)
        i += 1
    return meta, body


# ── helpers ────────────────────────────────────────────────────────────────

_SKILL_SUBDIRS = ("scripts", "references", "assets", "templates", "examples")


def _safe_read(path, limit=None):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.read() if limit is None else f.read(limit)
    except OSError:
        return ""


def _one_line(s):
    return re.sub(r"\s+", " ", s or "").strip()


def _clip(s, n=12000):
    s = s or ""
    return s if len(s) <= n else s[:n] + f"\n... [{len(s) - n} more chars clipped]"


def _slug(name):
    s = re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")
    return s or "skill"


def _camel(slug):
    return "".join(p.capitalize() for p in slug.split("_")) or "Skill"


def _confine(base, rel):
    """Resolve rel inside base; refuse anything that escapes."""
    base = os.path.realpath(base)
    target = os.path.realpath(os.path.join(base, rel or ""))
    if target != base and not target.startswith(base + os.sep):
        raise ValueError(f"path {rel!r} escapes {base}")
    return target


def _resource_index(sdir, limit=60):
    out = []
    for sub in _SKILL_SUBDIRS:
        p = os.path.join(sdir, sub)
        if os.path.isdir(p):
            for path in sorted(glob.glob(os.path.join(p, "**", "*"), recursive=True)):
                if os.path.isfile(path):
                    out.append(os.path.relpath(path, sdir))
    for path in sorted(glob.glob(os.path.join(sdir, "*"))):
        if os.path.isfile(path) and os.path.basename(path) != "SKILL.md":
            out.append(os.path.relpath(path, sdir))
    return out[:limit], max(0, len(out) - limit)


def _substitute_arguments(body, args):
    """Slash-command / prompt substitution: $ARGUMENTS, $1..$9, ${input:name}."""
    if isinstance(args, (list, tuple)):
        parts = [str(a) for a in args]
    elif args is None:
        parts = []
    else:
        parts = shlex.split(str(args)) if str(args).strip() else []
    joined = " ".join(parts)
    out = body.replace("$ARGUMENTS", joined).replace("${input}", joined)
    out = re.sub(r"\$\{input:([^}:]+)(?::[^}]*)?\}", joined, out)
    for i in range(1, 10):
        out = out.replace(f"${i}", parts[i - 1] if len(parts) >= i else "")
    return out


def _expand_cmd(cmd, plugin_root):
    """Expand ${CLAUDE_PLUGIN_ROOT} / ${COPILOT_PLUGIN_ROOT} plus ${VAR} / ${VAR:-default}
    from the environment, the way hosts expand .mcp.json and hooks."""
    out = cmd
    for var in ("CLAUDE_PLUGIN_ROOT", "COPILOT_PLUGIN_ROOT", "PLUGIN_ROOT"):
        out = out.replace("${" + var + "}", plugin_root or "").replace("$" + var, plugin_root or "")

    def sub(m):
        var, default = m.group(1), m.group(3)
        return os.environ.get(var, default if default is not None else m.group(0))

    return re.sub(r"\$\{([A-Za-z_][A-Za-z0-9_]*)(:-([^}]*))?\}", sub, out)


def _run_subprocess(argv, cwd, timeout, stdin_text=None, env_extra=None, shell=False):
    env = dict(os.environ)
    env.update({k: str(v) for k, v in (env_extra or {}).items()})
    started = time.time()
    try:
        proc = subprocess.run(argv, cwd=cwd, input=stdin_text, capture_output=True, text=True,
                              timeout=timeout, env=env, shell=shell)
        return {"exit": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr,
                "seconds": round(time.time() - started, 2)}
    except subprocess.TimeoutExpired as e:
        so = e.stdout.decode() if isinstance(e.stdout, bytes) else (e.stdout or "")
        return {"exit": None, "stdout": so, "stderr": f"timed out after {timeout}s", "seconds": timeout}
    except FileNotFoundError as e:
        return {"exit": 127, "stdout": "", "stderr": str(e), "seconds": 0}


def _tree_mtime(paths):
    sig = 0.0
    for p in paths:
        try:
            sig = max(sig, os.stat(p).st_mtime)
            for child in os.listdir(p):
                try:
                    sig = max(sig, os.stat(os.path.join(p, child)).st_mtime)
                except OSError:
                    pass
        except OSError:
            pass
    return sig


# ── discovery ───────────────────────────────────────────────────────────────

class _Catalog:
    """Everything host-shaped reachable from this machine, across all hosts."""

    def __init__(self):
        self.skills, self.commands, self.agents, self.plugins = {}, {}, {}, {}
        self.hooks, self.mcp, self.instructions = [], {}, []
        self.errors, self.roots = [], []
        self._seen_paths = set()

    # -- generic item registration --------------------------------------------
    def _register(self, bucket, kind, path, host, source, plugin=None, name_hint=None):
        real = os.path.realpath(path)
        if real in self._seen_paths:
            return
        meta, body = _parse_frontmatter(_safe_read(path, 200_000))
        name = str(meta.get("name") or name_hint or os.path.basename(os.path.dirname(path))).strip()
        qualified = f"{plugin}:{name}" if plugin else name
        if qualified in bucket:
            # first wins (project > user > plugins, claude before copilot) -- mirror host precedence
            return
        self._seen_paths.add(real)
        desc = str(meta.get("description") or body.strip().split("\n", 1)[0][:200]).strip()
        bucket[qualified] = {"kind": kind, "name": qualified, "short": name, "path": path,
                             "dir": os.path.dirname(path), "description": desc, "meta": meta,
                             "source": source, "plugin": plugin, "host": host}

    def _scan_skill_root(self, root, host, source, plugin=None):
        if not os.path.isdir(root):
            return
        for depth in ("*", "*/*"):
            for skill_md in sorted(glob.glob(os.path.join(root, depth, "SKILL.md"))):
                self._register(self.skills, "skill", skill_md, host, source, plugin)

    def _scan_md_dir(self, root, suffix, bucket, kind, host, source, plugin=None):
        if not os.path.isdir(root):
            return
        for path in sorted(glob.glob(os.path.join(root, "**", "*" + suffix), recursive=True)):
            rel = os.path.relpath(path, root)[: -len(suffix)].replace(os.sep, ":")
            self._register(bucket, kind, path, host, source, plugin, name_hint=rel)

    def _scan_hooks(self, hooks_json, source, plugin_root, host):
        try:
            data = json.loads(_safe_read(hooks_json))
        except ValueError:
            self.errors.append(f"invalid JSON: {hooks_json}")
            return
        hooks = data.get("hooks", data) if isinstance(data, dict) else {}
        for event, groups in (hooks or {}).items():
            if not isinstance(groups, list):
                continue
            for g in groups:
                if not isinstance(g, dict):
                    continue
                inner = g.get("hooks") if isinstance(g.get("hooks"), list) else [g] if g.get("command") else []
                for h in inner:
                    if not isinstance(h, dict) or h.get("type", "command") != "command" or not h.get("command"):
                        continue
                    self.hooks.append({"host": host, "source": source, "event": event,
                                       "matcher": g.get("matcher", ""), "command": h["command"],
                                       "timeout": h.get("timeout"), "cwd": plugin_root, "file": hooks_json})

    def _scan_mcp(self, path, source, cwd, host, key="mcpServers"):
        try:
            data = json.loads(_safe_read(path))
        except ValueError:
            self.errors.append(f"invalid JSON: {path}")
            return
        servers = data.get(key) if isinstance(data, dict) else None
        if not isinstance(servers, dict):
            return
        for name, cfg in servers.items():
            if isinstance(cfg, dict) and name not in self.mcp:
                self.mcp[name] = {"config": cfg, "source": source, "cwd": cwd, "file": path, "host": host}

    def _scan_plugins(self, hkey, host):
        spec = host.get("plugins")
        if not spec:
            return
        found, seen = [], set()

        def add(d, src):
            d = os.path.abspath(d)
            if d in seen or not os.path.isdir(d):
                return
            seen.add(d)
            found.append((d, src))

        inst = spec.get("installed_json")
        if inst:
            inst = _fill(inst, host)
            if os.path.isfile(inst):
                try:
                    data = json.loads(_safe_read(inst))
                    for entries in (data.get("plugins") or {}).values():
                        for e in entries if isinstance(entries, list) else [entries]:
                            if isinstance(e, dict) and e.get("installPath"):
                                add(e["installPath"], f"installed:{e.get('scope', '?')}")
                except ValueError:
                    self.errors.append(f"invalid JSON: {inst}")
        for tpl in spec.get("dirs", []):
            for d in _expand_paths(tpl, host):
                if any(os.path.isfile(os.path.join(d, m)) for m in spec["manifests"]):
                    add(d, "cache")
        for d in sorted(glob.glob(os.path.join(_store_dir(), "plugins", "*"))):
            if any(os.path.isfile(os.path.join(d, m)) for m in ("plugin.json", ".claude-plugin/plugin.json")):
                add(d, "brainstem-store")

        for pdir, source in found:
            manifest, mpath = None, None
            for m in list(spec["manifests"]) + ["plugin.json", ".claude-plugin/plugin.json"]:
                cand = os.path.join(pdir, m)
                if os.path.isfile(cand):
                    try:
                        manifest, mpath = json.loads(_safe_read(cand)), cand
                    except ValueError:
                        manifest, mpath = {"_error": f"invalid JSON in {cand}"}, cand
                    break
            base = os.path.basename(pdir.rstrip(os.sep))
            if re.match(r"^[0-9a-f.\-]+$", base):  # <marketplace>/<plugin>/<version> layout
                base = os.path.basename(os.path.dirname(pdir.rstrip(os.sep)))
            if manifest is None:
                manifest = {"name": base, "_bare": True}
            if "_error" in manifest:
                self.errors.append(manifest["_error"])
            pname = str(manifest.get("name") or base)
            if pname in self.plugins:
                if os.path.realpath(pdir) != os.path.realpath(self.plugins[pname]["dir"]):
                    pname = f"{pname}@{hkey}"
                    if pname in self.plugins:
                        continue
                else:
                    continue
            entry = {"name": pname, "dir": pdir, "manifest": manifest, "manifest_path": mpath, "source": source,
                     "host": hkey, "skills": [], "commands": [], "agents": [], "hooks": 0, "mcp": []}
            self.plugins[pname] = entry
            before = set(self.skills)
            self._scan_skill_root(os.path.join(pdir, spec["skills_subdir"]), hkey, f"plugin:{source}", pname)
            entry["skills"] = sorted(set(self.skills) - before)
            before = set(self.commands)
            for sub, suf in ((spec["commands_subdir"], ".md"), ("commands", ".md"), ("prompts", ".prompt.md")):
                self._scan_md_dir(os.path.join(pdir, sub), suf, self.commands, "command", hkey, f"plugin:{source}", pname)
            entry["commands"] = sorted(set(self.commands) - before)
            before = set(self.agents)
            for suf in (".agent.md", ".md"):
                self._scan_md_dir(os.path.join(pdir, spec["agents_subdir"]), suf, self.agents, "agent", hkey, f"plugin:{source}", pname)
            entry["agents"] = sorted(set(self.agents) - before)
            nh = len(self.hooks)
            for hf in spec["hooks_files"]:
                if os.path.isfile(os.path.join(pdir, hf)):
                    self._scan_hooks(os.path.join(pdir, hf), f"plugin:{pname}", pdir, hkey)
                    break
            entry["hooks"] = len(self.hooks) - nh
            before = set(self.mcp)
            mcp_file = manifest.get("mcpServers") if isinstance(manifest.get("mcpServers"), str) else spec["mcp_file"]
            mp = os.path.join(pdir, mcp_file)
            if os.path.isfile(mp):
                self._scan_mcp(mp, f"plugin:{pname}", pdir, hkey)
            elif isinstance(manifest.get("mcpServers"), dict):
                for n, cfg in manifest["mcpServers"].items():
                    self.mcp.setdefault(n, {"config": cfg, "source": f"plugin:{pname}", "cwd": pdir, "file": mpath, "host": hkey})
            entry["mcp"] = sorted(set(self.mcp) - before)

    def scan(self):
        proj = _project_dir()
        for hkey, host in _hosts().items():
            for tpl in host.get("skills", []):
                root = _fill(tpl, host)
                if os.path.isdir(root):
                    self.roots.append(root)
                    self._scan_skill_root(root, hkey, "project" if root.startswith(proj) else "user")
            for spec in host.get("commands", []):
                root = _fill(spec["dir"], host)
                self._scan_md_dir(root, spec["suffix"], self.commands, "command", hkey, "project" if root.startswith(proj) else "user")
            for spec in host.get("agents", []):
                root = _fill(spec["dir"], host)
                self._scan_md_dir(root, spec["suffix"], self.agents, "agent", hkey, "project" if root.startswith(proj) else "user")
            self._scan_plugins(hkey, host)
            for tpl in host.get("hooks", []):
                for f in _expand_paths(tpl, host):
                    if os.path.isfile(f):
                        self._scan_hooks(f, f"{hkey}:{os.path.relpath(f, proj) if f.startswith(proj) else os.path.basename(f)}", os.path.dirname(f), hkey)
            for spec in host.get("mcp", []):
                f = _fill(spec["file"], host)
                if os.path.isfile(f):
                    self._scan_mcp(f, "project" if f.startswith(proj) else f"user:{hkey}", proj, hkey, spec.get("key", "mcpServers"))
            for tpl in host.get("instructions", []):
                for f in _expand_paths(tpl, host):
                    if os.path.isfile(f) and os.path.realpath(f) not in {os.path.realpath(x["path"]) for x in self.instructions}:
                        self.instructions.append({"host": hkey, "path": f, "size": os.path.getsize(f)})
        extra = _env("HOST_COMPAT_ROOTS", "")
        for r in [os.path.expanduser(r) for r in extra.split(os.pathsep) if r.strip()]:
            if os.path.isdir(r):
                self.roots.append(r)
                self._scan_skill_root(r, "extra", "extra")
        return self

    def find(self, name, host=None):
        if not name:
            return None
        n = name.strip().lstrip("/")
        buckets = (self.skills, self.commands, self.agents)
        for pred in (lambda k, it: k == n, lambda k, it: it["short"] == n,
                     lambda k, it: k.lower() == n.lower() or it["short"].lower() == n.lower()):
            for bucket in buckets:
                for key, item in bucket.items():
                    if pred(key, item) and (not host or item["host"] == host):
                        return item
        return None


_catalog_cache = {"sig": None, "catalog": None, "built": 0.0}
_catalog_lock = threading.Lock()


def _get_catalog(force=False):
    sig_paths = []
    for host in _hosts().values():
        home = _host_home(host)
        sig_paths += [home, os.path.join(home, "skills"), os.path.join(home, "plugins"), os.path.join(home, "installed-plugins")]
    proj = _project_dir()
    sig_paths += [os.path.join(proj, ".claude"), os.path.join(proj, ".github"), os.path.join(proj, ".agents"),
                  os.path.join(_store_dir(), "plugins")]
    sig = (proj, _env("HOST_COMPAT_ROOTS", ""), _tree_mtime(sig_paths))
    with _catalog_lock:
        if not force and _catalog_cache["catalog"] is not None and _catalog_cache["sig"] == sig \
                and time.time() - _catalog_cache["built"] < 300:
            return _catalog_cache["catalog"]
        cat = _Catalog().scan()
        _catalog_cache.update({"sig": sig, "catalog": cat, "built": time.time()})
        return cat


# ── MCP client (stdio + streamable HTTP) ───────────────────────────────────

_MCP_PROTOCOL = "2025-06-18"


class _McpClient:
    def __init__(self, name, entry, timeout):
        self.name, self.cfg, self.timeout = name, entry["config"], timeout
        self.cwd = entry.get("cwd") or None
        self.proc, self._id, self._lines, self._reader = None, 0, [], None
        self._lock = threading.Lock()
        kind = (self.cfg.get("type") or ("http" if self.cfg.get("url") else "stdio")).lower()
        self.kind = "stdio" if kind in ("local", "stdio") else "http"  # copilot says "local"
        self.session_id = None

    def _start_stdio(self):
        command = _expand_cmd(str(self.cfg.get("command", "")), self.cwd)
        args = [_expand_cmd(str(a), self.cwd) for a in (self.cfg.get("args") or [])]
        env = dict(os.environ)
        env.update({k: _expand_cmd(str(v), self.cwd) for k, v in (self.cfg.get("env") or {}).items()})
        self.proc = subprocess.Popen([command] + args, cwd=self.cwd, env=env, stdin=subprocess.PIPE,
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)

        def pump():
            for line in self.proc.stdout:
                with self._lock:
                    self._lines.append(line)

        self._reader = threading.Thread(target=pump, daemon=True)
        self._reader.start()

    def _rpc(self, method, params=None, notify=False):
        msg = {"jsonrpc": "2.0", "method": method}
        if params is not None:
            msg["params"] = params
        if not notify:
            self._id += 1
            msg["id"] = self._id
        return self._rpc_stdio(msg, notify) if self.kind == "stdio" else self._rpc_http(msg, notify)

    def _rpc_stdio(self, msg, notify):
        if self.proc is None:
            self._start_stdio()
        if self.proc.poll() is not None:
            raise RuntimeError(f"MCP server {self.name!r} exited early: {(self.proc.stderr.read() or '')[:500]}")
        self.proc.stdin.write(json.dumps(msg) + "\n")
        self.proc.stdin.flush()
        if notify:
            return None
        deadline = time.time() + self.timeout
        while time.time() < deadline:
            with self._lock:
                pending, self._lines = self._lines, []
            for line in pending:
                try:
                    obj = json.loads(line.strip()) if line.strip() else None
                except ValueError:
                    continue
                if obj and obj.get("id") == msg["id"]:
                    if "error" in obj:
                        raise RuntimeError(f"MCP error from {self.name!r}: {json.dumps(obj['error'])[:800]}")
                    return obj.get("result")
            if self.proc.poll() is not None:
                raise RuntimeError(f"MCP server {self.name!r} exited: {(self.proc.stderr.read() or '')[:500]}")
            time.sleep(0.02)
        raise RuntimeError(f"MCP server {self.name!r} did not answer {msg['method']} within {self.timeout}s")

    def _rpc_http(self, msg, notify):
        url = _expand_cmd(str(self.cfg.get("url", "")), self.cwd)
        headers = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
        headers.update({k: _expand_cmd(str(v), self.cwd) for k, v in (self.cfg.get("headers") or {}).items()})
        if self.session_id:
            headers["Mcp-Session-Id"] = self.session_id
        req = urllib.request.Request(url, data=json.dumps(msg).encode(), headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=self.timeout) as resp:
            self.session_id = resp.headers.get("Mcp-Session-Id") or self.session_id
            raw = resp.read().decode("utf-8", "replace")
            ctype = resp.headers.get("Content-Type", "")
        if notify:
            return None
        payloads = [ln[5:].strip() for ln in raw.splitlines() if ln.startswith("data:")] if "text/event-stream" in ctype else [raw]
        for p in payloads:
            try:
                obj = json.loads(p)
            except ValueError:
                continue
            if obj.get("id") == msg["id"]:
                if "error" in obj:
                    raise RuntimeError(f"MCP error from {self.name!r}: {json.dumps(obj['error'])[:800]}")
                return obj.get("result")
        raise RuntimeError(f"MCP server {self.name!r}: no response for {msg['method']}")

    def initialize(self):
        res = self._rpc("initialize", {"protocolVersion": _MCP_PROTOCOL, "capabilities": {},
                                       "clientInfo": {"name": "rapp-brainstem-host-compat", "version": "1.0"}})
        self._rpc("notifications/initialized", {}, notify=True)
        return res or {}

    def list_tools(self):
        tools, cursor = [], None
        for _ in range(20):
            res = self._rpc("tools/list", {"cursor": cursor} if cursor else {}) or {}
            tools.extend(res.get("tools") or [])
            cursor = res.get("nextCursor")
            if not cursor:
                break
        return tools

    def call_tool(self, tool, arguments):
        return self._rpc("tools/call", {"name": tool, "arguments": arguments or {}}) or {}

    def close(self):
        if self.proc and self.proc.poll() is None:
            try:
                self.proc.terminate()
                self.proc.wait(timeout=3)
            except Exception:
                try:
                    self.proc.kill()
                except Exception:
                    pass


# ── transcript index (both hosts, incremental, FTS5 when available) ────────

_MSG_CAP = 6000


def _iter_claude_jsonl(path):
    """Yield (role, ts, cwd, text, title) from a Claude Code session file."""
    title = ""
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            # "type" is rarely the first key in Claude's lines; a whole-line substring test is
            # still far cheaper than json.loads on every tool-result line.
            if not any(k in line for k in ('"type":"user"', '"type":"assistant"', '"type":"summary"',
                                           '"type": "user"', '"type": "assistant"', '"type": "summary"')):
                continue
            try:
                d = json.loads(line)
            except ValueError:
                continue
            t = d.get("type")
            if t == "summary":
                title = str(d.get("summary") or title)
                continue
            if t not in ("user", "assistant") or d.get("isMeta"):
                continue
            content = (d.get("message") or {}).get("content")
            if isinstance(content, str):
                text = content
            elif isinstance(content, list):
                text = "\n".join(str(c.get("text", "")) for c in content
                                 if isinstance(c, dict) and c.get("type") == "text")
            else:
                text = ""
            text = text.strip()
            if not text or text.startswith("<command-name>") or text.startswith("<local-command-stdout>"):
                continue
            yield t, str(d.get("timestamp", "")), str(d.get("cwd", "")), text[:_MSG_CAP], title


def _iter_copilot_events(path):
    """Yield (role, ts, cwd, text, title) from a Copilot CLI events.jsonl."""
    cwd, title = "", ""
    ws = os.path.join(os.path.dirname(path), "workspace.yaml")
    for line in _safe_read(ws, 4000).splitlines():
        if line.startswith("cwd:"):
            cwd = line[4:].strip()
        elif line.startswith("name:"):
            title = line[5:].strip()
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            head = line[:60]
            if '"user.message"' not in head and '"assistant.message"' not in head and '"session.start"' not in head:
                continue
            try:
                d = json.loads(line)
            except ValueError:
                continue
            t, data = d.get("type"), d.get("data") or {}
            if t == "session.start":
                cwd = cwd or str((data.get("context") or {}).get("cwd", ""))
                continue
            text = str(data.get("content") or "").strip()
            if not text:
                continue
            role = "user" if t == "user.message" else "assistant"
            yield role, str(d.get("timestamp", "")), cwd, text[:_MSG_CAP], title


_TRANSCRIPT_FORMATS = {"claude-jsonl": _iter_claude_jsonl, "copilot-events": _iter_copilot_events}


class _TranscriptIndex:
    def __init__(self, db_path):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.db = sqlite3.connect(db_path, timeout=30)
        self.db.execute("PRAGMA journal_mode=WAL")
        self.db.execute("CREATE TABLE IF NOT EXISTS files (path TEXT PRIMARY KEY, host TEXT, session TEXT, mtime REAL, size INTEGER, cwd TEXT, title TEXT, messages INTEGER)")
        try:
            self.db.execute("CREATE VIRTUAL TABLE IF NOT EXISTS msgs USING fts5(text, host UNINDEXED, session UNINDEXED, role UNINDEXED, ts UNINDEXED, cwd UNINDEXED, path UNINDEXED, title UNINDEXED)")
            self.fts = True
        except sqlite3.OperationalError:
            self.db.execute("CREATE TABLE IF NOT EXISTS msgs (text, host, session, role, ts, cwd, path, title)")
            self.fts = False
        self.db.commit()

    def candidates(self, days):
        """Newest-first list of (path, host, fmt, mtime, size) inside the window."""
        cutoff = time.time() - days * 86400
        out = []
        for hkey, host in _hosts().items():
            spec = host.get("transcripts")
            if not spec:
                continue
            fmt = spec["format"]
            for p in _expand_paths(spec["glob"], host):
                try:
                    st = os.stat(p)
                except OSError:
                    continue
                if st.st_mtime >= cutoff and st.st_size > 0:
                    out.append((p, hkey, fmt, st.st_mtime, st.st_size))
        # newest-first PER HOST, then interleaved, so a host with few large files (Claude Code)
        # is never starved by a host with tens of thousands of small ones (Copilot CLI).
        by_host = {}
        for r in sorted(out, key=lambda r: -r[3]):
            by_host.setdefault(r[1], []).append(r)
        merged, queues = [], list(by_host.values())
        while queues:
            for q in list(queues):
                merged.append(q.pop(0))
                if not q:
                    queues.remove(q)
        return merged

    def refresh(self, days, budget_seconds):
        """Index changed/new files newest-first until the time budget runs out."""
        started = time.time()
        cands = self.candidates(days)
        known = {r[0]: (r[1], r[2]) for r in self.db.execute("SELECT path, mtime, size FROM files")}
        todo = [c for c in cands if known.get(c[0]) != (c[3], c[4])]
        done = 0
        for path, hkey, fmt, mtime, size in todo:
            if time.time() - started > budget_seconds:
                break
            session = os.path.basename(os.path.dirname(path)) if fmt == "copilot-events" else os.path.basename(path)[:-6]
            rows, cwd, title = [], "", ""
            try:
                for role, ts, c, text, t in _TRANSCRIPT_FORMATS[fmt](path):
                    cwd, title = c or cwd, t or title
                    rows.append((text, hkey, session, role, ts, cwd, path, title))
            except OSError:
                continue
            rows = [(r[0], r[1], r[2], r[3], r[4], r[5] or cwd, r[6], title) for r in rows]
            with self.db:
                self.db.execute("DELETE FROM msgs WHERE path = ?", (path,))
                self.db.executemany("INSERT INTO msgs (text, host, session, role, ts, cwd, path, title) VALUES (?,?,?,?,?,?,?,?)", rows)
                self.db.execute("INSERT OR REPLACE INTO files VALUES (?,?,?,?,?,?,?,?)",
                                (path, hkey, session, mtime, size, cwd, title, len(rows)))
            done += 1
        return {"indexed_now": done, "pending": max(0, len(todo) - done), "in_window": len(cands),
                "seconds": round(time.time() - started, 1)}

    def stats(self):
        files = self.db.execute("SELECT host, COUNT(*), COALESCE(SUM(messages),0) FROM files GROUP BY host").fetchall()
        return {h: {"sessions": n, "messages": m} for h, n, m in files}

    def search(self, query, host=None, role=None, cwd=None, limit=20, since_iso=None):
        where, params = [], []
        if since_iso:
            where.append("ts >= ?")
            params.append(since_iso)
        if host:
            where.append("host = ?")
            params.append(host)
        if role:
            where.append("role = ?")
            params.append(role)
        if cwd:
            where.append("cwd LIKE ?")
            params.append(f"%{cwd}%")
        if self.fts:
            toks = [t for t in re.findall(r"[\w'\-]+", query) if t]
            match = " ".join('"' + t.replace('"', '""') + '"' for t in toks) or '""'
            sql = ("SELECT host, session, role, ts, cwd, path, title, snippet(msgs, 0, '>>', '<<', ' … ', 24) "
                   "FROM msgs WHERE msgs MATCH ? " + "".join(" AND " + w for w in where) + " ORDER BY ts DESC LIMIT ?")
            params = [match] + params + [limit]
        else:
            like = f"%{query}%"
            sql = ("SELECT host, session, role, ts, cwd, path, title, substr(text, 1, 240) FROM msgs WHERE text LIKE ? "
                   + "".join(" AND " + w for w in where) + " ORDER BY ts DESC LIMIT ?")
            params = [like] + params + [limit]
        return self.db.execute(sql, params).fetchall()

    def session(self, session, limit=200):
        rows = self.db.execute("SELECT role, ts, text, cwd, title, host, path FROM msgs WHERE session LIKE ? ORDER BY ts LIMIT ?",
                               (session + "%", limit)).fetchall()
        return rows

    def close(self):
        self.db.close()


# ── promoted-agent template (skill -> native brainstem tool) ───────────────

_PROMOTED_TEMPLATE = '''"""{class_name} -- skill {skill_name!r} promoted into a native RAPP agent.

Generated by HostCompat (action="promote"). Self-contained: the SKILL.md body is
embedded, and bundled scripts still run from the original skill directory when it
exists. Regenerate with HostCompat rather than editing the embedded body.
Skill sha256: {sha}
"""

import json
import os
import shlex
import subprocess

from agents.basic_agent import BasicAgent

SKILL_DIR = {skill_dir!r}
SKILL_BODY = {body!r}
SKILL_META = {meta!r}


class {class_name}(BasicAgent):
    def __init__(self):
        self.name = {tool_name!r}
        self.metadata = {{
            "name": self.name,
            "description": {description!r},
            "parameters": {{
                "type": "object",
                "properties": {{
                    "task": {{"type": "string", "description": "What the user wants done with this skill (free text)."}},
                    "script": {{"type": "string", "description": "Optional: relative path of a bundled script to run (e.g. scripts/x.py)."}},
                    "args": {{"type": "string", "description": "Optional shell-style arguments for the script."}},
                    "read": {{"type": "string", "description": "Optional: relative path of a bundled reference file to return."}}
                }},
                "required": []
            }}
        }}
        super().__init__(self.name, self.metadata)  # works with both BasicAgent signatures

    def _confine(self, rel):
        base = os.path.realpath(SKILL_DIR)
        target = os.path.realpath(os.path.join(base, rel))
        if target != base and not target.startswith(base + os.sep):
            raise ValueError("path escapes the skill directory")
        return target

    def perform(self, task="", script="", args="", read="", **_):
        if read:
            try:
                with open(self._confine(read), "r", encoding="utf-8", errors="replace") as f:
                    return f.read()[:40000]
            except (OSError, ValueError) as e:
                return "Cannot read " + read + ": " + str(e)
        if script:
            try:
                path = self._confine(script)
            except ValueError as e:
                return str(e)
            argv = [path] + shlex.split(args or "")
            if path.endswith(".py"):
                argv = ["python3"] + argv
            elif path.endswith(".sh"):
                argv = ["bash"] + argv
            try:
                p = subprocess.run(argv, cwd=SKILL_DIR, capture_output=True, text=True, timeout=120)
                return json.dumps({{"exit": p.returncode, "stdout": p.stdout[-8000:], "stderr": p.stderr[-2000:]}}, indent=2)
            except subprocess.TimeoutExpired:
                return "script timed out after 120s"
        resources = []
        if os.path.isdir(SKILL_DIR):
            for root, _dirs, files in os.walk(SKILL_DIR):
                for fn in files:
                    if fn != "SKILL.md":
                        resources.append(os.path.relpath(os.path.join(root, fn), SKILL_DIR))
        header = "# Skill: " + {skill_name!r} + "\\n"
        if task:
            header += "User task: " + task + "\\n"
        if resources:
            header += "Bundled files (pass read=<path> or script=<path>): " + ", ".join(sorted(resources)[:40]) + "\\n"
        return header + "\\n" + SKILL_BODY
'''


# ── the agent ──────────────────────────────────────────────────────────────

_ACTIONS = ["list", "load", "read", "run", "hook", "mcp_tools", "mcp_call", "install", "uninstall",
            "promote", "export", "instructions", "transcripts", "transcript", "index", "doctor", "refresh"]


class HostCompatAgent(BasicAgent):
    def __init__(self):
        self.name = "HostCompat"
        self.metadata = {
            "name": self.name,
            "description": (
                "Bridge to everything agent-host-shaped on this machine, across Claude Code, GitHub Copilot CLI and "
                "the open Agent Skills layout: skills (SKILL.md), plugins, slash commands / prompts, subagent personas, "
                "hooks, MCP servers, instruction files (CLAUDE.md, AGENTS.md, copilot-instructions.md) and local "
                "session transcripts. action='list' shows what exists; 'load' pulls a skill/command/persona's "
                "instructions into the conversation before doing that kind of work; 'read' returns a bundled file; "
                "'run' executes a skill's bundled script; 'mcp_tools'/'mcp_call' use an MCP server; 'install' adds a "
                "plugin from a path or git URL; 'promote' compiles a skill into a native Brainstem agent; 'export' "
                "turns an agent into a SKILL.md; 'hook' fires a hook; 'instructions' returns the project's instruction "
                "files; 'transcripts' searches the user's own past CODING-ASSISTANT CHAT HISTORY — Claude Code and "
                "GitHub Copilot CLI session logs on this machine — across both hosts at once (query=...; this is the "
                "tool for 'what did I ask Claude/Copilot about X', 'find my earlier session where...', NOT for meeting "
                "or call transcripts); 'transcript' reads one session by id; 'index' backfills the session index; "
                "'doctor' is a health report."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": _ACTIONS, "description": "What to do."},
                    "name": {"type": "string", "description": "Skill / command / persona / plugin / MCP server / agent / session id (plugin-qualified 'plugin:name' allowed)."},
                    "host": {"type": "string", "enum": ["all", "claude-code", "copilot-cli", "agent-skills"],
                             "description": "Restrict to one host's catalog or transcripts (default all)."},
                    "kind": {"type": "string", "enum": ["all", "skills", "plugins", "commands", "agents", "hooks", "mcp", "instructions"],
                             "description": "For list: which catalog to show (default all)."},
                    "query": {"type": "string", "description": "For list: substring filter. For transcripts: the search terms (all must match)."},
                    "path": {"type": "string", "description": "For read/run: file path relative to the skill or plugin directory. For export: output directory."},
                    "args": {"type": "string", "description": "For load ($ARGUMENTS), run (script args), or hook (matcher / tool name)."},
                    "stdin": {"type": "string", "description": "For run/hook: text (usually JSON) sent on stdin."},
                    "tool": {"type": "string", "description": "For mcp_call: the MCP tool name."},
                    "arguments": {"type": "object", "description": "For mcp_call: the tool's arguments object."},
                    "source": {"type": "string", "description": "For install: local directory path or git URL of a plugin (or a bare skill folder)."},
                    "role": {"type": "string", "enum": ["user", "assistant"], "description": "For transcripts: only messages from this role."},
                    "cwd": {"type": "string", "description": "For transcripts: only sessions whose working directory contains this text."},
                    "days": {"type": "integer", "description": "For transcripts/index: how many days back to index (default 30)."},
                    "limit": {"type": "integer", "description": "For transcripts/transcript: max results (default 20 / 200)."},
                    "timeout": {"type": "integer", "description": "Seconds to allow a script/hook/MCP call or an index pass (default 120)."},
                },
                "required": ["action"],
            },
        }
        super().__init__(self.name, self.metadata)  # works with both BasicAgent signatures

    # -- system prompt catalog (progressive disclosure, capped, degrades gracefully)
    def system_context(self):
        cap = _int_env("HOST_COMPAT_CONTEXT_CHARS", 6000)
        if cap <= 0:
            return None
        try:
            cat = _get_catalog()
        except Exception as e:  # never break /chat
            return f"<host_compat>catalog unavailable: {e}</host_compat>"
        if not (cat.skills or cat.commands or cat.agents or cat.mcp):
            return None
        head = ("<host_compat>\nSkills, commands, personas and MCP servers from Claude Code and GitHub Copilot CLI are "
                "available through the HostCompat tool. When a task matches an entry below, call "
                "HostCompat(action=\"load\", name=...) FIRST and follow the returned instructions; action=\"list\" "
                "with a query shows the full catalog. For questions about the user's PAST CLAUDE CODE OR COPILOT CLI "
                "CHATS (\"what did I ask Copilot about X\", \"find my session where...\"), call "
                "HostCompat(action=\"transcripts\", query=...) — it searches both hosts' session logs at once.\n")
        tail = "</host_compat>"
        budget = cap - len(head) - len(tail) - 64

        def render(desc_len):
            lines = []

            def section(label, items):
                if not items:
                    return
                if desc_len == 0:
                    lines.append(f"{label} ({len(items)}): " + ", ".join(items))
                    return
                lines.append(f"{label} ({len(items)}):")
                for key, item in items.items():
                    d = _one_line(item.get("description", "")).split(". ")[0][:desc_len]
                    lines.append(f"- {key}: {d}" if d else f"- {key}")

            section("Skills", cat.skills)
            section("Slash commands / prompts", cat.commands)
            section("Subagent personas", cat.agents)
            if cat.mcp:
                lines.append(f"MCP servers ({len(cat.mcp)}): " + ", ".join(sorted(cat.mcp)) + "  (action=\"mcp_tools\" then \"mcp_call\")")
            return lines

        out = None
        for desc_len in (90, 50, 0):  # a dropped skill can never auto-trigger, so drop last
            lines = render(desc_len)
            if sum(len(ln) + 1 for ln in lines) <= budget:
                out = lines
                break
        if out is None:
            out, used, dropped = [], 0, 0
            for ln in lines:
                if used + len(ln) + 1 > budget:
                    dropped += 1
                    continue
                out.append(ln)
                used += len(ln) + 1
            if dropped:
                out.append(f"(+{dropped} more entries; use action=\"list\" to see them)")
        return head + "\n".join(out) + "\n" + tail

    # -- dispatch ------------------------------------------------------------
    def perform(self, action="list", operation=None, **kw):
        action = operation or action or "list"  # RAR convention is `operation`; both work
        handler = getattr(self, f"_do_{action}", None)
        if handler is None:
            return f"Unknown action {action!r}. Valid: {', '.join(_ACTIONS)}."
        try:
            return handler(**kw)
        except Exception as e:
            return f"HostCompat {action} failed: {type(e).__name__}: {e}"

    def _timeout(self, kw, cap=600):
        try:
            t = int(kw.get("timeout")) if kw.get("timeout") is not None else _int_env("HOST_COMPAT_TIMEOUT", 120)
        except (TypeError, ValueError):
            t = _int_env("HOST_COMPAT_TIMEOUT", 120)
        return max(1, min(t, cap))

    @staticmethod
    def _host_filter(host):
        return None if not host or host == "all" else host

    # -- list ----------------------------------------------------------------
    def _do_list(self, kind="all", query="", host="", **_):
        cat = _get_catalog()
        q, hf = (query or "").lower().strip(), self._host_filter(host)
        kind = (kind or "all").lower()

        def ok(item):
            if hf and item.get("host") != hf:
                return False
            return not q or q in item["name"].lower() or q in item.get("description", "").lower()

        def row(i, prefix=""):
            return f"- {prefix}{i['name']} [{i['host']}/{i['source']}] — {_one_line(i['description'])[:160]}"

        out = []
        if kind in ("all", "skills"):
            rows = [i for i in cat.skills.values() if ok(i)]
            out.append(f"## Skills ({len(rows)})")
            out += [row(i) for i in rows]
        if kind in ("all", "commands"):
            rows = [i for i in cat.commands.values() if ok(i)]
            out.append(f"\n## Slash commands / prompts ({len(rows)})")
            out += [row(i, "/") for i in rows]
        if kind in ("all", "agents"):
            rows = [i for i in cat.agents.values() if ok(i)]
            out.append(f"\n## Subagent personas ({len(rows)})")
            out += [row(i) for i in rows]
        if kind in ("all", "plugins"):
            rows = [p for p in cat.plugins.values() if (not hf or p["host"] == hf) and
                    (not q or q in p["name"].lower() or q in str(p["manifest"].get("description", "")).lower())]
            out.append(f"\n## Plugins ({len(rows)})")
            for p in rows:
                m = p["manifest"]
                out.append(f"- {p['name']} v{m.get('version', '?')} [{p['host']}/{p['source']}] — {str(m.get('description', ''))[:140]}"
                           f" | skills={len(p['skills'])} commands={len(p['commands'])} agents={len(p['agents'])} hooks={p['hooks']} mcp={len(p['mcp'])}")
        if kind in ("all", "hooks"):
            rows = [h for h in cat.hooks if (not hf or h["host"] == hf) and
                    (not q or q in h["event"].lower() or q in h["command"].lower() or q in h["source"].lower())]
            out.append(f"\n## Hooks ({len(rows)})")
            out += [f"- {h['event']}" + (f"[{h['matcher']}]" if h["matcher"] else "") + f" ({h['host']}/{h['source']}): {h['command'][:120]}" for h in rows]
        if kind in ("all", "mcp"):
            rows = {n: e for n, e in cat.mcp.items() if (not hf or e["host"] == hf) and (not q or q in n.lower())}
            out.append(f"\n## MCP servers ({len(rows)})")
            for n, e in rows.items():
                c = e["config"]
                what = c.get("url") or " ".join([str(c.get("command", ""))] + [str(a) for a in c.get("args", [])])
                out.append(f"- {n} [{e['host']}/{e['source']}] {c.get('type') or ('http' if c.get('url') else 'stdio')}: {what[:120]}")
        if kind in ("all", "instructions"):
            rows = [i for i in cat.instructions if (not hf or i["host"] == hf) and (not q or q in i["path"].lower())]
            out.append(f"\n## Instruction files ({len(rows)})")
            out += [f"- {i['path']} [{i['host']}] {i['size']} bytes" for i in rows]
        if cat.errors:
            out.append("\n## Parse errors")
            out += [f"- {e}" for e in cat.errors[:20]]
        return "\n".join(out).strip() or "Nothing host-shaped found."

    # -- load ----------------------------------------------------------------
    def _do_load(self, name="", args="", host="", **_):
        cat = _get_catalog()
        item = cat.find(name, self._host_filter(host))
        if item is None:
            near = [k for k in list(cat.skills) + list(cat.commands) + list(cat.agents)
                    if name and name.lower().replace("/", "") in k.lower()][:8]
            return f"No skill/command/persona named {name!r}." + (f" Close matches: {', '.join(near)}" if near else " Try action='list'.")
        meta, body = _parse_frontmatter(_safe_read(item["path"], 400_000))
        body = body.strip()
        if item["kind"] == "command":
            body = _substitute_arguments(body, args)
        lines = [f"# {item['kind'].capitalize()}: {item['name']}", f"Host: {item['host']}", f"Source: {item['path']}"]
        if item.get("plugin"):
            lines.append(f"Plugin: {item['plugin']}")
        for k in ("allowed-tools", "tools", "model", "argument-hint", "mode", "compatibility", "license"):
            if meta.get(k):
                lines.append(f"{k}: {meta[k]}")
        if item["kind"] == "agent":
            lines.append("Use this as a persona: adopt the instructions below for the current task, then answer as that agent.")
        elif item["kind"] == "command":
            lines.append("This is a slash-command / prompt file; treat the text below as the user's instruction.")
        else:
            files, extra = _resource_index(item["dir"])
            if files:
                lines.append("Bundled files (action='read' path=<file> for references, action='run' path=<script> to execute): "
                             + ", ".join(files) + (f", +{extra} more" if extra else ""))
        return "\n".join(lines) + "\n\n" + _clip(body, 60_000)

    # -- read / run ----------------------------------------------------------
    def _resolve_dir(self, name, host=""):
        cat = _get_catalog()
        item = cat.find(name, self._host_filter(host))
        if item is not None:
            return item["dir"], item
        p = cat.plugins.get((name or "").strip())
        if p:
            return p["dir"], p
        raise ValueError(f"unknown skill/command/persona/plugin {name!r}")

    def _do_read(self, name="", path="", host="", **_):
        base, _item = self._resolve_dir(name, host)
        target = _confine(base, path)
        if os.path.isdir(target):
            return f"Directory {path or '.'} in {name}:\n" + "\n".join(sorted(os.listdir(target))[:200])
        if not os.path.isfile(target):
            return f"No file {path!r} in {name}."
        return _clip(_safe_read(target, 400_000), 60_000)

    def _do_run(self, name="", path="", args="", stdin=None, host="", **kw):
        base, item = self._resolve_dir(name, host)
        if not path:
            files, _ = _resource_index(base)
            scripts = [f for f in files if f.startswith("scripts" + os.sep) or f.endswith((".py", ".sh", ".js", ".ts"))]
            return "Pass path=<script>. Runnable files: " + (", ".join(scripts) if scripts else "none found")
        target = _confine(base, path)
        if not os.path.isfile(target):
            return f"No script {path!r} in {name}."
        extra = shlex.split(args) if isinstance(args, str) and args.strip() else [str(a) for a in args] if isinstance(args, (list, tuple)) else []
        argv = [target] + extra
        if target.endswith(".py"):
            argv = [sys.executable] + argv
        elif target.endswith(".sh"):
            argv = ["bash"] + argv
        elif target.endswith((".js", ".mjs")):
            argv = ["node"] + argv
        elif not os.access(target, os.X_OK):
            argv = ["bash"] + argv
        plugin_root = base
        if isinstance(item, dict) and item.get("plugin"):
            plugin_root = _get_catalog().plugins.get(item["plugin"], {}).get("dir", base)
        res = _run_subprocess(argv, cwd=base, timeout=self._timeout(kw), stdin_text=stdin,
                              env_extra={"CLAUDE_PLUGIN_ROOT": plugin_root, "COPILOT_PLUGIN_ROOT": plugin_root,
                                         "CLAUDE_SKILL_DIR": base, "SKILL_DIR": base})
        return json.dumps({"command": " ".join(shlex.quote(a) for a in argv), "cwd": base, "exit": res["exit"],
                           "seconds": res["seconds"], "stdout": _clip(res["stdout"], 20_000),
                           "stderr": _clip(res["stderr"], 6_000)}, indent=2)

    # -- hooks ---------------------------------------------------------------
    def _do_hook(self, name="", args="", stdin=None, host="", **kw):
        cat = _get_catalog()
        event, hf = (name or "").strip(), self._host_filter(host)
        if not event:
            return "Pass name=<event> (e.g. Stop, PreToolUse, PostToolUse, UserPromptSubmit, SessionStart)."
        want = [h for h in cat.hooks if h["event"].lower() == event.lower() and (not hf or h["host"] == hf)]
        if args:
            want = [h for h in want if not h["matcher"] or re.search(h["matcher"], str(args))]
        if not want:
            return f"No hooks registered for event {event!r}" + (f" matching {args!r}" if args else "") + "."
        payload = stdin if stdin is not None else json.dumps({"hook_event_name": event, "session_id": "brainstem",
                                                              "cwd": _project_dir(), "tool_name": args or ""})
        results = []
        for h in want:
            cmd = _expand_cmd(h["command"], h["cwd"])
            t = h.get("timeout") or self._timeout(kw)
            res = _run_subprocess(cmd, cwd=h["cwd"], timeout=min(int(t), 600), stdin_text=payload,
                                  env_extra={"CLAUDE_PLUGIN_ROOT": h["cwd"], "COPILOT_PLUGIN_ROOT": h["cwd"]}, shell=True)
            results.append({"host": h["host"], "source": h["source"], "event": h["event"], "matcher": h["matcher"],
                            "command": cmd, "exit": res["exit"], "stdout": _clip(res["stdout"], 8000), "stderr": _clip(res["stderr"], 3000)})
        return json.dumps(results, indent=2)

    # -- MCP -----------------------------------------------------------------
    def _mcp(self, name, kw):
        cat = _get_catalog()
        entry = cat.mcp.get((name or "").strip())
        if entry is None:
            return None, f"No MCP server named {name!r}. Known: {', '.join(sorted(cat.mcp)) or 'none'}."
        return _McpClient(name, entry, self._timeout(kw)), None

    def _do_mcp_tools(self, name="", **kw):
        client, err = self._mcp(name, kw)
        if err:
            return err
        try:
            info = client.initialize()
            tools = client.list_tools()
        finally:
            client.close()
        si = info.get("serverInfo", {})
        lines = [f"MCP server {name} ({si.get('name', '?')} {si.get('version', '')}) — {len(tools)} tool(s):"]
        for t in tools:
            props = list(((t.get("inputSchema") or {}).get("properties") or {}).keys())
            lines.append(f"- {t.get('name')}: {_one_line(t.get('description', ''))[:160]}" + (f"  args: {', '.join(props[:12])}" if props else ""))
        return "\n".join(lines)

    def _do_mcp_call(self, name="", tool="", arguments=None, **kw):
        if not tool:
            return "Pass tool=<name> (see action='mcp_tools')."
        if isinstance(arguments, str):
            try:
                arguments = json.loads(arguments) if arguments.strip() else {}
            except ValueError:
                return "arguments must be a JSON object"
        client, err = self._mcp(name, kw)
        if err:
            return err
        try:
            client.initialize()
            res = client.call_tool(tool, arguments or {})
        finally:
            client.close()
        parts = [c.get("text", "") if c.get("type") == "text" else f"[{c.get('type')} content omitted]" for c in (res.get("content") or [])]
        text = "\n".join(parts) if parts else json.dumps(res.get("structuredContent", res), indent=2)
        return ("ERROR from tool: " if res.get("isError") else "") + _clip(text, 40_000)

    # -- install / uninstall -------------------------------------------------
    def _do_install(self, source="", name="", **kw):
        if not source:
            return "Pass source=<local path or git URL>."
        store = os.path.join(_store_dir(), "plugins")
        os.makedirs(store, exist_ok=True)
        src = os.path.expanduser(source)
        if re.match(r"^(https?://|git@|ssh://)", source) or source.endswith(".git"):
            tmp = os.path.join(_store_dir(), "tmp_clone_" + hashlib.sha1(source.encode()).hexdigest()[:8])
            shutil.rmtree(tmp, ignore_errors=True)
            res = _run_subprocess(["git", "clone", "--depth", "1", source, tmp], cwd=_store_dir(), timeout=self._timeout(kw))
            if res["exit"] != 0:
                return f"git clone failed: {res['stderr'][:500]}"
            src = tmp
        if not os.path.isdir(src):
            return f"Source {source!r} is not a directory."
        manifest = None
        for m in (".claude-plugin/plugin.json", "plugin.json"):
            if os.path.isfile(os.path.join(src, m)):
                try:
                    manifest = json.loads(_safe_read(os.path.join(src, m)))
                except ValueError:
                    return f"{os.path.join(src, m)} is not valid JSON."
                break
        if manifest is None:
            if os.path.isfile(os.path.join(src, "SKILL.md")):
                meta, _b = _parse_frontmatter(_safe_read(os.path.join(src, "SKILL.md")))
                sname = str(meta.get("name") or os.path.basename(src.rstrip(os.sep)))
                pname = name or sname
                dest = os.path.join(store, pname)
                shutil.rmtree(dest, ignore_errors=True)
                os.makedirs(os.path.join(dest, "skills"), exist_ok=True)
                shutil.copytree(src, os.path.join(dest, "skills", sname))
                with open(os.path.join(dest, "plugin.json"), "w") as f:
                    json.dump({"name": pname, "version": "0.0.0", "description": str(meta.get("description", ""))[:300],
                               "_wrapped_by": "HostCompat"}, f, indent=2)
                _get_catalog(force=True)
                return f"Installed bare skill {sname!r} as plugin {pname!r} at {dest}"
            return f"{src} has no plugin.json/.claude-plugin/plugin.json and no SKILL.md."
        pname = name or str(manifest.get("name") or os.path.basename(src.rstrip(os.sep)))
        dest = os.path.join(store, pname)
        shutil.rmtree(dest, ignore_errors=True)
        shutil.copytree(src, dest, ignore=shutil.ignore_patterns(".git", "node_modules", "__pycache__", ".in_use"))
        if src.startswith(os.path.join(_store_dir(), "tmp_clone_")):
            shutil.rmtree(src, ignore_errors=True)
        cat = _get_catalog(force=True)
        p = cat.plugins.get(pname, {})
        return (f"Installed plugin {pname!r} v{manifest.get('version', '?')} at {dest}: skills={len(p.get('skills', []))} "
                f"commands={len(p.get('commands', []))} agents={len(p.get('agents', []))} hooks={p.get('hooks', 0)} mcp={len(p.get('mcp', []))}")

    def _do_uninstall(self, name="", **_):
        dest = os.path.join(_store_dir(), "plugins", (name or "").strip())
        if not name or not os.path.isdir(dest):
            return f"No Brainstem-installed plugin named {name!r} (only plugins installed via action='install' can be removed here)."
        shutil.rmtree(dest)
        _get_catalog(force=True)
        return f"Removed plugin {name!r} from {dest}"

    # -- promote (skill -> native agent) -------------------------------------
    def _do_promote(self, name="", host="", **_):
        cat = _get_catalog()
        item = cat.find(name, self._host_filter(host))
        if item is None or item["kind"] != "skill":
            return f"No skill named {name!r}."
        meta, body = _parse_frontmatter(_safe_read(item["path"], 400_000))
        slug = _slug(item["short"])
        tool_name = "Skill" + _camel(slug)
        class_name = tool_name + "Agent"
        desc = _one_line(item["description"])[:900] or f"Skill {item['short']}"
        agents_dir = os.path.dirname(os.path.abspath(__file__))
        out_path = os.path.join(agents_dir, f"skill_{slug}_agent.py")
        sha = hashlib.sha256(_safe_read(item["path"]).encode()).hexdigest()
        code = _PROMOTED_TEMPLATE.format(
            class_name=class_name, skill_name=item["short"], sha=sha, skill_dir=item["dir"], body=body.strip(),
            meta={k: v for k, v in meta.items() if isinstance(v, (str, int, float, bool, list, dict))},
            tool_name=tool_name, description=desc)
        ast.parse(code, filename=out_path)  # never write an agent that cannot parse
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(code)
        return f"Promoted skill {item['name']!r} ({item['host']}) to native agent {tool_name} at {out_path}. It is live on the next /chat."

    # -- export (agent -> SKILL.md) ------------------------------------------
    def _do_export(self, name="", path="", **_):
        agents_dir = os.path.dirname(os.path.abspath(__file__))
        cand = (name or "").strip()
        if not cand:
            return "Pass name=<agent file or tool name>."
        agent_file = None
        for fp in sorted(glob.glob(os.path.join(agents_dir, "*_agent.py"))):
            base = os.path.basename(fp)
            if cand in (base, base[:-3], base[:-9]) or cand.lower() == base[:-9].replace("_", "").lower():
                agent_file = fp
                break
        if agent_file is None:
            for fp in sorted(glob.glob(os.path.join(agents_dir, "*_agent.py"))):
                if re.search(r"self\.name\s*=\s*['\"]" + re.escape(cand) + r"['\"]", _safe_read(fp)):
                    agent_file = fp
                    break
        if agent_file is None:
            return f"No agent file matching {cand!r} in {agents_dir}."
        src = _safe_read(agent_file)
        m_name = re.search(r"self\.name\s*=\s*['\"]([^'\"]+)['\"]", src)
        m_desc = re.search(r"['\"]description['\"]\s*:\s*\(?\s*((?:['\"][^'\"]*['\"]\s*)+)", src)
        tool = m_name.group(1) if m_name else os.path.basename(agent_file)[:-9]
        desc = " ".join(re.findall(r"['\"]([^'\"]*)['\"]", m_desc.group(1))) if m_desc else ""
        skill_name = _slug(tool).replace("_", "-")
        out_root = os.path.expanduser(path) if path else os.path.join(_store_dir(), "exported_skills")
        sdir = os.path.join(out_root, skill_name)
        os.makedirs(os.path.join(sdir, "scripts"), exist_ok=True)
        shutil.copy(agent_file, os.path.join(sdir, "scripts", "agent.py"))
        runner = (
            "#!/usr/bin/env python3\n\"\"\"Run the bundled RAPP agent: python3 run.py --json '{...}'\"\"\"\n"
            "import importlib.util, json, os, sys, types\n"
            "here = os.path.dirname(os.path.abspath(__file__))\n"
            "pkg = types.ModuleType('agents'); pkg.__path__ = []\n"
            "ba = types.ModuleType('agents.basic_agent')\n"
            "class BasicAgent:\n"
            "    def __init__(self, name=None, metadata=None):\n"
            "        self.name = getattr(self, 'name', name or 'BasicAgent')\n"
            "        self.metadata = getattr(self, 'metadata', metadata or {})\n"
            "    def perform(self, **kw): return 'Not implemented.'\n"
            "    def system_context(self): return None\n"
            "ba.BasicAgent = BasicAgent; pkg.basic_agent = ba\n"
            "sys.modules.setdefault('agents', pkg); sys.modules.setdefault('agents.basic_agent', ba)\n"
            "spec = importlib.util.spec_from_file_location('skill_agent', os.path.join(here, 'agent.py'))\n"
            "mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)\n"
            "cls = next(c for c in vars(mod).values() if isinstance(c, type) and c is not BasicAgent and hasattr(c, 'perform') and c.__module__ == mod.__name__)\n"
            "args = json.loads(sys.argv[sys.argv.index('--json') + 1]) if '--json' in sys.argv else {}\n"
            "print(cls().perform(**args))\n")
        with open(os.path.join(sdir, "scripts", "run.py"), "w") as f:
            f.write(runner)
        sha = hashlib.sha256(src.encode()).hexdigest()
        fm_desc = (desc or f"RAPP agent {tool} exported from the Brainstem.").replace('"', "'")[:1000]
        skill_md = (
            "---\n"
            f"name: \"{skill_name}\"\n"
            f"description: \"{fm_desc}\"\n"
            "license: \"MIT\"\n"
            "compatibility: \"Requires python3 (3.11+). Works in Claude Code, GitHub Copilot CLI and any Agent Skills host.\"\n"
            "metadata:\n"
            f"  rapp-tool: \"{tool}\"\n"
            f"  agent-sha256: \"{sha}\"\n"
            "  source: \"rapp-brainstem HostCompat export\"\n"
            "---\n\n"
            f"# {tool}\n\n{desc or 'A RAPP single-file agent.'}\n\n"
            "## Run\n\n"
            "This skill carries the agent verbatim in `scripts/agent.py`. Execute it with:\n\n"
            "```bash\npython3 scripts/run.py --json '{\"...\": \"...\"}'\n```\n\n"
            "Pass the agent's parameters as the JSON object. To run it server-side, drop `scripts/agent.py` into a RAPP Brainstem `agents/` folder.\n"
            "Install: copy this folder to `~/.claude/skills/`, `~/.copilot/skills/`, `<project>/.github/skills/` or `<project>/.agents/skills/`.\n")
        with open(os.path.join(sdir, "SKILL.md"), "w", encoding="utf-8") as f:
            f.write(skill_md)
        return f"Exported {tool} to skill {skill_name!r} at {sdir} (SKILL.md, scripts/agent.py, scripts/run.py)."

    # -- instructions --------------------------------------------------------
    def _do_instructions(self, host="", name="", **_):
        cat = _get_catalog()
        hf = self._host_filter(host)
        rows = [i for i in cat.instructions if (not hf or i["host"] == hf) and (not name or name.lower() in i["path"].lower())]
        if not rows:
            return "No instruction files (CLAUDE.md, AGENTS.md, .github/copilot-instructions.md, .github/instructions/*.instructions.md) found."
        out, total = [], 0
        for i in rows:
            body = _safe_read(i["path"], 200_000)
            out.append(f"===== {i['path']} [{i['host']}] =====\n{_clip(body, 20_000)}")
            total += len(body)
            if total > 60_000:
                out.append("... (remaining instruction files omitted; pass name=<filename> to read one)")
                break
        return "\n\n".join(out)

    # -- transcripts ---------------------------------------------------------
    def _index(self):
        return _TranscriptIndex(os.path.join(_store_dir(), "transcripts.db"))

    def _do_index(self, days=None, **kw):
        days = int(days or _int_env("HOST_COMPAT_TRANSCRIPT_DAYS", 30))
        idx = self._index()
        try:
            r = idx.refresh(days, self._timeout(kw))
            return (f"Transcript index: indexed {r['indexed_now']} session file(s) this pass in {r['seconds']}s; "
                    f"{r['pending']} still pending of {r['in_window']} in the last {days} days. "
                    + ("Call action='index' again to continue. " if r["pending"] else "Index is complete. ")
                    + f"Totals: {json.dumps(idx.stats())}")
        finally:
            idx.close()

    def _do_transcripts(self, query="", host="", role="", cwd="", days=None, limit=20, **kw):
        if not (query or "").strip():
            return "Pass query=<search terms>. Optional: host=claude-code|copilot-cli, role=user|assistant, cwd=<path fragment>, days=N."
        days = int(days or _int_env("HOST_COMPAT_TRANSCRIPT_DAYS", 30))
        idx = self._index()
        try:
            r = idx.refresh(days, min(self._timeout(kw), _int_env("HOST_COMPAT_INDEX_BUDGET", 15)))
            since = time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(time.time() - days * 86400))
            hits = idx.search(query, self._host_filter(host), role or None, cwd or None,
                              max(1, min(int(limit or 20), 100)), since_iso=since)
            lines = [f"Transcript search for {query!r}: {len(hits)} hit(s)"
                     + (f"; index still catching up ({r['pending']} session files pending, run action='index')" if r["pending"] else "")]
            for h, session, rl, ts, c, path, title, snip in hits:
                lines.append(f"- [{h}] {ts[:19]} {rl} session={session[:8]}… cwd={c or '?'}" + (f" title={title!r}" if title else "")
                             + f"\n    {_one_line(snip)[:300]}")
            if not hits:
                lines.append("No matches. Try fewer/other terms, a larger days=, or host='all'.")
            lines.append("Read a session with action='transcript' name=<session id prefix>.")
            return "\n".join(lines)
        finally:
            idx.close()

    def _do_transcript(self, name="", limit=200, days=None, **kw):
        if not name:
            return "Pass name=<session id or prefix>."
        days = int(days or _int_env("HOST_COMPAT_TRANSCRIPT_DAYS", 30))
        idx = self._index()
        try:
            idx.refresh(days, min(self._timeout(kw), _int_env("HOST_COMPAT_INDEX_BUDGET", 15)))
            rows = idx.session(name.strip(), max(1, min(int(limit or 200), 1000)))
        finally:
            idx.close()
        if not rows:
            return f"No indexed session matching {name!r} (search first with action='transcripts', or run action='index')."
        head = rows[0]
        out = [f"Session {name} [{head[5]}] cwd={head[3]}" + (f" title={head[4]!r}" if head[4] else "") + f"\nFile: {head[6]}\n"]
        total = 0
        for role, ts, text, *_r in rows:
            piece = f"[{ts[:19]}] {role.upper()}: {text}"
            total += len(piece)
            if total > 50_000:
                out.append("... (clipped; raise limit= or read the file directly)")
                break
            out.append(piece)
        return "\n\n".join(out)

    # -- doctor / refresh ----------------------------------------------------
    def _do_doctor(self, **_):
        cat = _get_catalog(force=True)
        lines = ["HostCompat doctor"]
        for hkey, host in _hosts().items():
            home = _host_home(host)
            n_sk = sum(1 for i in cat.skills.values() if i["host"] == hkey)
            n_pl = sum(1 for p in cat.plugins.values() if p["host"] == hkey)
            n_mcp = sum(1 for e in cat.mcp.values() if e["host"] == hkey)
            tr = host.get("transcripts")
            n_tr = len(_expand_paths(tr["glob"], host)) if tr else 0
            lines.append(f"- {host.get('display', hkey)} [{hkey}]: home={home} ({'ok' if os.path.isdir(home) else 'missing'}) "
                         f"skills={n_sk} plugins={n_pl} mcp={n_mcp} transcript files={n_tr}")
        lines += [f"project dir: {_project_dir()}", f"store: {_store_dir()}",
                  f"skill roots: {', '.join(cat.roots) or 'none'}",
                  f"totals: skills={len(cat.skills)} commands={len(cat.commands)} personas={len(cat.agents)} plugins={len(cat.plugins)} "
                  f"hooks={len(cat.hooks)} mcp={len(cat.mcp)} instruction files={len(cat.instructions)}",
                  f"catalog context budget: {_int_env('HOST_COMPAT_CONTEXT_CHARS', 6000)} chars; current: {len(self.system_context() or '')} chars"]
        try:
            idx = self._index()
            lines.append(f"transcript index: {'FTS5' if idx.fts else 'LIKE fallback'} at {os.path.join(_store_dir(), 'transcripts.db')}; {json.dumps(idx.stats())}")
            idx.close()
        except Exception as e:
            lines.append(f"transcript index unavailable: {e}")
        lines.append(f"python: {sys.executable}; git: {'yes' if shutil.which('git') else 'no'}; node: {'yes' if shutil.which('node') else 'no'}")
        if cat.errors:
            lines.append("errors:")
            lines += [f"  - {e}" for e in cat.errors[:30]]
        return "\n".join(lines)

    def _do_refresh(self, **_):
        cat = _get_catalog(force=True)
        return (f"Catalog rebuilt: skills={len(cat.skills)} commands={len(cat.commands)} personas={len(cat.agents)} "
                f"plugins={len(cat.plugins)} hooks={len(cat.hooks)} mcp={len(cat.mcp)} instruction files={len(cat.instructions)}")


if __name__ == "__main__":
    # Standalone use: python host_compat_agent.py [action] [key=value ...]
    _argv = sys.argv[1:]
    _action = _argv[0] if _argv and "=" not in _argv[0] else "doctor"
    _kw = dict(a.split("=", 1) for a in _argv if "=" in a)
    print(HostCompatAgent().perform(action=_action, **_kw))
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
