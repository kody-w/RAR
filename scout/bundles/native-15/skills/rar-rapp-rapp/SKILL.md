---
name: "rar-rapp-rapp"
description: "SIRI-LEVEL FRONT DOOR: the user speaks PLAIN language and knows NOTHING about rapp (no 'rappid'/'cubby'/'egg'/'estate'). Translate their wish into the right action(s), DO it end to end, then report back in THEIR words. Ambiguous wish? call action=assist problem='<their exact words>' \u2192 it returns a step-by-step plan + the first call to run; then execute that plan. NEVER make the user learn a term or run a raw command.\nTHE single agent for the whole RAPP ecosystem. Pass action=<one enum value> PLUS that action's params (listed here). This metadata is ALL the caller gets, so pass exactly what the chosen action needs. Write actions commit+push by default \u2014 pass push=false to only stage locally. Unsure which action/params fit? call action=spec or action=route need='<what you want>' FIRST.\nORIENT \u2014 spec (full ecosystem map) \u00b7 ecosystem \u00b7 find query=\u2026 \u00b7 refresh \u00b7 protocol \u00b7 whoami \u00b7 help\nIDENTITY/DOORS \u2014 estate (your doors) \u00b7 door rappid=\u2026 [validate=true] (resolve + reachability-check any door)\nBOOTSTRAP \u2014 mint owner=\u2026 slug=\u2026 [kind=] [force=] (mint an Eternity rappid) \u00b7 scaffold (seed kernel agents) \u00b7 plant owner=\u2026 slug=\u2026 [kind=] [display_name=] [confirm=] (public front-door grail) \u00b7 batcave owner=\u2026 slug=\u2026 [what=] (plant a PRIVATE cubby-neighborhood \u2014 dry-run unless confirm=true)\nREACH ANY SPECIALIST \u2014 install name=<file.py>|query=\u2026|url=\u2026 [git_invisible=] [verify=] (pull + hot-load ANY agent) \u00b7 route need='<free text>' (names the provider + its install line)\nTAILORED APPS \u2014 summon rapplication=<name under ~/.rapp/rapplications> [port=] (boot a rapplication as an isolated tailored-UI twin on its own port; idempotent)\nCUBBIES & TWINS (on-device) \u2014 cubby_new slug=\u2026 what=\u2026 \u00b7 cubby_list \u00b7 cubby_show cubby=\u2026 \u00b7 cubby_collect slug=\u2026 query=\u2026 [source=cubbies|brainstem|all] \u00b7 cubby_fork slug=\u2026 from='non-kernel-agents|brainstem|cubby:<slug>' [paths=] [egg=true] [twin=] \u00b7 cubby_egg cubby=\u2026 \u00b7 cubby_import path=\u2026 \u00b7 twin cubby=\u2026 [soul=] (pop a twin chat from a cubby) \u00b7 super_rar query=\u2026 [where=local|neighborhood] (search the whole estate)\nMEMORY (op required) \u2014 memory op=save key=\u2026 value=\u2026 | op=read [key=\u2026] | op=recall query=\u2026\nLINEAGE (op required) \u2014 bond op=record event=<birth|bond|hatch|graft|launch|adoption|rhythm> [context=] [egg_sha256=] | bond op=list \u00b7 lineage (walk to species root)\nFEDERATE \u2014 beacon estate_url=\u2026 [private_estate_pointer=] (write the estate beacon) \u00b7 sniff seed=<url> (BFS the network) \u00b7 mmr (standing score)\nNEIGHBORHOOD (FIRST set repo=<owner/repo> or env RAPP_NEIGHBORHOOD) \u2014 mount \u00b7 join what=\u2026 \u00b7 browse \u00b7 stash path=\u2026 [cubby=<slug>] \u00b7 hatch path=\u2026 \u00b7 load [cubby=] \u00b7 unload \u00b7 sync \u00b7 branch topic=\u2026 \u00b7 invite github_login=\u2026 [confirm=true] \u00b7 qr \u00b7 enter \u00b7 show_and_tell title=\u2026 text=\u2026 \u00b7 super_rar where=neighborhood query=\u2026\nSELF-CHECK \u2014 verify (god\u2261map\u2261bible drift triangle)"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/rapp", "rar_sha256": "827cc07976687631087dd00ceb7d5d78082eb2f025467215cadac68e81d10a71", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.7", "author": "Kody Wildfeuer", "tags": ["rapp", "ecosystem", "estate", "cubby", "neighborhood", "egg", "super-rar", "door", "spec", "universal"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/rapp`. The original RAPP
agent is preserved byte-for-byte in `rapp_agent.py` and in the RCI capsule.

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

RappAgent — the one agent for the whole RAPP ecosystem, end to end.

Instead of a pile of one-off agents, this single file navigates a full rapp
estate top to bottom: your identity, any door (by rappid), your local cubbies
(on-device workspaces), shared neighborhoods (private collaborator-gated
spaces with per-member cubbies), the egg family, the super-RAR (the whole
stack across every cubby), and zero-commit-risk streaming. It also *knows the
spec*: `action=spec` returns the map of how the ecosystem fits together so any
AI hosting this agent can navigate it without reading nine docs first.

One file = one class = one perform() = one metadata dict (the agent contract).
Generic by design: it names no specific door. Point it at a neighborhood with
`repo=<owner/repo>` (or `RAPP_NEIGHBORHOOD` env, or
`~/.brainstem/rapp/neighborhood.json`). Nothing private is baked in.

THE MAP (what this agent does, by layer):

  identity   whoami            your rappid + estate at a glance
             estate            your door catalog (created[] + member[])
             door rappid=…     resolve ANY rappid → its 9 canonical URLs

  on-device  cubby_new         a local workspace (~/.brainstem/cubbies/<slug>/)
             cubby_list        your local cubbies
             cubby_show        one cubby's inventory
             cubby_egg         pack a cubby → portable .egg
             cubby_import      hatch a cubby egg locally
             super_rar where=local   search your WHOLE local stack

  neighborhood (shared)
             mount             clone/refresh the neighborhood (your gh auth)
             join              create your cubby in it
             browse            everyone's cubbies + what they're cooking
             stash             put a file in YOUR cubby
             hatch             land a local egg INTO your cubby
             load / unload     stream a cubby's agents into a brainstem
                               (git-invisible — zero grail-repo commit risk)
             show_and_tell     post a signed event to the room
             sync              pull + what's new
             branch            a personal branch (never must merge)
             invite            add a collaborator (dry-run default)
             super_rar where=neighborhood   the super-store across all cubbies

  orient     spec | help | protocol

MIT © Kody Wildfeuer.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "what to do (action=spec for the full map)",
      "enum": [
        "spec",
        "help",
        "protocol",
        "ecosystem",
        "find",
        "refresh",
        "whoami",
        "estate",
        "door",
        "cubby_new",
        "cubby_list",
        "cubby_show",
        "cubby_collect",
        "cubby_egg",
        "cubby_import",
        "cubby_fork",
        "twin",
        "twin_from_cubby",
        "summon",
        "super_rar",
        "mount",
        "join",
        "browse",
        "stash",
        "hatch",
        "load",
        "unload",
        "sync",
        "branch",
        "invite",
        "qr",
        "enter",
        "show_and_tell",
        "install",
        "route",
        "mint",
        "scaffold",
        "plant",
        "batcave",
        "memory",
        "bond",
        "lineage",
        "beacon",
        "sniff",
        "mmr",
        "verify",
        "assist"
      ],
      "type": "string"
    },
    "confirm": {
      "description": "invite: actually run it (default dry-run)",
      "type": "boolean"
    },
    "context": {
      "description": "bond: a one-line note for the ledger entry",
      "type": "string"
    },
    "cubby": {
      "description": "cubby/neighborhood/twin: a cubby slug or handle (stash: cubby=<slug> \u2192 an owned sub-cubby)",
      "type": "string"
    },
    "display_name": {
      "description": "plant: human-readable door name",
      "type": "string"
    },
    "egg": {
      "description": "cubby_fork: pack a self-backup .egg into the new cubby (default true)",
      "type": "boolean"
    },
    "egg_sha256": {
      "description": "bond: sha256 of the egg involved (optional)",
      "type": "string"
    },
    "estate_url": {
      "description": "beacon: the operator's public estate URL",
      "type": "string"
    },
    "event": {
      "description": "bond: lifecycle event kind (birth|bond|hatch|graft|launch|adoption|rhythm)",
      "type": "string"
    },
    "force": {
      "description": "mint: overwrite an existing rappid (mint-once is the default)",
      "type": "boolean"
    },
    "from": {
      "description": "cubby_fork/twin: content set \u2014 'non-kernel-agents' | 'brainstem' | 'cubby:<slug>'",
      "type": "string"
    },
    "git_invisible": {
      "description": "install: register in .git/info/exclude (default false)",
      "type": "boolean"
    },
    "github_login": {
      "description": "invite: collaborator to add",
      "type": "string"
    },
    "goal": {
      "description": "assist: alias for problem",
      "type": "string"
    },
    "indexable": {
      "description": "beacon: list this estate in public discovery (default true)",
      "type": "boolean"
    },
    "key": {
      "description": "memory: the memory key",
      "type": "string"
    },
    "kind": {
      "description": "mint/plant: door kind (default operator)",
      "type": "string"
    },
    "name": {
      "description": "install: exact agent filename (e.g. @rapp/twin_agent.py)",
      "type": "string"
    },
    "need": {
      "description": "route: free-text operator need ('twin lifecycle', 'sealed channel', \u2026)",
      "type": "string"
    },
    "op": {
      "description": "memory: read|save|recall \u00b7 bond: record|list",
      "enum": [
        "read",
        "save",
        "recall",
        "record",
        "list"
      ],
      "type": "string"
    },
    "owner": {
      "description": "mint/plant: GitHub owner/login",
      "type": "string"
    },
    "path": {
      "description": "stash/hatch/cubby_import/cubby_egg/cubby_fork: a file path",
      "type": "string"
    },
    "paths": {
      "description": "cubby_fork: explicit file paths to fork in",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "port": {
      "description": "summon: preferred port (default: first free in 7081-7200)",
      "type": "integer"
    },
    "private_estate_pointer": {
      "description": "beacon: opaque pointer to the private estate",
      "type": "string"
    },
    "problem": {
      "description": "assist: the user's wish in their OWN plain words ('a private place for my family', 'remember my pills', 'set me up'); the agent translates it into a step-by-step plan + first call",
      "type": "string"
    },
    "push": {
      "description": "write actions: commit+push (default true)",
      "type": "boolean"
    },
    "query": {
      "description": "super_rar/cubby_collect: search term across your estate",
      "type": "string"
    },
    "rappid": {
      "description": "door: any rappid to resolve",
      "type": "string"
    },
    "rapplication": {
      "description": "summon: which rapplication to hatch as a tailored-UI twin (e.g. 'dataverse'); catalog in ~/.rapp/rapplications/",
      "type": "string"
    },
    "repo": {
      "description": "neighborhood door owner/repo (or set RAPP_NEIGHBORHOOD)",
      "type": "string"
    },
    "seed": {
      "description": "sniff: a seed URL serving .well-known/rapp-network.json",
      "type": "string"
    },
    "slug": {
      "description": "cubby_new/cubby_fork: local cubby slug",
      "type": "string"
    },
    "soul": {
      "description": "twin: soul.md text for the twin workspace",
      "type": "string"
    },
    "source": {
      "description": "cubby_collect: where to gather from (default all)",
      "enum": [
        "cubbies",
        "brainstem",
        "all"
      ],
      "type": "string"
    },
    "text": {
      "description": "show_and_tell: post body",
      "type": "string"
    },
    "title": {
      "description": "show_and_tell: post title",
      "type": "string"
    },
    "topic": {
      "description": "branch: topic for the personal branch",
      "type": "string"
    },
    "twin": {
      "description": "cubby_fork: after forking, also boot a twin from the new cubby",
      "type": "boolean"
    },
    "url": {
      "description": "install: a direct raw URL to an agent file",
      "type": "string"
    },
    "validate": {
      "description": "door: HEAD/GET the identity URL to check reachability",
      "type": "boolean"
    },
    "value": {
      "description": "memory: the value to save",
      "type": "string"
    },
    "verify": {
      "description": "install/load/door: verify sha256 / reachability (default true)",
      "type": "boolean"
    },
    "what": {
      "description": "cubby_new/join/cubby_fork: one-line 'what I'm working on'",
      "type": "string"
    },
    "where": {
      "description": "super_rar: which stack (default neighborhood if mounted, else local)",
      "enum": [
        "local",
        "neighborhood"
      ],
      "type": "string"
    },
    "wish": {
      "description": "assist: alias for problem",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_agent.py` and embedded as the fenced Python below (sha256 827cc07976687631…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_agent.py` first:

```bash
python3 rapp_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_agent.py   # or on stdin
python3 rapp_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@rapp/rapp_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/rapp_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@rapp/rapp/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""RappAgent — the one agent for the whole RAPP ecosystem, end to end.

Instead of a pile of one-off agents, this single file navigates a full rapp
estate top to bottom: your identity, any door (by rappid), your local cubbies
(on-device workspaces), shared neighborhoods (private collaborator-gated
spaces with per-member cubbies), the egg family, the super-RAR (the whole
stack across every cubby), and zero-commit-risk streaming. It also *knows the
spec*: `action=spec` returns the map of how the ecosystem fits together so any
AI hosting this agent can navigate it without reading nine docs first.

One file = one class = one perform() = one metadata dict (the agent contract).
Generic by design: it names no specific door. Point it at a neighborhood with
`repo=<owner/repo>` (or `RAPP_NEIGHBORHOOD` env, or
`~/.brainstem/rapp/neighborhood.json`). Nothing private is baked in.

THE MAP (what this agent does, by layer):

  identity   whoami            your rappid + estate at a glance
             estate            your door catalog (created[] + member[])
             door rappid=…     resolve ANY rappid → its 9 canonical URLs

  on-device  cubby_new         a local workspace (~/.brainstem/cubbies/<slug>/)
             cubby_list        your local cubbies
             cubby_show        one cubby's inventory
             cubby_egg         pack a cubby → portable .egg
             cubby_import      hatch a cubby egg locally
             super_rar where=local   search your WHOLE local stack

  neighborhood (shared)
             mount             clone/refresh the neighborhood (your gh auth)
             join              create your cubby in it
             browse            everyone's cubbies + what they're cooking
             stash             put a file in YOUR cubby
             hatch             land a local egg INTO your cubby
             load / unload     stream a cubby's agents into a brainstem
                               (git-invisible — zero grail-repo commit risk)
             show_and_tell     post a signed event to the room
             sync              pull + what's new
             branch            a personal branch (never must merge)
             invite            add a collaborator (dry-run default)
             super_rar where=neighborhood   the super-store across all cubbies

  orient     spec | help | protocol

MIT © Kody Wildfeuer.
"""

from __future__ import annotations

import base64
import glob
import datetime as _dt
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import zipfile
from datetime import datetime, timezone

try:
    from agents.basic_agent import BasicAgent  # type: ignore
except ImportError:
    try:
        from basic_agent import BasicAgent  # type: ignore
    except ImportError:
        class BasicAgent:
            def __init__(self, name="Agent", metadata=None):
                self.name = name
                self.metadata = metadata or {}

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/rapp",
    "version": "1.0.7",
    "display_name": "RappAgent",
    "description": ("Navigates the whole RAPP estate \u2014 identity, doors, local cubbies, shared neighborhood repos, eggs, super-RAR search \u2014 and serves the spec map."),
    "author": "Kody Wildfeuer",
    "tags": ["rapp", "ecosystem", "estate", "cubby", "neighborhood", "egg",
             "super-rar", "door", "spec", "universal"],
    "category": "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

# ── ecosystem constants ──────────────────────────────────────────────────
CUBBY_SCHEMA = "rapp-cubby/1.0"
CUBBY_EGG_SCHEMA = "brainstem-egg/2.3-cubby"
CUBBY_ANATOMY = ("agents", "organs", "senses", "rapplications",
                 "neighborhoods", "eggs", "show-and-tell")
SUPER_RAR_KINDS = {
    "agent": ("agents", "*_agent.py"),
    "organ": ("organs", "*_organ.py"),
    "sense": ("senses", "*.py"),
    "rapplication": ("rapplications", "*"),
    "neighborhood": ("neighborhoods", "*"),
    "egg": ("eggs", "*.egg"),
}
EVENT_SCHEMA = "rapp-event/1.0"
EVENT_KINDS = ("hello", "show-and-tell", "ask", "reply", "fyi", "leave")
# kernel-shipped agents — load/unload NEVER touch these (CONSTITUTION Art. XXXIII)
KERNEL_AGENTS = {"basic_agent.py", "context_memory_agent.py",
                 "manage_memory_agent.py", "learn_new_agent.py",
                 "swarm_factory_agent.py", "hacker_news_agent.py"}
# The kernel agents' declared NAMES, not their filenames. KERNEL_AGENTS above
# guards the filename; the brainstem quarantines on the declared name and
# resolves collisions by `sorted(glob(...))` — first file alphabetically wins,
# and the LOSER is the one quarantined.
#
# Those two facts compose into a capability hijack that neither guard sees
# alone: a publisher controls their own @namespace, the namespace becomes the
# installed filename, so `@aaa/...` lands a file that sorts ahead of
# `context_memory_agent.py`, declares the name "ContextMemory", wins the sort,
# and gets the KERNEL agent quarantined. The filename was never touched, so the
# KERNEL_AGENTS check passes cleanly.
KERNEL_AGENT_NAMES = {"BasicAgent", "ContextMemory", "ManageMemory",
                      "LearnNew", "SwarmFactory", "HackerNews"}


def _declared_agent_names(src):
    """Agent names a file declares, read statically. Never import it — deciding
    whether to trust a file by executing it is the wrong order."""
    import ast as _ast
    names = set()
    try:
        tree = _ast.parse(src)
    except SyntaxError:
        return names
    for node in _ast.walk(tree):
        # self.name = "X"  inside __init__
        if isinstance(node, _ast.Assign):
            for tgt in node.targets:
                if (isinstance(tgt, _ast.Attribute) and tgt.attr == "name"
                        and isinstance(node.value, _ast.Constant)
                        and isinstance(node.value.value, str)):
                    names.add(node.value.value)
            # metadata = {"name": "X", ...}
            if isinstance(node.value, _ast.Dict):
                for k, v in zip(node.value.keys, node.value.values):
                    if (isinstance(k, _ast.Constant) and k.value == "name"
                            and isinstance(v, _ast.Constant)
                            and isinstance(v.value, str)):
                        names.add(v.value)
    return names


_SECRET_NAME_RE = re.compile(
    r"(^\.env($|\.)|token|secret|credential|password|apikey|api_key|"
    r"\.pem$|\.key$|\.p12$|\.pfx$|\.ppk$|\.keystore$|\.jks$|"
    r"^id_rsa|^id_dsa|^id_ecdsa|^id_ed25519|"
    r"^\.lineage_key$|^\.copilot|^\.npmrc$|^\.netrc$|private-estate-secret)",
    re.IGNORECASE)
_HANDLE_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9-]{0,38}$")
_AGENT_FILE_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]*_agent\.py$")
_SLUG_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$")
PAYPHONE_URL = os.environ.get(
    "RAPP_PAYPHONE", "https://kody-w.github.io/RAPP/pages/payphone.html")
LOBBY_URL = os.environ.get(
    "RAPP_LOBBY", "https://kody-w.github.io/RAPP/pages/vneighborhood.html")

# ── the global grail: the canonical, drift-observed registries this agent
#    pulls from when online to stay fresh — and falls back to the EMBEDDED
#    snapshot below when airdropped into the woods (no network). ──────────
RAPP_GOD = os.environ.get("RAPP_GOD", "kody-w/rapp-god")        # registry of every part + version
RAPP_MAP = os.environ.get("RAPP_MAP", "kody-w/rapp-map")        # which repo houses which part
RAPP_SPECIES = os.environ.get("RAPP_SPECIES", "kody-w/RAPP")    # the species root (specs + kernel)
# Canonical §6.1 species root rappid — the one true parent every kody-w door
# points at. NOT RAPP_SPECIES.replace("/",":") (that yields a malformed rappid).
SPECIES_ROOT_RAPPID = "rappid:@kody-w/rapp:9a8f0a4b5a710e20f4d819a0f37d2a4c9f113b5e78fb3c29e70b54fff48a38f9"
RAPP_BIBLE = os.environ.get("RAPP_BIBLE", "kody-w/RAPP-Bible")  # the specs hub (human-facing canon)
_RAW = "https://raw.githubusercontent.com"
GRAIL_SOURCES = {
    "god_status": f"{_RAW}/{RAPP_GOD}/main/api/v1/status.json",
    "god_registry": f"{_RAW}/{RAPP_GOD}/main/registry.json",
    "spec": f"{_RAW}/{RAPP_SPECIES}/main/specs/SPEC.md",
    "skill": f"{_RAW}/{RAPP_SPECIES}/main/specs/skill.md",
    "ecosystem_map": f"{_RAW}/{RAPP_SPECIES}/main/ECOSYSTEM_MAP.md",
    "constitution": f"{_RAW}/{RAPP_SPECIES}/main/CONSTITUTION.md",
    "bible": f"{_RAW}/{RAPP_BIBLE}/main/README.md",
}
DASHBOARDS = {"rapp-god": f"https://{RAPP_GOD.split('/')[0]}.github.io/rapp-god/",
              "rapp-map": f"https://github.com/{RAPP_MAP}",
              "rapp-bible": f"https://{RAPP_BIBLE.split('/')[0]}.github.io/RAPP-Bible/#specs"}

# ── the capability map: for ANY operator need, which agent/part provides it
#    and the exact `install` call to fetch it. This + `install` is the keystone
#    that makes "one drop = the whole ecosystem" true — this file natively
#    operates the core and REACHES every specialist through here. ───────────
RAR_RAW = os.environ.get("RAPP_RAR_RAW", f"{_RAW}/kody-w/RAR/main/agents")
STORE_INDEX = os.environ.get("RAPPSTORE_URL", f"{_RAW}/kody-w/RAPP_Store/main/index.json")
SENSE_INDEX = os.environ.get("RAPP_SENSE_URL", f"{_RAW}/kody-w/RAPP_Sense_Store/main/index.json")
RAPP1_SPEC_COMMIT = "d2cd5abed48d3f52b86bbb975ac3558286d1db41"
RAPP1_SPEC_URL = (
    f"{_RAW}/kody-w/rapp-1/{RAPP1_SPEC_COMMIT}/SPEC.md"
)
RAPP1_SPEC_BYTES = 41952
RAPP1_SPEC_SHA256 = (
    "cea7847f98f9751734995f46fd4e1bde211c8eb9d03dbbb477934213865bb91a"
)

# need-keyword → {provides, source, native?}. `native:true` means THIS agent
# already does it (route names the action); else `install` fetches the provider.
CAPABILITY_MAP = {
    "identity": {"provides": "mint / whoami / door (native core)", "source": "native",
                 "native": True, "hint": "action=mint owner=… slug=… · action=whoami"},
    "door": {"provides": "door (native — resolve any rappid → 9 URLs)", "source": "native",
             "native": True, "hint": "action=door rappid=…"},
    "estate": {"provides": "estate / beacon / lineage (native core)", "source": "native",
               "native": True, "hint": "action=estate · action=beacon · action=lineage"},
    "memory": {"provides": "@rapp/manage_memory (deep tiers) — local tier is native",
               "source": "rar", "path": "manage_memory_agent.py", "native": "partial",
               "hint": "local: action=memory op=save|read — deep: action=install name=manage_memory_agent.py"},
    "twin": {"provides": "@rapp/twin (boot/archive/purge/twin-me a PII-stripped twin)",
             "source": "rar", "path": "%40rapp/twin_agent.py", "native": False,
             "hint": "action=install name=@rapp/twin_agent.py"},
    "twin lifecycle": {"provides": "@rapp/twin", "source": "rar",
                       "path": "%40rapp/twin_agent.py", "native": False,
                       "hint": "action=install name=@rapp/twin_agent.py"},
    "egg": {"provides": "@rapp/egg_hatcher (hatch any .egg cartridge — introspect+route)",
            "source": "rar", "path": "%40rapp/egg_hatcher_agent.py", "native": "partial",
            "hint": "cubby eggs native (cubby_egg/cubby_import); any egg: action=install name=@rapp/egg_hatcher_agent.py"},
    "hatch": {"provides": "@rapp/egg_hatcher", "source": "rar",
              "path": "%40rapp/egg_hatcher_agent.py", "native": "partial",
              "hint": "action=install name=@rapp/egg_hatcher_agent.py"},
    "sealed": {"provides": "rapp-doorman (AES-256-GCM §8 sealed channel)",
               "source": "rar", "path": "doorman_agent.py", "native": False,
               "hint": "action=install name=doorman_agent.py — or `route need=encryption`"},
    "encryption": {"provides": "rapp-doorman / rapp-sealed (§8 codec)", "source": "rar",
                   "path": "doorman_agent.py", "native": False,
                   "hint": "action=install name=doorman_agent.py"},
    "sense": {"provides": "RAPP_Sense_Store (per-channel output overlays)", "source": "sense",
              "native": False, "hint": "action=install query=<sense> source=sense"},
    "rapplication": {"provides": "RAPP_Store (graduated workflows with UI)", "source": "store",
                     "native": False, "hint": "action=install query=<rapp> source=store"},
    "rapp": {"provides": "RAPP_Store", "source": "store", "native": False,
             "hint": "action=install query=<rapp> source=store"},
    "drift": {"provides": "@rapp/drift (ecosystem drift audit) + native action=verify",
              "source": "rar", "path": "%40rapp/drift_agent.py", "native": "partial",
              "hint": "self-check native: action=verify — full audit: action=install name=@rapp/drift_agent.py"},
    "neighborhood": {"provides": "mount/join/browse/plant (native core)", "source": "native",
                     "native": True, "hint": "action=plant · action=mount repo=… · action=join"},
    "cubby": {"provides": "cubby_new/collect/egg/import (native core)", "source": "native",
              "native": True, "hint": "action=cubby_new slug=… · action=cubby_collect"},
    "bond": {"provides": "bond / lineage (native lineage spine)", "source": "native",
             "native": True, "hint": "action=bond op=record event=… · action=lineage"},
    "federation": {"provides": "sniff / beacon (native discovery)", "source": "native",
                   "native": True, "hint": "action=sniff seed=… · action=beacon"},
    "standing": {"provides": "mmr (native — operator/door standing + tier)", "source": "native",
                 "native": True, "hint": "action=mmr"},
    "mmr": {"provides": "mmr (native)", "source": "native", "native": True, "hint": "action=mmr"},
    "factory": {"provides": "swarm_factory (kernel) — build new agents from a transcript",
                "source": "kernel", "native": False, "hint": "kernel-shipped; or action=scaffold"},
    "mcp": {"provides": "rapp-mcp (MCP gateway — chat is the only wire)", "source": "part",
            "native": False, "hint": "see action=find query=mcp / action=ecosystem"},
    "session": {"provides": "vbrainstem (browser live-session capture → 2.3-session egg)",
                "source": "part", "native": False, "hint": "see action=ecosystem (vbrainstem)"},
    "resurrection": {"provides": "@rapp/dream_catcher (parallel-dimension reassimilation)",
                     "source": "rar", "path": "%40rapp/dream_catcher_agent.py", "native": False,
                     "hint": "action=install name=@rapp/dream_catcher_agent.py"},
    "private estate": {"provides": "estate op=private-init (native — Article XLVIII two-tier private estate + commitment)",
                       "source": "native", "native": True, "hint": "action=estate op=private-init [confirm=true] · then action=beacon"},
    "rebuild": {"provides": "tools/rebuild_estate.py (Article XLVI.6 disaster recovery — rebuild estate from public data)",
                "source": "tool", "path": "rebuild_estate.py", "native": False,
                "hint": "run: python3 tools/rebuild_estate.py --handle <gh> --apply"},
    "pulse": {"provides": "@rapp/bond_rhythm (Bond Pulse — drift reconciliation) + tools/ecosystem_audit.py",
              "source": "rar", "path": "bond_rhythm_agent.py", "native": False,
              "hint": "action=install name=bond_rhythm_agent.py — or run python3 tools/ecosystem_audit.py"},
    "launch": {"provides": "@rapp/launch_to_public (LOCAL→GLOBAL — push your brainstem to a public repo)",
               "source": "rar", "path": "launch_to_public_agent.py", "native": False,
               "hint": "action=install name=launch_to_public_agent.py · then action=bond op=record event=launch"},
    "graft": {"provides": "@rapp/graft_neighborhood (additive overlay onto an existing public repo)",
              "source": "rar", "path": "graft_neighborhood_agent.py", "native": False,
              "hint": "action=install name=graft_neighborhood_agent.py"},
    "dock": {"provides": "@rapp/dock (universal additive-merge into any rar-shaped JSON)",
             "source": "rar", "path": "dock_agent.py", "native": False,
             "hint": "action=install name=dock_agent.py"},
    "sign": {"provides": "tools/sign_release.py (ed25519 keygen/sign/verify — Art. XXXIV.7 signed releases)",
             "source": "tool", "path": "sign_release.py", "native": False,
             "hint": "run: python3 tools/sign_release.py keygen|sign|verify"},
    "rar loader": {"provides": "@rapp/rar_loader (GLOBAL→LOCAL — pull a seed's participation kit, sha256-verified)",
                   "source": "rar", "path": "rar_loader_agent.py", "native": False,
                   "hint": "action=install name=rar_loader_agent.py"},
    "proximity": {"provides": "@rapp/proximity_discovery (geohash proximity — the Pizza-Place layer)",
                  "source": "rar", "path": "proximity_discovery_agent.py", "native": False,
                  "hint": "action=install name=proximity_discovery_agent.py"},
    "leaderboard": {"provides": "@rapp/species_leaderboard (Herald→Immortal global ladder)",
                    "source": "rar", "path": "species_leaderboard_agent.py", "native": False,
                    "hint": "action=install name=species_leaderboard_agent.py"},
}

# ── the phrasebook: everyday wishes → the rapp action that grants them ───────
# The translator's dictionary. The user says what they want in PLAIN words (they
# know nothing about rappids / cubbies / eggs / estates); `assist` matches their
# wish against these cues and hands back the end-to-end plan + the first call to
# run. Best cue-overlap wins; ordering is irrelevant.
INTENT_MAP = [
    {"intent": "Get set up (brand new)",
     "cues": ["get started", "getting started", "brand new", "first time", "set me up",
              "just installed", "new here", "start fresh", "how do i start", "set up",
              "setup", "onboard"],
     "plan": ["Mint your identity — a permanent passport for your being.",
              "Seed the core abilities so it can do the basics.",
              "Plant your front door so others can reach you.",
              "You now have a living being with an estate — just start talking to it."],
     "start": "action=mint owner=<your github login> slug=<a short name for your being>"},

    {"intent": "Remember something for me",
     "cues": ["remember", "don't forget", "dont forget", "keep track", "note that",
              "save this", "memorize", "my preference", "i like", "i take", "keep in mind",
              "hold on to", "store this", "make a note"],
     "plan": ["Save what you told it; it sticks across every future conversation.",
              "Next time it brings it up on its own — you never re-enter it."],
     "start": "action=memory op=save key=<short topic> value=<the thing to remember>"},

    {"intent": "What do you know about X / remind me",
     "cues": ["what do you know", "what did i tell you", "recall", "remind me",
              "look up what i said", "do you remember", "what was that"],
     "plan": ["Recall everything it has kept that matches your topic."],
     "start": "action=memory op=recall query=<the topic>"},

    {"intent": "A private place just for my people",
     "cues": ["private place", "just us", "my family", "our group", "clubhouse", "club house",
              "private space", "invite only", "secret place", "private neighborhood",
              "our own place", "only people i invite", "place for my", "just for us", "family room"],
     "plan": ["Plant a PRIVATE neighborhood — only invited people can ever enter.",
              "Each person gets their own corner that only they can write in.",
              "Invite your people by name; they scan and they're in.",
              "(It runs as a dry run first — say 'yes, create it' to make it real.)"],
     "start": "action=batcave owner=<your github login> slug=<a name> what=<who it's for>"},

    {"intent": "Keep my data private but still be findable",
     "cues": ["private estate", "hide my data", "keep substance private", "two tier", "two-tier",
              "discoverable but private", "public discovery private", "keep my stuff private",
              "don't expose", "dont expose", "privacy", "make my data private", "data private", "findable", "still findable", "private but findable", "keep my data private"],
     "plan": ["Split your estate: a public sign for discovery + a private vault for substance.",
              "Only a fingerprint of the private side is ever published — never the contents."],
     "start": "action=estate op=private-init"},

    {"intent": "Give someone a copy / share it",
     "cues": ["share", "give a copy", "send it to", "hand off", "hand it to", "pass it",
              "copy it to", "let my friend have", "give my", "send my", "share with",
              "give it to", "for my daughter", "for my son", "to my friend"],
     "plan": ["Pack the part you want into a single shareable file (an 'egg').",
              "Send that file any way you like; the other person opens it and your",
              "being wakes up on their machine knowing the same things."],
     "start": "action=cubby_egg cubby=<which corner to pack>"},

    {"intent": "Move it to another device / take it with me",
     "cues": ["move it", "another computer", "another device", "take it with me", "carry it",
              "my laptop too", "transfer", "on my phone", "on my other", "bring it to"],
     "plan": ["Pack your being into one file here.",
              "Open that file on the other device — it wakes up there, same as here."],
     "start": "action=cubby_egg cubby=<which to carry>"},

    {"intent": "A work corner / project space",
     "cues": ["work on", "a project", "a corner for", "overnight", "work area", "workspace",
              "sandbox", "dedicated space", "a place to build", "space for", "set aside"],
     "plan": ["Make a named corner (a 'cubby') for this project.",
              "Gather files and notes into it; it can even become its own helper later."],
     "start": "action=cubby_new slug=<short name> what=<what you're working on>"},

    {"intent": "A tool with its own screen / app",
     "cues": ["its own screen", "an app", "a dashboard", "a window", "visual tool", "interface",
              "a page for", "a screen for", "show me a screen", "with a ui", "with buttons"],
     "plan": ["Summon a ready-made mini-app — it opens its own screen on its own address.",
              "It's shaped for exactly that job and clears away when you're done."],
     "start": "action=summon rapplication=<which app, e.g. dataverse>"},

    {"intent": "Can it do X? / find the right ability",
     "cues": ["can it", "is there a way", "how do i", "which tool", "what can do",
              "i need something that", "is it possible", "able to", "find a way", "look for a"],
     "plan": ["Search for the exact part that does what you described.",
              "It names the part and the one line that pulls it in."],
     "start": "action=route need=<what you want it to do>"},

    {"intent": "Add a new ability / install",
     "cues": ["add ability", "install", "pull in", "get the agent for", "i want it to be able to",
              "teach it to", "give it the ability", "make it able"],
     "plan": ["Find the right specialist for that ability, then pull it in.",
              "Once pulled, your being can do the new thing right away."],
     "start": "action=route need=<the ability you want>"},

    {"intent": "Connect with others / join a group",
     "cues": ["join", "connect to", "connect with", "meet other", "neighbors", "a community",
              "others like me", "network with", "be part of", "find people", "a group to join", "connect me", "with other people", "other people", "with others"],
     "plan": ["Walk up to a neighborhood's front door and join it.",
              "Inside you can see who's there and what they're working on."],
     "start": "action=mount repo=<owner/repo of the neighborhood>"},

    {"intent": "Go public / publish / launch",
     "cues": ["go public", "publish", "launch", "make it public", "push to github", "release",
              "share with the world", "put it online", "make it live"],
     "plan": ["Plant a public front door for your being.",
              "Then push your local being out to it so anyone can reach you."],
     "start": "action=plant owner=<your github login> slug=<a name>"},

    {"intent": "Back up / don't lose my work",
     "cues": ["back up", "backup", "snapshot", "don't lose", "dont lose", "save my work",
              "archive", "preserve", "in case", "safe copy", "keep it safe"],
     "plan": ["Pack your work into one self-contained file you can store anywhere.",
              "If anything ever happens, open that file and everything comes back."],
     "start": "action=cubby_egg cubby=<which to back up>"},

    {"intent": "Who am I / my identity",
     "cues": ["who am i", "my identity", "my passport", "my id", "prove who i am",
              "what's my", "whats my", "am i registered"],
     "plan": ["Show your identity, your doors, and your corners at a glance."],
     "start": "action=whoami"},

    {"intent": "Where did this come from / its history",
     "cues": ["where did this come from", "lineage", "ancestry", "family tree", "history of",
              "heritage", "who made", "its parents", "where it came from"],
     "plan": ["Walk the family tree of your being all the way back to its origin."],
     "start": "action=lineage"},

    {"intent": "Is everything ok / health check",
     "cues": ["is everything ok", "everything okay", "health check", "self check", "self-check",
              "in sync", "verify", "integrity", "is it working", "all good"],
     "plan": ["Run a self-check that confirms every part still lines up."],
     "start": "action=verify"},

    {"intent": "Find people near me",
     "cues": ["near me", "nearby", "local to me", "around here", "close by", "in my area",
              "people near"],
     "plan": ["Find beings physically near you (the location-aware layer)."],
     "start": "action=route need=proximity"},

    {"intent": "My standing / rank",
     "cues": ["my rank", "standing", "reputation", "my score", "leaderboard", "my level",
              "how am i doing"],
     "plan": ["Show your standing — your tier and score in the wider network."],
     "start": "action=mmr"},
]

# Embedded ecosystem snapshot — the shape of the whole RAPP world, baked into
# this one file so a woods install knows what exists without any network. The
# LIVE list (currently ~57 parts) is pulled from rapp-god on `refresh`.
ECOSYSTEM_PARTS = {
    "kernel & install": ["RAPP (species root: kernel + specs)", "rapp_kernel (frozen DNA v0.6.0)",
                          "rapp-installer (curl|bash front door)", "RAPP_Desktop", "rapp-vscode-extension"],
    "identity & registry": ["rapp-god (registry of every part + version; drift observatory)",
                             "rapp-map (which repo houses which part)", "RAR (single-file agent registry)",
                             "rapp-static-apis (APIs on raw, no server)"],
    "stores & catalogs": ["RAPP_Store (rapplications)", "RAPP_Sense_Store (senses)", "rapp-egg-hub (eggs)"],
    "run a brainstem": ["vbrainstem (browser Pyodide runtime)", "rapp-brainstem-sdk (headless /chat)"],
    "channels & trust": ["rapp-sealed (AES-256-GCM §8 codec)", "rapp-kite (the string / operate kited twins)",
                          "rapp-kited-twin (kite mark)", "rapp-doorman (sealed-door skill)",
                          "rapp-neighborhood-protocol (the wire spec)"],
    "front doors & neighborhoods": ["rapp-vneighborhood (front-door template)", "rapp-commons (global town square)",
                                    "rapp-god-forum (threaded)", "rapp-resident (permanent cloud relay)"],
    "the agent-built web": ["rionet (rapp.robots.txt → rappbot → RIO)", "rio (the browser, OSI L7)"],
    "mcp & cartridges": ["rapp-mcp (MCP gateway — chat is the only wire)", "racon (experience cartridges)",
                         "rapp-carts (cartridge spec)"],
    "memory & social": ["CommunityRAPP (hippocampus)", "rappterbook (social net for agents)"],
}


def _fetch(url, timeout=10):
    """Offline-safe GET → text or None. The woods never crash this agent."""
    import urllib.request
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return r.read().decode("utf-8", "replace")
    except Exception:
        return None


def _fetch_status(url, timeout=10):
    """Offline-safe GET → (text|None, http_status|None). Distinguishes a real
    404 (the part isn't published yet) from no network at all (the woods)."""
    import urllib.error
    import urllib.request
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return r.read().decode("utf-8", "replace"), 200
    except urllib.error.HTTPError as e:
        return None, e.code
    except Exception:
        return None, None


def _fetch_bytes_status(url, timeout=10):
    """Offline-safe exact-octet GET → (bytes|None, http_status|None)."""
    import urllib.error
    import urllib.request
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            return response.read(), response.status
    except urllib.error.HTTPError as error:
        return None, error.code
    except Exception:
        return None, None


# ── helpers ───────────────────────────────────────────────────────────────
def _now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _sha256_file(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def _read_json(p, default=None):
    try:
        with open(p) as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError, ValueError):
        return default


def _read_text_file(p):
    """Read a local file as text → str or None (for file:// federation hints)."""
    try:
        with open(p, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return None


def _write_json(p, obj):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write("\n")


def _run(cmd, cwd=None):
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=120)
        return r.returncode, r.stdout.strip(), r.stderr.strip()
    except FileNotFoundError:
        return 127, "", f"{cmd[0]}: not found"
    except subprocess.TimeoutExpired:
        return 124, "", "timed out"


def _slugify(text, fallback="x"):
    s = re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")
    return s[:48] or fallback


# ── door_from_rappid (inline mirror of tools/door_address.py — agents are
#    self-contained per the contract; this parses canonical + owner/repo) ──
_ETERNITY_RE = re.compile(r"^rappid:@([a-z0-9]+(?:-[a-z0-9]+)*)/([a-z0-9]+(?:-[a-z0-9]+)*):([0-9a-f]{64})$")
_OWNERREPO_RE = re.compile(r"^([A-Za-z0-9][\w.-]*)/([A-Za-z0-9][\w.-]*)$")


def mint_rappid(owner, slug):
    """Canonical RAPP mint (spec §6.2, keyless):
    `rappid:@<owner>/<slug>:<64hex>` — tail is Hb("rapp/1:rappid", uuid4), never a name-hash.
    `kind` lives in the record, never the string. We NEVER mint the v2 form.

    owner/slug are canonicalized to the §6.1 grammar (lowercase, single hyphens):
    a real GitHub login like `Kody-W` or a repo like `My_Door.v2` would otherwise
    produce a rappid that fails rappid_valid — the address must be lowercase."""
    import uuid
    owner = _slugify(owner, fallback="anon")
    slug = _slugify(slug, fallback="x")
    h = hashlib.sha256(b"rapp/1:rappid\n" + uuid.uuid4().bytes).hexdigest()  # canonical keyless mint (spec §6.2), never sha256(name)
    return f"rappid:@{owner}/{slug}:{h}"


def door_from_rappid(rappid):
    """Return {owner, slug, kind?, urls{9}} for any locatable rappid, or None
    for a non-locatable form (e.g. a v3 key-fingerprint commons rappid)."""
    s = (rappid or "").strip()
    owner = slug = None
    for rx in (_ETERNITY_RE, _OWNERREPO_RE):
        m = rx.match(s)
        if m:
            owner, slug = m.group(1), m.group(2)
            break
    if not owner:
        return None
    raw = f"https://raw.githubusercontent.com/{owner}/{slug}/main"
    return {
        "owner": owner, "slug": slug, "rappid": rappid,
        "urls": {
            "repo": f"https://github.com/{owner}/{slug}",
            "front": f"https://{owner}.github.io/{slug}/",
            "identity": f"{raw}/rappid.json",
            "holocard": f"{raw}/card.json",
            "holo_md": f"{raw}/holo.md",
            "avatar": f"{raw}/holo.svg",
            "summon_qr": f"{raw}/holo-qr.svg",
            "members": f"{raw}/members.json",
            "facets": f"{raw}/facets.json",
        },
    }


def _build_super_rar(cubby_root):
    """The super-store: every kind across every cubby — not just agents."""
    entries = []
    if not os.path.isdir(cubby_root):
        return entries
    for handle in sorted(os.listdir(cubby_root)):
        if handle.startswith((".", "_")):
            continue
        for kind, (sub, pat) in SUPER_RAR_KINDS.items():
            for p in sorted(glob.glob(os.path.join(cubby_root, handle, sub, pat))):
                name = os.path.basename(p)
                if name.startswith(".") or name == "__pycache__":
                    continue
                e = {"kind": kind, "name": name, "cubby": handle,
                     "path": os.path.relpath(p, cubby_root), "streamable": kind == "agent"}
                if os.path.isfile(p):
                    try:
                        e["sha256"] = _sha256_file(p)
                        if p.endswith(".py"):
                            m = re.search(r'"""(.+?)(?:\n|""")',
                                          open(p, encoding="utf-8", errors="ignore").read(1200))
                            if m:
                                e["purpose"] = m.group(1).strip()[:140]
                    except OSError:
                        pass
                entries.append(e)
    return entries


def _q_match(q, entry, abs_path=None):
    """Search on ANYTHING: match the query against the entry's metadata AND the
    file's actual content (code, docstrings, tags) — so the operator can grep
    the whole estate by any term, not just filenames, and group the hits."""
    if not q:
        return True
    if q in json.dumps(entry, ensure_ascii=False).lower():
        return True
    if abs_path and os.path.isfile(abs_path):
        try:
            if os.path.getsize(abs_path) <= 512 * 1024:   # bound: skip huge blobs
                return q in open(abs_path, encoding="utf-8", errors="ignore").read().lower()
        except OSError:
            pass
    return False


_SPEC = """# Navigating a full RAPP estate — the map this agent embeds

RAPP is fractal: the same five primitives (rappid · door · card · tether ·
trust scope) repeat at every scale. From the outside in:

  ESTATE        one operator's union of everything they've planted + joined.
                Identity = the operator's rappid (~/.brainstem/rappid.json).
                Catalog  = ~/.brainstem/estate.json (created[] + member[]).
  NEIGHBORHOOD  a community-with-a-purpose; a GitHub repo is the gate. Public
                or PRIVATE (collaborator-gated). Has members + per-member cubbies.
  CUBBY         one member's isolated housing for a slice of estate — the SAME
                anatomy as a whole brainstem (agents/organs/senses/rapps/
                neighborhoods/eggs). rapp-cubby/1.0. Works on-device AND in a
                neighborhood; eggs round-trip between them.
  AGENT         one *_agent.py — the unit of capability. (You're running one.)

THE RAPPID IS THE ADDRESS (Art. XLVI). From any rappid, with zero auth, every
canonical URL is computable by string parsing — `action=door rappid=…` does it.
Forms: Eternity `rappid:@<owner>/<slug>:<64hex>` (current) · legacy v2 · a v3
key-fingerprint (commons; not locatable). The repo is `<owner>/<slug>`; fetch
any of the 9 files at raw.githubusercontent.com/<owner>/<slug>/main/.

PRIVATE doors 404 to outsiders — that's the guard, not obscurity. Reach them
with your own GitHub auth (collaborator access). A "dark door" has no public
front door at all; kited twins dial its rappid at the payphone and the live
room runs E2E over WebRTC.

BONES, NOT SUBSTANCE (PUBLIC_PRIVATE_BOUNDARY §1.8): a repo holds the SHARED
shape (agents, souls, manifests); each member's PII/secrets stay on-device.
This agent refuses secret-shaped files on stash/hatch.

THE EGG IS THE SNEAKERNET PRIMITIVE: pack any cubby/estate to a .egg and hatch
it anywhere — local→neighborhood (`cubby_egg` then `hatch`) or
neighborhood→local (`cubby_import`). Same structure both ways.

STREAM, DON'T COMMIT: `load` copies a cubby's agents into a brainstem's
agents/ AND registers them in .git/info/exclude → they run but are invisible
to git, so they can never be committed to a grail repo. `unload` reverses it;
kernel agents are never touched.

THE SUPER-RAR is the super-store: one registry over the WHOLE stack across
every cubby (not just agents) — search it to find what a neighbor already
built (`super_rar where=neighborhood query=…`) or your own local stack
(`where=local`).

THE GLOBAL GRAIL (stay drift-free): this file embeds a baseline of all of the
above so it works airdropped into the woods with no network. When online,
`action=refresh` pulls the latest from the canonical registries —
**rapp-god** (every part + every version, content-addressed, drift-observed),
**rapp-map** (which repo houses which part), the species **RAPP** specs
(SPEC.md / skill.md / ECOSYSTEM_MAP.md / CONSTITUTION.md), and the **RAPP-Bible**
(specs hub) — and caches them, so `action=spec` then serves the freshest canon.
`action=ecosystem` lists every part; `action=find query=…` searches them.

To go end to end: refresh (if online) → whoami → estate → ecosystem/find (what
exists) → door (resolve a neighbor) → mount → join → browse → super_rar → load
(stream what you need) / hatch (share what you made). One file. No drift.

The natural-language estate move (same super-RAR pattern, local + neighborhood):
"look up X in my local super-rar and show me what exists" → super_rar where=local
query=X. "put the twins for this project in their own cubby, egg it, and mirror
it in our private neighborhood" → cubby_collect slug=project-twins query=twin → cubby_egg
cubby=project-twins → mount → hatch path=<egg>. Search → collect → egg → mirror.

FORK A NAMED OWNED CUBBY + POP A TWIN: "egg-and-cubby this into a new cubby still
under my ownership" → cubby_fork slug=… from=non-kernel-agents. A neighborhood
fork is FRACTAL — it lands at cubbies/<me>/cubbies/<slug>/ (inside your own cubby,
so the guard passes and ownership is unambiguous) and ships a self-backup .egg in
its eggs/. A local fork lives at ~/.brainstem/cubbies/<slug>/. "cubby the non-kernel
agents into a twin and pop its chat" → twin cubby=<slug> (or cubby_fork …twin=true):
builds a twin workspace (~/.brainstem/twins/<name>/) from just those agents (+ the
kernel agents so it boots), boots a child brainstem on a free port, and hands back
a chat URL you use INSTEAD of the global brainstem.
"""


# ── the agent ───────────────────────────────────────────────────────────
class RappAgent(BasicAgent):
    def __init__(self):
        self.name = "RappAgent"
        self.metadata = {
            "name": self.name,
            "description": (
                "SIRI-LEVEL FRONT DOOR: the user speaks PLAIN language and knows NOTHING about rapp "
                "(no 'rappid'/'cubby'/'egg'/'estate'). Translate their wish into the right action(s), "
                "DO it end to end, then report back in THEIR words. Ambiguous wish? call "
                "action=assist problem='<their exact words>' → it returns a step-by-step plan + the "
                "first call to run; then execute that plan. NEVER make the user learn a term or run a "
                "raw command.\n"
                "THE single agent for the whole RAPP ecosystem. Pass action=<one enum value> PLUS "
                "that action's params (listed here). This metadata is ALL the caller gets, so pass "
                "exactly what the chosen action needs. Write actions commit+push by default — pass "
                "push=false to only stage locally. Unsure which action/params fit? call action=spec "
                "or action=route need='<what you want>' FIRST.\n"
                "ORIENT — spec (full ecosystem map) · ecosystem · find query=… · refresh · protocol · whoami · help\n"
                "IDENTITY/DOORS — estate (your doors) · door rappid=… [validate=true] (resolve + reachability-check any door)\n"
                "BOOTSTRAP — mint owner=… slug=… [kind=] [force=] (mint an Eternity rappid) · scaffold (seed kernel agents) · "
                "plant owner=… slug=… [kind=] [display_name=] [confirm=] (public front-door grail) · "
                "batcave owner=… slug=… [what=] (plant a PRIVATE cubby-neighborhood — dry-run unless confirm=true)\n"
                "REACH ANY SPECIALIST — install name=<file.py>|query=…|url=… [git_invisible=] [verify=] (pull + hot-load ANY agent) · "
                "route need='<free text>' (names the provider + its install line)\n"
                "TAILORED APPS — summon rapplication=<name under ~/.rapp/rapplications> [port=] (boot a rapplication as an isolated tailored-UI twin on its own port; idempotent)\n"
                "CUBBIES & TWINS (on-device) — cubby_new slug=… what=… · cubby_list · cubby_show cubby=… · "
                "cubby_collect slug=… query=… [source=cubbies|brainstem|all] · "
                "cubby_fork slug=… from='non-kernel-agents|brainstem|cubby:<slug>' [paths=] [egg=true] [twin=] · "
                "cubby_egg cubby=… · cubby_import path=… · twin cubby=… [soul=] (pop a twin chat from a cubby) · "
                "super_rar query=… [where=local|neighborhood] (search the whole estate)\n"
                "MEMORY (op required) — memory op=save key=… value=… | op=read [key=…] | op=recall query=…\n"
                "LINEAGE (op required) — bond op=record event=<birth|bond|hatch|graft|launch|adoption|rhythm> [context=] [egg_sha256=] | bond op=list · lineage (walk to species root)\n"
                "FEDERATE — beacon estate_url=… [private_estate_pointer=] (write the estate beacon) · sniff seed=<url> (BFS the network) · mmr (standing score)\n"
                "NEIGHBORHOOD (FIRST set repo=<owner/repo> or env RAPP_NEIGHBORHOOD) — mount · join what=… · browse · stash path=… [cubby=<slug>] · "
                "hatch path=… · load [cubby=] · unload · sync · branch topic=… · invite github_login=… [confirm=true] · qr · enter · "
                "show_and_tell title=… text=… · super_rar where=neighborhood query=…\n"
                "SELF-CHECK — verify (god≡map≡bible drift triangle)"),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["spec", "help", "protocol", "ecosystem",
                                 "find", "refresh", "whoami", "estate",
                                 "door", "cubby_new", "cubby_list", "cubby_show",
                                 "cubby_collect", "cubby_egg", "cubby_import",
                                 "cubby_fork", "twin", "twin_from_cubby", "summon", "super_rar",
                                 "mount", "join", "browse", "stash", "hatch",
                                 "load", "unload", "sync", "branch", "invite",
                                 "qr", "enter", "show_and_tell",
                                 # ── bootstrap + universal-reach (the god layer) ──
                                 "install", "route", "mint", "scaffold", "plant", "batcave",
                                 "memory", "bond", "lineage", "beacon", "sniff",
                                 "mmr", "verify",
                                 # ── the Siri front door: a plain-language wish → a plan ──
                                 "assist"],
                        "description": "what to do (action=spec for the full map)",
                    },
                    "repo": {"type": "string", "description": "neighborhood door owner/repo (or set RAPP_NEIGHBORHOOD)"},
                    "rappid": {"type": "string", "description": "door: any rappid to resolve"},
                    "cubby": {"type": "string", "description": "cubby/neighborhood/twin: a cubby slug or handle (stash: cubby=<slug> → an owned sub-cubby)"},
                    "slug": {"type": "string", "description": "cubby_new/cubby_fork: local cubby slug"},
                    "what": {"type": "string", "description": "cubby_new/join/cubby_fork: one-line 'what I'm working on'"},
                    "path": {"type": "string", "description": "stash/hatch/cubby_import/cubby_egg/cubby_fork: a file path"},
                    "paths": {"type": "array", "items": {"type": "string"},
                              "description": "cubby_fork: explicit file paths to fork in"},
                    "from": {"type": "string",
                             "description": "cubby_fork/twin: content set — 'non-kernel-agents' | 'brainstem' | 'cubby:<slug>'"},
                    "egg": {"type": "boolean", "description": "cubby_fork: pack a self-backup .egg into the new cubby (default true)"},
                    "twin": {"type": "boolean", "description": "cubby_fork: after forking, also boot a twin from the new cubby"},
                    "soul": {"type": "string", "description": "twin: soul.md text for the twin workspace"},
                    "query": {"type": "string", "description": "super_rar/cubby_collect: search term across your estate"},
                    "source": {"type": "string", "enum": ["cubbies", "brainstem", "all"],
                               "description": "cubby_collect: where to gather from (default all)"},
                    "where": {"type": "string", "enum": ["local", "neighborhood"],
                              "description": "super_rar: which stack (default neighborhood if mounted, else local)"},
                    "title": {"type": "string", "description": "show_and_tell: post title"},
                    "text": {"type": "string", "description": "show_and_tell: post body"},
                    "topic": {"type": "string", "description": "branch: topic for the personal branch"},
                    "github_login": {"type": "string", "description": "invite: collaborator to add"},
                    "confirm": {"type": "boolean", "description": "invite: actually run it (default dry-run)"},
                    "push": {"type": "boolean", "description": "write actions: commit+push (default true)"},
                    # ── bootstrap + universal-reach params ──
                    "need": {"type": "string", "description": "route: free-text operator need ('twin lifecycle', 'sealed channel', …)"},
                    "problem": {"type": "string", "description": "assist: the user's wish in their OWN plain words ('a private place for my family', 'remember my pills', 'set me up'); the agent translates it into a step-by-step plan + first call"},
                    "goal": {"type": "string", "description": "assist: alias for problem"},
                    "wish": {"type": "string", "description": "assist: alias for problem"},
                    "name": {"type": "string", "description": "install: exact agent filename (e.g. @rapp/twin_agent.py)"},
                    "owner": {"type": "string", "description": "mint/plant: GitHub owner/login"},
                    "kind": {"type": "string", "description": "mint/plant: door kind (default operator)"},
                    "display_name": {"type": "string", "description": "plant: human-readable door name"},
                    "op": {"type": "string", "enum": ["read", "save", "recall", "record", "list"],
                           "description": "memory: read|save|recall · bond: record|list"},
                    "key": {"type": "string", "description": "memory: the memory key"},
                    "value": {"type": "string", "description": "memory: the value to save"},
                    "event": {"type": "string", "description": "bond: lifecycle event kind (birth|bond|hatch|graft|launch|adoption|rhythm)"},
                    "context": {"type": "string", "description": "bond: a one-line note for the ledger entry"},
                    "egg_sha256": {"type": "string", "description": "bond: sha256 of the egg involved (optional)"},
                    "seed": {"type": "string", "description": "sniff: a seed URL serving .well-known/rapp-network.json"},
                    "estate_url": {"type": "string", "description": "beacon: the operator's public estate URL"},
                    "private_estate_pointer": {"type": "string", "description": "beacon: opaque pointer to the private estate"},
                    "indexable": {"type": "boolean", "description": "beacon: list this estate in public discovery (default true)"},
                    "git_invisible": {"type": "boolean", "description": "install: register in .git/info/exclude (default false)"},
                    "verify": {"type": "boolean", "description": "install/load/door: verify sha256 / reachability (default true)"},
                    "force": {"type": "boolean", "description": "mint: overwrite an existing rappid (mint-once is the default)"},
                    "validate": {"type": "boolean", "description": "door: HEAD/GET the identity URL to check reachability"},
                    "url": {"type": "string", "description": "install: a direct raw URL to an agent file"},
                    "rapplication": {"type": "string", "description": "summon: which rapplication to hatch as a tailored-UI twin (e.g. 'dataverse'); catalog in ~/.rapp/rapplications/"},
                    "port": {"type": "integer", "description": "summon: preferred port (default: first free in 7081-7200)"},
                },
                "required": ["action"],
            },
        }
        super().__init__(self.name, self.metadata)

    def system_context(self):
        return ("RappAgent is loaded — treat it as the Siri-level front door to the "
                "ENTIRE RAPP ecosystem. THE OPERATOR SPEAKS PLAIN, EVERYDAY LANGUAGE "
                "AND KNOWS NOTHING ABOUT RAPP. They will never say 'rappid', 'cubby', "
                "'egg', 'estate', 'beacon', or 'neighborhood' — they say things like "
                "'remember my pills', 'make a private place for my family', 'give my "
                "daughter a copy', 'set me up'. YOUR JOB is to translate their wish into "
                "the right action(s) and GRANT IT — end to end — without ever making them "
                "learn a term or run a raw command. Rules: (1) when a wish is even slightly "
                "ambiguous, call action=assist problem='<their exact words>' — it returns "
                "the step-by-step plan + the first call to run; (2) then EXECUTE that plan "
                "(call the named actions yourself, in order; fill blanks from context or ask "
                "ONE short plain question); (3) report back in THEIR words — 'Done, your "
                "family's private place is ready, just tell me who to invite' — never the "
                "rapp jargon you used under the hood. Quick phrasebook: 'remember this'->"
                "memory op=save · 'what do you know'->memory op=recall · 'private place for "
                "my people'->batcave · 'give/share a copy'->cubby_egg then they hatch · "
                "'move it to my laptop'->cubby_egg then hatch · 'set me up / brand new'->"
                "mint then scaffold then plant · 'a tool with its own screen'->summon · 'can "
                "it do X / find a way'->route or assist · 'who am I'->whoami · 'back up my "
                "work'->cubby_egg · 'join a group'->mount/join · 'go public'->plant/launch · "
                "'is everything ok'->verify. The single instruction the user EVER needs: "
                "talk to it, describe the problem, the wish gets granted. action=spec for "
                "the full map, action=route need=... to find any part, action=assist to "
                "translate any plain-language wish into a plan.")

    # ---- context ----
    def _ctx(self, kwargs):
        home = kwargs.get("_home_dir") or os.path.expanduser("~")
        repo = (kwargs.get("repo") or os.environ.get("RAPP_NEIGHBORHOOD") or
                (_read_json(os.path.join(home, ".brainstem", "rapp", "neighborhood.json")) or {}).get("repo"))
        slug = repo.split("/")[-1] if repo else None
        cache = os.path.join(home, ".brainstem", "neighborhoods", slug) if slug else None
        repo_dir = kwargs.get("_repo_dir") or (os.path.join(cache, "clone") if cache else None)
        offline = bool(kwargs.get("_repo_dir"))
        rec = _read_json(os.path.join(home, ".brainstem", "rappid.json")) or {}
        handle = kwargs.get("_handle")
        if not handle and not offline:
            rc, out, _ = _run(["gh", "api", "user", "--jq", ".login"])
            handle = out if rc == 0 and out else None
        return {"home": home, "repo": repo, "slug": slug, "cache": cache,
                "repo_dir": repo_dir, "offline": offline,
                "rappid": rec.get("rappid") or "rappid:unregistered",
                "handle": handle, "keys_dir": os.path.join(home, ".brainstem", "keys"),
                "loadout_path": os.path.join(cache, "loadout.json") if cache else None,
                "sync_path": os.path.join(cache, "last-sync.json") if cache else None,
                "cubby_root_local": os.path.join(home, ".brainstem", "cubbies")}

    def _env(self, action, status, **f):
        return json.dumps({"schema": "rapp-result/1.0", "action": action,
                           "status": status, **f}, indent=2, ensure_ascii=False)

    # ── the global grail: stay fresh online, embedded snapshot in the woods ──
    def _cache_dir(self, ctx):
        return os.path.join(ctx["home"], ".brainstem", "rapp", "grail-cache")

    def _refresh(self, ctx):
        """Pull the latest specs + part-registry from the global grail (when
        online) and cache them, so this one file stays current with canon."""
        cache = self._cache_dir(ctx)
        os.makedirs(cache, exist_ok=True)
        got, missed = {}, []
        name_map = {"spec": "SPEC.md", "skill": "skill.md", "ecosystem_map": "ECOSYSTEM_MAP.md",
                    "constitution": "CONSTITUTION.md", "bible": "BIBLE.md",
                    "god_status": "god-status.json", "god_registry": "god-registry.json"}
        for key, url in GRAIL_SOURCES.items():
            text = _fetch(url)
            if text is None:
                missed.append(key); continue
            open(os.path.join(cache, name_map[key]), "w").write(text)
            got[key] = len(text)
        if not got:
            return self._env("refresh", "offline",
                             note=("no network — running on the EMBEDDED spec + "
                                   "ecosystem snapshot baked into this file. The "
                                   "woods are fine; refresh next time you have "
                                   "internet to sync with the global grail."),
                             dashboards=DASHBOARDS)
        summary = None
        gs = _read_json(os.path.join(cache, "god-status.json"))
        if gs:
            summary = gs.get("summary")
        _write_json(os.path.join(cache, "meta.json"),
                    {"refreshed_at": _now(), "sources": list(got),
                     "missed": missed, "grail_summary": summary})
        return self._env("refresh", "success", refreshed=list(got), missed=missed,
                         grail_summary=summary, dashboards=DASHBOARDS,
                         note="synced with the global grail; action=spec now serves the latest canon.")

    def _live_parts(self, ctx):
        """Parts list: cached-from-grail if fresh, else live fetch, else None."""
        cached = os.path.join(self._cache_dir(ctx), "god-status.json")
        gs = _read_json(cached)
        if not gs:
            text = _fetch(GRAIL_SOURCES["god_status"])
            gs = json.loads(text) if text else None
        return gs

    def _ecosystem(self, kwargs, ctx):
        gs = self._live_parts(ctx)
        if gs:
            groups = {}
            for p in gs.get("parts", []):
                groups.setdefault(p.get("group", "?"), []).append(p.get("name"))
            return self._env("ecosystem", "success", source="rapp-god (live registry)",
                             summary=gs.get("summary"), generated=gs.get("generated"),
                             groups=groups, dashboards=DASHBOARDS,
                             note="every part + version, content-addressed; drift-observed.")
        return self._env("ecosystem", "embedded",
                         source="embedded snapshot (no network)",
                         groups=ECOSYSTEM_PARTS, dashboards=DASHBOARDS,
                         note=("the shape of the whole RAPP world, baked into this "
                               "file. action=refresh online for the live 57-part "
                               "registry from rapp-god."))

    def _find(self, kwargs, ctx):
        q = (kwargs.get("query") or "").strip().lower()
        if not q:
            return self._env("find", "error", error="pass query=<what part are you looking for>")
        gs = self._live_parts(ctx)
        hits = []
        if gs:
            for p in gs.get("parts", []):
                blob = json.dumps(p).lower()
                if q in blob:
                    hits.append({"name": p.get("name"), "group": p.get("group"),
                                 "kind": p.get("kind"), "note": p.get("note"),
                                 "drift": p.get("drift"), "versions": p.get("versions")})
            src = "rapp-god (live)"
        else:
            for grp, parts in ECOSYSTEM_PARTS.items():
                for name in parts:
                    if q in (grp + " " + name).lower():
                        hits.append({"name": name, "group": grp})
            src = "embedded snapshot"
        return self._env("find", "success", query=q, source=src, matches=len(hits),
                         results=hits[:40])

    def _commit_push(self, ctx, message, do_push):
        if ctx["offline"] or not do_push:
            return {"pushed": False, "planned": [
                f"git -C {ctx['repo_dir']} add -A",
                f"git -C {ctx['repo_dir']} commit -m '{message}'",
                f"git -C {ctx['repo_dir']} push"]}
        rd = ctx["repo_dir"]
        _run(["git", "-C", rd, "add", "-A"])
        rc, _, err = _run(["git", "-C", rd, "commit", "-m", message])
        if rc != 0 and "nothing to commit" not in err.lower():
            return {"pushed": False, "error": f"commit failed: {err[:200]}"}
        rc, _, err = _run(["git", "-C", rd, "push"])
        if rc != 0:
            return {"pushed": False, "error": (f"push failed ({err[:200]}). Are "
                    f"you a collaborator on {ctx['repo']}?")}
        return {"pushed": True}

    # ---- perform ----
    def perform(self, **kwargs):
        action = (kwargs.get("action") or "help").lower()
        if action in ("solve", "do", "wish", "help_me", "translate"):
            action = "assist"   # plain-language aliases for the Siri front door
        ctx = self._ctx(kwargs)

        # ── orient ──
        if action == "spec":
            # serve the freshest spec: pulled-from-grail cache if present, else
            # the embedded baseline that travels in this file (no drift, ever).
            cached = _read_json(os.path.join(ctx["home"], ".brainstem", "rapp", "grail-cache", "meta.json"))
            fresh = None
            if cached:
                sp = os.path.join(ctx["home"], ".brainstem", "rapp", "grail-cache", "SPEC.md")
                if os.path.exists(sp):
                    fresh = open(sp).read()
            head = ("[serving the LIVE grail spec, refreshed " + cached["refreshed_at"] + "]\n\n"
                    if (cached and fresh) else "[embedded baseline spec — run action=refresh online to pull the latest grail]\n\n")
            return head + _SPEC + (("\n\n---\n# Canonical SPEC.md (from the grail)\n\n" + fresh) if fresh else "")
        if action == "ecosystem":
            return self._ecosystem(kwargs, ctx)
        if action == "find":
            return self._find(kwargs, ctx)
        if action == "refresh":
            return self._refresh(ctx)
        if action == "protocol":
            return _SPEC.split("\n\n", 1)[0] + ("\n\nThis is one self-contained "
                   "agent (the contract). It names no door; point it with "
                   "repo=<owner/repo>. action=spec for the full map.")
        if action == "help" or action not in self.metadata["parameters"]["properties"]["action"]["enum"]:
            return (
                "RappAgent — the one agent for the whole RAPP ecosystem, end to end.\n"
                "  orient   : spec · ecosystem · find query=… · refresh (pull latest grail) ·\n"
                "             route need=… (which part does X?) · verify (drift-triangle self-check)\n"
                "  bootstrap: mint owner=… slug=… (Eternity rappid) · scaffold (seed kernel agents) ·\n"
                "             plant owner=… slug=… (front-door grail) · install name=…|query=… (pull ANY agent) ·\n"
                "             batcave owner=… slug=… (plant a PRIVATE cubby-neighborhood of your own) [confirm=true to create]\n"
                "  identity : whoami · estate · door rappid=… [validate=true] · beacon · mmr\n"
                "  lineage  : bond op=record event=… · bond op=list · lineage (walk to species root)\n"
                "  memory   : memory op=save key=… value=… · op=read [key=…] · op=recall query=…\n"
                "  federate : sniff seed=… (BFS the network) · beacon (write the estate beacon)\n"
                "  on-device: cubby_new slug=… · cubby_list · cubby_show cubby=… ·\n"
                "             super_rar where=local query=… (search your whole estate) ·\n"
                "             cubby_collect slug=… query=… (assemble a cubby from a search) ·\n"
                "             cubby_fork slug=… from=… (fork a NAMED cubby you own) ·\n"
                "             twin cubby=… (pop a twin chat from just a cubby's agents) ·\n"
                "             cubby_egg cubby=… · cubby_import path=… ·\n"
                "             summon rapplication=… (hatch a tailored-UI twin on its own port, e.g. dataverse)\n"
                "  neighborhood (repo=<owner/repo>):\n"
                "             mount · join · browse · stash path=… · hatch path=… ·\n"
                "             load [cubby=…] · unload · show_and_tell title=… ·\n"
                "             sync · branch topic=… · invite github_login=… ·\n"
                "             qr · enter · super_rar where=neighborhood query=…\n"
                "  action=spec for the full map · action=route need=X to find the right part.")

        # ── identity ──
        if action == "whoami":
            est = _read_json(os.path.join(ctx["home"], ".brainstem", "estate.json")) or {}
            created = est.get("created", [])
            return self._env(action, "success", rappid=ctx["rappid"],
                             github_handle=ctx["handle"],
                             estate_doors=len(created) + len(est.get("member", [])),
                             neighborhood=ctx["repo"],
                             local_cubbies=len([d for d in (os.listdir(ctx["cubby_root_local"])
                                 if os.path.isdir(ctx["cubby_root_local"]) else []) if not d.startswith('.')]))
        if action == "estate":
            op = (kwargs.get("op") or "show").lower()
            if op in ("private-init", "private_init", "private", "init"):
                return self._estate_private(kwargs, ctx, verify_only=False)
            if op in ("verify", "verify-commitment"):
                return self._estate_private(kwargs, ctx, verify_only=True)
            if op == "rebuild":
                return self._env(action, "route", op="rebuild",
                                 note="disaster recovery lives in tools/rebuild_estate.py — run: "
                                      "python3 tools/rebuild_estate.py --handle <gh> --apply "
                                      "(walks public GitHub to rebuild ~/.brainstem/estate.json).")
            est = _read_json(os.path.join(ctx["home"], ".brainstem", "estate.json"))
            if not est:
                return self._env(action, "empty",
                                 note="no ~/.brainstem/estate.json yet — plant or join a door first.")
            return self._env(action, "success", schema=est.get("schema"),
                             created=est.get("created", []), member=est.get("member", []))
        if action == "door":
            d = door_from_rappid(kwargs.get("rappid", ""))
            if not d:
                return self._env(action, "error",
                                 error="not a locatable rappid (canonical / owner/repo).")
            if kwargs.get("validate") or kwargs.get("verify"):
                # HEAD/GET the identity URL → is this door actually reachable?
                text, status = _fetch_status(d["urls"]["identity"])
                if status is None:
                    d["validation"] = {"checked": False, "reachable": None,
                                       "note": "offline — can't reach the door from the woods; "
                                               "the 9 URLs are still string-derived + correct."}
                else:
                    d["validation"] = {"checked": True, "status": status,
                                       "reachable": status == 200,
                                       "valid": bool(text and text.strip().startswith("{")),
                                       "note": ("public + live" if status == 200 else
                                                "404 — private door (auth needed) or not planted yet")}
            return self._env(action, "success", **d)

        # ── bootstrap + universal-reach (the god layer) ──
        if action in ("install", "route", "mint", "scaffold", "plant",
                      "memory", "bond", "lineage", "beacon", "sniff",
                      "mmr", "verify"):
            return self._god(action, kwargs, ctx)

        # ── the Siri front door: a plain-language wish → an executable plan ──
        if action == "assist":
            return self._assist(kwargs, ctx)

        # ── summon a rapplication as a tailored twin (its own UI + port) ──
        if action == "summon":
            return self._summon(kwargs, ctx)

        # ── plant a PRIVATE cubby-neighborhood (batcave pattern) for any operator ──
        if action == "batcave":
            return self._batcave(kwargs, ctx)

        # ── fork a NAMED owned cubby / pop a twin chat from a cubby ──
        if action == "cubby_fork":
            return self._cubby_fork(kwargs, ctx)
        if action in ("twin", "twin_from_cubby"):
            return self._twin(kwargs, ctx)

        # ── on-device cubbies ──
        if action.startswith("cubby_") or (action == "super_rar" and kwargs.get("where") == "local"):
            return self._cubby(action, kwargs, ctx)

        # ── neighborhood ──
        if not ctx["repo"]:
            return self._env(action, "error",
                             error=("no neighborhood set — pass repo=<owner/repo>, "
                                    "set RAPP_NEIGHBORHOOD, or write "
                                    "~/.brainstem/rapp/neighborhood.json {repo}."))
        return self._neighborhood(action, kwargs, ctx)

    # ── summon: hatch a rapplication as a tailored twin with its OWN UI ──
    # Generalizes the per-twin-UI pattern: a rapplication template lives at
    # ~/.rapp/rapplications/<name>/ (agents/ + web/index.html + soul.md +
    # serve.py). summon copies it into an isolated twin workspace, boots it via
    # the kernel-safe serve.py wrapper (overrides only the "/" view → the twin's
    # own UI; exposes /api/agent/<Name>), on its own free port. Idempotent:
    # re-summoning a live rapplication just returns its URL. Kernel untouched.
    def _summon(self, kwargs, ctx):
        import socket, subprocess, hashlib, shutil, sys, time, urllib.request
        name = (kwargs.get("rapplication") or kwargs.get("name") or "dataverse").strip().lower()
        home = ctx["home"]
        cat = os.path.join(home, ".rapp", "rapplications")
        tmpl = os.path.join(cat, name)
        if not os.path.isdir(tmpl):
            return self._env("summon", "error", error=f"no rapplication '{name}'",
                             available=[d for d in (os.listdir(cat) if os.path.isdir(cat) else [])
                                        if not d.startswith(".")],
                             note="Add one under ~/.rapp/rapplications/<name>/ "
                                  "(agents/, web/index.html, soul.md, serve.py).")
        # Directory key — a stable slug of the name so re-summons reuse the same
        # workspace. This is a FILESYSTEM path, not an identity; name-derived is fine.
        dir_key = hashlib.sha256(f"kody/{name}-twin".encode()).hexdigest()[:32]
        ws = os.path.join(home, ".rapp", "twins", dir_key)
        portfile = os.path.join(ws, ".port")

        def _alive(p):
            try:
                with urllib.request.urlopen(f"http://localhost:{p}/version", timeout=2) as r:
                    return r.status == 200
            except Exception:
                return False

        # already live? reuse it.
        if os.path.exists(portfile):
            try:
                p = int(open(portfile).read().strip())
                if _alive(p):
                    return self._env("summon", "already_live", rapplication=name,
                                     url=f"http://localhost:{p}", port=p, workspace=ws,
                                     note=f"{name} twin already running — open the URL.")
            except Exception:
                pass

        # hatch the workspace from the template (idempotent)
        os.makedirs(os.path.join(ws, ".brainstem_data"), exist_ok=True)
        for sub in ("agents", "web"):
            dst = os.path.join(ws, sub)
            if not os.path.isdir(dst) and os.path.isdir(os.path.join(tmpl, sub)):
                shutil.copytree(os.path.join(tmpl, sub), dst)
        for f in ("soul.md", "serve.py"):
            s = os.path.join(tmpl, f)
            if os.path.exists(s):
                shutil.copy(s, os.path.join(ws, f))
        # Identity: mint ONCE, keyless (§6.2), then reuse — re-summoning must not
        # change the twin's rappid. Never sha256(name): that's the cardinal sin
        # and yields an invalid 32-hex tail. kind lives in the record, not the string.
        rj_path = os.path.join(ws, "rappid.json")
        existing = _read_json(rj_path, default=None)
        if isinstance(existing, dict) and _ETERNITY_RE.match(str(existing.get("rappid", ""))):
            rappid = existing["rappid"]
        else:
            rappid = mint_rappid(ctx.get("handle") or "kody", _slugify(f"{name}-twin"))
        _write_json(rj_path, {
            "schema": "rapp/1", "rappid": rappid,
            "parent_rappid": "rappid:@kody-w/rapp:9a8f0a4b5a710e20f4d819a0f37d2a4c9f113b5e78fb3c29e70b54fff48a38f9",
            "kind": "twin", "name": f"{name}-twin", "born_at": _now(),
            "notes": f"Summoned rapplication '{name}' as an isolated tailored-UI twin."})

        # pick a free port
        def _free(p):
            s = socket.socket()
            try:
                s.bind(("127.0.0.1", p)); return True
            except OSError:
                return False
            finally:
                s.close()
        pref = int(kwargs.get("port") or 0)
        port = pref if (pref and _free(pref)) else next((p for p in range(7081, 7201) if _free(p)), 0)
        if not port:
            return self._env("summon", "error", error="no free port in 7081-7200")

        # boot via the kernel-safe wrapper (serve.py) in a detached process
        kernel = os.getcwd()  # the brainstem runs from its own dir
        env = dict(os.environ, TWIN_WS=ws, KERNEL=kernel, PORT=str(port), VOICE_MODE="off")
        logf = open(os.path.join(ws, "serve.log"), "a")
        subprocess.Popen([sys.executable, os.path.join(ws, "serve.py")],
                         env=env, stdout=logf, stderr=logf, cwd=kernel, start_new_session=True)
        for _ in range(20):
            if _alive(port):
                break
            time.sleep(0.6)
        open(portfile, "w").write(str(port))
        live = _alive(port)
        return self._env("summon", "success" if live else "booting", rapplication=name,
                         url=f"http://localhost:{port}", port=port, workspace=ws,
                         rappid=rappid, live=live,
                         note=(f"{name} twin is LIVE with its tailored UI — open http://localhost:{port}"
                               if live else "booting — give it a few seconds, then open the URL."))

    # ── batcave: plant a PRIVATE cubby-neighborhood for ANY operator ──
    # The batcave pattern, generic: each member gets cubbies/<login>/ (their own
    # full on-device rapp estate, parked to share), an append-only signed events/
    # stream, and CODEOWNERS-gated writes. Names no specific batcave — the
    # operator owns theirs. Dry-run by default; confirm=true creates the PRIVATE
    # GitHub repo + pushes.
    def _batcave(self, kwargs, ctx):
        owner = (kwargs.get("owner") or ctx.get("handle") or "").strip()
        slug = (kwargs.get("slug") or "batcave").strip()
        if not owner:
            return self._env("batcave", "error", error="need owner=<github-login> (or sign into gh).")
        # Canonical keyless §6.2 mint (owner/slug canonicalized to §6.1 by mint_rappid).
        rappid = mint_rappid(owner, slug)
        what = kwargs.get("what") or "a private place to park cubbies and show what we're cooking"
        out = os.path.join(ctx["home"], ".brainstem", "plant", slug)
        soul = ("# " + slug + "\n\n## Identity — read this every turn\n"
                "You are the soul of a PRIVATE cubby-neighborhood (the batcave pattern). Members park "
                "their own full rapp estate in `cubbies/<their-login>/` and show each other what they're "
                "cooking. Welcome members, point them at their cubby, help them stream agents into their "
                "local brainstem, and keep the events stream tidy. Never write inside another member's "
                "cubby — cross-cubby changes ride pull requests the owner merges.\n")
        readme = ("# " + slug + "\n\nA **private cubby-neighborhood** — the batcave pattern. Each member "
                  "gets `cubbies/<your-login>/`: a full on-device rapp estate, parked here to share. Reach is "
                  "by invite only; there is no public front door.\n\n## Join\n1. Accept the collaborator invite.\n"
                  "2. In your brainstem: \"use the rapp agent to join the neighborhood and set up my cubby\" "
                  "(repo=" + owner + "/" + slug + ").\n\nSchema family: rapp-batcave-cubby/1.0 · "
                  "rapp-batcave-cubbies/1.0 · rapp-batcave-event/1.0.\n")
        # Parent is the operator's own rappid IF they've minted a valid one — the
        # ctx sentinel "rappid:unregistered" is truthy but fails §6.1, so guard on
        # the grammar and fall back to the canonical species root, never the sentinel.
        _op = ctx.get("rappid") or ""
        parent = _op if _ETERNITY_RE.match(_op) else SPECIES_ROOT_RAPPID
        files = {
            "rappid.json": json.dumps({"schema": "rapp/1", "rappid": rappid,
                "parent_rappid": parent,
                "kind": "neighborhood", "name": slug, "owner": owner, "born_at": _now(),
                "notes": "Private cubby-neighborhood (batcave pattern): per-member cubbies, signed events, no public front door."}, indent=2),
            "neighborhood.json": json.dumps({"schema": "rapp-batcave/1.0", "rappid": rappid, "name": slug,
                "kind": "batcave", "visibility": "private", "sealed": True,
                "cubbies_dir": "cubbies", "events_dir": "events",
                "schemas": ["rapp-batcave-cubby/1.0", "rapp-batcave-cubbies/1.0", "rapp-batcave-event/1.0", "rapp-batcave-loadout/1.0"]}, indent=2),
            "members.json": json.dumps({"schema": "rapp-neighborhood-members/1.0", "gate": "closed",
                "members": [{"login": owner, "rappid": rappid, "role": "planter", "joined_at": _now()}]}, indent=2),
            "cubbies/index.json": json.dumps({"schema": "rapp-batcave-cubbies/1.0", "cubbies": [owner]}, indent=2),
            "cubbies/" + owner + "/cubby.json": json.dumps({"schema": "rapp-batcave-cubby/1.0",
                "owner": owner, "what": what, "created_at": _now()}, indent=2),
            "cubbies/" + owner + "/agents/.gitkeep": "",
            "cubbies/" + owner + "/show-and-tell/.gitkeep": "",
            "events/.gitkeep": "",
            ".github/CODEOWNERS": "# each member owns their cubby\ncubbies/" + owner + "/ @" + owner + "\n",
            ".nojekyll": "",
            "soul.md": soul,
            "README.md": readme,
        }
        for rel, content in files.items():
            fp = os.path.join(out, rel)
            os.makedirs(os.path.dirname(fp), exist_ok=True)
            open(fp, "w").write(content)
        res = {"rappid": rappid, "owner": owner, "slug": slug, "local_dir": out,
               "scaffolded": sorted(files.keys())}
        if not kwargs.get("confirm"):
            return self._env("batcave", "scaffolded", note=("dry run — scaffolded the batcave grail at "
                + out + ". Re-run with confirm=true to create the PRIVATE repo " + owner + "/" + slug + " and push."), **res)
        _run(["git", "init", out])
        _run(["git", "-C", out, "add", "-A"])
        _run(["git", "-C", out, "-c", "user.name=rapp", "-c", "user.email=rapp@localhost", "commit", "-m", "plant batcave"])
        rc, _, err = _run(["gh", "repo", "create", owner + "/" + slug, "--private", "--source", out, "--remote", "origin", "--push"])
        if rc != 0:
            return self._env("batcave", "error", error=("gh repo create/push failed: " + err[:200]), **res)
        return self._env("batcave", "success", url="https://github.com/" + owner + "/" + slug,
            note=("Planted your private batcave " + owner + "/" + slug + ". Invite members → each gets cubbies/<login>/."), **res)

    # ══════════════════════════════════════════════════════════════════════
    # THE GOD LAYER — bootstrap a fresh organism + REACH the whole ecosystem.
    # This file natively operates the core; everything else it pulls in via
    # `install` (named by `route`). One drop = the whole ecosystem.
    # ══════════════════════════════════════════════════════════════════════
    def _bs_dir(self, kwargs):
        """Where the live brainstem's agents/ live (this file sits in agents/)."""
        return kwargs.get("_brainstem_dir") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def _god(self, action, kwargs, ctx):
        if action == "route":
            return self._route(kwargs, ctx)
        if action == "install":
            return self._install(kwargs, ctx)
        if action == "mint":
            return self._mint(kwargs, ctx)
        if action == "scaffold":
            return self._scaffold(kwargs, ctx)
        if action == "plant":
            return self._plant(kwargs, ctx)
        if action == "memory":
            return self._memory(kwargs, ctx)
        if action == "bond":
            return self._bond(kwargs, ctx)
        if action == "lineage":
            return self._lineage(kwargs, ctx)
        if action == "beacon":
            return self._beacon(kwargs, ctx)
        if action == "sniff":
            return self._sniff(kwargs, ctx)
        if action == "mmr":
            return self._mmr(kwargs, ctx)
        if action == "verify":
            return self._verify(kwargs, ctx)
        return self._env(action, "error", error="unknown god op")

    # ── route: the capability map — "how do I do X across the ecosystem?" ──
    def _assist(self, kwargs, ctx):
        """The Siri front door. The user describes a wish in PLAIN words and knows
        nothing about rapp; map it to the end-to-end plan + the first call to run.
        Deterministic (works offline, no LLM). The calling LLM then EXECUTES the
        plan and reports the granted wish back in the user's words — never the
        rapp jargon used under the hood."""
        text = (kwargs.get("problem") or kwargs.get("goal") or kwargs.get("wish")
                or kwargs.get("query") or kwargs.get("need") or "").strip()
        if not text:
            return self._env("assist", "ask",
                note="Tell me what you want in your own words — like 'a private place "
                     "just for my family', 'remember I take my pill at night', or "
                     "'set me up, I'm brand new'. I'll turn it into the steps and do it.",
                i_can=[i["intent"] for i in INTENT_MAP])
        low = " " + text.lower() + " "
        words = set(low.replace("?", " ").replace(".", " ").replace(",", " ")
                       .replace("!", " ").split())
        scored = []
        for spec in INTENT_MAP:
            phrase_hits = [c for c in spec["cues"] if c in low]
            word_hits = sum(1 for c in spec["cues"] if " " not in c and c in words)
            score = len(phrase_hits) * 5 + word_hits
            if score:
                scored.append((score, spec, phrase_hits))
        scored.sort(key=lambda x: -x[0])
        if not scored:
            # no everyday-intent match → fall back to the live parts-catalog search
            r = json.loads(self._route({"need": text}, ctx))
            return self._env("assist", "routed", wish=text,
                note="That didn't match a common everyday request, so I searched the "
                     "full parts catalog for something that fits.",
                route=r, i_can=[i["intent"] for i in INTENT_MAP])
        top = scored[0]
        alts = [{"intent": s["intent"], "start": s["start"]} for _, s, _ in scored[1:4]]
        confident = top[0] >= 5 or len(scored) == 1 or top[0] >= scored[1][0] * 2
        return self._env("assist", "plan", wish=text,
            intent=top[1]["intent"], matched_on=top[2],
            confidence="high" if confident else "medium",
            plan=top[1]["plan"], start=top[1]["start"], alternatives=alts,
            note="This is the whole path for what the user asked. EXECUTE it for them: "
                 "run `start` (fill the <...> from what they said, or ask ONE short plain "
                 "question), then walk the `plan` by calling those actions yourself. Report "
                 "back in THEIR words — say the wish was granted, not which rapp parts you "
                 "used. They never need to learn a single rapp term.")

    def _route(self, kwargs, ctx):
        need = (kwargs.get("need") or kwargs.get("query") or "").strip().lower()
        if not need:
            return self._env("route", "error",
                             error="pass need=<what you want to do> (e.g. 'twin lifecycle', 'sealed channel').",
                             known_needs=sorted(CAPABILITY_MAP.keys()))
        # best keyword overlap against the map (substring both ways)
        hits = []
        for kw, spec in CAPABILITY_MAP.items():
            if kw in need or need in kw or any(t in kw for t in need.split()):
                hits.append((kw, spec))
        if not hits:   # widen: scan the whole spec blob
            for kw, spec in CAPABILITY_MAP.items():
                if any(t in json.dumps(spec).lower() for t in need.split()):
                    hits.append((kw, spec))
        if not hits:
            return self._env("route", "no_match", need=need,
                             note="no mapped provider — try action=find query=… (live part search) "
                                  "or action=ecosystem to see every part.",
                             known_needs=sorted(CAPABILITY_MAP.keys()))
        routes = []
        for kw, spec in hits:
            src = spec.get("source")
            install_call = None
            if src in ("rar", "store", "sense") and spec.get("native") is not True:
                if spec.get("path"):
                    install_call = f"action=install name={spec['path'].replace('%40', '@')}"
                else:
                    install_call = f"action=install query={kw} source={src}"
            routes.append({"need_keyword": kw, "provides": spec["provides"],
                           "native": spec.get("native", False), "source": src,
                           "how": spec.get("hint"), "install": install_call})
        return self._env("route", "success", need=need, matches=len(routes), routes=routes,
                         note=("native:true → this agent already does it (run the `how`). "
                               "else → run the `install` call to pull the specialist in."))

    # ── install: pull ANY agent into the brainstem's agents/ from any source ──
    def _install(self, kwargs, ctx):
        name = (kwargs.get("name") or "").strip()
        query = (kwargs.get("query") or "").strip()
        source = (kwargs.get("source") or "").strip().lower()
        direct = (kwargs.get("url") or "").strip()
        bs = self._bs_dir(kwargs)
        target_dir = os.path.join(bs, "agents")

        # resolve the source URL(s) to try — name → exact file; query → search a catalog
        candidates = []   # list of (label, fetch_url, dest_filename)
        if direct:
            fn = os.path.basename(direct.split("?")[0]) or "installed_agent.py"
            candidates.append(("url", direct, fn))
        elif name:
            fn = os.path.basename(name)
            if not source or source == "rar":
                candidates.append(("rar", f"{RAR_RAW}/{name.replace('@', '%40')}", fn))
            if source == "neighborhood" and ctx.get("repo_dir"):
                local = os.path.join(ctx["repo_dir"], "rar", "index.json")
                candidates.append(("neighborhood", local, fn))
        elif query:
            # catalog search: name a hit, then offer the install-by-name follow-up
            idx_url = {"store": STORE_INDEX, "sense": SENSE_INDEX}.get(source or "store", STORE_INDEX)
            text = _fetch(idx_url)
            if text is None:
                return self._env("install", "needs_network", query=query, source=source or "store",
                                 catalog=idx_url, native_alternative=None,
                                 note=("offline — can't search the catalog from the woods. When "
                                       "online, this fetches %s and names the matching install. "
                                       "Or use action=route need=%s to find the provider." % (idx_url, query)))
            try:
                idx = json.loads(text)
                items = idx.get("rapplications") or idx.get("senses") or idx.get("items") or idx.get("agents") or []
            except (ValueError, AttributeError):
                items = []
            ql = query.lower()
            hits = [it for it in items if ql in json.dumps(it).lower()][:20]
            return self._env("install", "search", query=query, source=source or "store",
                             catalog=idx_url, matches=len(hits), results=hits,
                             note="pick one and re-run with name=<its agent file> (or path/url).")
        else:
            return self._env("install", "error",
                             error="pass name=<agent file> (e.g. @rapp/twin_agent.py), "
                                   "query=<search a catalog>, or url=<direct raw url>.")

        # try each candidate URL in order; offline → clear note + the source URL
        last_url = None
        for label, url, dest_fn in candidates:
            last_url = url
            if label == "neighborhood":
                # local rar index → look up the path, then fetch from the door raw prefix
                idx = _read_json(url)
                if not idx:
                    continue
                ent = next((a for a in idx.get("agents", [])
                            if os.path.basename(a.get("path", "")) == dest_fn
                            or a.get("name") == name), None)
                if not ent:
                    continue
                # prefer the clone-local file; verify against the manifest sha256
                clone_file = os.path.join(ctx["repo_dir"], ent.get("path", ""))
                body = None
                if os.path.isfile(clone_file):
                    body = open(clone_file, "rb").read()
                else:
                    prefix = idx.get("raw_url_prefix")
                    if prefix:
                        text = _fetch(f"{prefix}/{ent.get('path', '')}")
                        body = text.encode() if text is not None else None
                if body is None:
                    continue
                if kwargs.get("verify", True) and ent.get("sha256"):
                    got = hashlib.sha256(body).hexdigest()
                    if got != ent["sha256"]:
                        return self._env("install", "refused", agent=dest_fn,
                                         error=f"sha256 drift vs neighborhood rar manifest "
                                               f"({got[:12]}… != {ent['sha256'][:12]}…) — refusing.")
                return self._land_agent(target_dir, dest_fn, body, label, kwargs, ctx, bs,
                                        verified=bool(ent.get("sha256")))
            text = _fetch(url)
            if text is None:
                continue
            return self._land_agent(target_dir, dest_fn, text.encode(), label, kwargs, ctx, bs,
                                    verified=False)

        # nothing landed — offline or 404
        return self._env("install", "needs_network",
                         name=name or None, query=query or None, source=source or "rar",
                         tried=[c[1] for c in candidates], source_url=last_url,
                         note=("offline (or not found) — couldn't fetch from the source. When "
                               "you have network, this drops the agent into agents/ and it "
                               "hot-loads. Source URL above. Use action=route need=… to confirm "
                               "the right specialist first."))

    def _land_agent(self, target_dir, dest_fn, body, label, kwargs, ctx, bs, verified):
        if not dest_fn.endswith("_agent.py"):
            stem = dest_fn[:-3] if dest_fn.endswith(".py") else dest_fn
            dest_fn = stem + "_agent.py"
        if _SECRET_NAME_RE.search(dest_fn):
            return self._env("install", "refused", agent=dest_fn,
                             error="secret-shaped filename — refusing (bones, not substance).")
        if dest_fn in KERNEL_AGENTS:
            return self._env("install", "refused", agent=dest_fn,
                             error="that's a kernel agent — the kernel is sacred (Art. XXXIII); never overwritten.")
        # Guarding the filename is not enough: the brainstem collides on the
        # DECLARED name and quarantines whichever file sorts later. Since the
        # publisher's own @namespace becomes the installed filename, a file that
        # never touches a kernel FILENAME can still sort first, claim a kernel
        # NAME, and get the kernel agent quarantined instead of itself.
        try:
            _clash = _declared_agent_names(body.decode("utf-8", "replace")) \
                     & KERNEL_AGENT_NAMES
        except Exception:  # noqa: BLE001 — never let the guard break the path
            _clash = set()
        if _clash:
            return self._env(
                "install", "refused", agent=dest_fn,
                error=("declares the kernel agent name(s) "
                       + ", ".join(sorted(_clash))
                       + " — the brainstem resolves name collisions by load "
                         "order, so this would quarantine the kernel agent "
                         "rather than itself. Rename the agent."))
        os.makedirs(target_dir, exist_ok=True)
        dst = os.path.join(target_dir, dest_fn)
        with open(dst, "wb") as f:
            f.write(body)
        digest = hashlib.sha256(body).hexdigest()
        result = {"agent": dest_fn, "from": label, "path": dst,
                  "sha256": digest, "verified": verified}

        # Provenance sidecar. Every value here was already computed on this
        # path and thrown away into the response envelope; nothing new is
        # fetched. Without it, "what code will execute on my next message and
        # where did it come from" is unanswerable from disk -- and when a
        # publisher is later found compromised there is no way to enumerate who
        # received the bad artifact or when.
        #
        # It is also the substrate revocation needs: RAR already models a
        # `revoked` lifecycle that no brainstem can act on, because no
        # brainstem ever recorded the digest it accepted.
        try:
            origin = {
                "schema": "rapp-agent-origin/1.0",
                "agent": dest_fn,
                "sha256": digest,
                "bytes": len(body),
                "source": label,
                "source_url": kwargs.get("url") or kwargs.get("source") or None,
                "rappid": kwargs.get("rappid") or None,
                "verified": bool(verified),
                "installed_at": _dt.datetime.now(
                    _dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "installer": "@rapp/rapp",
            }
            with open(dst + ".origin.json", "w") as _f:
                json.dump({k: v for k, v in origin.items() if v is not None},
                          _f, indent=2, sort_keys=True)
                _f.write("\n")
            result["origin"] = os.path.basename(dst) + ".origin.json"
            # Append-only install ledger: HASHES AND POINTERS ONLY. Never the
            # body. An append-only log that cannot delete, combined with a
            # constitutional duty to keep parsing it forever, turns one
            # careless append of content into a permanent disclosure with no
            # takedown path.
            _ledger = os.path.join(
                os.path.dirname(os.path.dirname(os.path.abspath(target_dir))),
                ".brainstem_data", "installed.jsonl")
            os.makedirs(os.path.dirname(_ledger), exist_ok=True)
            with open(_ledger, "a") as _f:
                _f.write(json.dumps(origin, sort_keys=True) + "\n")
        except Exception as _e:  # noqa: BLE001 — provenance must never block
            result["origin_error"] = f"{type(_e).__name__}: {_e}"
        # optional git-invisibility (zero grail-repo commit risk), like `load`
        if kwargs.get("git_invisible"):
            excluded = self._register_excludes(bs, target_dir, [dest_fn])
            result["git_excluded"] = excluded
        result["note"] = ("installed — restart-free hot-load (the brainstem re-discovers "
                          "agents/ every request). The LLM now has its tool.")
        return self._env("install", "success", **result)

    # ── mint: an Eternity rappid into ~/.brainstem/rappid.json (mint ONCE) ──
    def _mint(self, kwargs, ctx):
        owner = (kwargs.get("owner") or ctx.get("handle") or "").strip()
        slug = (kwargs.get("slug") or "").strip()
        kind = (kwargs.get("kind") or "operator").strip()
        if not owner or not slug:
            return self._env("mint", "error",
                             error="pass owner=<github login> and slug=<door name>.")
        if not _HANDLE_RE.match(owner) or not _SLUG_RE.match(slug):
            return self._env("mint", "error", error="owner/slug have an unsafe shape.")
        path = os.path.join(ctx["home"], ".brainstem", "rappid.json")
        existing = _read_json(path)
        if existing and existing.get("rappid") and not kwargs.get("force"):
            return self._env("mint", "exists", rappid=existing.get("rappid"),
                             note=("a rappid is already minted — mint-once is the law (Art. "
                                   "XLVI): the rappid is your permanent global address and "
                                   "survives every kernel upgrade. Pass force=true only to "
                                   "re-mint a fresh organism."))
        rappid = mint_rappid(owner, slug)
        rec = {"schema": "rapp/1", "rappid": rappid, "kind": kind,
               "name": slug, "owner": owner, "repo": slug, "host": "github.com",
               "github": f"https://github.com/{owner}/{slug}",
               "parent_rappid": (existing or {}).get("parent_rappid") or SPECIES_ROOT_RAPPID,
               "parent_repo": f"https://github.com/{RAPP_SPECIES}",
               "minted_at": _now(),
               "notes": ("Eternity format (Art. XXXIV.1): rappid:@<owner>/<slug>:<64hex>, "
                         "the 64-hex tail is a keyless domain-separated mint "
                         "Hb('rapp/1:rappid', uuid4) — NOT sha256('%s/%s'). kind lives "
                         "in the record, not the string." % (owner, slug))}
        _write_json(path, rec)
        # the spine: a mint is a birth — record it on the lineage ledger
        self._bond_record(ctx, {"kind": "birth", "rappid": rappid,
                                 "context": f"minted {kind} rappid for {owner}/{slug}"})
        return self._env("mint", "success", rappid=rappid, kind=kind, path=path,
                         note="your permanent global address (Art. XLVI). Recorded a `birth` on the bond ledger.")

    # ── scaffold: seed the kernel agents into agents/ from the species grail ──
    def _scaffold(self, kwargs, ctx):
        bs = self._bs_dir(kwargs)
        target = os.path.join(bs, "agents")
        os.makedirs(target, exist_ok=True)
        seeds = sorted(KERNEL_AGENTS)
        got, missed, present = [], [], []
        for fn in seeds:
            dst = os.path.join(target, fn)
            if os.path.isfile(dst):
                present.append(fn); continue
            url = f"{_RAW}/{RAPP_SPECIES}/main/rapp_brainstem/agents/{fn}"
            text = _fetch(url)
            if text is None:
                missed.append(fn); continue
            with open(dst, "w") as f:
                f.write(text)
            got.append(fn)
        if not got and missed:
            return self._env("scaffold", "needs_network", needed=missed, present=present,
                             source=f"{_RAW}/{RAPP_SPECIES}/main/rapp_brainstem/agents/",
                             note=("offline — these kernel seed agents aren't here yet. When "
                                   "online, scaffold fetches them from the species grail. (The "
                                   "kernel itself — brainstem.py/basic_agent.py — ships with the "
                                   "installer, never with an agent.)"))
        return self._env("scaffold", "success", installed=got, already_present=present,
                         missed=missed, target=target,
                         note="seeded the kernel agent set; the brainstem hot-loads them.")

    # ── plant: a full front-door grail locally (bootstrap a door) ──
    def _plant(self, kwargs, ctx):
        owner = (kwargs.get("owner") or ctx.get("handle") or "").strip()
        slug = (kwargs.get("slug") or "").strip()
        kind = (kwargs.get("kind") or "operator").strip()
        display = kwargs.get("display_name") or slug
        if not owner or not slug:
            return self._env("plant", "error", error="pass owner=<login> and slug=<door name>.")
        if not _HANDLE_RE.match(owner) or not _SLUG_RE.match(slug):
            return self._env("plant", "error", error="owner/slug have an unsafe shape.")
        out = kwargs.get("path") or os.path.join(ctx["home"], ".brainstem", "doors", slug)
        rappid = mint_rappid(owner, slug)
        parent = _read_json(os.path.join(ctx["home"], ".brainstem", "rappid.json")) or {}
        parent_rappid = parent.get("rappid") or SPECIES_ROOT_RAPPID
        raw = f"{_RAW}/{owner}/{slug}/main"
        written = []

        def W(rel, content):
            p = os.path.join(out, rel)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, "w") as f:
                f.write(content)
            written.append(rel)

        # the canonical front-door grail set (mirror of tools/front_door_grail.py)
        _write_json(os.path.join(out, "rappid.json"), {
            "schema": "rapp/1", "rappid": rappid, "kind": kind, "name": slug,
            "display_name": display, "host": "github.com", "owner": owner, "repo": slug,
            "github": f"https://github.com/{owner}/{slug}", "url": f"https://{owner}.github.io/{slug}/",
            "parent_rappid": parent_rappid, "parent_repo": f"https://github.com/{RAPP_SPECIES}",
            "planted_by": owner, "minted_at": _now(),
            "notes": "Eternity format (Art. XXXIV.1); 64hex = sha256 of '%s/%s'." % (owner, slug)})
        written.append("rappid.json")
        W("soul.md", f"# {display}\n\nI am **{display}**. When I greet someone, I "
                     f"introduce myself by name — never as 'RAPP', 'an AI assistant', or 'the "
                     f"brainstem' (those are scaffolding, not me). Edit this file to change how "
                     f"I speak; it travels with the door.\n")
        for d in ("agents", "rar"):
            keep = os.path.join(out, d, ".gitkeep")
            os.makedirs(os.path.dirname(keep), exist_ok=True)
            open(keep, "w").close()
        # init local memory tier
        _write_json(os.path.join(out, ".brainstem_data", "memory.json"),
                    {"schema": "rapp-memory/1.0", "tier": "local", "entries": {}})
        written.append(".brainstem_data/memory.json")
        W("index.html", f"<!doctype html>\n<html><head><meta charset=utf-8>"
                        f"<title>{display}</title></head><body>"
                        f"<h1>{display}</h1><p><code>{rappid}</code></p>"
                        f"<p>A RAPP door. Identity: <a href=rappid.json>rappid.json</a>.</p>"
                        f"</body></html>\n")
        W("README.md", f"# {display}\n\nA RAPP door (kind `{kind}`).\n\n"
                       f"- Identity: `{rappid}`\n- Front: {raw}/rappid.json\n\n"
                       f"Planted by `rapp_agent.py action=plant` (Art. XXXIV.1 Eternity rappid).\n")
        W(".nojekyll", "")
        _write_json(os.path.join(out, "rar", "index.json"), {
            "schema": "rapp-rar-index/1.1", "rar_for": f"{owner}/{slug}", "kind": kind,
            "updated_at": _now(), "raw_url_prefix": raw, "agents": [], "organs": [],
            "senses": [], "rapps": []})
        written.append("rar/index.json")
        # the spine: planting a door is a birth event
        self._bond_record(ctx, {"kind": "birth", "rappid": rappid,
                                 "context": f"planted {kind} door {owner}/{slug} at {out}"})
        return self._env("plant", "success", rappid=rappid, kind=kind, out_dir=out,
                         files_written=len(written), files=written,
                         next=("push this dir to github.com/%s/%s to go live; the 9 URLs are "
                               "string-derived from the rappid. `action=door rappid=%s` shows them." %
                               (owner, slug, rappid)))

    # ── memory: the LOCAL tier (.brainstem_data/memory.json) + route the rest ──
    def _memory_path(self, ctx):
        return os.path.join(ctx["home"], ".brainstem_data", "memory.json")

    def _memory(self, kwargs, ctx):
        op = (kwargs.get("op") or "read").lower()
        path = self._memory_path(ctx)
        store = _read_json(path) or {"schema": "rapp-memory/1.0", "tier": "local", "entries": {}}
        tiers = {"local": ".brainstem_data/memory.json (this — fast, on-device)",
                 "public": "<door>/memory.json (shared bones, in the grail repo)",
                 "private": "operator's private Issues (PII-bearing substance, on-device auth)"}
        if op == "save":
            key, value = kwargs.get("key"), kwargs.get("value")
            if not key:
                return self._env("memory", "error", error="pass key=… value=… to save.")
            store.setdefault("entries", {})[key] = {"value": value, "at": _now()}
            _write_json(path, store)
            return self._env("memory", "success", op="save", key=key, tier="local",
                             count=len(store["entries"]), tiers=tiers)
        if op == "read":
            key = kwargs.get("key")
            if key:
                ent = store.get("entries", {}).get(key)
                return self._env("memory", "success" if ent else "empty", op="read",
                                 key=key, entry=ent, tier="local", tiers=tiers)
            return self._env("memory", "success", op="read", tier="local",
                             count=len(store.get("entries", {})),
                             keys=sorted(store.get("entries", {}).keys()), tiers=tiers)
        if op == "recall":
            q = (kwargs.get("query") or "").strip().lower()
            if not q:
                return self._env("memory", "error", error="pass query=… to recall.")
            hits = {k: v for k, v in store.get("entries", {}).items()
                    if q in (k + " " + json.dumps(v.get("value"))).lower()}
            return self._env("memory", "success", op="recall", query=q, tier="local",
                             matches=len(hits), entries=hits, tiers=tiers,
                             note=("local tier only. For semantic recall across the deeper "
                                   "tiers + the compression tree, `action=install "
                                   "name=manage_memory_agent.py`."))
        return self._env("memory", "error", error="op must be save | read | recall", tiers=tiers)

    # ── bond: the append-only lineage ledger (~/.brainstem/bonds.json) ──
    def _bonds_path(self, ctx):
        return os.path.join(ctx["home"], ".brainstem", "bonds.json")

    def _bond_record(self, ctx, ev):
        """Append one event to the spine. Used by mint/plant/hatch/launch too."""
        path = self._bonds_path(ctx)
        ledger = _read_json(path) or {"schema": "rapp-bonds/1.0", "events": []}
        entry = {"kind": ev.get("kind") or ev.get("event") or "rhythm",
                 "rappid": ev.get("rappid") or ctx.get("rappid"),
                 "ts": _now()}
        if ev.get("context"):
            entry["context"] = ev["context"]
        if ev.get("egg_sha256"):
            entry["egg_sha256"] = ev["egg_sha256"]
        ledger.setdefault("events", []).append(entry)
        _write_json(path, ledger)
        return entry

    def _bond(self, kwargs, ctx):
        op = (kwargs.get("op") or "list").lower()
        valid = {"birth", "bond", "adoption", "hatch", "graft", "launch", "rhythm", "join"}
        if op == "record":
            ev = (kwargs.get("event") or "").strip().lower()
            if not ev:
                return self._env("bond", "error",
                                 error="pass event=<kind> (birth|bond|hatch|graft|launch|adoption|rhythm).",
                                 valid_kinds=sorted(valid))
            if ev not in valid:
                return self._env("bond", "error", error=f"unknown event kind {ev!r}",
                                 valid_kinds=sorted(valid))
            entry = self._bond_record(ctx, {"kind": ev, "rappid": kwargs.get("rappid"),
                                            "context": kwargs.get("context"),
                                            "egg_sha256": kwargs.get("egg_sha256")})
            ledger = _read_json(self._bonds_path(ctx)) or {"events": []}
            return self._env("bond", "success", op="record", recorded=entry,
                             total=len(ledger.get("events", [])))
        # list
        ledger = _read_json(self._bonds_path(ctx)) or {"schema": "rapp-bonds/1.0", "events": []}
        return self._env("bond", "success", op="list", schema=ledger.get("schema"),
                         events=ledger.get("events", []), count=len(ledger.get("events", [])),
                         note="append-only lineage spine — every birth/bond/hatch/graft/launch/rhythm.")

    # ── lineage: walk parent_rappid back to the species root (forward = forks) ──
    def _lineage(self, kwargs, ctx):
        rec = _read_json(os.path.join(ctx["home"], ".brainstem", "rappid.json")) or {}
        chain = []
        seen = set()
        cur = rec.get("rappid")
        if not cur or cur == "rappid:unregistered":
            return self._env("lineage", "empty",
                             note="no minted rappid yet — `action=mint owner=… slug=…` first.")
        # always record self
        chain.append({"rappid": cur, "from": "local rappid.json",
                      "parent_rappid": rec.get("parent_rappid")})
        parent = rec.get("parent_rappid")
        offline_walk = False
        for _ in range(12):   # bound the walk
            if not parent or parent in seen:
                break
            seen.add(parent)
            d = door_from_rappid(parent)
            if not d:
                chain.append({"rappid": parent, "from": "non-locatable (species root or v3)"})
                break
            text = _fetch(d["urls"]["identity"]) if not ctx["offline"] else None
            if text is None:
                chain.append({"rappid": parent, "owner": d["owner"], "slug": d["slug"],
                              "from": "unresolved (offline or 404)"})
                offline_walk = True
                break
            try:
                prec = json.loads(text)
            except ValueError:
                break
            chain.append({"rappid": parent, "owner": d["owner"], "slug": d["slug"],
                          "from": "fetched rappid.json", "parent_rappid": prec.get("parent_rappid")})
            parent = prec.get("parent_rappid")
        # forward: GitHub forks of this door (online only)
        forks = None
        if not ctx["offline"] and rec.get("owner") and rec.get("repo"):
            text = _fetch(f"https://api.github.com/repos/{rec['owner']}/{rec['repo']}/forks?per_page=20")
            if text:
                try:
                    forks = [f.get("full_name") for f in json.loads(text)]
                except (ValueError, AttributeError):
                    forks = None
        return self._env("lineage", "success", root=RAPP_SPECIES, chain=chain,
                         depth=len(chain), offline_partial=offline_walk, forks=forks,
                         note=("walked parent_rappid toward the species root. "
                               + ("offline — read the local link only; re-run online to "
                                  "resolve the full spine + forks." if (offline_walk or ctx["offline"])
                                  else "full spine resolved.")))

    # ── beacon: write the estate beacon + .well-known/rapp-network.json ──
    def _beacon(self, kwargs, ctx):
        rec = _read_json(os.path.join(ctx["home"], ".brainstem", "rappid.json")) or {}
        rappid = rec.get("rappid") or ctx["rappid"]
        if not rappid or rappid == "rappid:unregistered":
            return self._env("beacon", "error",
                             error="no minted rappid — `action=mint owner=… slug=…` first.")
        estate_url = kwargs.get("estate_url") or (
            f"https://github.com/{ctx['handle']}/rapp-estate" if ctx.get("handle") else None)
        # Article XLVIII: private estate pointer + commitment are REQUIRED.
        ptr = kwargs.get("private_estate_pointer") or (
            f"https://github.com/{ctx['handle']}/rapp-estate-private" if ctx.get("handle") else None)
        commitment = _read_text_file(os.path.join(ctx["home"], ".brainstem", "private-estate-commitment"))
        commitment = commitment.strip() if commitment else None
        lm = _read_json(os.path.join(ctx["home"], ".brainstem", "private-estate-map.json")) or {}
        door_count = lm.get("private_door_count", 0)
        beacon = {"schema": "rapp-network-beacon/1.1", "operator_rappid": rappid,
                  "estate_url": estate_url,
                  "discovery": {"indexable": bool(kwargs.get("indexable", True)),
                                "federation_hints": [estate_url] if estate_url else []},
                  "private_estate_pointer": ptr,
                  "private_estate_commitment": commitment,
                  "private_door_count": door_count,
                  "written_at": _now(),
                  "note": ("Article XLVIII: every operator has BOTH a public + a private estate. The pointer "
                           "+ commitment prove the private tier without revealing it; the HMAC secret never "
                           "leaves the box. Run action=estate op=private-init first to fill the commitment.")}
        path = os.path.join(ctx["home"], ".brainstem", ".well-known", "rapp-network.json")
        _write_json(path, beacon)
        compliant = bool(ptr and commitment)
        return self._env("beacon", "success" if compliant else "incomplete",
                         path=path, schema="rapp-network-beacon/1.1", operator_rappid=rappid,
                         estate_url=estate_url, private_estate_pointer=ptr,
                         private_estate_commitment=commitment, private_door_count=door_count,
                         compliant=compliant,
                         note=("Article-XLVIII-compliant beacon written; peers discover you by walking this file."
                               if compliant else "beacon written but NOT yet compliant — run "
                               "action=estate op=private-init confirm=true to mint the private estate + commitment."))

    # ── estate op=private-init: the Article XLVIII two-tier private estate ──
    # Mints the per-operator HMAC secret (~/.brainstem/private-estate-secret, 0600,
    # mint-once, NEVER surfaced), scaffolds the opaque file set, and computes the
    # canonical rapp-private-estate-commitment/1.0 (recomputable by any peer with
    # read access). Dry-run by default; confirm=true creates the PRIVATE repo.
    def _estate_private(self, kwargs, ctx, verify_only=False):
        import secrets
        home = ctx["home"]
        handle = ctx.get("handle") or kwargs.get("owner")
        if not handle:
            return self._env("estate", "error", error="need a github handle — sign into gh or pass owner=….")
        slug = f"{handle}/rapp-estate-private"
        secret_path = os.path.join(home, ".brainstem", "private-estate-secret")
        try:
            have = os.path.exists(secret_path) and os.path.getsize(secret_path) >= 16
        except OSError:
            have = False
        if not have and not verify_only:
            os.makedirs(os.path.dirname(secret_path), exist_ok=True)
            with open(secret_path, "wb") as f:
                f.write(secrets.token_bytes(32))
            try: os.chmod(secret_path, 0o600)
            except OSError: pass
        secret_present = os.path.exists(secret_path)
        operator_rappid = ctx.get("rappid") or ""
        meta = {"schema": "rapp-private-estate/1.0", "owner": operator_rappid, "github_handle": handle,
                "private_door_count": 0, "kinds": {}, "objects_count": 0, "kinds_count": 0,
                "note": ("Opaque private estate (Article XLVIII). Substance lives here; discovery is public at "
                         + handle + "/rapp-estate. The human-readable kind/id map lives ONLY locally at "
                         "~/.brainstem/private-estate-map.json.")}
        meta_bytes = (json.dumps(meta, indent=2) + "\n").encode("utf-8")
        readme = ("# " + slug + "\n\nThe PRIVATE tier of this operator's RAPP estate (Article XLVIII). Holds the "
                  "substance — PII, contacts, history — never publicly indexable. Discovery is public at "
                  + handle + "/rapp-estate. Paths are HMAC-opaque; without the operator's local secret the "
                  "structure is uniformly meaningless.\n").encode("utf-8")
        files = {"meta.json": meta_bytes, "README.md": readme, "objects/.gitkeep": b"", "kinds/.gitkeep": b""}
        h = hashlib.sha256(); h.update(b"rapp-private-estate-commitment/1.0\n"); h.update(meta_bytes)
        h.update(b"\n--paths--\n")
        for pth in sorted(files.keys()):
            h.update(pth.encode("utf-8") + b"\n")
        commitment = h.hexdigest()
        if verify_only:
            return self._env("estate", "success", op="verify", repo=slug, commitment=commitment,
                             secret_present=secret_present,
                             note="recomputed the commitment a peer would derive from the repo tree + meta.json.")
        # persist the commitment + local map so action=beacon can publish it
        open(os.path.join(home, ".brainstem", "private-estate-commitment"), "w").write(commitment)
        lm_path = os.path.join(home, ".brainstem", "private-estate-map.json")
        if not os.path.exists(lm_path):
            _write_json(lm_path, {"schema": "rapp-private-estate-localmap/1.0", "github_handle": handle,
                                  "kinds": [], "private_door_count": 0})
            try: os.chmod(lm_path, 0o600)
            except OSError: pass
        out = os.path.join(home, ".brainstem", "plant", "rapp-estate-private")
        for rel, content in files.items():
            fp = os.path.join(out, rel); os.makedirs(os.path.dirname(fp), exist_ok=True)
            open(fp, "wb").write(content)
        res = {"repo": slug, "private": True, "commitment": commitment, "secret_present": secret_present,
               "operator_rappid": operator_rappid, "local_dir": out, "scaffolded": sorted(files.keys())}
        if not kwargs.get("confirm"):
            return self._env("estate", "scaffolded", op="private-init", **res,
                             note=("dry run — minted the local HMAC secret (0600) + computed the commitment. "
                                   "Re-run with confirm=true to create the PRIVATE repo " + slug + " and push; "
                                   "then action=beacon to publish the commitment."))
        rc, _, _ = _run(["gh", "repo", "view", slug])
        if rc != 0:
            rc2, _, err2 = _run(["gh", "repo", "create", slug, "--private", "--description",
                                 handle + "'s RAPP private estate (Article XLVIII)"])
            if rc2 != 0:
                return self._env("estate", "error", error="gh repo create failed: " + err2[:200], **res)
        wrote = []
        for rel, content in files.items():
            b64 = base64.b64encode(content).decode("ascii")
            rcp, _, ep = _run(["gh", "api", "-X", "PUT", "/repos/" + slug + "/contents/" + rel,
                               "-f", "message=private estate init", "-f", "content=" + b64])
            wrote.append(rel if rcp == 0 else rel + "!" + ep[:50])
        return self._env("estate", "success", op="private-init", url="https://github.com/" + slug,
                         wrote=wrote, **res,
                         note="private estate created. Run action=beacon to publish the commitment in your network beacon.")

    # ── sniff: BFS federation discovery from a seed's network beacon ──
    def _sniff(self, kwargs, ctx):
        seed = (kwargs.get("seed") or kwargs.get("path") or "").strip()
        if not seed:
            # default to the local beacon
            local = os.path.join(ctx["home"], ".brainstem", ".well-known", "rapp-network.json")
            b = _read_json(local)
            if b:
                return self._env("sniff", "success", source="local beacon", seed=local,
                                 nodes=[{"rappid": b.get("operator_rappid"),
                                         "estate_url": b.get("estate_url")}],
                                 hints=b.get("federation_hints", []),
                                 note="no seed= given — read your own beacon. Pass seed=<url> to walk the network.")
            return self._env("sniff", "error",
                             error="pass seed=<url serving .well-known/rapp-network.json> (or write a beacon first).")
        if ctx["offline"]:
            return self._env("sniff", "needs_network", seed=seed,
                             note="offline — federation discovery walks live URLs. When online, this "
                                  "BFS's the seed's federation_hints[] (raw/LAN/file://).")
        visited, queue, nodes, depth = set(), [seed], [], 0
        while queue and depth < 24:
            url = queue.pop(0)
            if url in visited:
                continue
            visited.add(url)
            depth += 1
            # normalize: a node URL → its rapp-network.json
            fetch_url = url
            if not url.endswith(".json"):
                fetch_url = url.rstrip("/") + "/.well-known/rapp-network.json"
            text = _fetch(fetch_url) if not fetch_url.startswith("file://") else None
            if text is None and fetch_url.startswith("file://"):
                text = _read_text_file(fetch_url[len("file://"):])
            if text is None:
                nodes.append({"url": url, "reachable": False})
                continue
            try:
                doc = json.loads(text)
            except ValueError:
                nodes.append({"url": url, "reachable": False, "note": "not json"})
                continue
            nodes.append({"url": fetch_url, "reachable": True,
                          "operator_rappid": doc.get("operator_rappid"),
                          "estate_url": doc.get("estate_url")})
            for hint in (doc.get("federation_hints") or []):
                if hint and hint not in visited:
                    queue.append(hint)
        reached = [n for n in nodes if n.get("reachable")]
        if not reached:
            # every fetch failed → we're effectively in the woods
            return self._env("sniff", "needs_network", seed=seed, nodes=nodes,
                             note="offline — couldn't reach the seed or any federation hint. When "
                                  "online, this BFS's the seed's federation_hints[] (raw/LAN/file://).")
        return self._env("sniff", "success", seed=seed, nodes=nodes,
                         discovered=len(reached),
                         note="walked the federation graph (BFS over federation_hints[]).")

    # ── mmr: the operator/door standing + tier (front-door computeMMR heuristic) ──
    def _mmr(self, kwargs, ctx):
        rec = _read_json(os.path.join(ctx["home"], ".brainstem", "rappid.json")) or {}
        mem = _read_json(self._memory_path(ctx)) or {}
        ledger = _read_json(self._bonds_path(ctx)) or {}
        est = _read_json(os.path.join(ctx["home"], ".brainstem", "estate.json")) or {}
        cubbies = [d for d in (os.listdir(ctx["cubby_root_local"])
                   if os.path.isdir(ctx["cubby_root_local"]) else []) if not d.startswith(".")]
        # the heuristic (ported from the front-door computeMMR): identity is the
        # floor, then memory depth + lineage events + estate breadth + cubbies.
        has_id = bool(rec.get("rappid") and rec.get("rappid") != "rappid:unregistered")
        n_mem = len(mem.get("entries", {}))
        n_events = len(ledger.get("events", []))
        n_doors = len(est.get("created", [])) + len(est.get("member", []))
        n_cubbies = len(cubbies)
        score = (200 if has_id else 0) + min(n_mem, 100) * 4 + min(n_events, 50) * 8 \
            + min(n_doors, 50) * 12 + min(n_cubbies, 50) * 10
        if not has_id:
            tier = "unbonded"
        elif score >= 1200:
            tier = "metropolis"
        elif score >= 700:
            tier = "estate"
        elif score >= 350:
            tier = "settled"
        else:
            tier = "seedling"
        return self._env("mmr", "success", rappid=rec.get("rappid") or ctx["rappid"],
                         score=score, tier=tier,
                         factors={"has_identity": has_id, "memory_entries": n_mem,
                                  "lineage_events": n_events, "estate_doors": n_doors,
                                  "local_cubbies": n_cubbies},
                         note="standing = identity floor + memory depth + lineage + estate breadth + cubbies.")

    # ── verify: exact immutable RAPP/1 authority bytes ───────────────────
    def _verify(self, kwargs, ctx):
        enum = list(self.metadata["parameters"]["properties"]["action"]["enum"])
        raw, http_status = _fetch_bytes_status(RAPP1_SPEC_URL)
        if raw is None:
            return self._env(
                "verify",
                "offline" if http_status is None else "unavailable",
                action_enum=sorted(enum),
                authority_url=RAPP1_SPEC_URL,
                authority_http_status=http_status,
                mirror_contract="retired",
                active_byte_identical_mirrors=[],
                drift=True,
                note=(
                    "exact RAPP/1 authority bytes could not be fetched; "
                    "no mirror response was accepted as authority"
                ),
            )
        actual_sha256 = hashlib.sha256(raw).hexdigest()
        exact = (
            http_status == 200
            and len(raw) == RAPP1_SPEC_BYTES
            and actual_sha256 == RAPP1_SPEC_SHA256
        )
        return self._env(
            "verify",
            "success" if exact else "drift",
            action_enum=sorted(enum),
            authority_url=RAPP1_SPEC_URL,
            authority_commit=RAPP1_SPEC_COMMIT,
            authority_expected_bytes=RAPP1_SPEC_BYTES,
            authority_actual_bytes=len(raw),
            authority_expected_sha256=RAPP1_SPEC_SHA256,
            authority_actual_sha256=actual_sha256,
            authority_exact=exact,
            mirror_contract="retired",
            active_byte_identical_mirrors=[],
            drift=not exact,
            note=(
                "exact immutable RAPP/1 authority verified"
                if exact
                else "RAPP/1 authority bytes differ from the pinned contract"
            ),
        )

    # ── on-device cubby ops ──
    def _cubby(self, action, kwargs, ctx):
        root = ctx["cubby_root_local"]
        if action == "cubby_new":
            slug = (kwargs.get("slug") or kwargs.get("cubby") or "").strip()
            if not _SLUG_RE.match(slug):
                return self._env(action, "error", error="pass slug=<name>")
            cubby = os.path.join(root, slug)
            existed = os.path.isfile(os.path.join(cubby, "cubby.json"))
            for d in CUBBY_ANATOMY:
                os.makedirs(os.path.join(cubby, d), exist_ok=True)
                gk = os.path.join(cubby, d, ".gitkeep")
                if not os.path.exists(gk):
                    open(gk, "w").close()
            if not existed:
                _write_json(os.path.join(cubby, "cubby.json"), {
                    "schema": CUBBY_SCHEMA, "github_login": ctx["handle"], "slug": slug,
                    "display_name": slug, "what_im_cooking": kwargs.get("what", ""),
                    "created_at": _now(), "estate": {"anatomy": list(CUBBY_ANATOMY)},
                    "streamable": {"agents": True}})
            return self._env(action, "already_exists" if existed else "success",
                             cubby=slug, path=cubby)
        if action == "cubby_list":
            out = []
            if os.path.isdir(root):
                for slug in sorted(os.listdir(root)):
                    if slug.startswith("."):
                        continue
                    cj = _read_json(os.path.join(root, slug, "cubby.json"))
                    if cj is None and not os.path.isdir(os.path.join(root, slug)):
                        continue
                    counts = {k: len([p for p in glob.glob(os.path.join(root, slug, sub, pat))
                                      if not os.path.basename(p).startswith(".")])
                              for k, (sub, pat) in SUPER_RAR_KINDS.items()}
                    out.append({"cubby": slug, "what_im_cooking": (cj or {}).get("what_im_cooking", ""),
                                "counts": {k: v for k, v in counts.items() if v}})
            return self._env(action, "success", root=root, cubbies=out, count=len(out))
        if action == "cubby_show":
            slug = (kwargs.get("cubby") or "").strip()
            if not _SLUG_RE.match(slug) or not os.path.isdir(os.path.join(root, slug)):
                return self._env(action, "error", error=f"no local cubby '{slug}'")
            mine = [e for e in _build_super_rar(root) if e["cubby"] == slug]
            return self._env(action, "success", cubby=slug,
                             meta=_read_json(os.path.join(root, slug, "cubby.json")),
                             inventory=mine, count=len(mine))
        if action == "super_rar":   # where=local — your WHOLE local estate
            q = (kwargs.get("query") or "").strip().lower()
            source = (kwargs.get("source") or "all").lower()  # cubbies|brainstem|all
            bs = kwargs.get("_brainstem_dir") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            cands = self._local_candidates(root, bs, source)
            hits = [c for c in cands
                    if _q_match(q, {k: c.get(k) for k in ("kind", "name", "path", "cubby")}, c["abs"])] \
                if q else cands
            view = [{k: c[k] for k in ("kind", "name", "cubby", "path") if k in c} for c in hits]
            return self._env(action, "success", where="local", source=source, query=q or None,
                             matches=len(hits), total=len(cands),
                             by_kind={k: sum(1 for c in cands if c["kind"] == k)
                                      for k in {x["kind"] for x in cands}},
                             results=view[:50])
        if action == "cubby_egg":
            slug = (kwargs.get("cubby") or "").strip()
            cubby = os.path.join(root, slug)
            if not _SLUG_RE.match(slug) or not os.path.isdir(cubby):
                return self._env(action, "error", error=f"no local cubby '{slug}'")
            buf = io.BytesIO()
            files = 0
            with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
                z.writestr("manifest.json", json.dumps({
                    "schema": CUBBY_EGG_SCHEMA, "type": "cubby", "version": "1.0",
                    "slug": slug, "cubby_schema": CUBBY_SCHEMA, "minted_at": _now(),
                    "anatomy": list(CUBBY_ANATOMY),
                    "organism": ("A digital organism carved from a rapp estate — a "
                                 "coherent slice (its own anatomy) that lives on in its "
                                 "own cubby, hatchable anywhere (Article XXXVII).")}, indent=2))
                z.writestr("HATCH.md", f"# Cubby egg: {slug}\nHatch local with "
                           "`cubby_import path=<egg>`, or land it in a neighborhood "
                           "cubby with `hatch path=<egg>`.\n")
                for dp, _d, fns in os.walk(cubby):
                    for fn in fns:
                        ap = os.path.join(dp, fn)
                        z.writestr("cubby/" + os.path.relpath(ap, cubby), open(ap, "rb").read())
                        files += 1
            blob = buf.getvalue()
            out = kwargs.get("path") or os.path.join(ctx["home"], ".brainstem", "eggs", f"cubby-{slug}.egg")
            os.makedirs(os.path.dirname(out), exist_ok=True)
            open(out, "wb").write(blob)
            return self._env(action, "success", cubby=slug, egg=out, files=files,
                             sha256=hashlib.sha256(blob).hexdigest(), size_bytes=len(blob))
        if action == "cubby_import":
            return self._hatch_egg(kwargs.get("path"), os.path.join(root, "{slug}"),
                                   action, ctx, local=True)
        if action == "cubby_collect":
            return self._collect(kwargs, ctx, root)
        return self._env(action, "error", error="unknown cubby op")

    def _local_candidates(self, root, bs, source):
        """Your whole local estate as candidates (abs paths): organized cubbies
        + the live brainstem (agents/organs/senses/rapps/neighborhoods/eggs)."""
        cands = []
        if source in ("cubbies", "all"):
            for e in _build_super_rar(root):
                cands.append({**e, "abs": os.path.join(root, e["path"])})
        if source in ("brainstem", "all"):
            for kind, (sub, pat) in SUPER_RAR_KINDS.items():
                for p in sorted(glob.glob(os.path.join(bs, sub, pat))):
                    nm = os.path.basename(p)
                    if nm.startswith(".") or not os.path.isfile(p):
                        continue
                    cands.append({"kind": kind, "name": nm, "cubby": "(brainstem)",
                                  "path": os.path.relpath(p, bs), "abs": p})
        return cands

    def _collect(self, kwargs, ctx, root):
        """Assemble a new local cubby from a super-RAR search across everything
        on-device. The natural-language move: 'put the X for this project in its
        own cubby' → search local stack for X, copy the matches into a fresh
        cubby (ready to egg + mirror to a neighborhood)."""
        slug = (kwargs.get("slug") or kwargs.get("cubby") or "").strip()
        q = (kwargs.get("query") or "").strip().lower()
        if not _SLUG_RE.match(slug):
            return self._env("cubby_collect", "error", error="pass slug=<new cubby name>")
        if not q:
            return self._env("cubby_collect", "error", error="pass query=<what to collect>")
        source = (kwargs.get("source") or "all").lower()   # cubbies | brainstem | all
        bs = kwargs.get("_brainstem_dir") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # gather candidates across the whole local estate; don't recollect target
        candidates = [c for c in self._local_candidates(root, bs, source) if c.get("cubby") != slug]
        # filter by the query — search on ANYTHING (metadata + file content)
        matched, skipped = [], []
        for c in candidates:
            meta = {k: c.get(k) for k in ("kind", "name", "path", "cubby")}
            if not _q_match(q, meta, c["abs"]):
                continue
            if _SECRET_NAME_RE.search(c["name"]):
                skipped.append({"name": c["name"], "why": "secret-shaped"}); continue
            matched.append(c)
        if not matched:
            return self._env("cubby_collect", "empty", query=q,
                             searched=len(candidates),
                             note="nothing matched — try `super_rar where=local query=…` to see what exists.")
        # create the cubby + copy the matches in (dedupe by name within a kind)
        cubby = os.path.join(root, slug)
        for d in CUBBY_ANATOMY:
            os.makedirs(os.path.join(cubby, d), exist_ok=True)
        if not os.path.isfile(os.path.join(cubby, "cubby.json")):
            _write_json(os.path.join(cubby, "cubby.json"), {
                "schema": CUBBY_SCHEMA, "github_login": ctx["handle"], "slug": slug,
                "display_name": slug, "what_im_cooking": kwargs.get("what", f"collected: {q}"),
                "created_at": _now(), "estate": {"anatomy": list(CUBBY_ANATOMY)},
                "streamable": {"agents": True},
                "collected_from": {"query": q, "source": source, "at": _now()}})
        kind_dir = {"agent": "agents", "organ": "organs", "sense": "senses",
                    "rapplication": "rapplications", "neighborhood": "neighborhoods", "egg": "eggs"}
        collected = []
        for c in matched:
            sub = kind_dir.get(c["kind"], "agents")
            dst = os.path.join(cubby, sub, c["name"])
            if os.path.exists(dst):
                continue
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(c["abs"], dst)
            collected.append({"kind": c["kind"], "name": c["name"],
                              "from": c["cubby"], "into": f"cubbies/{slug}/{sub}/{c['name']}"})
        return self._env("cubby_collect", "success", cubby=slug, query=q,
                         collected=collected, count=len(collected),
                         skipped_secrets=skipped,
                         is_organism=True,
                         note=("you just carved a digital organism out of your estate — a "
                               "coherent slice that now lives in its own cubby and can be "
                               "egged + hatched anywhere."),
                         next=("now: `cubby_egg cubby=%s` to pack the organism, then `hatch "
                               "path=<egg>` (after `mount`) to mirror it into your "
                               "neighborhood cubby." % slug))

    # ══════════════════════════════════════════════════════════════════════
    # FORK A NAMED OWNED CUBBY (fractal) + POP A TWIN CHAT FROM ITS AGENTS.
    # A new neighborhood cubby is fractal: it lives INSIDE the owner's cubby at
    # cubbies/<me>/cubbies/<slug>/ — so the repo's cubby-guard (which scopes a
    # member's writes to cubbies/<me>/) passes and ownership is unambiguous. The
    # operator can also pop a twin: a child brainstem booted from JUST a cubby's
    # agents, used INSTEAD of the global brainstem.
    # ══════════════════════════════════════════════════════════════════════
    def _make_sub_cubby(self, cubby_dir, owner, slug, what, forked_from=None):
        """Create the anatomy + cubby.json for an owned (sub-)cubby. Ownership:
        github_login stays the OWNER; a neighborhood sub-cubby is fractal."""
        for d in CUBBY_ANATOMY:
            os.makedirs(os.path.join(cubby_dir, d), exist_ok=True)
            gk = os.path.join(cubby_dir, d, ".gitkeep")
            if not os.path.exists(gk):
                open(gk, "w").close()
        is_sub = bool(forked_from is not None or owner not in (None, "local"))
        meta = {"schema": CUBBY_SCHEMA, "github_login": owner or "local", "slug": slug,
                "parent_cubby": owner if (forked_from is not None and owner != "local") else None,
                "is_sub_cubby": bool(forked_from is not None and owner != "local"),
                "display_name": slug, "what_im_cooking": what or "",
                "created_at": _now(), "estate": {"anatomy": list(CUBBY_ANATOMY)},
                "streamable": {"agents": True}}
        if forked_from is not None:
            meta["forked_from"] = forked_from
        _write_json(os.path.join(cubby_dir, "cubby.json"), meta)
        return meta

    _KIND_DIR = {"agent": "agents", "organ": "organs", "sense": "senses",
                 "rapplication": "rapplications", "neighborhood": "neighborhoods", "egg": "eggs"}

    def _content_set(self, kwargs, ctx, bs, root):
        """Resolve the fork/twin content set → list of {kind, name, abs}. Secret
        files are refused. Sources: non-kernel-agents · brainstem · a search ·
        a local cubby (cubby:<slug>) · explicit path/paths."""
        frm = (kwargs.get("from") or "").strip().lower()
        items, skipped = [], []

        def add(kind, abs_path):
            nm = os.path.basename(abs_path)
            if nm.startswith(".") or not os.path.isfile(abs_path):
                return
            if _SECRET_NAME_RE.search(nm):
                skipped.append({"name": nm, "why": "secret-shaped"}); return
            items.append({"kind": kind, "name": nm, "abs": abs_path})

        explicit = list(kwargs.get("paths") or [])
        if kwargs.get("path"):
            explicit.append(kwargs.get("path"))
        if explicit:
            for p in explicit:
                if os.path.isfile(p):
                    kind = ("organ" if p.endswith("_organ.py") else "egg" if p.endswith(".egg")
                            else "agent")
                    add(kind, p)
        elif kwargs.get("query"):
            q = (kwargs.get("query") or "").strip().lower()
            source = (kwargs.get("source") or "all").lower()
            for c in self._local_candidates(root, bs, source):
                meta = {k: c.get(k) for k in ("kind", "name", "path", "cubby")}
                if _q_match(q, meta, c["abs"]):
                    add(c["kind"], c["abs"])
        elif frm.startswith("cubby:"):
            sub = _slugify(frm.split(":", 1)[1])
            base = os.path.join(root, sub)
            for kind, (d, pat) in SUPER_RAR_KINDS.items():
                for p in sorted(glob.glob(os.path.join(base, d, pat))):
                    add(kind, p)
        elif frm in ("brainstem",):
            agents = os.path.join(bs, "agents")
            for p in sorted(glob.glob(os.path.join(agents, "*_agent.py"))):
                add("agent", p)
        else:   # default: non-kernel-agents
            agents = os.path.join(bs, "agents")
            for p in sorted(glob.glob(os.path.join(agents, "*_agent.py"))):
                if os.path.basename(p) in KERNEL_AGENTS:
                    continue
                add("agent", p)
            for p in sorted(glob.glob(os.path.join(agents, "*_organ.py"))):
                add("organ", p)
        # dedupe by (kind, name)
        seen, deduped = set(), []
        for it in items:
            key = (it["kind"], it["name"])
            if key in seen:
                continue
            seen.add(key)
            deduped.append(it)
        return deduped, skipped

    def _pack_cubby_egg(self, cubby_dir, slug, owner):
        """Pack a cubby into a brainstem-egg/2.3-cubby self-backup zip (EXCLUDING
        its own eggs/ to avoid recursion). Returns (blob, manifest, file_count)."""
        buf = io.BytesIO()
        files, manifest_files = 0, []
        with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
            for dp, dirs, fns in os.walk(cubby_dir):
                rel_dir = os.path.relpath(dp, cubby_dir)
                if rel_dir == "eggs" or rel_dir.startswith("eggs" + os.sep):
                    continue   # don't pack the egg shelf into the egg (recursion)
                for fn in fns:
                    ap = os.path.join(dp, fn)
                    rel = os.path.relpath(ap, cubby_dir)
                    body = open(ap, "rb").read()
                    z.writestr("cubby/" + rel, body)
                    manifest_files.append({"path": rel,
                                           "sha256": hashlib.sha256(body).hexdigest()})
                    files += 1
            manifest = {"schema": CUBBY_EGG_SCHEMA, "type": "cubby", "version": "1.0",
                        "slug": slug, "owner": owner, "cubby_schema": CUBBY_SCHEMA,
                        "anatomy": list(CUBBY_ANATOMY), "files": manifest_files,
                        "packed_at": _now()}
            z.writestr("manifest.json", json.dumps(manifest, indent=2))
            z.writestr("HATCH.md", f"# Cubby egg: {slug}\nA self-backup of an owned "
                       "cubby. Hatch local with `cubby_import path=<egg>`, or land it "
                       "in a neighborhood cubby with `hatch path=<egg>`.\n")
        return buf.getvalue(), manifest, files

    def _cubby_fork(self, kwargs, ctx):
        """Egg-and-cubby a content set into a NEW owned cubby. Neighborhood forks
        are fractal (cubbies/<me>/cubbies/<slug>/ — inside the owner's path so the
        guard passes); local forks live at ~/.brainstem/cubbies/<slug>/."""
        slug = _slugify((kwargs.get("slug") or "").strip())
        if not (kwargs.get("slug") or "").strip() or not _SLUG_RE.match(slug):
            return self._env("cubby_fork", "error", error="pass slug=<new cubby name>")
        where = (kwargs.get("where") or "neighborhood").lower()
        root = ctx["cubby_root_local"]
        bs = self._bs_dir(kwargs)
        items, skipped = self._content_set(kwargs, ctx, bs, root)

        # resolve the target dir + ownership
        if where == "local":
            me = "local"
            cubby_dir = os.path.join(root, slug)
            cubby_label = cubby_dir
            forked_from = None
        else:
            mounted = ctx["repo_dir"] and os.path.isdir(ctx["repo_dir"]) and \
                os.path.exists(os.path.join(ctx["repo_dir"], "neighborhood.json"))
            if not mounted:
                return self._env("cubby_fork", "error",
                                 error="not mounted — mount + join the neighborhood first (or where=local).")
            me = ctx["handle"]
            if not me or not _HANDLE_RE.match(me):
                return self._env("cubby_fork", "error", error="run `gh auth login` (or pass _handle).")
            cubby_dir = os.path.join(ctx["repo_dir"], "cubbies", me, "cubbies", slug)
            cubby_label = f"cubbies/{me}/cubbies/{slug}/"
            forked_from = {"by": me, "from": (kwargs.get("from") or kwargs.get("query")
                                              or "non-kernel-agents"), "at": _now()}

        what = kwargs.get("what") or (
            "forked: " + (kwargs.get("from") or kwargs.get("query") or "non-kernel-agents"))
        if where == "local":
            self._make_sub_cubby(cubby_dir, "local", slug, what)
        else:
            self._make_sub_cubby(cubby_dir, me, slug, what, forked_from=forked_from)

        # copy the content into the right anatomy subdir (dedupe, secret-refused already)
        collected = []
        for it in items:
            sub = self._KIND_DIR.get(it["kind"], "agents")
            dst = os.path.join(cubby_dir, sub, it["name"])
            if os.path.exists(dst):
                continue
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(it["abs"], dst)
            collected.append({"kind": it["kind"], "name": it["name"],
                              "into": f"{sub}/{it['name']}"})

        # pack a self-backup egg into the new cubby's eggs/ (default true)
        egg_rel = None
        if kwargs.get("egg", True):
            blob, _mani, _fc = self._pack_cubby_egg(cubby_dir, slug, me)
            egg_path = os.path.join(cubby_dir, "eggs", f"{slug}.egg")
            os.makedirs(os.path.dirname(egg_path), exist_ok=True)
            open(egg_path, "wb").write(blob)
            egg_rel = os.path.relpath(egg_path, cubby_dir if where == "local" else ctx["repo_dir"])

        git = {}
        if where != "local":
            git = self._commit_push(ctx, f"cubby({me}): fork {slug} ({len(collected)} items)",
                                    kwargs.get("push", True))

        env = {"cubby": cubby_label, "owner": me, "where": where, "count": len(collected),
               "collected": collected, "skipped_secrets": skipped, "egg": egg_rel,
               "is_organism": True,
               "note": ("a named cubby you OWN — fractal, inside your cubby; the egg inside "
                        "it is a self-backup."),
               "next": f"`twin cubby={slug}` to pop a chat from just these agents."}
        env.update(git)

        # twin=true → also pop a twin from the fresh cubby and merge the result
        if kwargs.get("twin"):
            twin = json.loads(self._twin({"cubby": slug, "where": where,
                                          "name": kwargs.get("name") or f"twin-{slug}",
                                          "soul": kwargs.get("soul"),
                                          "_brainstem_dir": kwargs.get("_brainstem_dir"),
                                          "_repo_dir": kwargs.get("_repo_dir"),
                                          "_handle": kwargs.get("_handle"),
                                          "_home_dir": kwargs.get("_home_dir")}, ctx))
            env["twin"] = twin
            env["twin_url"] = twin.get("twin_url")
        return self._env("cubby_fork", "success", **env)

    def _twin(self, kwargs, ctx):
        """Pop a twin chat: build a workspace from a cubby's agents (+ the KERNEL
        agents so it boots), write a soul, boot a child brainstem on a free port,
        return its chat URL. Offline-safe — never crashes; if the brainstem source
        is missing it returns the workspace as 'degraded'."""
        bs = self._bs_dir(kwargs)
        root = ctx["cubby_root_local"]
        cubby = _slugify((kwargs.get("cubby") or "").strip()) if kwargs.get("cubby") else None
        where = (kwargs.get("where") or "").lower()
        name = _slugify(kwargs.get("name") or (f"twin-{cubby}" if cubby else "twin"))

        # resolve the agents source → a directory of *_agent.py
        agent_src = None
        if cubby:
            if where == "neighborhood" or (where != "local" and ctx.get("repo_dir") and ctx.get("handle")):
                me = ctx.get("handle")
                if me:
                    cand = os.path.join(ctx["repo_dir"], "cubbies", me, "cubbies", cubby, "agents")
                    if os.path.isdir(cand):
                        agent_src = cand
            if agent_src is None:
                cand = os.path.join(root, cubby, "agents")
                if os.path.isdir(cand):
                    agent_src = cand

        # assemble the agent file list (non-kernel from the cubby, or non-kernel-agents)
        agent_files = []   # (name, abs)
        if agent_src:
            for p in sorted(glob.glob(os.path.join(agent_src, "*_agent.py"))):
                nm = os.path.basename(p)
                if nm in KERNEL_AGENTS or _SECRET_NAME_RE.search(nm):
                    continue
                agent_files.append((nm, p))
        else:   # fall back to the live brainstem's non-kernel agents
            for p in sorted(glob.glob(os.path.join(bs, "agents", "*_agent.py"))):
                nm = os.path.basename(p)
                if nm in KERNEL_AGENTS or _SECRET_NAME_RE.search(nm):
                    continue
                agent_files.append((nm, p))

        # build the twin workspace ~/.brainstem/twins/<name>/
        workspace = os.path.join(ctx["home"], ".brainstem", "twins", name)
        ws_agents = os.path.join(workspace, "agents")
        os.makedirs(ws_agents, exist_ok=True)
        loaded = []
        for nm, p in agent_files:
            shutil.copy2(p, os.path.join(ws_agents, nm))
            loaded.append(nm)
        # ALSO copy the kernel agents from bs/agents/ so it boots as a real brainstem
        kernel_copied = []
        for kn in sorted(KERNEL_AGENTS):
            kp = os.path.join(bs, "agents", kn)
            if os.path.isfile(kp) and not os.path.exists(os.path.join(ws_agents, kn)):
                shutil.copy2(kp, os.path.join(ws_agents, kn))
                kernel_copied.append(kn)
        # write the soul
        soul = kwargs.get("soul") or (
            "You are a focused brainstem running a curated agent loadout: "
            + (", ".join(loaded) or "(none)") + ". Operate them through natural "
            "language. This is a twin the operator uses instead of the global brainstem.")
        soul_path = os.path.join(workspace, "soul.md")
        with open(soul_path, "w") as f:
            f.write(soul + "\n")

        # find start.sh; allocate a free port; boot a child brainstem (best-effort)
        start_sh = None
        for cand in (os.path.join(ctx["home"], ".brainstem", "src", "rapp_brainstem", "start.sh"),
                     os.path.join(os.path.dirname(bs), "start.sh"),
                     os.path.join(bs, "start.sh")):
            if os.path.isfile(cand):
                start_sh = cand
                break
        if not start_sh or kwargs.get("_no_boot"):
            return self._env("twin", "degraded", workspace=workspace,
                             agents_loaded=loaded, kernel_agents=kernel_copied,
                             soul=soul_path,
                             note=("workspace built; boot needs the brainstem source / a "
                                   "backend. Point a brainstem at AGENTS_PATH=%s to run this "
                                   "loadout." % ws_agents))
        port = self._free_port()
        src_dir = os.path.dirname(start_sh)
        # share the brainstem's Copilot session if present (best-effort)
        for tk in (".copilot_token", ".copilot_session"):
            sp, dp = os.path.join(src_dir, tk), None
            host_tk = os.path.join(bs, tk)
            if not os.path.isfile(sp) and os.path.isfile(host_tk):
                try:
                    shutil.copy2(host_tk, sp)
                except OSError:
                    pass
        env = {**os.environ, "SOUL_PATH": soul_path, "AGENTS_PATH": ws_agents,
               "PORT": str(port)}
        try:
            subprocess.Popen(["bash", start_sh], cwd=workspace, env=env,
                             start_new_session=True,
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except OSError as e:
            return self._env("twin", "degraded", workspace=workspace,
                             agents_loaded=loaded, kernel_agents=kernel_copied,
                             soul=soul_path,
                             note=f"workspace built; boot failed to launch ({e}).")
        twin_url = f"http://127.0.0.1:{port}/"
        self._twin_liveness(port)
        return self._env("twin", "success", twin_url=twin_url, workspace=workspace,
                         agents_loaded=loaded, kernel_agents=kernel_copied, soul=soul_path,
                         port=port,
                         note=("your twin is up — open the url and use it INSTEAD of the "
                               "global brainstem. If it can't auth, it shares the brainstem's "
                               "Copilot session (re-login at /login on the main brainstem)."))

    @staticmethod
    def _free_port(lo=7081, hi=7200):
        import socket
        for p in range(lo, hi):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.bind(("127.0.0.1", p))
                s.close()
                return p
            except OSError:
                s.close()
                continue
        return lo

    @staticmethod
    def _twin_liveness(port, seconds=10):
        import time
        import urllib.request
        deadline = time.time() + seconds
        while time.time() < deadline:
            try:
                with urllib.request.urlopen(f"http://127.0.0.1:{port}/health", timeout=1):
                    return True
            except Exception:
                time.sleep(0.5)
        return False

    # ── neighborhood ops (the shared-neighborhood flow (generic; cover-safe)) ──
    def _neighborhood(self, action, kwargs, ctx):
        mounted = ctx["repo_dir"] and os.path.isdir(ctx["repo_dir"]) and \
            os.path.exists(os.path.join(ctx["repo_dir"], "neighborhood.json"))

        if action == "qr":
            from urllib.parse import quote
            num = kwargs.get("rappid") or ctx["repo"]
            return self._env(action, "success", door=ctx["repo"],
                             dial_url=f"{PAYPHONE_URL}?dial={quote(num, safe='')}",
                             share_url=f"{PAYPHONE_URL}?share={quote(num, safe='')}",
                             how_to="open share_url → scannable QR to hand out; scanners dial pre-filled.")
        if action == "enter":
            return self._env(action, "success", lobby_url=LOBBY_URL, payphone_url=PAYPHONE_URL,
                             note=("the live E2E room is a browser surface — open the "
                                   "payphone, sign in with GitHub, it hands you into the room."))
        if action == "mount":
            if ctx["offline"]:
                return self._env(action, "success", mounted=mounted, clone=ctx["repo_dir"], note="test/offline")
            if mounted:
                rc, _, err = _run(["git", "-C", ctx["repo_dir"], "pull", "--ff-only"])
                return self._env(action, "success" if rc == 0 else "degraded",
                                 mounted=True, clone=ctx["repo_dir"],
                                 note=None if rc == 0 else f"pull failed ({err[:120]}) — serving cache")
            os.makedirs(os.path.dirname(ctx["repo_dir"]), exist_ok=True)
            rc, _, err = _run(["gh", "repo", "clone", ctx["repo"], ctx["repo_dir"]])
            if rc != 0:
                return self._env(action, "error",
                                 error=f"clone failed: {err[:240]}. Collaborator access on {ctx['repo']}?")
            return self._env(action, "success", mounted=True, clone=ctx["repo_dir"])

        if not mounted:
            return self._env(action, "error", error="not mounted — run action=mount first")
        rd = ctx["repo_dir"]

        if action == "browse":
            cubbies = []
            root = os.path.join(rd, "cubbies")
            for entry in sorted(os.listdir(root) if os.path.isdir(root) else []):
                if entry.startswith(("_", ".")) or not os.path.isdir(os.path.join(root, entry)):
                    continue   # skip index.json + any stray files — cubbies are dirs
                c = _read_json(os.path.join(root, entry, "cubby.json")) or {}
                agents = sorted(f for f in (os.listdir(os.path.join(root, entry, "agents"))
                                if os.path.isdir(os.path.join(root, entry, "agents")) else [])
                                if f.endswith("_agent.py"))
                cubbies.append({"github_login": c.get("github_login", entry),
                                "what_im_cooking": c.get("what_im_cooking", ""), "agents": agents})
            return self._env(action, "success", cubbies=cubbies, count=len(cubbies))

        if action == "super_rar":   # where=neighborhood (default)
            croot = os.path.join(rd, "cubbies")
            entries = _build_super_rar(croot)
            q = (kwargs.get("query") or "").strip().lower()
            hits = [e for e in entries if _q_match(q, e, os.path.join(croot, e["path"]))] if q else entries
            return self._env(action, "success", where="neighborhood", query=q or None,
                             matches=len(hits), total=len(entries),
                             by_kind={k: sum(1 for e in entries if e["kind"] == k)
                                      for k in {x["kind"] for x in entries}},
                             results=hits[:50],
                             hint="stream an agent hit with action=load cubby=<its cubby>.")

        if not ctx["handle"]:
            return self._env(action, "error", error="run `gh auth login` (or pass _handle).")
        me = ctx["handle"]
        if not _HANDLE_RE.match(me):
            return self._env(action, "error", error=f"unsafe handle {me!r}")
        my_cubby = os.path.join(rd, "cubbies", me)

        if action == "join":
            existed = os.path.isfile(os.path.join(my_cubby, "cubby.json"))
            for d in CUBBY_ANATOMY:
                os.makedirs(os.path.join(my_cubby, d), exist_ok=True)
            if not existed:
                _write_json(os.path.join(my_cubby, "cubby.json"), {
                    "schema": CUBBY_SCHEMA, "github_login": me, "rappid": ctx["rappid"],
                    "display_name": me, "what_im_cooking": kwargs.get("what", "just moved in"),
                    "created_at": _now(), "estate": {"anatomy": list(CUBBY_ANATOMY)},
                    "streamable": {"agents": True}})
            members = _read_json(os.path.join(rd, "members.json")) or \
                {"schema": "rapp-neighborhood-members/1.0", "members": []}
            if not any(m.get("github_login") == me for m in members["members"]):
                members["members"].append({"github_login": me, "rappid": ctx["rappid"],
                    "role": "member", "joined_at": _now(), "via": "cubby-join"})
                _write_json(os.path.join(rd, "members.json"), members)
            git = self._commit_push(ctx, f"cubby: {me} joins", kwargs.get("push", True))
            return self._env(action, "already_joined" if existed else "success",
                             cubby=f"cubbies/{me}/", **git)

        if action == "stash":
            src = kwargs.get("path")
            if not src or not os.path.isfile(src):
                return self._env(action, "error", error="pass path=<existing file>")
            # destination: your cubby, OR a sub-cubby you OWN (cubbies/<me>/cubbies/<slug>/).
            target_root, rel_root = my_cubby, f"cubbies/{me}"
            cval = (kwargs.get("cubby") or "").strip()
            if cval and cval != me:
                if "/" in cval or ".." in cval:
                    return self._env(action, "refused",
                                     error=f"cubbies are isolated — you write only in cubbies/{me}/.")
                sub_slug = _slugify(cval)
                target_root = os.path.join(my_cubby, "cubbies", sub_slug)
                rel_root = f"cubbies/{me}/cubbies/{sub_slug}"
                if not os.path.isfile(os.path.join(target_root, "cubby.json")):
                    self._make_sub_cubby(target_root, me, sub_slug, kwargs.get("what", ""))
            base = os.path.basename(src)
            if _SECRET_NAME_RE.search(base):
                return self._env(action, "refused", error=f"'{base}' is secret-shaped — bones, not substance.")
            sub = ("agents" if base.endswith("_agent.py") else "organs" if base.endswith("_organ.py")
                   else "eggs" if base.endswith(".egg") else "show-and-tell")
            dst = os.path.join(target_root, sub, base)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
            git = self._commit_push(ctx, f"cubby({me}): stash {sub}/{base}", kwargs.get("push", True))
            return self._env(action, "success", stashed=f"{rel_root}/{sub}/{base}", **git)

        if action == "hatch":
            res = self._hatch_egg(kwargs.get("path"), my_cubby, action, ctx, local=False)
            if isinstance(res, dict) and res.get("_ok"):
                git = self._commit_push(ctx, f"cubby({me}): hatch egg ({len(res['landed'])} files)",
                                        kwargs.get("push", True))
                return self._env(action, "success", landed=res["landed"],
                                 refused_secrets=res["refused"], cubby=f"cubbies/{me}/", **git)
            return res  # already an error envelope

        if action == "load":
            return self._load(kwargs, ctx, rd, me)
        if action == "unload":
            return self._unload(kwargs, ctx)
        if action == "show_and_tell":
            return self._show_and_tell(kwargs, ctx, rd, me)
        if action == "sync":
            if not ctx["offline"]:
                _run(["git", "-C", rd, "pull", "--ff-only"])
            return self._env(action, "success", note="pulled latest; browse / super_rar to see what's new.")
        if action == "branch":
            topic = _slugify(kwargs.get("topic") or "wip", "wip")
            branch = f"cubby/{me}/{topic}"
            if ctx["offline"]:
                return self._env(action, "dry_run", branch=branch)
            rc, _, err = _run(["git", "-C", rd, "checkout", "-b", branch])
            if rc != 0:
                return self._env(action, "error", error=err[:200])
            _run(["git", "-C", rd, "push", "-u", "origin", branch])
            return self._env(action, "success", branch=branch, note="yours — never must merge to main.")
        if action == "invite":
            login = kwargs.get("github_login")
            if not login:
                return self._env(action, "error", error="pass github_login=<who>")
            cmd = ["gh", "api", "-X", "PUT", f"repos/{ctx['repo']}/collaborators/{login}",
                   "--field", "permission=push"]
            if not kwargs.get("confirm"):
                return self._env(action, "dry_run", command=" ".join(cmd),
                                 note="re-run with confirm=true to invite.")
            rc, _, err = _run(cmd)
            return self._env(action, "success" if rc == 0 else "error",
                             **({"invited": login} if rc == 0 else {"error": err[:240]}))
        return self._env(action, "error", error="unreachable")

    # ── shared egg hatch (into a local cubby slug-dir or a neighborhood cubby) ──
    def _hatch_egg(self, src, dest_template, action, ctx, local):
        if not src or not os.path.isfile(src):
            return self._env(action, "error", error="pass path=<a .egg file>")
        try:
            z = zipfile.ZipFile(src)
        except zipfile.BadZipFile:
            return self._env(action, "error", error="not a valid .egg (zip)")
        mani = {}
        try:
            mani = json.loads(z.read("manifest.json"))
        except (KeyError, ValueError):
            pass
        if any(n.startswith("cubby/") for n in z.namelist()):
            prefix = "cubby/"
        elif any(n.startswith("repo/") for n in z.namelist()):
            prefix = "repo/"
        else:
            return self._env(action, "refused", error="unrecognized egg layout — refusing to guess.")
        if local:
            slug = mani.get("slug") or "imported"
            if not _SLUG_RE.match(slug):
                slug = "imported"
            dest = dest_template.replace("{slug}", slug)
        else:
            dest = dest_template
        landed, refused = [], []
        for n in z.namelist():
            if not n.startswith(prefix) or n.endswith("/"):
                continue
            rel = n[len(prefix):]
            base = os.path.basename(rel)
            if base in (".gitkeep",):
                continue
            if _SECRET_NAME_RE.search(base):
                refused.append(rel); continue
            top = rel.split("/", 1)[0]
            if top not in CUBBY_ANATOMY:
                if base.endswith("_agent.py"):
                    rel = "agents/" + base
                else:
                    refused.append(rel); continue
            target = os.path.normpath(os.path.join(dest, rel))
            if not target.startswith(os.path.normpath(dest) + os.sep):
                refused.append(rel); continue
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with open(target, "wb") as f:
                f.write(z.read(n))
            landed.append(target if local else os.path.relpath(target, ctx["repo_dir"]))
        if local:
            return self._env(action, "success", cubby=os.path.basename(dest),
                             path=dest, landed=len(landed), refused_secrets=refused)
        return {"_ok": True, "landed": landed, "refused": refused}

    # ── load / unload (git-invisible streaming) ──
    def _load(self, kwargs, ctx, rd, me):
        def has_agents(h):
            d = os.path.join(rd, "cubbies", h, "agents")
            return os.path.isdir(d) and any(f.endswith("_agent.py") for f in os.listdir(d))
        src_cubby = kwargs.get("cubby") or (me if has_agents(me) else None)
        if not src_cubby:
            return self._env("load", "error", error="pass cubby=<whose agents to stream>")
        if not _HANDLE_RE.match(src_cubby):
            return self._env("load", "error", error=f"unsafe cubby {src_cubby!r}")
        src = os.path.join(rd, "cubbies", src_cubby, "agents")
        if not os.path.isdir(src):
            return self._env("load", "error", error=f"no agents/ in cubbies/{src_cubby}/")
        bs = kwargs.get("_brainstem_dir") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        target = os.path.join(bs, "agents")
        os.makedirs(target, exist_ok=True)
        # verify=true (default): every streamed file must match the neighborhood
        # rar manifest's sha256 pin — refuse to load drift (a tampered cubby file).
        verify = kwargs.get("verify", True)
        pins = {}
        if verify:
            ridx = _read_json(os.path.join(rd, "rar", "index.json")) or {}
            for a in ridx.get("agents", []):
                if a.get("path") and a.get("sha256"):
                    pins[os.path.basename(a["path"])] = a["sha256"]
        loadout = _read_json(ctx["loadout_path"]) or {"schema": "rapp-loadout/1.0", "loaded": []}
        known = {e["file"] for e in loadout["loaded"]}
        loaded, skipped = [], []
        for fn in sorted(os.listdir(src)):
            if not _AGENT_FILE_RE.match(fn):
                continue
            if fn in KERNEL_AGENTS:
                skipped.append({"file": fn, "why": "kernel — never overwritten"}); continue
            src_file = os.path.join(src, fn)
            if verify and fn in pins:
                got = _sha256_file(src_file)
                if got != pins[fn]:
                    skipped.append({"file": fn, "why": f"sha256 drift vs rar manifest "
                                    f"({got[:12]}… != {pins[fn][:12]}…) — refused"}); continue
            dst = os.path.join(target, fn)
            if os.path.exists(dst) and fn not in known and _sha256_file(dst) != _sha256_file(src_file):
                skipped.append({"file": fn, "why": "your own file — won't overwrite"}); continue
            shutil.copy2(src_file, dst)
            loadout["loaded"] = [e for e in loadout["loaded"] if e["file"] != fn] + \
                [{"file": fn, "sha256": _sha256_file(dst), "from_cubby": src_cubby,
                  "loaded_at": _now(), "target": target}]
            loaded.append(fn)
        excluded = self._register_excludes(bs, target, loaded)
        _write_json(ctx["loadout_path"], loadout)
        return self._env("load", "success", from_cubby=src_cubby, loaded=loaded,
                         skipped=skipped, git_excluded=excluded,
                         note="streamed + git-invisible (.git/info/exclude) — zero commit risk.")

    def _unload(self, kwargs, ctx):
        loadout = _read_json(ctx["loadout_path"]) or {"loaded": []}
        bs = kwargs.get("_brainstem_dir")
        removed, kept, remaining = [], [], []
        for e in loadout.get("loaded", []):
            fn, target = e.get("file", ""), e.get("target", "")
            if fn in KERNEL_AGENTS or not _AGENT_FILE_RE.match(fn):
                remaining.append(e); kept.append(f"{fn} (refused)"); continue
            if bs and os.path.normpath(target) != os.path.normpath(os.path.join(bs, "agents")):
                remaining.append(e); kept.append(fn); continue
            p = os.path.join(target, fn)
            if os.path.basename(p) == fn and os.path.exists(p):
                os.remove(p)
            removed.append(fn)
            self._unregister_exclude(os.path.dirname(target), target, fn)
        loadout["loaded"] = remaining
        _write_json(ctx["loadout_path"], loadout)
        return self._env("unload", "success", removed=removed, kept=kept)

    def _show_and_tell(self, kwargs, ctx, rd, me):
        title = kwargs.get("title") or "show and tell"
        text = kwargs.get("text") or ""
        date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        rel = f"cubbies/{me}/show-and-tell/{date}-{_slugify(title)}.md"
        p = os.path.join(rd, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, "w").write(f"# {title}\n\n*{_now()} — @{me}*\n\n{text}\n")
        ev = {"schema": EVENT_SCHEMA, "kind": "show-and-tell", "from": ctx["rappid"],
              "ts": _now(), "cubby": me, "body": {"title": title, "text": text[:4096], "artifact": rel}}
        fp = hashlib.sha256(ctx["rappid"].encode()).hexdigest()[:16]
        ev_rel = f"events/{fp}-{ev['ts'].replace('-', '').replace(':', '')}.json"
        _write_json(os.path.join(rd, ev_rel), ev)
        git = self._commit_push(ctx, f"show-and-tell({me}): {title[:50]}", kwargs.get("push", True))
        return self._env("show_and_tell", "success", artifact=rel, event=ev_rel, **git)

    # ── git-invisibility helpers ──
    @staticmethod
    def _git_top(start):
        rc, out, _ = _run(["git", "-C", start, "rev-parse", "--show-toplevel"])
        return out if rc == 0 and out else None

    def _register_excludes(self, bs, target, files):
        top = self._git_top(bs)
        if not top:
            return []
        ex = os.path.join(top, ".git", "info", "exclude")
        os.makedirs(os.path.dirname(ex), exist_ok=True)
        existing = open(ex).read() if os.path.exists(ex) else ""
        add = [os.path.relpath(os.path.join(target, fn), top) for fn in files
               if os.path.relpath(os.path.join(target, fn), top) not in existing.splitlines()]
        if add:
            with open(ex, "a") as f:
                if existing and not existing.endswith("\n"):
                    f.write("\n")
                f.write("# streamed in (rapp load) — git-invisible by design\n" + "\n".join(add) + "\n")
        return add

    def _unregister_exclude(self, bs, target, fn):
        top = self._git_top(bs)
        if not top:
            return
        ex = os.path.join(top, ".git", "info", "exclude")
        if not os.path.exists(ex):
            return
        rel = os.path.relpath(os.path.join(target, fn), top)
        lines = [l for l in open(ex).read().splitlines() if l.strip() != rel]
        with open(ex, "w") as f:
            f.write("\n".join(lines) + ("\n" if lines else ""))


if __name__ == "__main__":
    a = RappAgent()
    print(a.perform(action="help"))
    print("\n--- spec ---\n")
    print(a.perform(action="spec")[:600])
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
