---
name: "rar-kody-w-host-compat"
description: "Bridge to everything agent-host-shaped on this machine, across Claude Code, GitHub Copilot CLI and the open Agent Skills layout: skills (SKILL.md), plugins, slash commands / prompts, subagent personas, hooks, MCP servers, instruction files (CLAUDE.md, AGENTS.md, copilot-instructions.md) and local session transcripts. action='list' shows what exists; 'load' pulls a skill/command/persona's instructions into the conversation before doing that kind of work; 'read' returns a bundled file; 'run' executes a skill's bundled script; 'mcp_tools'/'mcp_call' use an MCP server; 'install' adds a plugin from a path or git URL; 'promote' compiles a skill into a native Brainstem agent; 'export' turns an agent into a SKILL.md; 'hook' fires a hook; 'instructions' returns the project's instruction files; 'transcripts' searches the user's own past CODING-ASSISTANT CHAT HISTORY \u2014 Claude Code and GitHub Copilot CLI session logs on this machine \u2014 across both hosts at once (query=...; this is the tool for 'what did I ask Claude/Copilot about X', 'find my earlier session where...', NOT for meeting or call transcripts); 'transcript' reads one session by id; 'index' backfills the session index; 'doctor' is a health report."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/host_compat_agent", "rar_sha256": "284c111aa88d5588b9873c97f04d44676223ea37a80240a5e7b884bbdc7170c8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "kody-w", "tags": ["skills", "plugins", "claude-code", "copilot-cli", "agent-skills", "mcp", "hooks", "transcripts", "interop", "compat"]}
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
