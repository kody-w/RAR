---
name: "rar-kody-w-host-compat"
description: "Bridge to everything agent-host-shaped on this machine, across Claude Code, GitHub Copilot CLI and the open Agent Skills layout: skills (SKILL.md), plugins, slash commands / prompts, subagent personas, hooks, MCP servers, instruction files (CLAUDE.md, AGENTS.md, copilot-instructions.md) and local session transcripts. action='list' shows what exists; 'load' pulls a skill/command/persona's instructions into the conversation before doing that kind of work; 'read' returns a bundled file; 'run' executes a skill's bundled script; 'mcp_tools'/'mcp_call' use an MCP server; 'install' adds a plugin from a path or git URL; 'promote' compiles a skill into a native Brainstem agent; 'export' turns an agent into a SKILL.md; 'hook' fires a hook; 'instructions' returns the project's instruction files; 'transcripts' searches the user's own past CODING-ASSISTANT CHAT HISTORY \u2014 Claude Code and GitHub Copilot CLI session logs on this machine \u2014 across both hosts at once (query=...; this is the tool for 'what did I ask Claude/Copilot about X', 'find my earlier session where...', NOT for meeting or call transcripts); 'transcript' reads one session by id; 'index' backfills the session index; 'doctor' is a health report."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/host_compat_agent", "rar_sha256": "2d48518a96d17ecdf8f8379fc184647554304aeff533b39166b3387d8afcb889", "source_kind": "rar-agent", "source_commit": "97bb0520630a7a0e9ac17dd58dec6e85d344bfcf", "author": "kody-w", "tags": ["skills", "plugins", "claude-code", "copilot-cli", "agent-skills", "mcp", "hooks", "transcripts", "interop", "compat"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `host_compat_agent.py` and embedded as the fenced Python below (sha256 2d48518a96d17ecd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `host_compat_agent.py` first:

```bash
python3 host_compat_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 host_compat_agent.py   # or on stdin
python3 host_compat_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
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
    "version": "1.0.0",
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
        super().__init__()

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
        super().__init__()

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
