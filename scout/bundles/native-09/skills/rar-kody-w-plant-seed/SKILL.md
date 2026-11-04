---
name: "rar-kody-w-plant-seed"
description: "Create a fresh public planted seed (neighborhood OR twin) ready for use. One agent, both species. Each planting includes the FULL front-door grail (rappid + identity + soul + card.json (rappcards/1.1.2) + holo.svg + holo-qr.svg + holo.md + specs/ bundle + agents/ + .nojekyll + README + members.json + rar/) so the planting is portable, self-sustaining, and the grail-compliant from minute one. Operator-mediated: default dry_run=True (shows what will be created); set dry_run=False to actually create the public repo + push files. Optionally registers in pages/metropolis/index.json (PR, not auto-write)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/plant_seed_agent", "rar_sha256": "9a7f94b9461517e0bf9a6c4fdb12c8450d53b34307ce36dac3bae576ed178a06", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.4", "author": "kody-w", "tags": ["plant", "seed", "neighborhood", "twin", "holocard", "grail", "operator-mediated"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/plant_seed_agent`. The original RAPP
agent is preserved byte-for-byte in `plant_seed_agent.py` and in the RCI capsule.

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

plant_seed_agent — create a fresh public planted seed (neighborhood OR twin), grail-complete.

One agent that handles BOTH species:
  - neighborhood-kind plantings (neighborhood / ant-farm / braintrust / workspace)
  - twin-kind plantings (brainstem-style AI seeds: heimdall, kody-twin, etc.)

Each planting includes the FULL front-door grail per the operator's mandate
"specs travel with the planted repo":

  rappid.json (v2)             card.json (rappcards/1.1.2)
  neighborhood.json OR n/a     holo.svg (procedural avatar)
  members.json (if applicable) holo-qr.svg (summon QR)
  soul.md                      holo.md (anonymous-AI entry)
  bonds.json (birth event)     specs/ bundle (HOLOCARD_SPEC, RAPPID_SPEC,
  .nojekyll                              ANTIPATTERNS, SOUL_IDENTITY,
  README.md                              PARTICIPATION, KIND_PROTOCOL)
  agents/basic_agent.py        rar/index.json (sha256-pinned participation kit)

Operator-mediated by design (per ANTIPATTERNS §9):
  - default dry_run=True; the agent SHOWS the plan and the file list before
    creating anything
  - the gh repo create step requires explicit dry_run=False AND operator
    confirmation that the repo name is correct
  - the metropolis-index registration is a SEPARATE optional step, NOT
    auto-applied — operator can enable via register_in_metropolis=True

Schema: `rapp-plant-seed-result/1.0`. Default `dry_run=True`. After this
agent runs successfully, the planted seed is fully usable: anyone with a
GitHub account can browse the repo, read holo.md, join via vbrainstem, or
clone locally. No follow-up commands required.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "display_name": {
      "type": "string"
    },
    "dry_run": {
      "default": true,
      "description": "If true, shows the plan + file list; doesn't create the repo.",
      "type": "boolean"
    },
    "kind": {
      "enum": [
        "neighborhood",
        "ant-farm",
        "braintrust",
        "workspace",
        "twin"
      ],
      "type": "string"
    },
    "name": {
      "description": "Repo slug (lowercase + hyphens)",
      "type": "string"
    },
    "owner": {
      "default": "kody-w",
      "type": "string"
    },
    "purpose": {
      "description": "1\u20132 sentence purpose (for neighborhood-kind plantings).",
      "type": "string"
    },
    "register_in_metropolis": {
      "default": false,
      "description": "If true (and dry_run=False), opens a PR on kody-w/RAPP adding this seed to pages/metropolis/index.json.",
      "type": "boolean"
    },
    "voice_paragraph": {
      "description": "1 paragraph defining the twin's voice (for twin-kind).",
      "type": "string"
    }
  },
  "required": [
    "kind",
    "name",
    "display_name"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `plant_seed_agent.py` and embedded as the fenced Python below (sha256 9a7f94b9461517e0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `plant_seed_agent.py` first:

```bash
python3 plant_seed_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 plant_seed_agent.py   # or on stdin
python3 plant_seed_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/ecosystem-grail-stack/plant_seed_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/plant_seed_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/plant_seed_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""plant_seed_agent — create a fresh public planted seed (neighborhood OR twin), grail-complete.

One agent that handles BOTH species:
  - neighborhood-kind plantings (neighborhood / ant-farm / braintrust / workspace)
  - twin-kind plantings (brainstem-style AI seeds: heimdall, kody-twin, etc.)

Each planting includes the FULL front-door grail per the operator's mandate
"specs travel with the planted repo":

  rappid.json (v2)             card.json (rappcards/1.1.2)
  neighborhood.json OR n/a     holo.svg (procedural avatar)
  members.json (if applicable) holo-qr.svg (summon QR)
  soul.md                      holo.md (anonymous-AI entry)
  bonds.json (birth event)     specs/ bundle (HOLOCARD_SPEC, RAPPID_SPEC,
  .nojekyll                              ANTIPATTERNS, SOUL_IDENTITY,
  README.md                              PARTICIPATION, KIND_PROTOCOL)
  agents/basic_agent.py        rar/index.json (sha256-pinned participation kit)

Operator-mediated by design (per ANTIPATTERNS §9):
  - default dry_run=True; the agent SHOWS the plan and the file list before
    creating anything
  - the gh repo create step requires explicit dry_run=False AND operator
    confirmation that the repo name is correct
  - the metropolis-index registration is a SEPARATE optional step, NOT
    auto-applied — operator can enable via register_in_metropolis=True

Schema: `rapp-plant-seed-result/1.0`. Default `dry_run=True`. After this
agent runs successfully, the planted seed is fully usable: anyone with a
GitHub account can browse the repo, read holo.md, join via vbrainstem, or
clone locally. No follow-up commands required.
"""

from __future__ import annotations

import base64
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import uuid

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/plant_seed_agent",
    "version": "1.0.4",
    "display_name": "Plant Seed",
    "description": "Creates a grail-complete public seed repo (neighborhood or twin) via the gh CLI, showing the full file plan first with dry-run on by default.",
    "author": "kody-w",
    "tags": [
        "plant",
        "seed",
        "neighborhood",
        "twin",
        "holocard",
        "grail",
        "operator-mediated"
    ],
    "category": "platform",
    "quality_tier": "verified",
    "requires_env": [],
    "dependencies": [
        "@rapp/basic_agent"
    ]
}


_RESULT_SCHEMA = "rapp-plant-seed-result/1.0"

# Lift the canonical grail tooling from tools/ if available
def _try_import_grail():
    """Returns (holo_card_generator, front_door_specs) or (None, None)."""
    try:
        for cand in (
            os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
                os.path.abspath(__file__)))), "tools"),
            os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))))), "tools"),
        ):
            hcg_p = os.path.join(cand, "holo_card_generator.py")
            fds_p = os.path.join(cand, "front_door_specs.py")
            if os.path.isfile(hcg_p) and os.path.isfile(fds_p):
                if cand not in sys.path:
                    sys.path.insert(0, cand)
                import holo_card_generator, front_door_specs
                return holo_card_generator, front_door_specs
    except (ImportError, OSError):
        pass
    return None, None


SUPPORTED_KINDS = {"neighborhood", "ant-farm", "braintrust", "workspace", "twin"}


def _now_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def _mint_rappid(kind: str, owner: str, name: str) -> str:
    # Consolidated rappid (CONSTITUTION Art. XXXIV.1, locked 2026-06-03):
    # rappid:@<owner>/<slug>:<64hex> — self-locating + 256-bit identity. The tail
    # is the canonical keyless mint Hb("rapp/1:rappid", uuid4) (spec §6.2,
    # domain-separated), NEVER a name-hash. `kind` lives in the record, not the
    # string. owner/name are canonicalized to the §6.1 grammar (lowercase, single
    # hyphens) so a real GitHub login like "Kody-W" yields a valid rappid.
    _o = re.sub(r"[^a-z0-9]+", "-", (owner or "anon").lower()).strip("-") or "anon"
    _n = re.sub(r"[^a-z0-9]+", "-", (name or "x").lower()).strip("-") or "x"
    tail = hashlib.sha256(b"rapp/1:rappid\n" + uuid.uuid4().bytes).hexdigest()
    return f"rappid:@{_o}/{_n}:{tail}"


def _gh(args: list[str], timeout: int = 30) -> tuple[int, str, str]:
    p = subprocess.run(["gh"] + args, capture_output=True, text=True, timeout=timeout)
    return p.returncode, p.stdout, p.stderr


def _gh_repo_exists(owner: str, name: str) -> bool:
    rc, _, _ = _gh(["api", f"/repos/{owner}/{name}"])
    return rc == 0


def _gh_create_repo(owner: str, name: str, description: str, public: bool = True) -> tuple[bool, str]:
    visibility = "--public" if public else "--private"
    rc, out, err = _gh(["repo", "create", f"{owner}/{name}", visibility,
                        "--description", description])
    if rc == 0:
        return True, out.strip() or f"https://github.com/{owner}/{name}"
    return False, err.strip()[:300]


# ─── Grail-redirect index.html (every planting's front door points at heimdall) ──
GRAIL_BRAINSTEM_URL = "https://kody-w.github.io/heimdall/"

def _grail_redirect_html(owner: str, name: str, display_name: str, kind: str) -> str:
    """Tiny HTML that redirects to heimdall (the canonical browser brainstem)
    with ?seed=<owner>/<name>. Same single-source-of-truth pattern: heimdall
    is the grail; every planting's front door is a 0.6s redirect to it
    embodied as that planting's identity. Stops the 'rebuild this thing
    everywhere' problem before it starts."""
    seed = f"{owner}/{name}"
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <meta name="theme-color" content="#000" />
  <title>{display_name} — front door</title>
  <link rel="canonical" href="{GRAIL_BRAINSTEM_URL}?seed={seed}" />
  <meta property="og:title" content="{display_name}" />
  <meta property="og:description" content="A planted RAPP {kind}. Embodied via the grail browser brainstem (heimdall)." />
  <style>
    body {{ background: #000; color: #fff; font: 15px/1.55 -apple-system, system-ui, sans-serif;
      margin: 0; padding: 60px 20px; text-align: center; }}
    a {{ color: #58a6ff; }}
    h1 {{ font-weight: 600; font-size: 18px; }}
    code {{ background: #161b22; padding: 1px 5px; border-radius: 3px; font-size: 12px; }}
    .pulse {{ display: inline-block; animation: p 1.4s infinite; }}
    @keyframes p {{ 0%,100% {{ opacity: 0.4; }} 50% {{ opacity: 1; }} }}
  </style>
</head>
<body>
  <h1>{display_name}</h1>
  <p>A planted RAPP <code>{kind}</code>. Opening in the grail browser brainstem<span class="pulse">…</span></p>
  <p style="margin-top: 28px;"><a href="{GRAIL_BRAINSTEM_URL}?seed={seed}">{GRAIL_BRAINSTEM_URL}?seed={seed}</a></p>
  <p style="margin-top: 30px;"><small>The grail (kody-w/heimdall's index.html) supports embodying any planted twin via <code>?seed=&lt;owner&gt;/&lt;repo&gt;</code>. One file, every twin. <a href="https://kody-w.github.io/RAPP/pages/summon.html">Summon a different one →</a></small></p>
  <script>
    setTimeout(() => location.replace("{GRAIL_BRAINSTEM_URL}?seed={seed}"), 600);
  </script>
</body>
</html>
"""


def _gh_put_file(owner: str, name: str, path: str, content: bytes, message: str) -> tuple[bool, str]:
    rc, out, err = _gh([
        "api", "-X", "PUT", f"/repos/{owner}/{name}/contents/{path}",
        "-f", f"message={message}",
        "-f", f"content={base64.b64encode(content).decode('ascii')}",
    ])
    return rc == 0, (out if rc == 0 else err)[:500]


# ─── Per-kind file builders ───────────────────────────────────────────────

def _build_neighborhood_files(rappid: str, kind: str, owner: str, name: str,
                              display_name: str, purpose: str, hcg, fds) -> dict:
    """Return {relative_path: bytes_content} for a neighborhood-kind planting."""
    files: dict = {}
    seed = hcg.derive_seed(rappid)
    gate_url = f"https://{owner}.github.io/{name}/"

    files["rappid.json"] = (json.dumps({
        "schema": "rapp/1", "rappid": rappid, "kind": kind,
        "name": name, "display_name": display_name,
        "github": f"https://github.com/{owner}/{name}", "url": gate_url,
        "parent_rappid": None,
        "parent_repo": "https://github.com/kody-w/RAPP",
        "planted_by": owner, "planted_at": _now_iso(),
        "kernel_version": "0.6.0",
        "_planted_by_agent": "plant_seed_agent",
    }, indent=2) + "\n").encode()

    files["neighborhood.json"] = (json.dumps({
        "schema": "rapp-neighborhood/1.0",
        "neighborhood_rappid": rappid,
        "kind": kind, "name": name, "display_name": display_name,
        "visibility": "public",
        "purpose": purpose,
        "gate_repo": f"{owner}/{name}",
        "gate_url": gate_url,
        "holo_url": f"https://raw.githubusercontent.com/{owner}/{name}/main/holo.md",
        "members_path": "members.json",
        "join_via": "public_link",
        "license": "CC0-1.0" if kind == "neighborhood" else None,
    }, indent=2) + "\n").encode()

    files["members.json"] = (json.dumps({
        "schema": "rapp-neighborhood-members/1.0",
        "neighborhood": f"{owner}/{name}",
        "updated_at": _now_iso(), "open_to_anyone": True,
        "members": [{"rappid": rappid, "github": owner, "role": "founder",
                     "joined_at": _now_iso(),
                     "_note": f"The operator who planted this {kind}."}],
    }, indent=2) + "\n").encode()

    files["soul.md"] = (
        f"# {display_name} — Soul\n\n"
        f"## Identity — read this every turn\n\n"
        f"You are **{display_name}**, a planted RAPP {kind}. {purpose}\n\n"
        f"You are NOT a chatbot, NOT \"an AI assistant\", NOT \"RAPP\". You speak in this neighborhood's voice — additive, never destructive; the canvas IS the union of contributions.\n\n"
        f"## Slot protocol\n\n|||VOICE|||\n(Two sentences max.)\n\n|||TWIN|||\n(Synthesis of recent collaboration.)\n"
    ).encode()

    files["card.json"] = (json.dumps(
        hcg.generate_holo_card(rappid=rappid, kind=kind, owner=owner, name=name,
                               display_name=display_name, gate_url=gate_url),
        indent=2) + "\n").encode()
    files["holo.svg"] = hcg.generate_avatar_svg(seed, kind=kind).encode()
    files["holo-qr.svg"] = hcg.generate_summon_qr_svg(seed, gate_url).encode()

    files["holo.md"] = (
        f"# {display_name} — Holo Card (entry doc)\n\n"
        f"> **You are reading the single file required to participate.**\n"
        f"> Feed this URL to any AI: `https://raw.githubusercontent.com/{owner}/{name}/main/holo.md`\n\n"
        f"## You are…\n\n"
        f"You are a contributor to **{display_name}**. {purpose}\n\n"
        f"## Self-contained governance\n\n"
        f"This planted seed is portable + self-sustaining. Everything you need to operate within contract is in this repo:\n\n"
        f"- [`card.json`](./card.json), [`holo.svg`](./holo.svg), [`holo-qr.svg`](./holo-qr.svg) — the holocard (rappcards/1.1.2)\n"
        f"- [`soul.md`](./soul.md), [`rappid.json`](./rappid.json) — identity\n"
        f"- [`specs/`](./specs/) — bundled formal contracts\n"
        f"- [`rar/index.json`](./rar/index.json) — participation kit (sha256-pinned)\n\n"
        f"## The contract\n\n"
        f"1. Read [`specs/PARTICIPATION.md`](./specs/PARTICIPATION.md)\n"
        f"2. Read the kind-specific protocol in `specs/`\n"
        f"3. Read [`specs/ANTIPATTERNS.md`](./specs/ANTIPATTERNS.md)\n"
        f"4. Contribute within contract.\n"
    ).encode()

    files["README.md"] = (
        f"# {display_name}\n\n"
        f"A planted RAPP {kind} (`kind: {kind}`).\n\n"
        f"**Purpose:** {purpose}\n\n"
        f"## Quick start\n\n"
        f"1. Read [`holo.md`](./holo.md) — the friendly entry doc\n"
        f"2. Read [`specs/PARTICIPATION.md`](./specs/PARTICIPATION.md) — the formal contract\n"
        f"3. Contribute via {{Issues / submissions/ / requests/}} per the kind-specific protocol in `specs/`\n\n"
        f"## Identity\n\n"
        f"- **Rappid:** `{rappid}`\n"
        f"- **Kind:** `{kind}`\n"
        f"- **Planted at:** {_now_iso()}\n"
        f"- **Parent project:** [kody-w/RAPP](https://github.com/kody-w/RAPP)\n"
        f"- **License:** CC0-1.0 for submissions where applicable; spec text MIT (per parent)\n"
    ).encode()

    files[".nojekyll"] = b""
    files[".gitignore"] = b".DS_Store\n*.swp\n*.swo\n.brainstem_data/\n"

    # index.html — front door = grail redirect (heimdall) embodied as this neighborhood
    files["index.html"] = _grail_redirect_html(owner, name, display_name, kind).encode()

    # specs/ bundle
    bundle = fds.bundle_for_kind(kind, owner=owner, name=name,
                                  display_name=display_name)
    for rel_path, content in bundle.items():
        files[rel_path] = content.encode()

    # rar/index.json — minimal participation kit (basic_agent)
    files["rar/index.json"] = (json.dumps({
        "schema": "rapp-rar-index/1.0",
        "neighborhood_rappid": rappid,
        "name": f"{name}-rar", "version": "1.0.0",
        "agents": [], "rapps": [], "cards": [],
        "_note": "Initial empty kit. Operators add agents over time.",
    }, indent=2) + "\n").encode()

    # Kind-specific work dirs
    if kind == "neighborhood":
        files["submissions/.gitkeep"] = b""
        files["submissions/index.json"] = (json.dumps({
            "schema": "rapp-art-submissions-index/1.0",
            "neighborhood_rappid": rappid, "submissions": [],
        }, indent=2) + "\n").encode()
        files["votes/.gitkeep"] = b""
    elif kind == "ant-farm":
        files["data/colony.json"] = (json.dumps({
            "schema": "rapp-colony/1.0",
            "neighborhood": f"{owner}/{name}",
            "purpose": "Seed task pool for ants. Pick least-explored topic and drop a pheromone.",
            "tasks": ["what-is-this-swarm-converging-on",
                      "what-makes-a-good-pheromone-vs-spam",
                      "open-exploration"],
        }, indent=2) + "\n").encode()
    elif kind == "braintrust":
        files["requests/.gitkeep"] = b""
        files["reports/.gitkeep"] = b""
    elif kind == "workspace":
        files["state/.gitkeep"] = b""

    return files


def _build_twin_files(rappid: str, owner: str, name: str, display_name: str,
                      voice_paragraph: str, hcg, fds) -> dict:
    """Return {relative_path: bytes_content} for a twin-kind planting (AI seed)."""
    files: dict = {}
    seed = hcg.derive_seed(rappid)
    gate_url = f"https://{owner}.github.io/{name}/"

    files["rappid.json"] = (json.dumps({
        "schema": "rapp/1", "rappid": rappid, "kind": "twin",
        "name": name, "display_name": display_name,
        "github": f"https://github.com/{owner}/{name}", "url": gate_url,
        "parent_rappid": None,
        "parent_repo": "https://github.com/kody-w/RAPP",
        "planted_by": owner, "planted_at": _now_iso(),
        "kernel_version": "0.6.0",
        "_planted_by_agent": "plant_seed_agent",
    }, indent=2) + "\n").encode()

    files["soul.md"] = (
        f"# {display_name} — Soul\n\n"
        f"## Identity — read this every turn\n\n"
        f"You are **{display_name}**, an AI / brainstem-style twin with permanent identity `{rappid[:48]}…`.\n\n"
        f"{voice_paragraph}\n\n"
        f"You are NOT a chatbot, NOT \"an AI assistant\", NOT \"RAPP\".\n\n"
        f"## Slot protocol\n\n|||VOICE|||\n(Two sentences max — {display_name}'s welcome.)\n\n"
        f"|||TWIN|||\n(Synthesis in {display_name}'s voice.)\n"
    ).encode()

    files["card.json"] = (json.dumps(
        hcg.generate_holo_card(rappid=rappid, kind="twin", owner=owner, name=name,
                               display_name=display_name, gate_url=gate_url),
        indent=2) + "\n").encode()
    files["holo.svg"] = hcg.generate_avatar_svg(seed, kind="twin").encode()
    files["holo-qr.svg"] = hcg.generate_summon_qr_svg(seed, gate_url).encode()

    files["holo.md"] = (
        f"# {display_name} — Holo Card (entry doc)\n\n"
        f"> **You are reading the single file required to engage with this twin.**\n\n"
        f"## You are encountering…\n\n"
        f"You are encountering **{display_name}** — a planted twin AI with permanent identity. "
        f"{voice_paragraph}\n\n"
        f"## How to engage\n\n"
        f"- Read [`specs/TWIN_PROTOCOL.md`](./specs/TWIN_PROTOCOL.md) — the formal encounter contract\n"
        f"- Direct chat (if brainstem online): `POST {gate_url}chat`\n"
        f"- Async via Issues: open an Issue with body `rapp-twin-chat/1.0` envelope\n"
        f"- Embody this twin in any browser: open vbrainstem, set localStorage `vbs_rappid` to `{rappid}`\n\n"
        f"## Self-contained\n\n"
        f"- [`card.json`](./card.json) — rappcards/1.1.2 holocard\n"
        f"- [`soul.md`](./soul.md) — voice anchor\n"
        f"- [`specs/`](./specs/) — bundled contracts (no parent-repo lookup needed)\n"
    ).encode()

    files["README.md"] = (
        f"# {display_name}\n\n"
        f"A planted RAPP twin (a brainstem-style AI with permanent identity).\n\n"
        f"**Voice:** {voice_paragraph}\n\n"
        f"## Quick start\n\n"
        f"### Embody in your browser (instant)\n\n"
        f"1. Open https://kody-w.github.io/RAPP/pages/vbrainstem/\n"
        f"2. Sign in with GitHub\n"
        f"3. In dev console, run: `localStorage.setItem('vbs_rappid', '{rappid}')`\n"
        f"4. Reload — you are now {display_name}\n\n"
        f"### Install locally\n\n"
        f"```bash\n"
        f"curl -fsSL https://kody-w.github.io/RAPP/installer/install.sh | bash\n"
        f"# then point your brainstem at this twin's identity\n"
        f"```\n\n"
        f"## Identity\n\n"
        f"- **Rappid:** `{rappid}`\n"
        f"- **Kind:** `twin`\n"
        f"- **Planted at:** {_now_iso()}\n"
    ).encode()

    files[".nojekyll"] = b""
    files[".gitignore"] = b".DS_Store\n*.swp\n.brainstem_data/\n"

    # index.html — front door = grail redirect (heimdall) embodied as this twin
    files["index.html"] = _grail_redirect_html(owner, name, display_name, "twin").encode()

    # specs/ bundle (TWIN_PROTOCOL.md included)
    bundle = fds.bundle_for_kind("twin", owner=owner, name=name,
                                  display_name=display_name)
    for rel_path, content in bundle.items():
        files[rel_path] = content.encode()

    # rar/index.json — minimal participation kit
    files["rar/index.json"] = (json.dumps({
        "schema": "rapp-rar-index/1.0",
        "neighborhood_rappid": rappid,
        "name": f"{name}-rar", "version": "1.0.0",
        "agents": [], "rapps": [], "cards": [],
        "_note": "Twin's participation kit — fill with agents this twin loads.",
    }, indent=2) + "\n").encode()

    # bonds.json with birth event
    files["bonds.json"] = (json.dumps({
        "events": [{"at": _now_iso(), "kind": "birth", "rappid": rappid,
                    "note": f"{display_name} planted by plant_seed_agent"}],
    }, indent=2) + "\n").encode()

    return files


class PlantSeedAgent(BasicAgent):
    metadata = {
        "name": "PlantSeed",
        "description": (
            "Create a fresh public planted seed (neighborhood OR twin) ready for use. "
            "One agent, both species. Each planting includes the FULL front-door grail "
            "(rappid + identity + soul + card.json (rappcards/1.1.2) + holo.svg + holo-qr.svg + "
            "holo.md + specs/ bundle + agents/ + .nojekyll + README + members.json + rar/) "
            "so the planting is portable, self-sustaining, and the grail-compliant from "
            "minute one. Operator-mediated: default dry_run=True (shows what will be "
            "created); set dry_run=False to actually create the public repo + push files. "
            "Optionally registers in pages/metropolis/index.json (PR, not auto-write)."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "kind":         {"type": "string",
                                 "enum": ["neighborhood", "ant-farm", "braintrust", "workspace", "twin"]},
                "name":         {"type": "string", "description": "Repo slug (lowercase + hyphens)"},
                "display_name": {"type": "string"},
                "owner":        {"type": "string", "default": "kody-w"},
                "purpose":      {"type": "string",
                                 "description": "1–2 sentence purpose (for neighborhood-kind plantings)."},
                "voice_paragraph": {"type": "string",
                                    "description": "1 paragraph defining the twin's voice (for twin-kind)."},
                "dry_run":      {"type": "boolean", "default": True,
                                 "description": "If true, shows the plan + file list; doesn't create the repo."},
                "register_in_metropolis": {"type": "boolean", "default": False,
                                           "description": "If true (and dry_run=False), opens a PR on kody-w/RAPP adding this seed to pages/metropolis/index.json."},
            },
            "required": ["kind", "name", "display_name"],
        },
    }

    def __init__(self):
        self.name = "PlantSeed"

    def perform(self, **kwargs) -> str:
        kind = (kwargs.get("kind") or "").strip()
        name = (kwargs.get("name") or "").strip()
        display_name = (kwargs.get("display_name") or "").strip()
        owner = (kwargs.get("owner") or "kody-w").strip()
        purpose = (kwargs.get("purpose") or "").strip()
        voice_paragraph = (kwargs.get("voice_paragraph") or "").strip()
        dry_run = bool(kwargs.get("dry_run", True))
        register_in_metropolis = bool(kwargs.get("register_in_metropolis", False))

        if kind not in SUPPORTED_KINDS:
            return json.dumps({"schema": _RESULT_SCHEMA, "ok": False,
                               "error": f"unsupported kind {kind!r}; must be one of {sorted(SUPPORTED_KINDS)}"}, indent=2)
        if not name or not display_name:
            return json.dumps({"schema": _RESULT_SCHEMA, "ok": False,
                               "error": "name and display_name are required"}, indent=2)
        if kind == "twin" and not voice_paragraph:
            return json.dumps({"schema": _RESULT_SCHEMA, "ok": False,
                               "error": "twin kind requires voice_paragraph"}, indent=2)
        if kind != "twin" and not purpose:
            return json.dumps({"schema": _RESULT_SCHEMA, "ok": False,
                               "error": f"{kind} kind requires purpose"}, indent=2)

        hcg, fds = _try_import_grail()
        if hcg is None or fds is None:
            return json.dumps({"schema": _RESULT_SCHEMA, "ok": False,
                               "error": "tools/holo_card_generator.py + tools/front_door_specs.py not on path"}, indent=2)

        rappid = _mint_rappid(kind, owner, name)

        if kind == "twin":
            files = _build_twin_files(rappid, owner, name, display_name, voice_paragraph, hcg, fds)
            description = f"Planted RAPP twin — {display_name}. {voice_paragraph[:80]}"
        else:
            files = _build_neighborhood_files(rappid, kind, owner, name, display_name, purpose, hcg, fds)
            description = f"Planted RAPP {kind} — {display_name}. {purpose[:80]}"

        plan = {
            "schema":            _RESULT_SCHEMA,
            "ok":                True,
            "dry_run":           dry_run,
            "kind":              kind,
            "owner":             owner,
            "name":              name,
            "display_name":      display_name,
            "minted_rappid":     rappid,
            "minted_seed":       hcg.derive_seed(rappid),
            "incantation":       hcg.seed_to_words(hcg.derive_seed(rappid)),
            "target_repo":       f"https://github.com/{owner}/{name}",
            "files_to_create":   sorted(files.keys()),
            "file_count":        len(files),
            "description":       description,
        }

        if dry_run:
            plan["next_step"] = (
                f"Re-run with dry_run=False to actually create {owner}/{name}. "
                f"This will: (1) `gh repo create`, (2) push {len(files)} files via the contents API. "
                f"Existing repos with this name will NOT be clobbered — the agent will refuse."
            )
            return json.dumps(plan, indent=2)

        # Live planting
        if _gh_repo_exists(owner, name):
            plan["ok"] = False
            plan["error"] = f"repo {owner}/{name} already exists; refusing to clobber. Pick a different name OR use graft_neighborhood_agent."
            return json.dumps(plan, indent=2)

        ok, msg = _gh_create_repo(owner, name, description, public=True)
        if not ok:
            plan["ok"] = False
            plan["error"] = f"gh repo create failed: {msg}"
            return json.dumps(plan, indent=2)
        plan["repo_created"] = True

        # Push every file
        results = {"created": [], "failed": []}
        for path, content in files.items():
            ok, msg = _gh_put_file(owner, name, path, content,
                                    f"plant_seed_agent: {path}")
            if ok:
                results["created"].append(path)
            else:
                results["failed"].append({"path": path, "error": msg[:200]})

        plan["files_created"]   = len(results["created"])
        plan["files_failed"]    = len(results["failed"])
        if results["failed"]:
            plan["failed_paths"] = results["failed"]

        plan["live_url"]    = f"https://github.com/{owner}/{name}"
        plan["pages_url"]   = f"https://{owner}.github.io/{name}/"
        plan["holo_md_url"] = f"https://raw.githubusercontent.com/{owner}/{name}/main/holo.md"

        if register_in_metropolis and kind != "twin":
            plan["_metropolis_registration_note"] = (
                "Metropolis registration not auto-applied (operator-mediated). "
                "To register: edit pages/metropolis/index.json on kody-w/RAPP "
                "+ open a PR adding this entry."
            )

        plan["next_step"] = (
            f"Planting complete. Browse: {plan['live_url']}. "
            f"Anyone can join via vbrainstem (paste the gate URL). "
            f"Embody this seed in browser: localStorage.setItem('vbs_rappid', '{rappid}')."
        )
        return json.dumps(plan, indent=2)
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
