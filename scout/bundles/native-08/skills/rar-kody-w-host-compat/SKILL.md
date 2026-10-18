---
name: "rar-kody-w-host-compat"
description: "Bridge to everything agent-host-shaped on this machine, across Claude Code, GitHub Copilot CLI and the open Agent Skills layout: skills (SKILL.md), plugins, slash commands / prompts, subagent personas, hooks, MCP servers, instruction files (CLAUDE.md, AGENTS.md, copilot-instructions.md) and local session transcripts. action='list' shows what exists; 'load' pulls a skill/command/persona's instructions into the conversation before doing that kind of work; 'read' returns a bundled file; 'run' executes a skill's bundled script; 'mcp_tools'/'mcp_call' use an MCP server; 'install' adds a plugin from a path or git URL; 'promote' compiles a skill into a native Brainstem agent; 'export' turns an agent into a SKILL.md; 'hook' fires a hook; 'instructions' returns the project's instruction files; 'transcripts' searches the user's own past CODING-ASSISTANT CHAT HISTORY \u2014 Claude Code and GitHub Copilot CLI session logs on this machine \u2014 across both hosts at once (query=...; this is the tool for 'what did I ask Claude/Copilot about X', 'find my earlier session where...', NOT for meeting or call transcripts); 'transcript' reads one session by id; 'index' backfills the session index; 'doctor' is a health report."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/host_compat_agent", "rar_sha256": "a85517d560dcab529e0c4fc1dce80472c27ca85e6620e6202aee695c2f4dfa79", "source_kind": "rar-agent", "source_commit": "a52a0d5107d37e0ba8d737bc7a0aaf303da6cc52", "version": "1.0.1", "author": "kody-w", "tags": ["skills", "plugins", "claude-code", "copilot-cli", "agent-skills", "mcp", "hooks", "transcripts", "interop", "compat"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `host_compat_agent.py` and embedded as the fenced Python below (sha256 a85517d560dcab52…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `host_compat_agent.py` first:

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
