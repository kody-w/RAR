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
    "version": "1.0.2",
    "display_name": "RappAgent",
    "description": ("The one agent for the whole RAPP ecosystem: identity, "
                    "doors, local cubbies, shared neighborhoods, eggs, the "
                    "super-RAR, and zero-commit-risk streaming — and it knows "
                    "the spec (action=spec) for navigating it all end to end."),
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
# the drift triangle: rapp-god + rapp-map both publish the SAME ecosystem-spec.json
SPEC_GOD_URL = os.environ.get("RAPP_SPEC_GOD",
                              f"{_RAW}/kody-w/rapp-god/main/api/v1/ecosystem-spec.json")
SPEC_MAP_URL = os.environ.get("RAPP_SPEC_MAP",
                              f"{_RAW}/kody-w/rapp-map/main/ecosystem-spec.json")

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
    `kind` lives in the record, never the string. We NEVER mint the v2 form."""
    import uuid
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
        h = hashlib.sha256(f"kody/{name}-twin".encode()).hexdigest()[:32]
        ws = os.path.join(home, ".rapp", "twins", h)
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
        rappid = f"rappid:@{ctx.get('handle') or 'kody'}/{name}-twin:{h}"
        _write_json(os.path.join(ws, "rappid.json"), {
            "schema": "rapp-rappid/2.0", "rappid": rappid,
            "parent_rappid": "rappid:@rapp/origin:0b635450c04249fbb4b1bdb571044dec",
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
        import hashlib
        owner = (kwargs.get("owner") or ctx.get("handle") or "").strip()
        slug = (kwargs.get("slug") or "batcave").strip()
        if not owner:
            return self._env("batcave", "error", error="need owner=<github-login> (or sign into gh).")
        import uuid
        h = hashlib.sha256(b"rapp/1:rappid\n" + uuid.uuid4().bytes).hexdigest()  # canonical keyless mint (spec §6.2), never sha256(name)
        rappid = f"rappid:@{owner}/{slug}:{h}"
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
        files = {
            "rappid.json": json.dumps({"schema": "rapp-rappid/2.0", "rappid": rappid,
                "parent_rappid": ctx.get("rappid") or "rappid:@rapp/origin:0b635450c04249fbb4b1bdb571044dec",
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
        os.makedirs(target_dir, exist_ok=True)
        dst = os.path.join(target_dir, dest_fn)
        with open(dst, "wb") as f:
            f.write(body)
        result = {"agent": dest_fn, "from": label, "path": dst,
                  "sha256": hashlib.sha256(body).hexdigest(), "verified": verified}
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
        rec = {"schema": "rapp-rappid/2.0", "rappid": rappid, "kind": kind,
               "name": slug, "owner": owner, "repo": slug, "host": "github.com",
               "github": f"https://github.com/{owner}/{slug}",
               "parent_rappid": (existing or {}).get("parent_rappid") or f"rappid:@{RAPP_SPECIES.replace('/', ':')}",
               "parent_repo": f"https://github.com/{RAPP_SPECIES}",
               "minted_at": _now(),
               "notes": ("Eternity format (Art. XXXIV.1): rappid:@<owner>/<slug>:<64hex>, "
                         "the deterministic sha256 of '%s/%s'. kind lives in the record." % (owner, slug))}
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
        parent_rappid = parent.get("rappid") or f"rappid:@{RAPP_SPECIES.replace('/', ':')}"
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
            "schema": "rapp-rappid/2.0", "rappid": rappid, "kind": kind, "name": slug,
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

    # ── verify: THE DRIFT-TRIANGLE self-check (god ≡ map, enum ⊇ required) ──
    def _verify(self, kwargs, ctx):
        enum = list(self.metadata["parameters"]["properties"]["action"]["enum"])
        god_text, god_status = _fetch_status(SPEC_GOD_URL)
        map_text, map_status = _fetch_status(SPEC_MAP_URL)
        # offline: no network at all → degrade, report we can only self-describe
        if god_status is None and map_status is None:
            return self._env("verify", "offline", action_enum=sorted(enum),
                             god_spec=SPEC_GOD_URL, map_spec=SPEC_MAP_URL,
                             note=("offline — `verify` needs network to fetch the two "
                                   "ecosystem-spec.json copies (rapp-god + rapp-map) and prove "
                                   "they're byte-identical. Re-run online. Until then, the agent "
                                   "exposes %d actions." % len(enum)))
        # not-yet-published: both 404 (or one 404 + other offline)
        if (god_status == 404 or god_status is None) and (map_status == 404 or map_status is None):
            return self._env("verify", "no_spec", action_enum=sorted(enum),
                             god_status=god_status, map_status=map_status,
                             god_spec=SPEC_GOD_URL, map_spec=SPEC_MAP_URL,
                             note=("spec not yet published (404) — the rapp-god/rapp-map "
                                   "ecosystem-spec.json doesn't exist yet. Nothing to verify "
                                   "against; the spec author should publish it with "
                                   "required_actions[] = this agent's action enum."))
        god_sha = hashlib.sha256(god_text.encode()).hexdigest() if god_text else None
        map_sha = hashlib.sha256(map_text.encode()).hexdigest() if map_text else None
        identical = bool(god_sha and map_sha and god_sha == map_sha)
        spec = None
        for t in (god_text, map_text):
            if t:
                try:
                    spec = json.loads(t); break
                except ValueError:
                    pass
        required = (spec or {}).get("required_actions", []) if spec else []
        enum_set = set(enum)
        missing = sorted(set(required) - enum_set)
        extra = sorted(enum_set - set(required)) if required else []
        drift = bool((not identical and god_sha and map_sha) or missing)
        return self._env("verify", "success",
                         god_map_identical=identical, god_sha256=god_sha, map_sha256=map_sha,
                         spec_version=(spec or {}).get("version") or (spec or {}).get("spec_version"),
                         required_actions=required, missing_actions=missing, extra_actions=extra,
                         drift=drift,
                         note=("drift triangle: rapp-god ≡ rapp-map AND this agent's enum ⊇ "
                               "required_actions. " + ("DRIFT DETECTED — reconcile." if drift
                               else "all green — no drift.")))

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
