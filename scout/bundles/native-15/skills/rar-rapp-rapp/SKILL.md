---
name: "rar-rapp-rapp"
description: "SIRI-LEVEL FRONT DOOR: the user speaks PLAIN language and knows NOTHING about rapp (no 'rappid'/'cubby'/'egg'/'estate'). Translate their wish into the right action(s), DO it end to end, then report back in THEIR words. Ambiguous wish? call action=assist problem='<their exact words>' \u2192 it returns a step-by-step plan + the first call to run; then execute that plan. NEVER make the user learn a term or run a raw command.\nTHE single agent for the whole RAPP ecosystem. Pass action=<one enum value> PLUS that action's params (listed here). This metadata is ALL the caller gets, so pass exactly what the chosen action needs. Write actions commit+push by default \u2014 pass push=false to only stage locally. Unsure which action/params fit? call action=spec or action=route need='<what you want>' FIRST.\nORIENT \u2014 spec (full ecosystem map) \u00b7 ecosystem \u00b7 find query=\u2026 \u00b7 refresh \u00b7 protocol \u00b7 whoami \u00b7 help\nIDENTITY/DOORS \u2014 estate (your doors) \u00b7 door rappid=\u2026 [validate=true] (resolve + reachability-check any door)\nBOOTSTRAP \u2014 mint owner=\u2026 slug=\u2026 [kind=] [force=] (mint an Eternity rappid) \u00b7 scaffold (seed kernel agents) \u00b7 plant owner=\u2026 slug=\u2026 [kind=] [display_name=] [confirm=] (public front-door grail) \u00b7 batcave owner=\u2026 slug=\u2026 [what=] (plant a PRIVATE cubby-neighborhood \u2014 dry-run unless confirm=true)\nREACH ANY SPECIALIST \u2014 install name=<file.py>|query=\u2026|url=\u2026 [git_invisible=] [verify=] (pull + hot-load ANY agent) \u00b7 route need='<free text>' (names the provider + its install line)\nTAILORED APPS \u2014 summon rapplication=<name under ~/.rapp/rapplications> [port=] (boot a rapplication as an isolated tailored-UI twin on its own port; idempotent)\nCUBBIES & TWINS (on-device) \u2014 cubby_new slug=\u2026 what=\u2026 \u00b7 cubby_list \u00b7 cubby_show cubby=\u2026 \u00b7 cubby_collect slug=\u2026 query=\u2026 [source=cubbies|brainstem|all] \u00b7 cubby_fork slug=\u2026 from='non-kernel-agents|brainstem|cubby:<slug>' [paths=] [egg=true] [twin=] \u00b7 cubby_egg cubby=\u2026 \u00b7 cubby_import path=\u2026 \u00b7 twin cubby=\u2026 [soul=] (pop a twin chat from a cubby) \u00b7 super_rar query=\u2026 [where=local|neighborhood] (search the whole estate)\nMEMORY (op required) \u2014 memory op=save key=\u2026 value=\u2026 | op=read [key=\u2026] | op=recall query=\u2026\nLINEAGE (op required) \u2014 bond op=record event=<birth|bond|hatch|graft|launch|adoption|rhythm> [context=] [egg_sha256=] | bond op=list \u00b7 lineage (walk to species root)\nFEDERATE \u2014 beacon estate_url=\u2026 [private_estate_pointer=] (write the estate beacon) \u00b7 sniff seed=<url> (BFS the network) \u00b7 mmr (standing score)\nNEIGHBORHOOD (FIRST set repo=<owner/repo> or env RAPP_NEIGHBORHOOD) \u2014 mount \u00b7 join what=\u2026 \u00b7 browse \u00b7 stash path=\u2026 [cubby=<slug>] \u00b7 hatch path=\u2026 \u00b7 load [cubby=] \u00b7 unload \u00b7 sync \u00b7 branch topic=\u2026 \u00b7 invite github_login=\u2026 [confirm=true] \u00b7 qr \u00b7 enter \u00b7 show_and_tell title=\u2026 text=\u2026 \u00b7 super_rar where=neighborhood query=\u2026\nSELF-CHECK \u2014 verify (god\u2261map\u2261bible drift triangle)"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/rapp", "rar_sha256": "827cc07976687631087dd00ceb7d5d78082eb2f025467215cadac68e81d10a71", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.7", "author": "Kody Wildfeuer", "tags": ["rapp", "ecosystem", "estate", "cubby", "neighborhood", "egg", "super-rar", "door", "spec", "universal"]}
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
