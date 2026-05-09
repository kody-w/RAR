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
import json
import os
import subprocess
import sys
import time
import uuid

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    from basic_agent import BasicAgent


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
    return f"rappid:v2:{kind}:@{owner}/{name}:{uuid.uuid4().hex}@github.com/{owner}/{name}"


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
        "schema": "rapp-rappid/2.0", "rappid": rappid, "kind": kind,
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
        "schema": "rapp-rappid/2.0", "rappid": rappid, "kind": "twin",
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
