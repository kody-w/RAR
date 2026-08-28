---
name: "rar-kody-w-launch-to-public"
description: "Snapshot a local brainstem's current state and launch it as a public repo (or graft into an existing one) so any cloud AI / brainstem can fetch from raw.githubusercontent.com and resume the work autonomously. Mirrors the ultraplan handoff pattern: local\u2192global launch with a continuation manifest. The inverse of rar_loader/graft (global\u2192local). Default dry_run=True."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/launch_to_public_agent", "rar_sha256": "857168ad0d4421f9099e93a63c4805ad22e229c31526b4d1cab37f9548fdff0e", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.5", "author": "kody-w", "tags": ["launch", "publish", "local-to-global", "bond-technique", "operator-mediated", "platform"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `launch_to_public_agent.py` and embedded as the fenced Python below (sha256 857168ad0d4421f9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `launch_to_public_agent.py` first:

```bash
python3 launch_to_public_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 launch_to_public_agent.py   # or on stdin
python3 launch_to_public_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/9S8ebeiSrYv+lV8eca4lVlmLqQTyDp5xgURUekURKWyxtr0IK00Iuy732d/ga7G1eXedc795+UYVRshYkbEbH9zRsT6/ZNZV0FWfPr+Kcqc9lvz6esnxy3tIsyrMEvBazU18zLIqoE5iDPbjAdWYYZpWbnJ38qBXReFm1aDsjIrd2CmziA269QOBiFoX4IueW3FoT0o3DwbfM6KgV+YXjUI0yoDrQfuOSyrMPUHWep+GZT9u3Zgx1ntDOj5AHoeamCD1p5bAcpekSWDwmzu/LAKaqsu3cLO0grM4s4GX/o5FG5ZJ+6gCtxBkxXRACwxS7Mkq8u4vRuIYVFkRXn5XMdVYeYxIB6AjpnnDXKzqtwi/X5d7M8agSnEjzMLLPxhaQ0YF6ysHzRMa7Nn0yAx09Bzy+puoAGqYXpyi9IdZB6YaHEfZ6bjFtB16Z+vxK6EL2N8uRuwrmeCqQycor0v6vSHVtTuHZCEezaTPHbLT9//+a+vn0Lw/On775/s2CzBq0/CZT5aplx4TPuABaAPWIwPPuYtEGsKfudu4WVFAl45Llje9dfn0o29r4O//z1qzMIvvwy+/ReQYfH9Zzp4+FeB9251fxHcj8Hna7s78Orzz083335++jIAYv35CTzcAQph/vnLM5HQG6RAc25pXRpDPz9dPoTp7beb0ft/hVvVRTo4lFl659RJXn7+/eenLPr56fuAM+PS/QoIub0o+zcvJjVI6rIaWO7gP7MmdYv/gv6zf/tfPz/9cTs3oFhFbffiK9+s8PbjX1ribYf/2TpezKtwj3VYuM7gc2IWkQOWM6jcczUAMrzo71XTiy/XpT2P+6BIYF0vlvXw+uenr4NexW6WUUZhfp/XZQC6WFkWv2TH/dNnwIObXhf9vX+20lfD3b/6fu+EYJFv+l8l90HnB7G+7hkBG3Xj+97Oevt71ffl1ycBju7GdyMgx2cqIfAWr2Xfv3zqkrqhH1hZEWSZ8678/eC+d0FfLy7uPjWB3/lxq9R3ZR6HPVmo5zp80/OW9GPHlzN50+JhWk9DvTMf4ASAkPMMuNg39G6+vafU1xfrV87zGg0soIO9tV68242CWkBK0d0tTwHTQy+0L37xHkg9L19L522Li2ifSfzHAEwii0/u64hzjTMvjO+Vir2yvWfVC7ILg181/6h1Wdi/auwCs/2zkV4s+eXXB+Zn5R2INsGde85B8Om1CLT8f6G75wFvNf69CX4wBvj4aogDkPnnl5Po3c6lYf8AgmB+/3Lcl+IwnQdZ9C1D5/nj9fd9PwqY0J+Md21817vCF2u7vgf9JQAEXoj3mUcAKZSfb0b78koAQLVfven/XYJ1lrvpi649NvHeaf1iLp8vHrsP3p+9CzN//+PLA6sfmPBaPO7ZdnMQ4mV12vvzrwPdjGv38vzlndFyEMbfBJIr6dch5HFOqjKdzKfq/VqWtfs1rShz9r2W94BSr4PAhWQv5HZh/QCAjxGMDeqyh15l7tqhC0JNlj3HlQeo4wIgEwPu3dr3O7r/etDbEQc5iFFucXKdnsitUimmHb0YzPdv4McbaYLP91Zbub07AVK0o/us8AHsKpN78OmNsr2whq+v4sWtv3yQGRfGrpRVXFanzoP0HsR40Rb3F7Oxei/6P4j53s9PngmGdwYAFfcr66l/H/zu/vESsXhAXG6RF1fXfg/Qbl5X7v3N689P0/r6wP5XhszUYexcmP4ufH1uevv5PulV797q+96//PDQ7/N7+vDj+p+vt9Hwx83z15edbsPKj9sfX28X/uPm+RWBm+j24+b56zsR6cfbVzfEXvFsC6JgCcQCFBUs1m7t+MZF5b1ClX32cd88tXuNZJ6+vIExgJaZ1vk90NP8Pff3HvlXmgg8ZGJGLqBcfn6v+ddrlnWfRT9eYb6LfwTN7i+m/+PdwX5p969m3//HA3p8l0RO//wZmL4Xnn9c/eW3q5l/e+M1b6dwS/G51S1nX0SYp669PQHfFb0gbgFTqvNf9gEzvL/kZffXxq8i31sv9B8DFWjLAP4+6CFrb0gAHwGDuNrR80QLEDHbVwruvcC77wSEhxDwON2wBEL9/ETzywcBqwzqKoxB8gtSvsJ1P98O8vV5Sl/e9u45dl/Gtf8Ssr5tWOfAHF0z6X1OElYXJ38d5xsQMHB1gPorD+gCY3lMQ/6vLfVW1/+igv/P1wkW8Q0s4h+XCV9qEK7zznLfWMdVXbSi7d16P4V/9Kt+SHaczC3Tv1XXqX8d2GBUEDzD6i2JPnrdgzUWRe+EwUQ+//PnJz+44jYzD/sHEEH6BZXQ7zfL++Pa5Nu3Ethkj/j/BcYJXDv6cQlBX94VCoCV/8+PwegD/v/HYHKdaK/4N6Wd91u/nuy1XtA/XZfbP9/Gg8tkr1TBp/dpXv/1DW+qVA8suNZDQBi9lIhepw6ff7/Go39+R7B//dFDIGT85REK/X4TVv75tz6KloGJ4GPwn6yo/vavP/7ChOwYeO8fXs9bwOsv7zd/V8NSt/nWc+CNVr3hJFCQCwPD9Pr0ZAQfjfem57fJi35XuSTZVRpAoRzn+pAVoR+mf7JswPSgqvLyOwRdq3F9Ce6lEt5dRn5veh+YzAuD/foOw+5Byn1pcGH45xcadOvt3nXcyPdB+VjQfCQ9+PyIUb9dlSYvAOYtqvbVpPtg8dQZzOPx+f6R0I0Du81dXju3y8pBNvEmPNwO8A5nXjv6GyFeo9fXQe8Z71+4w1/K72FkP80K98cD+euv+4c6aAnwy1WEXz5iKQpYapuelz0gy9uqxaDHA+XgM1CrsApBQp+l8Wu2PnV+wpiPb4BNfn4npXte9kPx5cfbIsyPp6d3GPCmrvLjzZt3ejlhmcdm+1GHSzHpR/9/X38RWN6A4NcK/uPV73eImX2l9/7C2R89Yvx6rapfUtsffS7yqs9HgsO+D5oifPDmz0nYYPgi0xj+Wapw4Y1ZmT24fQ9sPfmZvtEb9Hcb0h+pvI3oL/tc59qnfe/WHZ7JgFT00vSuzy1fj/wKgjxUGF7R/vLLmsKrxv2AjdWXXn5RX/DuLkx/TtXecY2PBgAcd98YQHLgQu9A+HJTp88k+8Gu1eJ+rdDtIv/48peAyc0IfW0379PzvzjCNWSYlxpO38CML2D36nbK15XoV4nrXxTYbVL7tlz0sfRej/Rr8b1ufZFfv0A3tbPe+wBrqivvG/knIn1K828pAkjyFSS1DrDVH8iXX+sCMNqfb5f439aEd7j3Vii9Vb8rjRc2K9AbacLfT2RJm0sbWpvL0l3i/EVpPA3xazE8Nfvv8v+Rja+KFv8jdn608D8+8qb490FgguTgWx+LrzWH9g1+uFbCvvZ7nJbl9hs7IOhd2z6hiPundreiuMUGX16DhSui+PxPgPD/+RpqAWJVdh1p9EZoT/N4h7M3He8fnu+f2n80tZulPaKSjxg2/j6wstQZuKd+B/nR8l9D4L7J/bXJ6/rIjeI97ndlxZ/l2D298s/1/tLsfc/zRAUQACpzmVvZK80///XHuznVK6t4nsFHae77pey3hnND6Vfm8XrSb+raf7qI/0Zx+9/n1AtJ//4+RRBtqp7AfZo192GZff7y9aOG12287zeK9WHTPl+82aV8rO5/fyhkftivyh72wL8PPq5rPjd/TisvVd+bjPPlt3/9mkLYuVfg8JbK7bePqVyQ4z2A5O5lkTHQpHf94pc/ofAAHABQjePwutH6htozuPiY2pPju5K92TC4knt68ZdJPPmgRxJPL/4yiUfvd1GDh+cP+95sgDyrzeXnh10e24JI83qP89Gpx4/1DGDbt+doHo+qfL4tq/YnAeIKgu9GX+7eVfUPLK7857NhPkXCZ1P88qvA/ex//ufI6ULrv4eZ3o0uxPfBQ8VgOLgcXHjRCGS0D/lVb3V/JbL054r6308nId5Z0V8ptgCM4oUPKLrPWe/cxAzj6+/rCaz/3b8u7/osPI/bu+fCyl+o4P23ZnA9WdD/XIIJDLYgBffc2i3+L433VFL6Rr9fCHqocN7f1jd/Of9ebg+fkz+pUD0Xqn7WDok64P9dcvSY7cYfmV6VDV6WUoGW9dr214aagiT66sy//4XK4l+nu77uDQ+eKpkY+W/1Z3q4Vbl2kIbH2v0+eK7KAAgam+0/Br+/cN9/e4gFf/vXlz8eKjmXqPGPwV8d8RW9h2hwoffwPPj8FD6A4/q32DzJvtGXw4uu841pvw8mQKqOO5CBdQ6wO2LwGRYvWY57Boj5Px/s6X+baRUUWR7avUn918dx8kWu9BfK5j8+Lpv3Ch6AHPmv63jhnr7lZlE+2CU/pdmPa8pvnFk/1tuTQf+u3V6Pe10+1q9qwg9T+g5cV3qd1+sN4Ob+uvkHZnNTJP7w2ObLmjF0pfvnW+rp27haAlkl5gUjPqRw66m6EbR7dcJPRfrre32uG/MfVEtvTs19f4wG7zZ7cSryzxBhj6Ge/MIrIPdu878ASv9NHALEcgUSfdMP8bZvVu59XcQPBxUeJfn7Q8n1j8f4FGbQ70811z+gX6DtXjl6P/hM9PdnffkDeltv+hWh2xLOnxN8pzDyS+ovCgofkP+oUPAx4csBu3sAOO7jMHUvR0A+f+yDwHg2GHrwzStVYfArVg2+ZQOoSvLbV//rf/3SVwPiIBxkg58/wao+iFQgRg1e0+3bD/5PH+TAWgbfzAFoN/hm/9lwYCnO4PaEG1QWNvTy8Nmf07gebUYH35JBv2NR3l3KCJfiywvibyb9AdX3coI/vr7vXK6RrBfZ4/O7DS8A+jFvuZ5k/aWVAURZ5Fn5kBGo/WHQx02oHj5fj44/Htt63La6RuQ+3fsW9pA5vOxdZWX17SGe3/1CC///nHT98THPL0lL3/3517uNX8bMvsPLN++71wBoXvJvCFILwnIQXq8avL1PEJix198R6L9eVPhK/26gmGFxTbOerw8MoIddnpfbaw/n9d5cKngMl/0YdwMtA6EocC9t275T8nyBIQNoKc6y/OHGwyCpK/N6tvcBJNd5YxYA8z3M+nrV4zKXb3kdx+WlzDfoz6b/AyyjvxvxACvj9usDDP52PW/V1wSvGea3fh/wV+pZAc71WwKuXYWPGw2CPKGFwXWRg5kgM+DX4xZMld1fU+T7y+7Yl1/6354zr4k/0Hugfh3q8zP7r2RBLvlWCH8+ogMWX907LoDe1dN1hSyLS8i1s7K9FJ0AdA2ru7x9P3d/Vx1TAGwvh9d+EUGe0MtlJ+3RhfQnT58um1xgbZ/xmHZVm3HcPpxGgS7XAcD7V4c97j50z73Cu+nLSzzPF3d6Mu8Hy5tLO3cf0X4+TXQpdn9QG/j56XoZ5qlG0h+SjAHj7wYP59ovZ0PADBtgDiAFugmtH4381wL+YPC5X+Dj9ihIs3rTuLmjMWhAhOrZ6WRf3l3lay/5x7ulEBCkexl9f6eU/3x07uPDA0VyOTpw2/jrwwGA+8uB1PK65frpj68vbqJ8+v7pP/5jIIZ2kZUZiEWqndXVAEijChO3h/+3rg5kL/1RQit2H9qBWHa4Glvv737739dCB/S+7f52vUR1TTaAw+mPOf9Mr/YHBngKTNfIB5zZt/6hv53w2/sEgVX9dlGxhwsM60mvlnlZx0DdwNS3vdJeJ2pfLqW5dl093j24BKb+YMH1QkLvl/rUNY4HVweSFe1VfS/H3H6mv/32m2X25aZHlHI9pVRCoMHTdAbfvvXaFAMnUv1MLwjsb7//8TeAqH7V60K8H0PpzffKaDDDhSpLA5BsACVLq/JyjrY/rt8z+vc/HpgJyACk+XAS1n0ISGEagVD7wFmVp7/1IM5yAUcBN5M8Ky5X84BXGswv203X+V58QFH1l/sCgDUGjts7dDe1W0DVBMt54uSlXAZiSemBQFCX13MGvz3X2W3Q/LeBOFEGvTPsTaO37svhZDPN0h7OPMn9+r7POP5WDphHEncDqVc14M8AhgwK82EMz7zKBQTHx+69exukbvMz7W/RuT2rLlHuyh7QCHDGfhDpt17ml+qh2e9dPIx9aQPcogOiqQkGL36m5YNOm0UvCrtHXe3Ar0PHTG33Hw8qVQZZHV+OwXvXAPwoBedBKhcdfF9zH/11+eEdzD+5c3l3NU138Pe/P15KfIp7f//7I/h4ix4eTv/cDdQMcPM6bRD47ehnCiA/WNOldvP9Me+/gSnv45TBY2AdvBNnn5zVZ7DEbz2d53tvFzaUX57c2OcHaPu4yKyX7CPi6U/QPbqiK//6iV61PQnLy3WHp+U/Tf56bPB5hu/AjOcZPlcIA/ed+7DuCXiJy62KHiV9HfRXS6tHwdycGr+p5v/qOunXSxwb9IGsurkc+0zo1S3Z3oSuYe72yuvgFJof35i9sOz2Tuzf//7hrdi///17X/kHZtDfQqvTXtuAR0x9oMA9L3rEF1yM5kFhKvcy+c+XRb5Y4m1w+XJZ3c/0ChpKt+yrgddq1GOnvvR4s6SLQwbTLHszda8ItF8lGBaYZWD2qlPWFhiin8LnWVjxtfXlYg181vQCuZS6nnQAvru5jnKR6uPlkgvZHp0DB/z9+4t7J0/W2adrt7dXrjWowfOdlG/gK4TcId8eu37pXdll67u4IpELqLm7UkDuBpPr3Y7e3q/ayc2l2XStrOeSNni4ygTA6BVd92Z8PbdVV/bjkdanyTxe9gDi/gaQOeBbP/KjYK+JY9U+DI3ePVwRMQe/3e4u3Yqu32P67RnoPDDhCn6ud1Sfxn6BBPvqQgkkBmQdpUAIz3ho0CPZhxlgQBIXo3m6LN4j0Ju7vReY9XRx/NrkYuzA/Ho5PS/8sdANXDKID4ADfbYMop7zrTQ99031+8vDDPAL+/udo9f1leFH+HV4Vbx37umAJfZ3DR5Ij+8G8uXE8gVmu6nZQyQFzL7sL79fXPHlGHh/8dcE4dGKH3WC6AHsJaMzn2T3eDsLcNaO637X7Rb3fXv0MheSm7Xw4htwB/27xwjw4vTfn533+/boZLLU/XYtYd1+fFDKWy70aertlZve7B7vvP92m6D8BjwskE3VPqpVeonv/XHf8pKPXAoeAHNc+l4NWr1Y2/eXCvu8HQoQEPN8zKQ/FXB7JqC/ZQ+Y5IJY/ul7CtLZr5/6AubT7fr+Aj1QngSkEEXZX75/KMuE7uXXezec+/cv/4TC58rtizL90ddBX+6orjCyPy9pltec+XJpFBh0YT/l9I+hpp9i1eb9nPqafur32PzN7ehfj3rzZxcuQ199XD+BG7jYc3l4OVT9/pBPW5+/HutyhnfwEA/Ar+ueaV9fuWzE3tDuL5qDPORC/MUdqV8P8HxP6ebCTc81sJb8GtzfXcDLK4Jvx3hRO/z8pGOD7cVB316gHA6ezwcBHH1y/2Q8INa3w70qe/ai7wXyOPD3PyuUfnl30Adrug53IfTpe9XvbLzD9Jtbcm+nx4UF8O7mFeHe5rEPgLYyIxBZgbKAgN1HF9t9f0Ivs8jXo4gv/qzBTSz5ECy8DCpNn4ldI8uHgeW9Wb28D/qCW9c/E/BuJ+A8Xja9Bbnv9XhzTPwtB9jrsfLB5S8AvLx/C+L0LYGnvxNSXoEeCIZ9p3fXdxMx3w758s9i3N5g6xOq5kr6WgRy+tKCafUi/sdz1L00APSvEffbc6R9iqkXh/PuzN5evXw7wccgeQnNBcAoj3HqgfMvgsl1dzYGU+vHC4FlXCi+Zcn1hVkUZvvpD/DiMcn49P2fL/j1Smf/9dQ1s/oqRk8LSKy6/lWV3z+B2GD2SOEhOjwUOi4GXnwr+xywD0OAap8lXZAK+PbrEshD42skBa1JnIDHpOmMHAxDYI8aUZRLoeYYtTFyhJsOgrgIQtkojCNjC3Ng27RQwqNwjPQczxu5gF6Z1QVwrtcKd6/kyNiDSQsbUaiLuvaIsBEPxSnHocYwiaGkO0JG5si66XrV/suqrpPsefhUjelX/7C43z9ZYwy05LFyTl//TSBKpxBcsNaF4MvEMOT8zKPVkUrM8MWpYtgA0Y0yWPNxoKrKHOsIHZsvxGmCTli6MXXLYai6kxTcZxSimkBEdSq9YZt2jFcuEjyGV/o2WAn76DRuQmJiMsdjWxbLtuyWnZjLDr51uoiE9Q1HzZJku8uVeXaKinMCQR3vIY7OJ8Ojrs+6ZLbjFJHYF/NOOy2PmrQ/dYwrUttVcVoih0lNiC2y1oK9wtSxNTlknQqpZXbc7+uRJhvwtl7z6/F5Xwa5u0s0ThCJ4XANQe2GO2FFLreHc2Q1NXKYVsdNtTtD/LKh64O+rOAyKvVInLFNgXXCcnIK1/q8lZL9zrDaMuvOCwE2uyxu9PNqadJcN/PS4jzOHF4YHroQdhWeQPzuxCpBl0hTmvaHkD3bcGWTpCtdVFJFaNizIBHL7VrHdys/xOgVm84Yk9yOp7vNZl9Q8lE9yYJTYBPs7No601RNthnaPuBuVrgT8RgOJWS50B3OyQAFFYfFRLWEucUwXhRP+ZGB8LpZIEyMZwyVHOzzvNS2toHV0Thzy2BT74vZFFcDX7GcMg120qrkcIo5Z0iLYdUk0Y5xlAoz4jgPITBNKd6ipn4uaBseTrmDpIlJmOW2RvvqwT/B0SROKbkVprmcLuXD4ngSZtIsKXdcVrpnfn2WttZi3hZZrcYbRIY49bRfYuw8khHcCbZRiB4DhkXNvTCjGNYpQ95sUCHs6P1IgPdxya45JdF2612UD1tVF41R0GmzYon6ioiPmCE1FffOmqn2x/XGzBPGF336hCumh5TJakcT4nBpwg0fcO2C08gFsj2VaIjHGx2jx2YJr4xGH6qCbU1cjdXUJTw5mY42FVP9bLeLbYYfq4jXJK+wN/NdhisNJa8JZt/MlWYynIh5RQF8PdfqrbGdMjI9MuZDgTL3TDCT8T1ODj0o1aLOPaHdGRruCbycTCxH5Gt67fF5M4TO8mhByhyxIUl2PT2Eviauw65eck3tczR25LqF0yjyCD0t1gTmlUFrSXtueKa6Ax3OSXKUO0ePmbsn2CtVTk6FtbqLsVMo5x67LPHpwVdlX9jrRV3FbKRCu3IDe3G0EabkEOa7hhkxYyQoaLVd2eV048RnZ8E7M4TkZzY+lUzYCi2XUczWYhf2jN8cFgq+jCAIzSaNWc/V+cSiBWJCkOU2C3OHHombsHDEAptuaoGeD6FIDIfrbL8P+B1pBIrirqeex2cx7irpaKvsCJikoC4WMMhVdhAsxs2BMnjuLDBCOtviS13e01F7EujsXKoUSyVHNhdFpzHmZJpsFjaTrAJuw3HjYp5MJrs2VN0ComECCvRWwiJHV5KSwdtmPV9167SUTTZXZuVWlI0psRshUbKc0grR4tluODntCSVfTnYsrac4pcFM6NRrOieT1TSYnpeQgforHh2qcMDOZ+OxJttTu2MxUU9n5XRnDEdb/LBhNpo01DVv7gYTt1SFUSyV+XmBsLsWOZKmmelFddwKu4BHl9TJ3FSSJhHRFh9i08LfITSNckumAV2pvbu0KXHJ4GjCNta8hMN2GfvwStpHYXzE0PUqFWLX4bR9sPUxDmNqb7eMqpSsTyfOPk+8CXYcmrGIL50j7KzzvMDgcgQb3Wx2OqqORa25qNmahnHMi9QkdHxsLDhMYnZbAj8GyyG0oAUDncWHNF0PfYek6NBjF3OFBM63HHojzI+XVoNOoOOYXa21hbRyTU2KJMpTMUaR6XC6Po0zfERlFumtMJWlqKEHR2V1VIpSL+PIhNdZQ0/2jUtPtfGmOzs5s/EEKRdW50UkuBAJYgpfRUnu5oWqlFJs2W6wLWJpF1PbiKQmxnY8axYYTJsaSgpsQI7r4zIirTTbrGTtKOkbdeGmjNW6a9jTFXakzUa7dg+xlJ8EmyBRTPZ4qIPgbG0qKLBEc7lK0hM+5clt6AicsIea6hBN2nq/dStll4+EasJ2Rmxz8mY71e3qLNSQhE5nzEja5E0sHWZUyjgbTY593d9ok6UxLhwni2SjOZKdes5PGFVW3B4bbZluRvNbCLhQ0lNSopVQEEooFR+TwwM8HtoQHSrjfeiPx62pdhBbBIoHn7IE2gUEzyJ7BRtT8iFXNGy4Zc+OnaKkxrdQ5Qkb4sBA0glAmZRCbCUaD4e7kqi70RBSLWycHmCyBA6GRxsHhajxcD9CJ7S1zvChe+KbHeR12WLXYeKuGEPiVqsIXwglQw/Zk0efV/x8Hu8Z0dnFnMnxBLt2xqwacvDWPswkuUumwehEYnzlgSlkIbTLQnJLCDgunU4BTpY764TGLFoboaYik9V8zoXuQYHbSeMzu6PYMGfg7zsT8mWeAikXbvtAO2JIEutlplCyNbTppbibWeepv8n3sD1KVHJMK3tvn0A42lXT6cwLk8aRIv2gNmsf2Fcw40MkxY7LDOY8w+ZohKHNLcVOl5tsp03UUzxNjiUtSls/0EKPi/mpYyH+bIMGp5bnPSUbMemIP5Ura1raDTfxSYelxYOFwWP6QIr6VEEiWNEyyJJ8jpoGQrPcHLbxaEdxM2duByxs8Yfd3D+rdAIsmV5NstYajvI6dvVzPTMa1qbnsMtrNi3m6XloE8KQmXAzehXy2mLkupO1Pd4tWfvE+SkhwBKC0mNElTMAEXZnQ5dkTVq31cRuFmgXuiu+1Yji7BPKohkqBxKC5+pZY6j5whBGdJFOqVMdHio696V1s06yTiqrIboKjd1Zn00UvI3T3RGj13yYDLe0UcyDolshrcpNWYZdzvfdLvJ2rczuYzfiSNxZQ5NDTjKwM6OFRd6mhbZZC3B4SopWhRlotcjS3IC4MRVNHFpwp+FeFdB2RS89JhIROglkNtL87d4SGVaFzhODYdgTN4x3nZ+iLayMoQOxmCdbJckQYdPpSqXzgrdnlgZ+jl2ZnKFLseSldokKma8x8myNodwGC8fz5VQLwbxYfZZTUhdMQyqc0NSElyjVmsfKap+IFHskMUJC/KSmJtkiQraaYXAqv9/TKMtoQ/60XhWhKi+ldLXsWBJrGXYqRtV4l9pZ1ABoSR98gBFCmkMnSMdI5XaysbYScubOQVSM6EBd74crfbOJYQOGZy19miZk5YeQKttwiiXtacQlxFkzaGO0r3bNUMJD4rTfm+Wuyn0ZmS2O4XaaCrY4VKhaX/qwyPPueiSvEDk9Tmds5mxIaCXC8300R1gIO0vx0MCZNQbwiTrxEL2anpCSyVNjvVvNYq41+aM0mU3M2ubFk7lCuLqp6my4FqVaik6rIjJkfljYVsWErbT3HQcolr9drbBtYzuuXlBTrxZcYjfHNcQFmrnqsG62mxa6sjn6opEs9Jm1rVbybreADrZbZQJcJnt5Ei9sW4fhaLtajBOZcCo6UnGHIgCI2EpCpbGCMnTdQ6li291c7Milr06JhWn4qbHSDNhNV/gqjEZzFhNkSdNDdJyM0LyDbM9mqQyi5GaUkP6GWbJZyIpJ62RUI00jfsEIh24zS9deTB+Skrc2lLEa1em8mBl4ixQbX3eFYK9t5HM8lKeboaRg8UpKXJZmspk7hny1m8vtJplbpyPQn24bYXITIRx3VrfH3eIkzFsfTc9bgzj6JAnL9saUV5sJypzaCB91+fS0ENxoqM3zWufoIJw4jBcw4rRV9ITPMmuvRiY9pAnLhEFoxt2gqEZLBqKMs+K6Aus62k7Ed17mQW1xmiAnpJJPAlmO3MOJ3B4UkuDQobKWKD4DltgQPiZJ9ooUMTjOJ5wk0Ot4PIWxzdqSzgfyzEnVzuq2XZoaxx23I+mpqjlkFnU2lmTQKfXF5bieHo9GEYsKFLqiEIqEW+GpbCN2P+G5mkp6QNoSPa2mEPB1cUUz40loEFua3gIcRuS6zdaiS66roTCdl8TKWYdB3JEcNpyz5NSOQYDDulxSvalx2KJdpORFHQLxqma1doM1CmInfaRQKgjN6flcz4er2bKMYHO1HkLEeryvj6totkE2Zsuvpsh2Bduoud3O07bGglaMliB8ok2JbuHD0dni09Oes+lqJsrcLtSi1focy+zpIG+Crc77YwjbZRjfVN76JBPEgY6cnUVzTowJIXY+GYZrm8d5e8rGlpjNlVMsx4IF73YJkrX8yXPX2fkU8jGCnasolWCMNz0ckWsGKPpxRNHw0nIncOROaBQ750ZpJGPYWRQlZC38tbX2hSBu4lSwEE7xdlF6lvYKaeQSTyQVhkD2yDYYpXHX2k7moLirGHOiWIwCHTGsBGANo1b0UescRhQcvPNVW7TOGup2taVubZVXyYxsQX7TMhxqhrZQY2itYgYqtZipxqSzGIu+SESbsyfUsjhxlubw6FpnmwsSl2MJh5mhtB7w7Xh7mAvxfi0eV0k9FpCdDJw8tLY0c4SPUMSp/EPJmNbIGcHNMXG6uuD3LMaerG5B1uICXh+YBOmOeZfWjjrcQ15cF4eEy9jSBPxZUR1Uw4y0dUHuQO40p/CbXJx3sgPLgYnN94ESz1C5atuYHycmRvO2P5HhTT1WWUti3dV+i7ZHbn0+LiU5gHdYnBtuHvuSJQ4XfHjcMJMV3Kmaz2Tt+OBye2a3QeHtpFWmHKS6I3ezSI7BEcHD8Z6vp2OYZzYrt5lJy2VG+jR1XEQqu6rrEQmTqrQocnVfJzrPngoB8B2z6LEkNOKxVeQNk5pNZWzjY1D7Mz+Mqpbhx7OCqUPODsdb6ZiMmrBm5AWZngBGbLx0e+aKKlrJvKw3woJahStnLLo6iBMArMbt7AzgaZJiaDwru2Kk+5CDqucAMk/IlEhFLhMXk3U6PJxK22h27j5DhYW3ADDcI87ZaeidjxHZGRCUejvMTJv9CqCqKApJO50Ox6egSQPLMdk5QMsocVgmfsmMPMptpe05OgJE5i7pocgS6VRfx9JQtWiVJecZ0Z5oPBg1tbudWexKn3pplCXHqSBZ5Byxy9RD0TYIceWIb0mqXcOH8VjF0ekCnhsGva+xaH4WrImcsBnAKeE4ylRJHq40FN5lToyG/GyoSNZqr9U0PS1Pq3bvACuNUQ5A5NacdP5IRTQKEhE3k0G4c1P+kOscObKzc7rnVu15z+MghijIqmspJMG3majRU19vQQaXgajDVY4gQtKcGI4hmzkkUDD23IlCpJPhUo3P+xSjNwHt7dmxPp45EbDFUuGOa5IuOFMYpsSehlx2gSyGy+k5ONYxpKJbz8YkjTY5bj4kk8LEkQ7da92o2w5DFBWlOVNPyog7AawjU3mD7iwAECM64/Wxt1BAdoWf6+myJgVMSdURRuXlkXDa1NgUx8hIV2ek65KKmiv41CRPMWXl+0jGQv+8Cadm5zv6cQmZ7cI1V0A/OGRbUzqkgNXgwozudmguZtFiHw/JNDUtX0saFgqyOD4tC2qHrBHPne+PKroI58UhyujsyMlL2Tlu4HI71iiTHC+3h7VbOWuLGQb6yEUcVzGUJT2e0GWizethcaQXWbdMjHqMUag6wosOpEO6HW4XypjI0DOxdTFnWzcicXYzUmoWetvtG4wtyBG7iqnNKB1OYZKDm8ZADjquaKPYavgSKVlJVY5Lz2+Ig6fKimtpOCoLyTk5rQR5n+8CTiu81D02Ex7GvAqHNFFf8MKBPtqNsz/gObRQhpKzYguDRdi1oasrFNvpM8jK1MzcmfpZJoD6QZLQEYtpu2P0RmYXyQIfNQqy6Li5rq3NemOhqw5fEcTU8E4BzHECwuUFFJ+GWxc+sV6YGTJ1FA8lKa5nfHluMDiahcTKn2HjfMLKVdTwDHacLzyHpeICO29iI5pAeX04cHNmZdihd56kWRKeisV6OJoRM/ZEB36OkIpF7UwNExdtSuKC5y7mzYLMWhob5R2cbkctsZquCZQPdzDmK0yyDOCM2VHQgYrWekchsBBD1qRxasdrmy6RO4LcLA4LmhkFc2+Lp3sigskjgcv5PgzkvBilPm9MnL2K4lu6MHldJ2lI5QWn5nDeqddREc9kX8/PpwlcEFJ9CKlipZBDAcX5pWVoYbYYnaPzGfHFabySPRveNepxqblExpdWLXkTvZ5MpOPB9lYU6yUcdnCCfHVMD/PASgp/tdHYYuZUnlz5qtOSLRK4vF+F1gigo3Q0bkehZjaQQFN+kEKmcZqNbWmnHVgJIjeOPprt9GGb8XI6pOYrZwIwxi6AlYheuuEGYg/xMjvxAKZg5gzL9DA9hSpw8+c8SBfjw5hBEcma62w9mhh7zPbnW63oQNxzi5Vqdwq9CyDDPJ0BaG6ViSHk0wLTUatcjUxzz9v03ovq5WQMok1IHiku13m9ifJAh9dncURxWzI+LEs225S7JYKb8wwLp8lhYlU5za/w7fqET1fIOGXjKDLaUTpDKBWaS4K2tryx4kIYNVwhKcBnTufH6JkdzUSjyFYsutEPZD2upb02PTm8Qzqob/HrVii6sx21jd/Q440xVaqRj0jqdKJHS8XMxocILw6zfTUsahOhy6O5GSrsgRlbyjaoipHp73V7NCzE9ICON5vzigwR6ezzS3U2yYpVCdJiPiVarEJHzonvcIKE6IOTueO9MaXg0UzhXaIw9p51NEp0LmWhGmIlcmwZk7OPO5Qdl+0pBq50kqNt7Qmx19ZmqbLbIka8EYcssXS44kQzsmcHPpfMNRlwlNnI1nKJI86Km+B4eOTPcmYYFe6h9SyOqBlu4jsnHrELEDRFW2lAMhMbh7UUHYGz28TePJ83+70ackk7B4GM98/TDT/s/MNMRlnSWk8PGN+6wnhq7w6BLjhHCilz4rxuEAASPHYMa2uYZNBpDifxpkWOUSeUEc9nY2k00k88nvom2XJ1Ka0kvG6oyfzUllos4Hq1QkRKkMymni2yYtcKiLaMIVoTUKvSGx3GkmHneYUQjqpiR1dLHnUOYmZ1Oht0OyRZmpFLqwxFeumi2yvQaDVMXdnsAWBpWW4+i0t4tvbhEb0ecbNORPDgsM6mztksNSNgsEYdTuR6WXMaMsflRPWOw0hp1nEmImsy185ApchIYgrpEAhLEHrGzb47S7TFYkcaX0PzBU2qCoqVrbnYraUQovlU9DodzeZ54McQV48bc9dmJtxoZol2MMUrHY4Pa2FdtzYUpacxO4SbYYEcAi4pjF0o+gcYZYe708klcDK1KyXVDGefQs0aDUruiPhIljeH+WQ58mfHXZSoeytwW6/yShdOasLDqLmLarZnSSIxR8/4sEtgvIaGwzWNJoLEoNb5aMQz0ZVFfrY9pUN8qVUcvSyXJD4e08u9sMwM0mE3Cm2u2DO97OIEo4+JOBWRhahZ53i5QjVuyu5pi4PziFjjK44WQ3oEUK0ZEaXPKBxbbUwyJJgSc/fCOuM9bY8sZ2F8KEewn9T4ei/vgyGIVv6sYrdnUmllW/IEJdhboU7M11CzCI7KOMwSeQOiyGzTxi26ZveLzQLNScU0ohhflD5CWKnnLRh0xsJJda71sYU3s0IymqQa0l5R7MbqjDO6cbtFqXEdhbbEjVxrtAxPy82UYaDJEi+Gy1J1cuBxU2WCISNlsvJG8xSrbVXJx1PMijtG303GCjves6OMyEjDNo0pv7SHka65s12Duqcdhs+UJpQ4qhKKfZpXFBzW8rFdIDrZgDwSoAMYcbWopWC2CWc6L5fYdjQbjo9O4KDH6WnULNysPFXJ6uCkC9JN2Ll2Wg+xAzzecsISyqc6FOvTHIeMZedtxOEENaGtOVro6tjfbthVGJKs1SB0U85sy9rnm/VBpiNvMsOxZZhF5wWiNZ2F70tc2RbKoYc6cDPbHdHZtFTILKZXGXuGx8Yu4adHI/AzUraU+Qned1TQLdoJyOWtiZhPFwSlx0nNn93Cm5xt8lRmqszs5zNbpJupQJPJSlRqYl1LaujiLME29Ga8FWERwdgSwg+qKc0mPBZXZ2JDEeGuM+wlIneeK83E5pTg2qI8jWg8jaomTEZwuDhTizPQwx09Z0ZcM62GnSJh0GjU7FgjQa0MdQI5EQ1jkvmhvPPHhkudJHpP1lRVj4pTWkO26Z0bkB87pMLM6QCTFkIltYKjl5OjzJ1MtGoRe4NHJY4zNslkCYUiHWOW3amkZmbkbdQoQIDVGdDKQGG5K42dCNqrvoTkR2pzrHe1Flvcwhp5sbSh9gHL+WVYaiWa0uOm4p0I26e8DNIeaTstUYRteK1SZWeKuudGAvML3MbYzILIwNkWn83ZPWJJ4/0qjdxgyM6mDLfFOCmDM05c1lgeIOezspnItNrEkDOhgr0u6CEK8otlpswPBOke63JN0BNemRtNucZK31uGuo3RZM7Xy9V+zfvkzJGHLS6LIBM7Twk5LdjcTddTh1kMmZ03wsq0ATBxAqWCop6XhANN/D1ddcA8kzmzJTgKyniDpD3ePMoYAo+w+XgqVCjErcSF0IwUQtzKQYcON8sRXE4l2fGOe39aMFgFMowRjaRNFqEohSZ1hliwE1VaNmOoEzJU5l3imgC/nEIMW8862QtDx9s3/lFrhVjmHaLGxizIE6gMIgzZ8O2lBKE6XyzQsBG1Yo8JMNIp/M6j9BQbSjUm27MZRxfistluhWwy5qrAkFnJ43bjBWkzUlPR8IY4pe55Qol0kuAwn8Tq8lAbkT9yJlEo7jsWiqaH+Xw4D04FnQkd8J6lta/UrbpOmGOBKmYhi+hKWBkAQ0GQ55tLxKVl7sDhSY9jDsypzVoprnYWB4Ec5Rj4GHqkRmuMMeNQwJeUnSykrtAReKUtPM7urBJJ9qw9ZO1z5zaxZixnBiZmAKaKBsVxNCyMTlF7PjFhuVpxjVKsg3W2Z+rNKu2G9vRY7ANMD6ec7/ORzsp7gaqgWWFHY6aqtag0D3FuQWRIlemw29VENSfDyWaMbSdmXI6MDch68pG29MpuuUIwEVZbM1p0zXoeOsP1GasNn0UMPoV9cgny16nkmsncOu7sFiVHrXUaB+eFWJKtOh8GEglBQxFyNxETsbMCWNwyY0PTLaJJeGzS3Uww4T2+Wla7MZ6ow5rC2ZWEVrOI2APbhBbTfE0xzggJhjNrvt5OOGaLqXaFMiGIFxt/qbs2nGhmIVUTFmWA34rTtTUzHCGUNFRYWUv80AaZNt8z7YyLt0D+a+DzMn+upaYkZk7n6uco1iUzP+03h323LFx9ueW4puN8TVW5tTs7cKQe5eIZF5a1sMyPjFDuGR4bam1ui22kbRZGJ4SGvsnH1h7nOhiYX80tVHSoVyOVp3dG0pAbY2m1hhp7MxtOTTbYnmY6HGqGdz6IEbQOjsQsJ910h41lHvzvNJ46q12HByd/MVdFgk53p81hXQBMczg17izH56WPRlsd32Aphekn2ecXawu39iMVs/I1Yq5n7IIy5I2268jWnDumM5ZOrpgkdD4Khlx5ypeLKlnkBuaeonp33jSZv+GZTcJVuJJv4vQIO/4M9rN1ro+c0RKeUitTVZl9Y5h7Qw0EbQkQDXxyTURkxLm6AIk51arlwY02u/mEBISn7LiaLoJulibJeZf4ObsYRdwYNydNsFb39E6hWXarlMUht1VP8jJHMrpak8LtbDP3Gy5y5Ng0qs1quQxEgz1sqQCtMs5S8AlpW97BG07mAtnNi9Roh6pZ4os5HE13SwvaQYQVL7ZHunV5saBTjc/i6Yhjk9P6MJ8tPWFBIqnYcrGfy2OhrieUfmzxYIwxh2mU90cBNDZdi00RRENbTe028AX/eM43q3K3bSj2VFqGyNLbgifnWrXglLWjzEbx4kguMW3TruJTLrFmzPrnYncQ3VEYjg+r2QzOjnSlLqBDG529ueiVnrvxrQ22ObPcTggniS5Ga8yfsYeNdExcaE+iikKn8xEtru19B9Jdu9FmI2I9rc7WjoaAFet+5Oxao5ESLWuPc4YUybGeugXwRCuWrtWm6Zhzwvh6VKO8i+4sXuZnK0ehM1aQJG4e6KuVnrKQvTqYFc2OF2NepkmRZXlmmcWdTfBNw9NMKIfT0FKJwtJInjZgTTrw24ZRj6u5uBpNmKDKVkS8HBN7l50ON9udf2LxXBeLSR67/GnFhZ5qDJcki3BSuJ6O+WW+CNnTeknu25xZxTY2nLj8sdH3MZJiu6NyaNDl0j+S+fjYWAcj3crLaY7kVtU0xKSbbDOpXgQ5ycRChCJuyIbZOFTT2WHPj88pS7ORAGxDP4XDWRic9udqip8I3Tx0u4mO7PN1LBs5v9GH8XYtEKv55oTtI3npLO0tTtAbfq0uF/KKYBOh5LHaDMScqLbtfD4d5xp+YlJnygB3Cxv5kqj9YIXNthiuq4vzkHSnS9/hD56FghzWj80sxyfmEa0n+zHJb9hpqm5FTkFHlbhmVyiX5AuG2kidWOOeEnAwfY7j+akqVtRMFSPZZnxezo+j8LzZRN1U9UJGtVeIoVP4hKCd4sAfmKQYjnTCLvbRkd2upiCmoM52a03kND+KJlEb4ywFFrxwhuzizJgbzucTDq4F9WhT1mzkEA42IxqLptWh2G7V84GQeQ5b0uiC6mbZsiymWl75yYqfjlCunPM5knnS8aTBUUucmRO8c5x9K/Mr8aCiCwSOI51CJ6lz9gp3FIeYIhbb1RHCJhPYOqbiegxDW4QYW0dnD1Ri6+/nG8uVoCqhV3vUxoJyG6x30X6rJExGIX7DO/x2yXV7EzG3tKbAxPxYB1G7PZzP3kHndQaqYb+OvckCJjRiXnRmZLZYOh3Pc2YH5budPW1YbZGP1Wy62fkEKRoixkS6MeXig65vNDvLAoEHKHt/UjneVPahvtsshCFWr0ms3HGR2/nmuva9BhdxATvDWLRPkmovwWbFEyurwGeTOkc2zHFbDq2GOmzHSr4i9Fw2CFlO4DNYgAczkHUM57HIFMSG7rpiJen4qqgmqhlHOUTVYkMSlCTjy006SZDJOuu6lRn68mRP7Pa71RhhFBbTipb1lT16aqd14+CjJBUE25Axwa40NzsLfLs5c1p2przNEOmOhnBckIsNhCyncdTCHSkxWtstdKUknUWTjECCoVjcdE6ZJ7Xmlf0iH3HOYjYNayJj9YnFomw1JUzdaA+Mw5TzsNsSBpMIFZ00wxRewm3lYtU2Eg6sxngmrCvphj8h1XyLCezeLUJyN5TS1EEpbQ51y/GZcpjOW81GwdEpj6dQylFltknKWZEQbkkn0x3pZy4Kr4bVIWnxBmQIgVssGA6oQbb1laVv+vk632OuNS7zWB/7BAZP9bPIACgZ6qTGOo3k8jPBwpgltoKnleFGvOVmiitGE3JPs0uzI+aTxV5bkQ27GQfrYJMEY49a2NTaGKYGCQmRxihn3leG6EnKzF22ikISI4k17Oe85o8lKHTmW6NUfbUN/SCfe5PGJtQ6PrUWcMxnLm+TRZRUpmaX4lFshgyuMfqWH9dVKrB0tTJ9Ik/jrBzhimztzbUra2WRq7o+g4Ojl269uUMum2hM1CSIvkpsFahNL45jeltnbavvHG8tmba2wbxUBnn9HoI4b7LKDSKjmbHpeg7pNL4wJ1HZ05QS4DiyXhNrC8Ixd5hyJamsVHeRI8Q65afOMrH2ijIFSG23OMArgtzggFRJVMmYJroNmi51Qq739SqBZhKvOaONaCxzdoWtzpImJBwhJ7FWcdq4yortbB57gTzfmc6JLsLMMndbk3e2DkLMCGpdww6+tlxC7hZWJp9G5WbbBUBFTGUWFvJus50tQFiNazXf6iKT7obCWdJz3BPH6HxmxYqdLiOV0dudKg4pnMkUD4owSQ406TTpDGeYHfeUC6eFejSlMyG68FgE2MGuIX8/nRFjY9zOktGCJKzIX4pUvZ0lRryRDHJErFoZlneFuR0d+I2H1+phV4M1VcetU2kn56i4zKIdpWiASiPDg/xu6PuaOx87+eYM25t5R7C5ru7jCe8u5Fq3MHKKL2eUA6cNWIM8KSErwVcHFl3NbUJQ9MIyTM3auEd0lB/zEBY9yzmpzR7aAOe/oNBNHVFLgpWEwyHl8lFlLJKd559AanSmIgeAdsqY7nHLEjZZulYW2yWyUkrUXRCiRagVDwuLY5ugup9NqMxUYYIjykr0pviYauN4Aw/RBSzXdW11Zzhww3q8hAJiYuKmt1rGMXxcKyTaQiMtpMDycNxk2NYmpVSYevBYoSPBCVxFQhtvT3bidFahMNnVDYuuh2OlJqml48jV/EiaWBWZ8rAey1YGLygWJszTUnOxiaXHZ9Hd2AEUTrshvlBystwBNEe4dohn0EQ/WVjR+qK+nKo+v9VPhGwCnLhfAHOLimO86E6pYgi8hbuajhyoXUbJDkJhmxk+YtwMw+szkRA8hCgUxAwXPCI6FnxenRQkDyskTAPUO7CiINpSDJLpE2VawsyblcGmPRzRHTx05LKSJNlDpaFFyO5x6dAbhhg1Ll0J+zk3m40Z0itlzIkmkIFwiY0f544RZzm2COSVXKMg907XZ3WGpOlUVncIZOzIeL1ZQ5SHbCFz12R5zgBzUtYkAhVoODmdtiOuQSgOMquU0abLIls6R98lw+KwTmGUMzQ69qAUPXR64pz9cbk+UvCqqecoOZw0elAyZKUIoexvh01wDsWiOG1slR+tDHGFzBqMGY/P64SmLQLbOejEaZ22YStmtpvvypJRkmV3iCc5Sq6XIGdR2GW00pxcqhpqb9jORKJ2PDsqd0gkebxhDSe4lYvJUSPR6Wx6QnajVt5kU2NMpnkOHBW+Sde6V2xJLS60EVRDEMRAUMQYAVw4xbhciChQ7Wk9Zopkm/KeeUDXy0Sd64c2PqGYXFnUeNt4gZ4pckpG9RglxP2q2LncQcAJvm6nOiZFQ8sr9VIymrlqL5JJOxfa05nPVmh+LA/YaT2HCqZLVudhMiX2eyqg1/bCbXZWeBjNT4gwBCrdEhrje2fOwk4lVsBOXG7StJ7Uw3FXt+xcOZSKgyL1iVqbhLMluyXFdkgsgJgqsXu7tDML2iyUiFxOxPnu4BINPg3EpQBhKLNUPLiQyZwokG4EIfW0xOTtnDVXwl6wvc28JDljOAvO8xkV5mZamLCm7hZDQzwysEoeuhRWdlwjo6IL5eqkPBsJPFyJ0YlFFqpS++MpIawIZnzKOMqnEXZWpjgzPtQrMlnrMWcLhhY525bCnKaesWOKBc56dhhR0STRRNRTwlwnO2dX1NbQtjrL0Ima9ia5asR1RI85t/bI1Zoanvmw2lBjvdlzx6Okwe7uHELEnuFM1OYYPR+1QpXqQyFjhCU2zvLD1HOzE8tO90gwVaEe1edbdkHzS5jiNG146tayk6IRyIy9BAmSainH7t4IDnp38DdluAmtEGB0IUocjdh6HIKqaJp1RiQg8ghfWvNkNJ6dS6KMdT1amAYA1orINL4xd1vds+PjYeke+aPlcOraR4viLIlDptQ2/jSIy1zATXkjU+P9ksIqaTG3F7CIZUaKpSkUuBaKN8TIF5JZ5AjG0jym+urEB2tD2mDJ2tPjuDlmzDGRvPERGaL7Gavoy9kk16k14QbYQV3NxHmsGQdzVW/8RHYdEE39CXReU9peMA0v6oLzAQ05xsdbexTVnWkBX4Jp3byKuvWIRghWLf0TAkmCxbaK3kUzkc5kr1nruI12WKjgVJBp49AQZSgde9Wp4kr7/1u5CbAb650dbhlS4JJlGVZZ4FeYXO7sqK/tV1LlbxoYVG5YnJ2dZOyb5O0XZu5oaFRqlmYalVRVHGpokR7kFJQTbpJpXqZf7pFm7FLqZpKf7ejoaGurpAM+RBm61xTnuSWg3TdU2wQE2a+TXwa0NS85FbTrCXRxgxXYLivcTojVUSpKzgQ6ALKLCXQtD3QbEGQPE2zLbUk+9PImkCLIoUbQ0zdhO2tLEtNBV1lDvQvaWgtSXwxiQS4TAxoBOYsCKIK6swwoADt4QDc3NSUTtDVNCWkfVix4YxlkLx/IoXqmSrUAhDJRqdx8AAA= -->
