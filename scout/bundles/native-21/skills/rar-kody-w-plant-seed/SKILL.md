---
name: "rar-kody-w-plant-seed"
description: "Create a fresh public planted seed (neighborhood OR twin) ready for use. One agent, both species. Each planting includes the FULL front-door grail (rappid + identity + soul + card.json (rappcards/1.1.2) + holo.svg + holo-qr.svg + holo.md + specs/ bundle + agents/ + .nojekyll + README + members.json + rar/) so the planting is portable, self-sustaining, and the grail-compliant from minute one. Operator-mediated: default dry_run=True (shows what will be created); set dry_run=False to actually create the public repo + push files. Optionally registers in pages/metropolis/index.json (PR, not auto-write)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/plant_seed_agent", "rar_sha256": "86727bec5fc6c29e5925402e0d26fc8b76078755fa3fb1664904a4f1cf190ad6", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.4", "author": "kody-w", "tags": ["plant", "seed", "neighborhood", "twin", "holocard", "grail", "operator-mediated"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `plant_seed_agent.py` and embedded as the fenced Python below (sha256 86727bec5fc6c29e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `plant_seed_agent.py` first:

```bash
python3 plant_seed_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 plant_seed_agent.py   # or on stdin
python3 plant_seed_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
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
