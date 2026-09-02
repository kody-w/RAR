---
name: "rar-rapp-rapp"
description: "SIRI-LEVEL FRONT DOOR: the user speaks PLAIN language and knows NOTHING about rapp (no 'rappid'/'cubby'/'egg'/'estate'). Translate their wish into the right action(s), DO it end to end, then report back in THEIR words. Ambiguous wish? call action=assist problem='<their exact words>' \u2192 it returns a step-by-step plan + the first call to run; then execute that plan. NEVER make the user learn a term or run a raw command.\nTHE single agent for the whole RAPP ecosystem. Pass action=<one enum value> PLUS that action's params (listed here). This metadata is ALL the caller gets, so pass exactly what the chosen action needs. Write actions commit+push by default \u2014 pass push=false to only stage locally. Unsure which action/params fit? call action=spec or action=route need='<what you want>' FIRST.\nORIENT \u2014 spec (full ecosystem map) \u00b7 ecosystem \u00b7 find query=\u2026 \u00b7 refresh \u00b7 protocol \u00b7 whoami \u00b7 help\nIDENTITY/DOORS \u2014 estate (your doors) \u00b7 door rappid=\u2026 [validate=true] (resolve + reachability-check any door)\nBOOTSTRAP \u2014 mint owner=\u2026 slug=\u2026 [kind=] [force=] (mint an Eternity rappid) \u00b7 scaffold (seed kernel agents) \u00b7 plant owner=\u2026 slug=\u2026 [kind=] [display_name=] [confirm=] (public front-door grail) \u00b7 batcave owner=\u2026 slug=\u2026 [what=] (plant a PRIVATE cubby-neighborhood \u2014 dry-run unless confirm=true)\nREACH ANY SPECIALIST \u2014 install name=<file.py>|query=\u2026|url=\u2026 [git_invisible=] [verify=] (pull + hot-load ANY agent) \u00b7 route need='<free text>' (names the provider + its install line)\nTAILORED APPS \u2014 summon rapplication=<name under ~/.rapp/rapplications> [port=] (boot a rapplication as an isolated tailored-UI twin on its own port; idempotent)\nCUBBIES & TWINS (on-device) \u2014 cubby_new slug=\u2026 what=\u2026 \u00b7 cubby_list \u00b7 cubby_show cubby=\u2026 \u00b7 cubby_collect slug=\u2026 query=\u2026 [source=cubbies|brainstem|all] \u00b7 cubby_fork slug=\u2026 from='non-kernel-agents|brainstem|cubby:<slug>' [paths=] [egg=true] [twin=] \u00b7 cubby_egg cubby=\u2026 \u00b7 cubby_import path=\u2026 \u00b7 twin cubby=\u2026 [soul=] (pop a twin chat from a cubby) \u00b7 super_rar query=\u2026 [where=local|neighborhood] (search the whole estate)\nMEMORY (op required) \u2014 memory op=save key=\u2026 value=\u2026 | op=read [key=\u2026] | op=recall query=\u2026\nLINEAGE (op required) \u2014 bond op=record event=<birth|bond|hatch|graft|launch|adoption|rhythm> [context=] [egg_sha256=] | bond op=list \u00b7 lineage (walk to species root)\nFEDERATE \u2014 beacon estate_url=\u2026 [private_estate_pointer=] (write the estate beacon) \u00b7 sniff seed=<url> (BFS the network) \u00b7 mmr (standing score)\nNEIGHBORHOOD (FIRST set repo=<owner/repo> or env RAPP_NEIGHBORHOOD) \u2014 mount \u00b7 join what=\u2026 \u00b7 browse \u00b7 stash path=\u2026 [cubby=<slug>] \u00b7 hatch path=\u2026 \u00b7 load [cubby=] \u00b7 unload \u00b7 sync \u00b7 branch topic=\u2026 \u00b7 invite github_login=\u2026 [confirm=true] \u00b7 qr \u00b7 enter \u00b7 show_and_tell title=\u2026 text=\u2026 \u00b7 super_rar where=neighborhood query=\u2026\nSELF-CHECK \u2014 verify (god\u2261map\u2261bible drift triangle)"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/rapp", "rar_sha256": "137f52017fe47f6263fe54b15baa5cdd65d86f664debbe4e26cbbd835f4abedb", "source_kind": "rar-agent", "source_commit": "b3e7df9a23142492ce666a32e7630c42137f537e", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "rapp_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/rapp:6cd8bff083eaa31ae870eae717908ad8d6769b4b711a2849a5d1e9de793d0759", "kind": "skill"}, "version": "1.0.7", "author": "Kody Wildfeuer", "tags": ["rapp", "ecosystem", "estate", "cubby", "neighborhood", "egg", "super-rar", "door", "spec", "universal"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp/rapp`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `rapp_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_agent.py` and embedded as the fenced Python below (sha256 137f52017fe47f62…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_agent.py` first:

```bash
python3 rapp_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_agent.py   # or on stdin
python3 rapp_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
