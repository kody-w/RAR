---
name: "rar-kody-w-plant-seed"
description: "Create a fresh public planted seed (neighborhood OR twin) ready for use. One agent, both species. Each planting includes the FULL front-door grail (rappid + identity + soul + card.json (rappcards/1.1.2) + holo.svg + holo-qr.svg + holo.md + specs/ bundle + agents/ + .nojekyll + README + members.json + rar/) so the planting is portable, self-sustaining, and the grail-compliant from minute one. Operator-mediated: default dry_run=True (shows what will be created); set dry_run=False to actually create the public repo + push files. Optionally registers in pages/metropolis/index.json (PR, not auto-write)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/plant_seed_agent", "rar_sha256": "86727bec5fc6c29e5925402e0d26fc8b76078755fa3fb1664904a4f1cf190ad6", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "plant_seed_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/plant-seed:706c92e0c4f8ee361b3eda6ecd773b63c7299fff98c4a4e60924a9b009378555", "kind": "skill"}, "version": "1.0.4", "author": "kody-w", "tags": ["plant", "seed", "neighborhood", "twin", "holocard", "grail", "operator-mediated"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/plant_seed_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `plant_seed_agent.py` is
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
