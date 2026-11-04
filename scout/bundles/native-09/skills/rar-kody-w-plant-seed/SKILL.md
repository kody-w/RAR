---
name: "rar-kody-w-plant-seed"
description: "Create a fresh public planted seed (neighborhood OR twin) ready for use. One agent, both species. Each planting includes the FULL front-door grail (rappid + identity + soul + card.json (rappcards/1.1.2) + holo.svg + holo-qr.svg + holo.md + specs/ bundle + agents/ + .nojekyll + README + members.json + rar/) so the planting is portable, self-sustaining, and the grail-compliant from minute one. Operator-mediated: default dry_run=True (shows what will be created); set dry_run=False to actually create the public repo + push files. Optionally registers in pages/metropolis/index.json (PR, not auto-write)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/plant_seed_agent", "rar_sha256": "9a7f94b9461517e0bf9a6c4fdb12c8450d53b34307ce36dac3bae576ed178a06", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.4", "author": "kody-w", "tags": ["plant", "seed", "neighborhood", "twin", "holocard", "grail", "operator-mediated"]}
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
