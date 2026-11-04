---
name: "rar-rapp-rapp"
description: "SIRI-LEVEL FRONT DOOR: the user speaks PLAIN language and knows NOTHING about rapp (no 'rappid'/'cubby'/'egg'/'estate'). Translate their wish into the right action(s), DO it end to end, then report back in THEIR words. Ambiguous wish? call action=assist problem='<their exact words>' \u2192 it returns a step-by-step plan + the first call to run; then execute that plan. NEVER make the user learn a term or run a raw command.\nTHE single agent for the whole RAPP ecosystem. Pass action=<one enum value> PLUS that action's params (listed here). This metadata is ALL the caller gets, so pass exactly what the chosen action needs. Write actions commit+push by default \u2014 pass push=false to only stage locally. Unsure which action/params fit? call action=spec or action=route need='<what you want>' FIRST.\nORIENT \u2014 spec (full ecosystem map) \u00b7 ecosystem \u00b7 find query=\u2026 \u00b7 refresh \u00b7 protocol \u00b7 whoami \u00b7 help\nIDENTITY/DOORS \u2014 estate (your doors) \u00b7 door rappid=\u2026 [validate=true] (resolve + reachability-check any door)\nBOOTSTRAP \u2014 mint owner=\u2026 slug=\u2026 [kind=] [force=] (mint an Eternity rappid) \u00b7 scaffold (seed kernel agents) \u00b7 plant owner=\u2026 slug=\u2026 [kind=] [display_name=] [confirm=] (public front-door grail) \u00b7 batcave owner=\u2026 slug=\u2026 [what=] (plant a PRIVATE cubby-neighborhood \u2014 dry-run unless confirm=true)\nREACH ANY SPECIALIST \u2014 install name=<file.py>|query=\u2026|url=\u2026 [git_invisible=] [verify=] (pull + hot-load ANY agent) \u00b7 route need='<free text>' (names the provider + its install line)\nTAILORED APPS \u2014 summon rapplication=<name under ~/.rapp/rapplications> [port=] (boot a rapplication as an isolated tailored-UI twin on its own port; idempotent)\nCUBBIES & TWINS (on-device) \u2014 cubby_new slug=\u2026 what=\u2026 \u00b7 cubby_list \u00b7 cubby_show cubby=\u2026 \u00b7 cubby_collect slug=\u2026 query=\u2026 [source=cubbies|brainstem|all] \u00b7 cubby_fork slug=\u2026 from='non-kernel-agents|brainstem|cubby:<slug>' [paths=] [egg=true] [twin=] \u00b7 cubby_egg cubby=\u2026 \u00b7 cubby_import path=\u2026 \u00b7 twin cubby=\u2026 [soul=] (pop a twin chat from a cubby) \u00b7 super_rar query=\u2026 [where=local|neighborhood] (search the whole estate)\nMEMORY (op required) \u2014 memory op=save key=\u2026 value=\u2026 | op=read [key=\u2026] | op=recall query=\u2026\nLINEAGE (op required) \u2014 bond op=record event=<birth|bond|hatch|graft|launch|adoption|rhythm> [context=] [egg_sha256=] | bond op=list \u00b7 lineage (walk to species root)\nFEDERATE \u2014 beacon estate_url=\u2026 [private_estate_pointer=] (write the estate beacon) \u00b7 sniff seed=<url> (BFS the network) \u00b7 mmr (standing score)\nNEIGHBORHOOD (FIRST set repo=<owner/repo> or env RAPP_NEIGHBORHOOD) \u2014 mount \u00b7 join what=\u2026 \u00b7 browse \u00b7 stash path=\u2026 [cubby=<slug>] \u00b7 hatch path=\u2026 \u00b7 load [cubby=] \u00b7 unload \u00b7 sync \u00b7 branch topic=\u2026 \u00b7 invite github_login=\u2026 [confirm=true] \u00b7 qr \u00b7 enter \u00b7 show_and_tell title=\u2026 text=\u2026 \u00b7 super_rar where=neighborhood query=\u2026\nSELF-CHECK \u2014 verify (god\u2261map\u2261bible drift triangle)"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/rapp", "rar_sha256": "137f52017fe47f6263fe54b15baa5cdd65d86f664debbe4e26cbbd835f4abedb", "source_kind": "rar-agent", "source_commit": "b3e7df9a23142492ce666a32e7630c42137f537e", "version": "1.0.7", "author": "Kody Wildfeuer", "tags": ["rapp", "ecosystem", "estate", "cubby", "neighborhood", "egg", "super-rar", "door", "spec", "universal"]}
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
