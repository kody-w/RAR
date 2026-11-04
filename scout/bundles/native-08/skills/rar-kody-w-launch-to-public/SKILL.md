---
name: "rar-kody-w-launch-to-public"
description: "Snapshot a local brainstem's current state and launch it as a public repo (or graft into an existing one) so any cloud AI / brainstem can fetch from raw.githubusercontent.com and resume the work autonomously. Mirrors the ultraplan handoff pattern: local\u2192global launch with a continuation manifest. The inverse of rar_loader/graft (global\u2192local). Default dry_run=True."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/launch_to_public_agent", "rar_sha256": "15f570244d281c16313f2711c180910bd839fce61609a37545358e63b7c1ea24", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.5", "author": "kody-w", "tags": ["launch", "publish", "local-to-global", "bond-technique", "operator-mediated", "platform"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/launch_to_public_agent`. The original RAPP
agent is preserved byte-for-byte in `launch_to_public_agent.py` and in the RCI capsule.

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

launch_to_public_agent — snapshot a local brainstem and launch it as a public repo.

The **inverse direction** of the global→local pattern. So far the stack
has shipped:

    rar_loader  / graft_neighborhood   →  GLOBAL → LOCAL
       (hot-load required agents)         (overlay public onto local repo)

This agent ships the missing direction:

    Launch  →  LOCAL → GLOBAL
       (snapshot the local brainstem's evolving state, plant it as a
        public repo with a continuation manifest, hand off to any cloud
        AI / brainstem to resume autonomously via raw.githubusercontent.com)

Mirrors the **ultraplan handoff pattern**: operator runs a thing
locally, hands the state off (with continuation instructions) to a
cloud session, work continues autonomously, results come back via the
shared substrate (GitHub).

How it works:

    1. Pack the local organism via bond.py::pack_organism — same egg
       schema (brainstem-egg/2.2-organism) used everywhere else.
    2. Compute a launch FINGERPRINT (rappid + sha256 of egg + utc) —
       the content-addressed handoff identity.
    3. Build a `rapp-launch-continuation/1.0` manifest — the markdown
       any cloud AI ingests to know what to do next.
    4. Plant or graft to target_repo (the existing graft agent's bond
       technique guarantees blind-safe additive overlay).
    5. Commit data/launch.egg + LAUNCH_CONTINUATION.md + the
       fingerprint at root.
    6. Optionally enable Pages so the gate is reachable.
    7. Return a handoff envelope including:
         - public gate URL
         - raw URL of the launch egg + continuation manifest
         - resume one-liner
         - sha256 fingerprint for verification

Default `dry_run=True` (safety — never forks/pushes by default).

Schema: `rapp-launch-result/1.0`. Bond event kind: "launch".

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "_local_brainstem_dir": {
      "description": "(test-only) treat this dir as both home + src for the snapshot.",
      "type": "string"
    },
    "_local_target_dir": {
      "description": "(test-only) graft into this local dir instead of fork+clone.",
      "type": "string"
    },
    "_skip_push": {
      "description": "(test-only) build locally but skip git push.",
      "type": "boolean"
    },
    "_workspace_dir": {
      "description": "(test-only) persistent workspace for inspection.",
      "type": "string"
    },
    "brainstem_home": {
      "description": "~/.brainstem (default). Where rappid.json + bonds.json live.",
      "type": "string"
    },
    "brainstem_src": {
      "description": "rapp_brainstem src dir (default: ~/.brainstem/src/rapp_brainstem).",
      "type": "string"
    },
    "dry_run": {
      "default": true,
      "type": "boolean"
    },
    "entry_point": {
      "description": "First action the resumer should take (one sentence).",
      "type": "string"
    },
    "instructions": {
      "description": "Markdown text \u2014 the continuation instructions any cloud AI will ingest to know what to do next.",
      "type": "string"
    },
    "kernel_version": {
      "default": "0.6.0",
      "type": "string"
    },
    "kind": {
      "default": "neighborhood",
      "type": "string"
    },
    "neighborhood_name": {
      "description": "Display name for the launched neighborhood. Defaults to repo name.",
      "type": "string"
    },
    "target_repo": {
      "description": "<owner>/<repo> destination. New repo created if absent; existing repo gets bond-technique additive graft.",
      "type": "string"
    },
    "verification_steps": {
      "description": "Optional override of the default verification checklist.",
      "items": {
        "type": "string"
      },
      "type": "array"
    }
  },
  "required": [
    "target_repo",
    "instructions"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `launch_to_public_agent.py` and embedded as the fenced Python below (sha256 15f570244d281c16…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `launch_to_public_agent.py` first:

```bash
python3 launch_to_public_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 launch_to_public_agent.py   # or on stdin
python3 launch_to_public_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/ecosystem-grail-stack/launch_to_public_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/launch_to_public_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/launch_to_public_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""launch_to_public_agent — snapshot a local brainstem and launch it as a public repo.

The **inverse direction** of the global→local pattern. So far the stack
has shipped:

    rar_loader  / graft_neighborhood   →  GLOBAL → LOCAL
       (hot-load required agents)         (overlay public onto local repo)

This agent ships the missing direction:

    Launch  →  LOCAL → GLOBAL
       (snapshot the local brainstem's evolving state, plant it as a
        public repo with a continuation manifest, hand off to any cloud
        AI / brainstem to resume autonomously via raw.githubusercontent.com)

Mirrors the **ultraplan handoff pattern**: operator runs a thing
locally, hands the state off (with continuation instructions) to a
cloud session, work continues autonomously, results come back via the
shared substrate (GitHub).

How it works:

    1. Pack the local organism via bond.py::pack_organism — same egg
       schema (brainstem-egg/2.2-organism) used everywhere else.
    2. Compute a launch FINGERPRINT (rappid + sha256 of egg + utc) —
       the content-addressed handoff identity.
    3. Build a `rapp-launch-continuation/1.0` manifest — the markdown
       any cloud AI ingests to know what to do next.
    4. Plant or graft to target_repo (the existing graft agent's bond
       technique guarantees blind-safe additive overlay).
    5. Commit data/launch.egg + LAUNCH_CONTINUATION.md + the
       fingerprint at root.
    6. Optionally enable Pages so the gate is reachable.
    7. Return a handoff envelope including:
         - public gate URL
         - raw URL of the launch egg + continuation manifest
         - resume one-liner
         - sha256 fingerprint for verification

Default `dry_run=True` (safety — never forks/pushes by default).

Schema: `rapp-launch-result/1.0`. Bond event kind: "launch".
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import uuid

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/launch_to_public_agent",
    "version": "1.0.5",
    "display_name": "Launch to Public",
    "description": "Snapshots the local brainstem via bond.py and plants it onto a public GitHub repo with a continuation manifest and launch fingerprint.",
    "author": "kody-w",
    "tags": [
        "launch",
        "publish",
        "local-to-global",
        "bond-technique",
        "operator-mediated",
        "platform"
    ],
    "category": "platform",
    "quality_tier": "verified",
    "requires_env": [],
    "dependencies": [
        "@rapp/basic_agent"
    ]
}

SPECIES_ROOT_RAPPID = (
    "rappid:@kody-w/rapp:"
    "9a8f0a4b5a710e20f4d819a0f37d2a4c9f113b5e78fb3c29e70b54fff48a38f9"
)
_AGENT_MANAGED_FILES = {"bonds.json"}


def _now_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def _run(cmd: list[str], cwd: str | None = None,
         check: bool = True) -> tuple[int, str, str]:
    """Run a bounded subprocess and return (status, stdout, stderr)."""
    try:
        process = subprocess.run(
            cmd, cwd=cwd, check=False, capture_output=True,
            text=True, timeout=120,
        )
    except FileNotFoundError as exc:
        raise RuntimeError(f"binary not found: {cmd[0]}") from exc
    if check and process.returncode != 0:
        detail = (process.stderr or process.stdout or "").strip()[:500]
        raise RuntimeError(f"{cmd[0]} failed (rc={process.returncode}): {detail}")
    return process.returncode, process.stdout or "", process.stderr or ""


def _sha256_file(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as source:
        for chunk in iter(lambda: source.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _walk_files(root: str) -> list[str]:
    files = []
    for current, directories, names in os.walk(root):
        directories[:] = [name for name in directories if name != ".git"]
        for name in names:
            full_path = os.path.join(current, name)
            files.append(os.path.relpath(full_path, root).replace(os.sep, "/"))
    return sorted(files)


def _snapshot_upstream(root: str) -> dict:
    snapshot = {}
    for relative_path in _walk_files(root):
        full_path = os.path.join(root, relative_path)
        snapshot[relative_path] = {
            "sha256": _sha256_file(full_path),
            "size": os.path.getsize(full_path),
        }
    return snapshot


def _verify_upstream_preserved(root: str, snapshot: dict) -> tuple[list, list]:
    preserved, clobbered = [], []
    for relative_path, metadata in snapshot.items():
        if relative_path in _AGENT_MANAGED_FILES:
            continue
        full_path = os.path.join(root, relative_path)
        if not os.path.exists(full_path):
            clobbered.append({"path": relative_path, "reason": "deleted"})
        elif _sha256_file(full_path) != metadata["sha256"]:
            clobbered.append({"path": relative_path, "reason": "modified"})
        else:
            preserved.append(relative_path)
    return preserved, clobbered


def _restore_clobbered(root: str, snapshot: dict, clobbered: list,
                       backup_root: str) -> int:
    del snapshot
    restored = 0
    for record in clobbered:
        relative_path = record["path"]
        backup_path = os.path.join(backup_root, relative_path)
        target_path = os.path.join(root, relative_path)
        if not os.path.exists(backup_path):
            continue
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        shutil.copy2(backup_path, target_path)
        restored += 1
    return restored


def _infer_agent_name(filename: str, path: str) -> str:
    try:
        with open(path, encoding="utf-8") as source:
            match = re.search(
                r'"name":\s*"([A-Za-z][A-Za-z0-9_-]*)"', source.read()
            )
        if match:
            return match.group(1)
    except OSError:
        pass
    stem = filename[:-3].removesuffix("_agent")
    return "".join(part.capitalize() for part in stem.split("_") if part) + "Agent"


def _build_rar_index(base: str, owner: str, repo: str, kind: str) -> dict:
    entries = []
    agents_dir = os.path.join(base, "agents")
    if os.path.isdir(agents_dir):
        for filename in sorted(os.listdir(agents_dir)):
            if not filename.endswith(".py"):
                continue
            path = os.path.join(agents_dir, filename)
            entries.append({
                "kind": "agent",
                "name": _infer_agent_name(filename, path),
                "file": f"agents/{filename}",
                "raw_url": (
                    f"https://raw.githubusercontent.com/{owner}/{repo}/main/"
                    f"agents/{filename}"
                ),
                "sha256": _sha256_file(path),
                "schema": "rapp-agent/1.0",
            })
    return {
        "schema": "rapp-rar-index/1.0",
        "name": repo,
        "rar_for": f"{owner}/{repo}",
        "version": "1.0",
        "created_at": _now_iso(),
        "kind": kind,
        "required_for_participation": entries,
        "optional_for_participation": [],
        "kernel_base_included": [],
        "verification": {"schema": "rapp-rar-manifest/1.0", "scheme": "sha256"},
    }


def _build_scaffolding(workspace: str, *, gh_user: str, repo_name: str,
                       neighborhood_name: str, display_name: str, kind: str,
                       upstream_repo: str, upstream_commit: str,
                       agent_files: dict[str, bytes] | None = None,
                       graft_path: str = "") -> dict:
    """Write minimum neighborhood scaffolding without replacing existing files."""
    written, skipped = [], []
    base = os.path.join(workspace, graft_path) if graft_path else workspace
    os.makedirs(base, exist_ok=True)

    def write_if_absent(relative_path: str, content: str | bytes) -> bool:
        target = os.path.join(base, relative_path)
        reported_path = f"{graft_path}/{relative_path}" if graft_path else relative_path
        if os.path.exists(target):
            skipped.append({"path": reported_path, "reason": "already_in_upstream"})
            return False
        os.makedirs(os.path.dirname(target) or base, exist_ok=True)
        if isinstance(content, bytes):
            with open(target, "wb") as destination:
                destination.write(content)
        else:
            with open(target, "w", encoding="utf-8") as destination:
                destination.write(content)
        written.append({"path": reported_path})
        return True

    # Canonical keyless mint (spec §6.2): Hb("rapp/1:rappid", uuid4). owner/slug
    # (@gh_user/repo_name) locate the door; kind lives in the rappid.json record,
    # never in the string. NEVER a hash of the name (the cardinal sin). owner/slug
    # are canonicalized to the §6.1 grammar so a real login like "Kody-W" or a
    # repo "My_Repo.v2" produces a valid (lowercase, hyphenated) rappid.
    _own = re.sub(r"[^a-z0-9]+", "-", (gh_user or "anon").lower()).strip("-") or "anon"
    _slug = re.sub(r"[^a-z0-9]+", "-", (repo_name or "x").lower()).strip("-") or "x"
    rappid = (
        f"rappid:@{_own}/{_slug}:"
        + hashlib.sha256(b"rapp/1:rappid\n" + uuid.uuid4().bytes).hexdigest()
    )
    grafted_onto = {
        "upstream_repo": upstream_repo,
        "upstream_url": f"https://github.com/{upstream_repo}",
        "upstream_commit": upstream_commit,
        "graft_mode": "additive_overlay",
        "graft_path": graft_path or "(root)",
        "grafted_at": _now_iso(),
        "bond_kind": "graft",
    }
    write_if_absent("rappid.json", json.dumps({
        "schema": "rapp/1",
        "rappid": rappid,
        "kind": kind,
        "name": neighborhood_name,
        "display_name": display_name,
        "github": f"https://github.com/{gh_user}/{repo_name}",
        "url": f"https://{gh_user}.github.io/{repo_name}",
        "parent_rappid": SPECIES_ROOT_RAPPID,
        "parent_repo": "https://github.com/kody-w/RAPP",
        "planted_by": gh_user,
        "planted_at": _now_iso(),
        "kernel_version": "0.6.0",
        "grafted_onto": grafted_onto,
    }, indent=2) + "\n")
    write_if_absent("neighborhood.json", json.dumps({
        "schema": "rapp-neighborhood/1.0",
        "name": neighborhood_name,
        "display_name": display_name,
        "kind": kind,
        "visibility": "public",
        "neighborhood_rappid": rappid,
        "gate_repo": f"{gh_user}/{repo_name}",
        "gate_url": f"https://{gh_user}.github.io/{repo_name}/",
        "members_path": "members.json",
        "join_via": "public_link",
        "rar_index_path": "rar/index.json",
        "grafted_onto": grafted_onto,
    }, indent=2) + "\n")
    write_if_absent("soul.md", (
        f"# {display_name} — Soul\n\n"
        f"You are **{display_name}**, a RAPP neighborhood layered additively "
        f"on {upstream_repo}. Preserve the upstream and its identity.\n"
    ))
    write_if_absent("card.json", json.dumps({
        "schema": "rapp-card/1.0",
        "title": display_name,
        "type_line": f"Neighborhood — Graft of {upstream_repo}",
        "abilities": [{"kw": "Bond", "text": "Additive overlay; upstream preserved."}],
    }, indent=2) + "\n")
    write_if_absent("members.json", json.dumps({
        "schema": "rapp-neighborhood-members/1.0",
        "neighborhood": f"{gh_user}/{repo_name}",
        "updated_at": _now_iso(),
        "members": [{"rappid": SPECIES_ROOT_RAPPID, "github": gh_user,
                     "role": "operator", "joined_at": _now_iso()}],
        "open_to_anyone": True,
    }, indent=2) + "\n")
    write_if_absent(".nojekyll", "")

    for relative_path, content in (agent_files or {}).items():
        write_if_absent(relative_path, content)

    rar_path = os.path.join(base, "rar", "index.json")
    if os.path.exists(rar_path):
        reported = f"{graft_path}/rar/index.json" if graft_path else "rar/index.json"
        skipped.append({"path": reported, "reason": "already_in_upstream"})
    else:
        write_if_absent(
            "rar/index.json",
            json.dumps(_build_rar_index(base, gh_user, repo_name, kind), indent=2) + "\n",
        )
    return {"written": written, "skipped": skipped, "rappid": rappid}


def _gh_fork_clone(upstream: str, destination: str) -> tuple[str, str]:
    status, stdout, stderr = _run(
        ["gh", "repo", "fork", upstream, "--clone=false"], check=False
    )
    if status != 0 and "already exists" not in (stdout + stderr).lower():
        raise RuntimeError(f"gh repo fork failed: {stderr or stdout}")
    _, login, _ = _run(["gh", "api", "user", "--jq", ".login"])
    fork = f"{login.strip() or 'anon'}/{upstream.split('/')[-1]}"
    _run(["git", "clone", "--depth", "1", f"https://github.com/{fork}.git", destination])
    _, head, _ = _run(["git", "-C", destination, "rev-parse", "HEAD"])
    return fork, head.strip()


_LAUNCH_RESULT_SCHEMA = "rapp-launch-result/1.0"
_LAUNCH_CONTINUATION_SCHEMA = "rapp-launch-continuation/1.0"


def _pack_organism_egg(brainstem_home: str, brainstem_src: str,
                       kernel_version: str = "0.6.0") -> bytes:
    """Use bond.py::pack_organism to snapshot the local organism state.

    Falls back to a minimal manual snapshot if bond.py isn't importable
    (e.g. test harness without the full kernel src tree).
    """
    try:
        # Try to use the canonical packer
        sys.path.insert(0, os.path.join(brainstem_src, "utils"))
        try:
            import bond as bond_mod  # type: ignore
            return bond_mod.pack_organism(brainstem_home, brainstem_src, kernel_version)
        finally:
            sys.path.remove(os.path.join(brainstem_src, "utils"))
    except (ImportError, FileNotFoundError, OSError):
        pass
    return _minimal_egg(brainstem_home, brainstem_src, kernel_version)


def _minimal_egg(brainstem_home: str, brainstem_src: str, kernel_version: str) -> bytes:
    """Stdlib-only fallback packer — captures rappid + soul + agents/ + .brainstem_data/."""
    import io, zipfile
    counts = {"agents": 0, "soul": 0, "rappid": 0, "data": 0}
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        rj = os.path.join(brainstem_home, "rappid.json")
        if os.path.exists(rj):
            with open(rj, "rb") as f:
                z.writestr("rappid.json", f.read())
            counts["rappid"] = 1
        soul = os.path.join(brainstem_src, "soul.md")
        if os.path.exists(soul):
            with open(soul, "rb") as f:
                z.writestr("soul.md", f.read())
            counts["soul"] = 1
        for sub_arc, sub_path in (("agents", "agents"), ("data", ".brainstem_data")):
            full_sub = os.path.join(brainstem_src, sub_path)
            if not os.path.isdir(full_sub):
                continue
            for r, _, files in os.walk(full_sub):
                for fname in files:
                    full = os.path.join(r, fname)
                    rel = os.path.relpath(full, full_sub).replace(os.sep, "/")
                    with open(full, "rb") as f:
                        z.writestr(f"{sub_arc}/{rel}", f.read())
                    counts[sub_arc] = counts.get(sub_arc, 0) + 1
        manifest = {
            "schema": "brainstem-egg/2.2-organism",
            "type": "organism",
            "exported_at": _now_iso(),
            "kernel_version": kernel_version,
            "counts": counts,
            "_minimal_egg": True,
        }
        z.writestr("manifest.json", json.dumps(manifest, indent=2))
    return buf.getvalue()


def _compute_fingerprint(egg_bytes: bytes, rappid: str) -> dict:
    """Content-addressed handoff identity for this launch."""
    h = hashlib.sha256(egg_bytes).hexdigest()
    return {
        "schema": "rapp-launch-fingerprint/1.0",
        "rappid": rappid,
        "egg_sha256": h,
        "egg_sha256_short": h[:16],
        "size_bytes": len(egg_bytes),
        "size_kb": round(len(egg_bytes) / 1024, 1),
        "computed_at": _now_iso(),
    }


def _build_continuation_manifest(*, rappid: str, target_repo: str,
                                 instructions: str, fingerprint: dict,
                                 entry_point: str = "Resume the work described in the instructions block.",
                                 verification_steps: list[str] | None = None) -> str:
    """Markdown manifest any cloud AI ingests to resume the work.

    Mirrors skill.md's "single file any AI can ingest" pattern but
    with state baked in (the launch egg) and a one-time-handoff
    intent (the continuation instructions).
    """
    raw_prefix = f"https://raw.githubusercontent.com/{target_repo}/main"
    verify = verification_steps or [
        f"Fetch {raw_prefix}/data/launch.egg and verify sha256 == `{fingerprint['egg_sha256']}`",
        f"Fetch {raw_prefix}/data/launch_fingerprint.json and confirm rappid matches",
        "Hatch the egg with `python3 -m utils.bond hatch <home> data/launch.egg`",
        "Confirm the local agents/ directory has the post-hatch contents",
    ]
    return f"""# Launch Continuation — {target_repo}

> *Schema: `{_LAUNCH_CONTINUATION_SCHEMA}`. Hand-off envelope from a
> local brainstem to any cloud AI (or another brainstem) that can fetch
> from raw.githubusercontent.com. Same primitive as a `/ultraplan`
> handoff — local context snapshotted, work continues autonomously.*

## Identity

- **Rappid:** `{rappid}`
- **Egg sha256:** `{fingerprint['egg_sha256']}`
- **Size:** {fingerprint['size_kb']} KB
- **Launched at:** {fingerprint['computed_at']}
- **Target repo:** [{target_repo}](https://github.com/{target_repo})

## Where to fetch the state

- Launch egg (binary, brainstem-egg/2.2-organism):
  `{raw_prefix}/data/launch.egg`
- Fingerprint (verification record):
  `{raw_prefix}/data/launch_fingerprint.json`
- This manifest:
  `{raw_prefix}/LAUNCH_CONTINUATION.md`

## Continuation instructions

{instructions}

## Entry point

{entry_point}

## Verification (any resumer should do these)

{chr(10).join(f"{i+1}. {step}" for i, step in enumerate(verify))}

## Resume one-liner (for a brainstem with utils/bond.py available)

```bash
# 1. Fetch the egg
curl -fsSL {raw_prefix}/data/launch.egg -o /tmp/launch.egg

# 2. Verify the fingerprint
echo "{fingerprint['egg_sha256']}  /tmp/launch.egg" | shasum -a 256 -c

# 3. Hatch it (preserves any local mutations per bond.py's additive semantics)
cd ~/.brainstem/src/rapp_brainstem && python3 -m utils.bond hatch ~/.brainstem /tmp/launch.egg

# 4. Resume — your local brainstem now has the launched state. Continue per the
#    "Continuation instructions" section above.
```

## Bond cycle semantics

This launch is the **local→global** half of the bond rhythm:

- **LOCAL → GLOBAL:** this manifest (launch_to_public_agent)
- **GLOBAL → LOCAL:** rar_loader_agent (hot-load required agents)
                       graft_neighborhood_agent (overlay public scaffolding)

Together they form a continuous bond loop: local mutations launch
upward into the public substrate; global state graft-pulls back down
into local; both directions additively, sha256-verified, append-only.

## Cross-references

- bond.py egg/hatch (the snapshot/restore primitive)
- skill.md (the read-only any-AI ingest contract)
- pages/vault/Decisions/2026-05-09 — Bond Rhythm (this loop's design note)
"""


class LaunchToPublicAgent(BasicAgent):
    metadata = {
        "name": "Launch",
        "description": (
            "Snapshot a local brainstem's current state and launch it as a "
            "public repo (or graft into an existing one) so any cloud AI / "
            "brainstem can fetch from raw.githubusercontent.com and resume "
            "the work autonomously. Mirrors the ultraplan handoff pattern: "
            "local→global launch with a continuation manifest. The inverse "
            "of rar_loader/graft (global→local). Default dry_run=True."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "target_repo": {"type": "string",
                                "description": "<owner>/<repo> destination. New repo created if absent; existing repo gets bond-technique additive graft."},
                "instructions": {"type": "string",
                                 "description": "Markdown text — the continuation instructions any cloud AI will ingest to know what to do next."},
                "brainstem_home": {"type": "string",
                                   "description": "~/.brainstem (default). Where rappid.json + bonds.json live."},
                "brainstem_src": {"type": "string",
                                  "description": "rapp_brainstem src dir (default: ~/.brainstem/src/rapp_brainstem)."},
                "kernel_version": {"type": "string", "default": "0.6.0"},
                "neighborhood_name": {"type": "string",
                                      "description": "Display name for the launched neighborhood. Defaults to repo name."},
                "kind": {"type": "string", "default": "neighborhood"},
                "entry_point": {"type": "string",
                                "description": "First action the resumer should take (one sentence)."},
                "verification_steps": {"type": "array", "items": {"type": "string"},
                                       "description": "Optional override of the default verification checklist."},
                "dry_run": {"type": "boolean", "default": True},
                "_local_brainstem_dir": {"type": "string",
                                         "description": "(test-only) treat this dir as both home + src for the snapshot."},
                "_local_target_dir": {"type": "string",
                                      "description": "(test-only) graft into this local dir instead of fork+clone."},
                "_workspace_dir": {"type": "string",
                                   "description": "(test-only) persistent workspace for inspection."},
                "_skip_push": {"type": "boolean",
                               "description": "(test-only) build locally but skip git push."},
            },
            "required": ["target_repo", "instructions"],
        },
    }

    def __init__(self):
        self.name = "Launch"

    def perform(self, **kwargs) -> str:
        target_repo = (kwargs.get("target_repo") or "").strip()
        if not target_repo or "/" not in target_repo:
            return json.dumps({"ok": False, "error": "target_repo must be <owner>/<repo>"})
        instructions = (kwargs.get("instructions") or "").strip()
        if not instructions:
            return json.dumps({"ok": False, "error": "instructions required (markdown text for the resumer)"})

        dry_run = kwargs.get("dry_run", True)
        skip_push = bool(kwargs.get("_skip_push"))
        local_brainstem = kwargs.get("_local_brainstem_dir")
        local_target = kwargs.get("_local_target_dir")
        kernel_version = kwargs.get("kernel_version") or "0.6.0"
        kind = (kwargs.get("kind") or "neighborhood").strip()
        gh_user, repo_name = target_repo.split("/", 1)
        neighborhood_name = (kwargs.get("neighborhood_name") or repo_name).strip()
        entry_point = (kwargs.get("entry_point") or "").strip() or "Resume the work described in the instructions block."
        verification_steps = kwargs.get("verification_steps")

        # Resolve local brainstem state
        if local_brainstem:
            brainstem_home = local_brainstem
            brainstem_src = local_brainstem
        else:
            brainstem_home = kwargs.get("brainstem_home") or os.path.expanduser("~/.brainstem")
            brainstem_src = kwargs.get("brainstem_src") or os.path.join(brainstem_home, "src", "rapp_brainstem")

        # Read local rappid
        rappid_path = os.path.join(brainstem_home, "rappid.json")
        rappid = None
        if os.path.exists(rappid_path):
            try:
                with open(rappid_path) as f:
                    rappid = (json.load(f) or {}).get("rappid")
            except (OSError, ValueError):
                pass
        if not rappid:
            rappid = SPECIES_ROOT_RAPPID
            rappid_note = "no local rappid.json — using species root for the launch envelope"
        else:
            rappid_note = "local rappid preserved"

        # Pack the launch egg
        try:
            egg_bytes = _pack_organism_egg(brainstem_home, brainstem_src, kernel_version)
        except (FileNotFoundError, OSError) as e:
            egg_bytes = b""
            return json.dumps({"ok": False, "error": f"failed to pack egg: {e}"})
        fingerprint = _compute_fingerprint(egg_bytes, rappid)

        # Build the continuation manifest
        continuation_md = _build_continuation_manifest(
            rappid=rappid, target_repo=target_repo,
            instructions=instructions, fingerprint=fingerprint,
            entry_point=entry_point, verification_steps=verification_steps,
        )

        # Workspace lifecycle
        persistent_workspace = kwargs.get("_workspace_dir")
        cleanup_temp = None
        if persistent_workspace:
            os.makedirs(persistent_workspace, exist_ok=True)
            work_root = persistent_workspace
        else:
            cleanup_temp = tempfile.mkdtemp(prefix="rapp-launch-")
            work_root = cleanup_temp
        workspace = os.path.join(work_root, "fork")
        backup = os.path.join(work_root, "pre_graft_backup")

        try:
            # Step 1: get the destination workspace ready
            if local_target:
                if not os.path.isdir(workspace):
                    shutil.copytree(local_target, workspace)
                fork_slug = target_repo
                upstream_commit = "(local-fixture)"
            elif dry_run:
                if not os.path.isdir(workspace):
                    os.makedirs(workspace, exist_ok=True)
                fork_slug = target_repo
                upstream_commit = "(dry-run; not fetched)"
            else:
                # Try to fork; if target doesn't exist, create it
                rc, _, err = _run(["gh", "api", f"repos/{target_repo}", "--silent"], check=False)
                if rc != 0:
                    # Create the public repo
                    _run(["gh", "repo", "create", target_repo, "--public",
                          "--description", f"Launched from local brainstem ({rappid[:24]}…) — {fingerprint['egg_sha256_short']}",
                          "--clone=false"])
                    upstream_commit = "(new-repo)"
                    _run(["git", "init", workspace])
                    _run(["git", "-C", workspace, "remote", "add", "origin",
                          f"https://github.com/{target_repo}.git"])
                else:
                    fork_slug, upstream_commit = _gh_fork_clone(target_repo, workspace)

            # Step 2: snapshot upstream (preserve-local property)
            pre_snapshot = _snapshot_upstream(workspace) if os.path.isdir(workspace) else {}
            if pre_snapshot:
                shutil.copytree(workspace, backup, dirs_exist_ok=True,
                                ignore=shutil.ignore_patterns(".git"))

            # Step 3: scaffold the neighborhood files (additive only)
            scaffold = _build_scaffolding(
                workspace, gh_user=gh_user, repo_name=repo_name,
                neighborhood_name=neighborhood_name,
                display_name=neighborhood_name, kind=kind,
                upstream_repo=target_repo, upstream_commit=upstream_commit,
                agent_files=None, graft_path="",
            )

            # Step 4: write the launch egg + fingerprint + continuation manifest
            data_dir = os.path.join(workspace, "data")
            os.makedirs(data_dir, exist_ok=True)

            launch_egg_path = os.path.join(data_dir, "launch.egg")
            if not os.path.exists(launch_egg_path):
                with open(launch_egg_path, "wb") as f:
                    f.write(egg_bytes)
                scaffold["written"].append({"path": "data/launch.egg"})
            else:
                scaffold["skipped"].append({"path": "data/launch.egg", "reason": "already_exists"})

            fingerprint_path = os.path.join(data_dir, "launch_fingerprint.json")
            if not os.path.exists(fingerprint_path):
                with open(fingerprint_path, "w", encoding="utf-8") as f:
                    json.dump(fingerprint, f, indent=2)
                    f.write("\n")
                scaffold["written"].append({"path": "data/launch_fingerprint.json"})

            cont_path = os.path.join(workspace, "LAUNCH_CONTINUATION.md")
            if not os.path.exists(cont_path):
                with open(cont_path, "w", encoding="utf-8") as f:
                    f.write(continuation_md)
                scaffold["written"].append({"path": "LAUNCH_CONTINUATION.md"})

            # Step 5: hatch-back verify
            preserved, clobbered = _verify_upstream_preserved(workspace, pre_snapshot) if pre_snapshot else ([], [])
            restored = 0
            if clobbered:
                restored = _restore_clobbered(workspace, pre_snapshot, clobbered, backup)

            # Step 6: bond event "launch"
            bond_event = None
            if not dry_run or local_target:
                bonds_path = os.path.join(workspace, "bonds.json")
                bonds = {"events": []}
                if os.path.exists(bonds_path):
                    try:
                        with open(bonds_path) as f:
                            bonds = json.load(f) or {"events": []}
                    except (OSError, ValueError):
                        bonds = {"events": []}
                bond_event = {
                    "at": _now_iso(),
                    "kind": "launch",
                    "from_brainstem_rappid": rappid,
                    "to_repo": target_repo,
                    "egg_sha256": fingerprint["egg_sha256"],
                    "egg_size_bytes": fingerprint["size_bytes"],
                    "files_added": len(scaffold["written"]),
                    "files_skipped_collision": len(scaffold["skipped"]),
                    "upstream_files_preserved": len(preserved),
                    "upstream_files_clobbered": len(clobbered),
                    "upstream_files_restored": restored,
                    "rappid_note": rappid_note,
                    "note": "Local brainstem snapshot launched as public repo handoff (rapp-launch-result/1.0).",
                }
                bonds["events"].append(bond_event)
                with open(bonds_path, "w", encoding="utf-8") as f:
                    json.dump(bonds, f, indent=2)
                    f.write("\n")

            # Step 7: commit + push
            git_commit_sha = None
            if not dry_run and not skip_push:
                _run(["git", "-C", workspace, "config", "user.email", "kody-w@users.noreply.github.com"], check=False)
                _run(["git", "-C", workspace, "config", "user.name", "Kody Wildfeuer"], check=False)
                _run(["git", "-C", workspace, "add", "-A"])
                rc, _, _ = _run(["git", "-C", workspace, "commit", "-m",
                                 f"🚀 launch local brainstem snapshot to {target_repo}\n\n"
                                 f"Egg sha256: {fingerprint['egg_sha256_short']}\n"
                                 f"Rappid: {rappid[:48]}\n"
                                 f"Bond technique: additive overlay; {len(scaffold['written'])} files added; "
                                 f"{len(scaffold['skipped'])} skipped (collision).\n\n"
                                 f"Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"],
                                check=False)
                if rc == 0:
                    rc, head, _ = _run(["git", "-C", workspace, "rev-parse", "HEAD"])
                    git_commit_sha = head.strip()
                    _run(["git", "-C", workspace, "push", "-u", "origin", "HEAD:main"])

            raw_prefix = f"https://raw.githubusercontent.com/{target_repo}/main"
            return json.dumps({
                "schema": _LAUNCH_RESULT_SCHEMA,
                "ok": True,
                "dry_run": dry_run,
                "target_repo": target_repo,
                "fingerprint": fingerprint,
                "rappid": rappid,
                "rappid_note": rappid_note,
                "handoff": {
                    "gate_url": f"https://{gh_user}.github.io/{repo_name}/",
                    "raw_egg_url": f"{raw_prefix}/data/launch.egg",
                    "raw_fingerprint_url": f"{raw_prefix}/data/launch_fingerprint.json",
                    "raw_continuation_url": f"{raw_prefix}/LAUNCH_CONTINUATION.md",
                    "resume_one_liner": (
                        f"curl -fsSL {raw_prefix}/data/launch.egg -o /tmp/launch.egg && "
                        f"echo \"{fingerprint['egg_sha256']}  /tmp/launch.egg\" | shasum -a 256 -c && "
                        "cd ~/.brainstem/src/rapp_brainstem && "
                        "python3 -m utils.bond hatch ~/.brainstem /tmp/launch.egg"
                    ),
                },
                "scaffold": scaffold,
                "bond_preserve_local": {
                    "_purpose": "Same property as graft — upstream files byte-identical post-overlay.",
                    "upstream_files_preserved": len(preserved),
                    "upstream_files_clobbered": len(clobbered),
                    "upstream_files_restored": restored,
                },
                "bond_event": bond_event,
                "git_commit_sha": git_commit_sha,
                "rhythm": {
                    "_purpose": "This is the local→global half of the bond rhythm. Pair with rar_loader / graft_neighborhood for the global→local return half. Together they form a continuous loop: local mutations launch upward; global state graft-pulls back down; both additively, sha256-verified, append-only.",
                    "this_direction": "LOCAL → GLOBAL (launch_to_public_agent)",
                    "return_direction": "GLOBAL → LOCAL (rar_loader_agent + graft_neighborhood_agent)",
                    "drift_detector": "tools/ecosystem_audit.py",
                },
                "next_step": (
                    "dry_run=True — pass dry_run=False to actually create/push to the public repo. "
                    "Then any cloud AI can fetch the LAUNCH_CONTINUATION.md and resume."
                    if dry_run else
                    f"Public handoff complete. Resume from anywhere: curl -fsSL "
                    f"{raw_prefix}/LAUNCH_CONTINUATION.md  (the manifest tells the resumer what to do)."
                ),
            }, indent=2)
        finally:
            if cleanup_temp:
                shutil.rmtree(cleanup_temp, ignore_errors=True)
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
