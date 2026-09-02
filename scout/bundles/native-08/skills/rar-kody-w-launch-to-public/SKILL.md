---
name: "rar-kody-w-launch-to-public"
description: "Snapshot a local brainstem's current state and launch it as a public repo (or graft into an existing one) so any cloud AI / brainstem can fetch from raw.githubusercontent.com and resume the work autonomously. Mirrors the ultraplan handoff pattern: local\u2192global launch with a continuation manifest. The inverse of rar_loader/graft (global\u2192local). Default dry_run=True."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/launch_to_public_agent", "rar_sha256": "857168ad0d4421f9099e93a63c4805ad22e229c31526b4d1cab37f9548fdff0e", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "launch_to_public_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/launch-to-public:cf6d58baa0b18e77dd7bf8cbbf76b016b0c042a39bc7f5dabe0591b9e3a4afd6", "kind": "skill"}, "version": "1.0.5", "author": "kody-w", "tags": ["launch", "publish", "local-to-global", "bond-technique", "operator-mediated", "platform"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/launch_to_public_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `launch_to_public_agent.py` is
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/9S8ebeiyLYv+lV8eca4O3ObuZAecp8844KIqHSKorJzj1X0IK00ItSt99lfoKtxdVm1z7n/vDVGVSpEzIiY7W/OiPD3T2ZdBVnx6funKHPab82nr58ct7SLMK/CLAWPtdTMyyCrBuYgzmwzHliFGaZl5SZ/Kwd2XRRuWg3KyqzcgZk6g9isUzsYhKB9CbrktRWH9qBw82zwOSsGfmF61SBMqwy0HrjnsKzC1B9kqftlUPbP2oEdZ7UzYGYD6HmogQ1ae24FKHtFlgwKs7nzwyqorbp0CztLKzCLOxu86edQuGWduIMqcAdNVkQDsMQszZKsLuP2biCFRZEV5eV1HVeFmceAeAA6Zp43yM2qcov0+3WxP2sEphE/ziyw8IelNWBcsLJ+0DCtzZ5Ng8RMQ88tq7vBGlAN05NblO4g88BEi/s4Mx23gK5L/3wldiV8GePL3YBzPRNMZeAU7X1Rpz/WRe3eAUm4ZzPJY7f89P2f//r6KQSfP33//ZMdmyV49Em8zGedqRceMz5gAegDFuODl3kLxJqC77lbeFmRgEeOC5Z3/fa5dGPv6+Dvf48as/DLL4Nv/wVkWHz/mQ4e/irw3K3uL4L7Mfh8bXcHHn3++enm3c9PXwZArD8/gQ93gEKYf/7yTCT0BinQnFtal8bQz0+XF2F6++5m9P6vcKu6SAeHMkvvnDrJy8+///yURT8/fR/wZly6XwEhtxdl/+TFpAZJXVYDyx38Z9akbvFf0H/2T//r56c/bucGFKuo7V585ZsV3r78S0u87fA/W8eLeRXusQ4L1xl8TswicsByBpV7rgZAhhf9vWp68eW6tOdxHxQJrOvFsh4e//z0ddCr2M0yyijM7/O6DEAXK8vil+y4f3oNeHDT66K/989W+mq4+1fv750QLPJN/6vkPuj8INbXPSNgo25839tZb3+v+r58+yTA0R1xNwJyfKYSAm/xWvb9w6cuqRv6gZUVQZY578rfD+57F/T14uLuUxP4nR+3Sn1X5nHYk4V6rsM3PW9JP3Z8OZM3LR6m9TTUO/MBTgAIOc+Ai31D7+bde0p9fbB65Tyv0cACOthb68W73SioBaQU3d3yFDA99EL74hfvgdTz8rV03ra4iPaZxH8MwCSy+OS+jjjXOPPC+F6p2Cvbe1a9ILsw+FXzj1qXhf2rxi4w2z8b6cWSX759YH5W3oFoE9y55xwEn16LQMv/F7p7HvBW49+b4AdjgJevhjgAmX9+OYne7Vwa9h9AEMzvX477Uhym8yCLvmXoPL+8fr/vRwET+pPxro3velf4Ym3X56C/DIDAC/E+8wgghfLzzWhfXgkAqParJ/3fJVhnuZu+6NpjE++d1i/m8vnisfvg/dm7MPP3P748sPqBCa/F455tNwchXtEmvT//OtDNuHYvn7+8M1oOwvibQHIl/TqEPM5JUyfj2US7XynK+n7FqOqMe6/lPaDU6yBwIdkLuV1YPwDgYwRjg7rsoVeZu3boglCTZc9x5QHquADIxIB7t/b9ju6/HvR2xEEOYpRbnFynJ3KrVKppRy8G8/0b+PFGmuD1vdVWbu9OgBTt6D4rfAC7yuQevHqjbC+s4eureHHrLx9kxoexK2cVn9Wp8yC9BzFetMX9xWys3ov+D2K+9/OTZ4LhnQFAxf3KeurfB7+7f7xELB4Ql1vkxdW13wO0m9eVe3/z+PPTtL4+sP+VIbN1GDsXpr8LX5+b3r6+T3rVu7f6vvcvXzz0+/yePvy4/vP1Nhr+uPn89WWn27Dy4/bL19uF/7j5/IrATXT7cfP56zsR6cfbRzfEXvFsC6JgCcQCFBUs1m7t+MZF5b1ClX32cd88tXuNZJ7evIExgJaZ1vk90NP8Pff3HvlXmgg8ZGJGLqBcfn6v+ddrlnWfRT9eYb6LfwTN7i+m/+PdwX5p969m3//jAT2+SyKn//wZmL4Xnn9c/eW3q5l/e+M1b6dwS/G51S1nX0SYp669PQHfFb0gbgFTqvNf9gEzvL/kZffXxq8i31sv9B8DDWjLAP4+6CFrb0gAHwGDuNrR80QLEDHbVwruvcC77wSEhxDwON2wBEL9/ETzywcBqwzqKoxB8gtSvsJ1P98O8vV5Sl/e9u45dl/Gtf8Ssr5tWOfAHF0z6X1OElYXJ38d5xsQMHB1gPorD+gCY3lMQ/6vLfVW1/+igv/P1wkW8Q0s4h+XCV9qEK7zznLfWMdVXdZF27v1fgr/6Ff9kOw4mVumf6uuU/86sMGoIHiG1VsSffS6B2ssit4Jg4l8/ufPT35wxW1mHvYfQATpF1RCv98s749rk2/fSmCTPeL/FxgncO3oxyUEfXlXKABW/j8/BqMP+P8fg/F1or3i35R23m/9erLXekH/6brc/vNtPLhM9koVvHqf5vWvb3hTpXpgwbUeAsLopUT0OnX4/Ps1Hv3zO4L9648eAiHEl0co9PtNWPnn3/ooWgYmghPgn6yo/vavP/7ChOwYeO8fXs9bwOsv7zd/V8NSt/nWc+CNVr3hJFCQCwPD9PrpyQg+Gu9Nz2/jF/2uckmyqzSAQjnO9UNWhH6Y/smyAdODqsrL7xB0rcb1JbiXSnh3Gfm96X1gMi8M9us7DLsHKfelwYXhn19o0K23e9dxI98H5WNB85H04PMjRv12VZq8AJi3qNpXk+6DxVNnMI/Hz/ePhG4c2G3u8tq5XVYOsok34eF2gHc489rR3wjxGr2+DnrPeP/CHf5Sfg8j+2lWuD8eyF+/3T/UQUuAX64i/PIRS1HAUtv0vOwBWd5WLQY9HigHn4FahVUIEvosjV+z9anzE8Z8fAJs8vM7Kd3zsh+KLz/eFmF+PH16hwFv6io/3jx5p5cTlnlsth91uBSTfvT/+/qLwPIGBL9W8B+vvr9DzOwrvfcXzv7oEePXa1X9ktr+6HORV30+Ehz2fdAU4YM3f07CBsMXmcbwz1KFC2/MyuzB7Xtg68nP9I3eoL/bkP5I5W1Ef9nnOtc+7Xu37vBMBqSil6Z3fW75euRXEOShwvCK9pdf1hReNe4HbKy+9PKL+oJ3d2H6c6r2jmt8NADguPvGAJIDF3oHwpebOn0m2Q92rRb3a4VuF/nHl78ETG5G6Gu7eZ+e/8URriHDvNRw+gZmfAG7V7dTvq5Ev0pc/6LAbpPat+Wij6X3eqRfi+9164v8+gW6qZ313gdYU11536g/EelTmn9LEUCSryCpdYCt/kC+/FoXgNH+fLvE/7YmvMO9t0LprfpdabywWZHZyGPhfqzI65m8YdYzRb5LnL8ojachfi2Gp2b/Xf4/svFV0eJ/xM6PFv7HR94U/z4ITJAcfOtj8bXm0L7BD9dK2Nd+j9Oy3H5jBwS9a9snFHH/1O5WFLfY4MtrsHBFFJ//CRD+P19DLUCsyq4jjd4I7Wke73D2puP9w+f7p/YfTe1maY+o5COGEd8HVpY6A/fU7yA/Wv5rCNw3ub82eV0fuVG8x/2urPizHLunV/653l+ave95nqgAAkBlLnMre6X557/+eDenemUVzzP4KM19v5T91nBuKP3KPF5P+k1d+08X8d8obv/7nHoh6d/fpwiiTdUTuE+z5j4ss89fvn7U8LqN9/1GsT5s2ueLN7uUj9X97w+FzA/7VdnDHvj3wcd1zefmz2nlpep7k3G+fPevX1MIO/cKHN5SuX33MZULcrwHkNy9LDIGmvSuX/zyJxQegAMAqnEcXjda31B7BhcfU3tyfFeyNxsGV3JPD/4yiScf9Eji6cFfJvHo/S5q8PD5w743GyDPanP5+mGXx7Yg0rze43x06vFjPQPY9u05msejKp9vy6r9SYC4guC70Ze7d1X9A4sr//lsmE+R8NkUv/wqcD/7n/85crrQ+u9hpnejC/l98FAxGA4uBxdeNAIZ7UN+1VvdX4ks/bmi/vvTSYh3VvRXii0Ao3jhA4ruc9Y7NzHD+Pr9egLrf/ePy7s+C8/j9u65sPIXKnj/rRlcTxb0XxdgAoMtSME9t3aL/0vjPZWUvjHvF4IeKpz3t/XNX86/l9vD6+RPKlTPhaqftUOhDvi/S40es934I9OrssHLUirQsl7b/tpQE5BEX535979QWfzrdFfXveHBUyUTo/6t/mwPtyrXDtLwWLvfB89VGQBBY7P9x+D3F+77bw+x4G//+vLHQyXnEjX+MfirI76i9xANLvQePg8+P4UP4Lj+LTaPs2/M5fCi63xj2++DMZCq4w4UYJ0D7I4cfIalS5bjngFi/s8He/rfZloFRZaHdm9S//VxnHyRK/2FsvmPj8vmvYIHIEf+6zpeuKdvuVmUD3YpTBju45ryG2fWj/X2ZNC/a7fX416Xl/WrmvDDlL4D15Ve5/V6A7i5v27+gdncFIk/PLb5smYMXen++ZZ6+jaulkBWiXnBiA8p3GqibcT1vTYWJhLz9b0+1435D6qlN6fmvj9Gg3ebvTgV+WeIsMdQT37hFZB7t/lfAKX/Jg4BYrkCib7ph3jbNyv3vi7ih4MKj5L8/aHk+sdjfAoz6Penmusf0C/Qdq8cvR98Jvr7s778Ab2tN/2K0G0J588JvlMY+SX1FwWFD8h/VCj4mPDlgN09ABz3cZi6lyMgnz/2QWA8Gww9+OaVmjj4FasG37IBVCX57aP/9b9+6asBcRAOssHPn2BVH0QqEKMGr+n27Qf/pw9yYC2Db+YAtBt8s/9sOLAUZ3B7wg0qCxt6efjsz2lcjzajg2/JoN+xKO8uZYRL8eUF8TeT/oDqeznBH1/fdy7XSNaL7PHzuw0vAPoxb7meZP2llQFEWeRZ+ZARaP1h0MdNqB4+X4+OPx7bety2ukbkPt37FvaQObzsXWVl9e0hnt/9Qgv//5x0/fExzy9JS9/9+du7jV/GzL7Dyyfvu9cAaF7ybwhyHYTlILxeNXh7nyAwY6+/I9C/vajwlf7dQDXD4ppmPV8fGEAPuzwvt9cezuu9uVTwGC77Me4G6wyEosC9tG37TsnzBYYMoKU4y/KHGw+DpK7M69neB5Bc541ZAMz3MOvrVY/LXL7ldRyXlzLfoD+b/g+wjP5uxAOsjNuvDzD42/W8VV8TvGaY3/p9wF+pZwU4128JuHYVPm40iMqYEQfXRQ6mosKCb49bMFV2f02R7y+7Y19+6X97zrwm/kDvgfp1qM/P7L+SBbnkWyH8+YgOWHx177gAeldP1xWyLC4h187K9lJ0AtA1rO7y9v3c/V11TAGwvRxe+0UEeUIvl520RxfSnzx9umxygbV9xmPaVW3GcftwGgW6XAcAz18d9rj70D33Cu+mLy/xPF/c6cm8HyxvLu3cfUT7+TTRpdj9QW3g56frZZinGkl/SDIGjL8bPJxrv5wNATNsgDmAFOgmtH408l8L+IPB536Bj9ujIM3qTePmjsagARGqZ6eTfXl3la+95B/vlkJAkO5l9P2dUv7z0bmPDw8UyeXowG3jrw8HAO4vB1LL65brpz++vriJ8un7p//4j4EU2kVWZiAWaXZWVwMgjSpM3B7+X1zdOjOBPjqD37TFTBQBV3579H7Oww2nKQjOlwMWh6vx9f7vt/99LXxA79vyb5dLVT/Ta/YBPFB/7vm6Cd5Tv+RmgMPfTv0Az9cUVuNe+fKyjt1/DH57nzSwt36GP1PgEwBo6E/gAoZkwOzDuL1eYLuEV/cMbGNQgET14uuu+xp3/bK3vcJfmWFfLrS5dl093lu4BLX+UML1MkPv0/q0N44HV+eTFe1V9S9H5H6mv/32m2X2papHhHM94VRCoMHThAffvvWaGAMHVP1ML+jtb7//8TeAxn7V60K8H0PtTf+qlmCGc02RByBRAQqaVuXlDG5/1L8Xyu9/XBnfzw6g1IdTtO6lM6D2LOF+BVdpPIqivOwJee7DJbtXfAOGAPjS3xC8bogAte9JZH2AakLgih6YeO18Zf2jbK/jXA9eX3kI5HQx6b7tRbl6YdpZ4dwNZpdNsiunLp6rqHqJBgAhAX3sw5Cb2i3oaVbPIrzU+EAALD0Qvere0fSUf3veHbBB898G0lgd9C68N+jeJ12OVJtpll5A2INyXh/3adLfgI6xjyTuBjIAJgXwwgD5BoVZXk9geOZVI0BIf+zfO+VB6jaD/uqf28voEpovmve+Rj96+PLDW5t/ckvz7mrM7uDvf3+8xvgUKf/+90e48hZvPJwXuhtoGVjJFZUAqGBHP1OQJAD3c6n2fH+sFNwAm/eRzeAxFA/eicxP7u0zWOK3ns7zTbkLG8ovT47v8wMYflxk1nP1ESP1Z+4endeVf/1Er5qXhOXlgsTT8p8mfz1o+DzDd4DJ8wyfa4qB+84NWvcEfMPlHkaPq4DhxGYv+qtgbs6Z39T/f3UB9esl8g360FfdXKd9JvTqXm2vvtfAeHtJdnAKzY/v2F5YdnuL9u9///Ae7d///r3fKyjMqr+3Vqe9tgE/mPpAgXte9Bix71I+KkzlXib/+bLIF0u8DUdfLqv7mV5hRumWff3wWr967NQXK2+WdHHDYJplDwncK2btV3nxZgCl9qpT1hYYop/C52lYCbX15WINQtb0ArkUx550AL67ucBykerjdZQL2R7PA7f7/fuLmypP1tkneLf3Xa5Vq8HzLZZv4C2E3CHfHrt+6f3IZbO8uGKXCwy6u1JA7gbj622Q3t6v2snP5Olkpa5m8nrwcPkJwNcrHu/N+HrSq67sx0OwT5N5vB4CxP0NYHnAt37kR8FeU82qfRgavXu4VGIOfrvdj7oVXb8r9dszNHpgwhUuXW+1Po39Ajv29QgQIHpZRykQwjOCGvTY92EGGJDExWierpf3mPXmNvDnaxx5uGp+bXIxdmB+vZyeF/5YGh/4NfDNgAN9fh0DFPatND33Tb38y8MM8Av7+72m1xWZ4UeId3hVvHdu9pjV5SrWA2nibqBczjhfgLmbmhYInSqYfdlfl7+44svB8f6qsAlCE3j90JPsIe8lBzSfZPd4nwtw1o7rfp/uFil+e/QyF5KblfjiHXAH/bPHCPDivOCfnRD89uhkstT9di163b58UMpbLvSJ7e0lnd7sHm/J/3ab0vwGPCyQTdU+qlV6ia39AeHyksFcSiSP+PNq0NrF2r6/VNjnDVSAe9jngyn9OYLbUwT9vXzAJDct3U/fU5AAf/3Ulzyf7uP3V+6B8iQg6SjK/rr+QyEndC/f3rsT3T9/+aMLnwHAqS5JMvB0fTZ2BY/9CUuzvGbZl2umwKAL+6kK8Bhq+ilWbd7Pqd8FSP0ezb+5T/3rUW9+qOEy9NXH9RO4AYk9l4eXY9jvD/m0WfrrsS6nfgcP8QB8u+6y9hWZy9btDe3+ajrIXC7EX9yq+vUAzzebbq7o9FwDa8mvwf3dBby8VPh2jBfVxs9POjbYXhz07ZXL4eD5RNEgBj7kT8YDYn073KtCaS/6XiCPA3//s9Lql3cHfbCm63AXQp++V/1eyDtMv7lX93Z6fFgA725e87rbzBfoZN0fDjcjEFmBsoCA3UcX231/Qi/zztejSC9+COEmlnwIFl4GlabPv66R5cPA8t6sXt4gfcGt6w8LvNsJOI+XTW9B7ns93hwsf8sB7noQfXD5zYCXN3ZBnL4l8PTLIuUV6IFg2Hd6d303EfPtkC9/SOP2zlufzDRX0teykdMXI0yrF/E/nqPupQGgf424354j7VNMvTicd2f29rLm2wk+BslLaC4ARnmMU4+Fh1si10Q1BlPrxwuBZVwovmXJ9YFZFGb76Q/w4DHJ+PT9ny/49Upn//XUNbP6OkdPC0isuv4Oy++fQGwwe6TQf77mxNfkDXT4sE4BxnjKL/vrL4nZN79UEy4/2XNZ5b0J4kyfR9688vuk+P6aEz8aNugM2GHGYXf5bZlP19HBtJ8LMxd3U3wr+7y4D4qAUu9M+ilflfppgKube3BPofP9ZTXnW5U93On6bnuEg1OWaY4smHJJ0nFIy6Nsy/JIwhrB4D97hCEmSls26eGOabkjnIYt2kVNzPQcAox1xckPY0Fwz9g+k3zk3q8LSZ+uja9oA7SmcBImKNMZORiGwB49ommXRk0CtTFqhJsOgrgIQtsojCOEhTmwbVoo6dE4RnmO543cnt5DaeM6wP1jGemRz2VWFyA+XbcVej+BEB5MWdiIRl3UtUekjXgoTjsOTcAUhlLuCBkB7vSUH7o+8LoXxXUNvRo+7c300nhYO9AkAgMtBaycMde/MUTrNIKL1qoQfYUchryfeYw20sgpPj9VLBcgulEGKyEONE2dYR2pY7O5NEnQMcc0pm45LF13sor7rEpWY4isTqU3bNOO9cp5gsfwUt8GS3EfnYgmJMcmezy2ZbFoy27RSbni4FuniyhY3/D0NEm2u1ydZaeoOCcQ1Ake4uhCMjzq+rRLpjtelch9MevWp8VxLe9PHetK9HZZnBbIYVyTUous1sFeZevYGh+yToO0Mjvu9/VorRjwtl4JK+K8L4Pc3SVrXpTI4XAFQe2GP2FFrrSHc2Q1NXKYVMdNtTtDwqJh6oO+qOAyKvVImnJNgXXiYnwKV/qslZP9zrDaMuvOcxE2uyxu9PNyYTJ8N/XS4kxkjiAOD10Iu6pAIn534tSgS+QJw/hDyJ5u+LJJ0qUuqakqNtxZlMnFdqXju6UfYsySS6esSW2JyW6z2Re0ctROiugU2Bg7u7bONlWTbYa2D7ibFe5YOoZDGVnMdYd3MkBBw2Ep0SxxZrGsF8UTYWQggm4WCBvjGUsnB/s8K9db28DqiMjcMtjU+2I6wbXAVy2nTIOdvCx5nGbPGdJiWDVO1sc4SsUpeZyFEJimHG9RUz8XjA0PJ/xBXktJmOX2mvG1g3+Co3Gc0korTnIlXSiH+fEkTuVpUu74rHTPwuosb635rC2yWos3iALx2mm/wLhZpCC4E2yjED0GLIeae3FKs5xThoLZoGLYMfuRCO/jklvxarLerXZRPmw1XTJGQbeeFgvUVyV8xA7pibR3Vmy1P642Zp6wvuQzJ1w1PaRMljuGlIYLE26EgG/n/JqaI9tTiYZ4vNExhjBLeGk0+lATbWvsrrm1toDHJ9NZT6RUP9vtfJvhxyoS1rJX2JvZLsPVhlZWJLtvZmozHo6lvKJBijJb11tjO2EVZmTMhiJt7tlgquB7nBp6ULqOOveEdmdouCfxcjy2HEmomZUn5M0QOiujOaXw5IaiuNXkEPpraRV29YJvap9nsCPfzZ1GVUboab4iMa8MWkve88Mz3R2YcEZRo9w5euzMPcFeqfFKKq60XYydQiX3uEWJTw6+pvjiXi/qKuYiDdqVG9iLo404oYaw0DXsiCWQoGC0dmmXk40Tn5254EwRSpja+EQ2YSu0XFY1W4ub21Nhc5ir+CKCIDQbN2Y902ZjixHJMUmV2yzMHWYkbcLCkQpssqlFZjaEIikcrrL9PhB2lBGoqruaeJ6QxbirpqOtuiNhioa6WMQgV91BsBQ3B9oQ+LPIiul0iy90Zc9E7UlksnOp0RydHLlckpzGmFFpspnbbLIM+A3PE8UsGY93bai5BcTAJBTorYxFjq4mJYu3zWq27FZpqZhcrk7LraQYE3I3QqJkMWFUssWz3XB82pNqvhjvOEZPcXoNs6FTr5icSpaTYHJeQAbqLwV0qMEBN5sSxFqxJ3bHYZKeTsvJzhiOtvhhw27W8lBfezM3GLulJo5iuczPc4TbtciRMs1ML6rjVtwFArqgT+amktcyGW3xITYp/B3CMCi/YBvQld67C5uWFiyOJlxjzUo4bBexDy/lPQi1RwxdLVMxdh1+vQ+2PsZjbO3tFlGVUvXpxNvnsTfGjkMzlvCFc4SdVZ4XGFyOYKObTk9HzbHoFR81W9MwjnmRmqSOE8acx2R2tyXxY7AYQnNGNNBpfEjT1dB3KJoJPW4+UyngfMuhN8L8eGE16Bg6EtxytZ7LS9dcy5FMexrGqgoTTlYnIsNHdGZR3hLTOJoeenBUVke1KPUyjkx4lTXMeN+4zGRNbLqzk7MbT5RzcXmeR6ILUSCmCFWU5G5eaGopx5btBtsilncxvY0oemxsiWkzx2DGXKOUyAUUUR8XEWWl2WaprI+yvtHmbsparbuCPV3lRuvpaNfuIY72k2ATJKrJHQ91EJytTQUFlmQulkl6wicCtQ0dkRf3UFMdonFb77dupe7ykViNuc6IbV7ZbCe6XZ3FGpLRyZQdyZu8ieXDlE5ZZ7NWYl/3N+vxwiAKx8kixWiOVKed8xNGlxW/x0ZbtpsywhYCLpTy1JRsZRSEElrDCWp4gImhDTGhSuxDnyBaU+sgrghUDz5lCbQLSIFD9ipG0MohV9fYcMudHTtFqbXQQpUnbsgDC8kngHRSGrHViBgOdyVZd6MhpFkYkR5gqgQORkAbB4VoYrgfoWPGWmX40D0JzQ7yumy+6zBpVxCQtF1XpC+GsqGH3MljzkthNov3rOTsYt7kBZJbOQSnhTy8tQ9TWemSSTA6UZhQeWAKWQjtspDakiKOy6dTgFPlzjqhMYfWRrjWkPFyNuND96DC7bjx2d1Ratgz8PedCfmKQIOsFbd9oB0xJEv1IlNpxRrazELaTa3zxN/ke9geJRpFMOre2ycQjnbVZDL1wqRx5Eg/aM3KB/YVTIUQSbHjIoN5z7B5BmEZc0tzk8Um263H2imeJMeSkeStH6xDj4+FiWMh/nSDBqdWEDw1G7HpSDiVS2tS2g0/9imHY6SDhcEEc6AkfaIiEayuM8iSfZ6eBGKz2By28WhH81NnZgccbAmH3cw/a0wCLJlZjrPWGo7yOnb1cz01Gs5mZrArrG1GytPz0CbFITvmp8wyFNbzkeuOVzaxW3D2ifdTUoRlBGUIRFMyABF2Z0OXlbW8aqux3czRLnSXQrsmi7NPqvNmqB4oCJ5p5zVLz+aGOGKKdEKf6vBQMbkvr5pVknVyWQ3RZWjszvp0rOJtnO6OGLMSwmS4ZYxiFhTdEmk1fsKx3GK273aRt2sVbh+7EU/hzgoaH3KKhZ0pI87zNi3Wm5UIh6ekaDWYhZbzLM0NiCfoaOwwojsJ95qItktm4bGRhDBJoHDR2t/uLYnlNOg8NliWO/HDeNf5KdrCKgEdyPks2apJhoibTlcrXRC9Pbsw8HPsKtQUXUilILcLVMz8NatMVxjKb7CQmC0m6xDMi9OnOS13wSSkwzFDjwWZ1qxZrC73iURzRwojZcRPanqczSNkuzYMXhP2ewbl2PVQOK2WRagpCzldLjqOwlqWm0hRRexSO4saAC2Zgw8wQsjw6BjpWLncjjfWVkbO/DmIihETaKv9cKlvNjFswPC0ZU6ThKr8ENIUG06xpD2N+IQ8rw3GGO2rXTOU8ZA87fdmuatyX0Gm82O4naSiLQ1VutYXPiwJgrsaKUtESY+TKZc5GwpaSvBsH80QDsLOcjw0cHaFAXyijT1EryYnpGTz1FjtltOYb03hKI+nY7O2BelkLhG+bqo6G64kuZaj07KIDEUYFrZVsWEr733HAYrlb5dLbNvYjqsX9MSrRZfczfA14gLNXHZYN91NCl3dHH3JSOb61NpWS2W3m0MH260yES6TvTKO57atw3C0Xc6JRCGdiok03KFJACK2slitOVEduu6h1LDtbiZ11MLXJuTcNPzUWK4N2E2X+DKMRjMOExV5rYcokYzQvINsz+boDKKVZpRQ/oZdcFnISUnrZHQjTyJhzoqHbjNNV17MHJJSsDa0sRzV6ayYGniLFBtfd8Vgv94o53ioTDZDWcXipZy4HMNmU5eAfK2bKe0mmVmnI9CfbhthShMhPH/Wtsfd/CTOWh9Nz1uDPPoUBSv2xlSWmzHKntoIH3X55DQX3Wi4nuW1zjNBOHZYL2ClSavqiZBl1l6LTGbIkJYJg9CMu0FRjRYsRBtn1XVFznXWOwnfeZkHtcVpjJyQSjmJVDlyDydqe1ApkkeH6kqmhQxYYkP6mCzbS0rC4Dgf87LIrGJiAmOblSWfD9SZl6ud1W27NDWOO35HMRNt7VBZ1NlYkkGn1JcWRD05Ho0illQodCUxlEi3wlPFRux+wjMtlfWAsmVmUk0g4OviimGJcWiQW4bZAhxG5rrN1ZJLraqhOJmV5NJZhUHcUTw2nHHUxI5BgMO6XNa8iXHYol2k5kUdAvFqZrVygxUKYidzpFE6CM3J+VzPhsvpooxgc7kaQuSK2NfHZTTdIBuzFZYTZLuEbdTcbmdpW2NBK0ULED7RpkS38OHobPHJac/bTDWVFH4XrqPl6hwr3OmgbIKtLvgEhO0yTGgqb3VSSPLARM7OYngnxsQQO58Mw7XN46w9ZYQlZTP1FCuxaMG7XYJkrXDy3FV2PoVCjGDnKkplGBNMD0eUmgWKfhzRDLyw3DEcuWMGxc65URoJATvzooSsub+yVr4YxE2cihbCq94uSs/yXqWMXBbIpMIQyB7ZBqs27mq9U3go7irWHKsWq0JHDCsBWMPoJXNcdw4riQ7e+ZotWec16na1pW1tTdCojGpBftOyPGqGtlhjaK1hBiq3mKnFlDMnJF8io83ZE2tFGjsLc3h0rbPNB4nLc6TDTlFGD4SW2B5mYrxfScdlUhMislOAk4dW1toc4SMUcSr/ULKmNXJGcHNMnK4uhD2HcSerm1O1NIdXBzZBumPepbWjDfeQF9fFIeEzrjQBf5Z0B9UwK29dkDtQu7VT+E0uzTrFgZXAxGb7QI2nqFK1bSwQiYkxgu2PFXhTExpnyZy73G/R9sivzseFrATwDotzw81jX7ak4VwIjxt2vIQ7be2zWUscXH7P7jYovB236oSHNHfkbubJMTgieEjshXpCwAK7WbrNVF4sMspn6OM80rhlXY8omNLkeZFr+zrRBe5UiIDvmMUQsthIx1ZVNmxqNpWxjY9B7U/9MKpaViCmBVuHvB0SW/mYjJqwZpU5lZ4ARmy8dHvmiypaKoKiN+KcXoZLh5BcHcQJAFbjdnoG8DRJMTSell0x0n3IQbVzAJknZEKmEp9J8/EqHR5OpW00O3efoeLcmwMY7pHn7DT0zseI6gwISr0dZqbNfglQVRSFlJ1OhsQpaNLAckxuBtAySh4WiV+yI492W3l7jo4AkbkLZihxZDrRV7E81CxG46hZRrYnBg9GTe1upxa31CdeGmXJcSLKFjVD7DL1ULQNQlw94luKblfwgSA0HJ3M4ZlhMPsai2Zn0RorCZcBnBISUabJynC5RuFd5sRoKEyHqmwt9+uaYSbladnuHWClMcoDiNya484faciahiTEzRQQ7txUOOQ6T43s7Jzu+WV73gs4iCEqsuxaGknwbSatmYmvtyCDy0DU4StHlCB5Rg4JyGYPCRQQnjtWyXQ8XGjxeZ9izCZgvD1H6MTUiYAtlip/XFFMwZviMCX3DORyc2Q+XEzOwbGOIQ3dejYmrxmT52dDKilMHOnQ/bobddthiKKSPGPrcRnxJ4B1FDpv0J0FAGLEZIJOeHMVZFf4uZ4sakrE1FQbYXReHkmnTY1NcYyMdHlGui6p6JmKT0zqFNNWvo8ULPTPm3Bidr6jHxeQ2c5dcwn0g0e2Na1DKlgNLk6ZbofmUhbN9/GQSlPT8tdJw0FBFsenRUHvkBXiubP9UUPn4aw4RBmTHXlloTjHDVxuiTVtUsRie1i5lbOy2GGgj1zEcVVDXTDEmCmT9aweFkdmnnWLxKgJjEa1EV50IB3S7XA7VwkyQ8/k1sWcbd1I5NnNKLmZ6223bzCuoEbcMqY3o3Q4gSkebhoDOei4uh7FViOUSMnJmnpceH5DHjxNUV1rjaOKmJyT01JU9vku4NeFl7rHZizAmFfh0FrS54J4YI524+wPeA7N1aHsLLnC4BBuZejaEsV2+hSyMi0zd6Z+VkigfpAsduR80u5YvVG4eTLHR42KzDt+pq9XZr2x0GWHL0lyYninAOZ5EeHzAopPw60LnzgvzAyFPkqHkpJWU6E8NxgcTUNy6U8xIh9zShU1AosdZ3PP4ei4wM6b2IjGUF4fDvyMXRp26J3HaZaEp2K+Go6m5JQ7MYGfI5Rq0TtzjUnzNqVw0XPns2ZOZS2DjfIOTrejllxOViQqhDsY81U2WQRwxu5o6EBHK72jEViMIWvcOLXjtU2XKB1JbeaHOcOOgpm3xdM9GcHUkcSVfB8GSl6MUl8wxs5eQ/EtU5iCrlMMpAmiU/O44NSrqIiniq/n59MYLki5PoR0sVSpoYjiwsIy1mE2H52j8xnxpUm8VDwb3jXacbF2yUworVr2xno9HsvHg+0tac5LeOzgBPnymB5mgZUU/nKz5oqpU3lK5WtOS7VI4Ap+FVojgI7SEdGOwrXZQCJD+0EKmcZpStjybn3gZIjaOPpoutOHbSYo6ZCeLZ0xwBi7AFYjZuGGG4g7xIvsJACYgplTLNPD9BRqwM2f8yCdEweCRRHZmulcPRobe8z2Z9t10YG45xZLze5UZhdAhnk6A9DcqmNDzCcFpqNWuRyZ5l6wmb0X1YsxAaJNSB1pPtcFvYnyQIdXZ2lE81sqPixKLtuUuwWCm7MMCyfJYWxVOSMs8e3qhE+WCJFycRQZ7SidIrQGzWRxvbI8QnUhjB4ukRTgM6fzY/TMjaaSUWRLDt3oB6omanm/npwcwaEc1LeEVSsW3dmO2sZvGGJjTNRq5COyNhnr0UI1M+IQ4cVhuq+GRW0iTHk0N0OVO7CEpW6DqhiZ/l63R8NCSg8osdmcl1SIyGdfWGjTcVYsS5AWCynZYhU6ck5Ch5MUxByczCX2xoSGR1NVcMnC2HvW0SjRmZyFWoiVyLFlTd4+7lCOKNtTDFzpOEfb2hNjr63NUuO2RYx4Ix5ZYOlwyUtmZE8PQi6bKyrgabNRrMUCR5wlP8bx8CiclcwwKtxD62kc0VPcxHdOPOLmIGhKttqAZCY2Dis5OgJnt4m9WT5r9nst5JN2BgKZ4J8nG2HY+YepgnKUtZocMKF1RWJi7w6BLjpHGilz8rxqEAASPI6A1yuYYtFJDifxpkWOUSeWkSBkhDwa6ScBT32Tavm6lJcyXjf0eHZqy3Us4nq1RCRalM2mns6zYteKyHoRQ8xaRK1Kb3QYS4ad5xViOKqKHVMtBNQ5SJnV6VzQ7ZBkYUYuo7E05aXzbq9Co+UwdRWzB4ClZbn5NC7h6cqHR8xqxE87CcGDwyqbOGezXBsBizXacKzUi5pfIzNcSTTvOIzUZhVnErKi8vUZqBQVyWwhHwJxAUIP0ey7s8xYHHZk8BU0mzOUpqJY2Zrz3UoOIUZIJa/T0WyWB34M8TXRmLs2M+FmbZZoB9OC2uH4sBZXdWtDUXoiuCHcDAvkEPBJYexCyT/AKDfcnU4uiVOpXanp2nD2KdSs0KDkj4iPZHlzmI0XI3963EWJtrcCt/Uqr3ThpCY9jJ656Nr2LFkiZ+gZH3YJjNfQcLhi0ESUWdQ6H414KrmKJEy3p3SIL9YVzyzKBYUTBLPYi4vMoBxuozLmkjsziy5OMOaYSBMJmUtr6xwvluian3B7xuLhPCJX+JJnpJAZAVRrRmTpsyrPVRuTCkm2xNy9uMoEb71HFtMwPpQj2E9qfLVX9sEQRCt/WnHbM6W2ii17ohrsrVAnZyuomQdHlQizRNmAKDLdtHGLrrj9fDNHc0o1jSjG56WPkFbqeXMWnXJwUp1rnbDwZlrIRpNUQ8Yrih2hTXmjI9otShN1FNoyP3Kt0SI8LTYTloXGC7wYLkrNyYHHTdUxhozU8dIbzVKstjU1JyaYFXesvhsTKkfsuVFGZpRhm8ZEWNjDSF+7012Duqcdhk/VJpR5uhKLfZpXNBzWyrGdIzrVgDwSoAMYcddRS8NcE051QSmx7Wg6JI5O4KDHyWnUzN2sPFXJ8uCkc8pNuNn6tBpiB5jY8uICyic6FOuTHIeMRedtpOEYNaGtOZrrGuFvN9wyDCnOahCmKae2Ze3zzeqgMJE3nuLYIsyi8xxZN52F70tc3RbqoYc6cDPdHdHppFSpLGaWGXeGCWOXCJOjEfgZpVjq7ATvOzro5u0Y5PLWWMonc5LW46QWzm7hjc82dSozTWH3s6ktMc1EZKhkKak1uaplLXRxjuQaZkNsJVhCMK6E8INmytOxgMXVmdzQZLjrDHuBKJ3nylOpOSX4el6eRgyeRlUTJiM4nJ/p+Rno4Y6ZsSO+mVTDTpUxaDRqdpyRoFaGOoGSSIYxzvxQ2fmE4dInmdlTNV3Vo+KU1pBteucG5McOpbIzJsDkuVjJrejo5fio8CcTrVrE3uBRieOsTbFZQqNIx5pldyrpqRl5Gy0KEGB1BrQ0UFjpSmMngfaaLyP5kd4c6129ji1+bo28WN7Q+4Dj/TIs1yWaMkRTCU6E7VNBAWmPvJ2UKMI1wrrSFGeCuudGBvML3MbYTIPIwLkWn864PWLJxH6ZRm4w5KYTlt9ivJzBGS8taiwPkPNZ3YwVRmtiyBnTwV4X9RAF+cUiU2cHknKPdbkimbGgzoymXGGl7y1C3cYYKhfqxXK/Enxq6ijDFlckkImdJ6SSFlzupquJw86H7M4bYWXaAJg4hlJR1c4L0oHG/p6pOmCeyYzdkjwNZYJBMZ5gHhUMgUfYjJiIFQrxS2kuNiOVlLZK0KHDzWIElxNZcbzj3p8ULFaBDGPEIGmTRShKo0mdIRbsRNU6m7L0CRmqsy5xTYBfTiGGraad4oWh4+0b/7huxVgRHLLGCA7kCXQGkYZi+PZChlBdKOZo2EjrYo+JMNKpws6j9RQbyjWm2NMpzxTSotluxWxM8FVgKJzs8TtiTtms3FQMvCFPqXse0xKTJDgsJLG2ONRG5I+ccRRK+46DoslhNhvOglPBZGIHvGdp7Sttq60S9ligqlkoEroUlwbAUBDk+eYCcRmFP/B40uOYA3tqs1aOq53FQyBHOQY+hh7p0QpjzTgU8QVtJ3O5K3QEXq7nHm93Vokke84ecva5c5t4bSymBiZlAKZKBs3zDCyOTlF7PrFhuVzyjVqsglW2Z+vNMu2G9uRY7ANMDye87wuRzil7ka6gaWFHBFvV66g0D3FuQVRIl+mw29VkNaPC8YbAtmMzLkfGBmQ9+Wi98MpusUQwCdZaM5p3zWoWOsPVGasNn0MMIYV9agHy14nsmsnMOu7sFqVGrXUigvNcKqlWmw0DmYKgoQS5m4iNuGkBLG6RcaHpFtE4PDbpbiqa8B5fLqodgSfasKZxbimj1TQi98A2ofkkX9GsM0KC4dSarbZjnt1iml2hbAjixcZf6K4NJ2uzkKsxh7LAb8XpypoajhjKa1RcWgv80AbZerZn2ykfb4H8V8DnZf5snZqylDmdq5+jWJfN/LTfHPbdonD1xZbnm47315rGr9zpgaf0KJfOuLioxUV+ZMVyzwrYcN3mttRG683c6MTQ0Dc5Ye1xvoOB+dX8XEOHejXSBGZnJA21MRZWa2ixN7Xh1OSC7Wmqw+Ha8M4HKYJWwZGc5pSb7jBCEcB/J2LiLHcdHpz8+UyTSCbdnTaHVQEwzeHUuNMcn5U+Gm11fIOlNKafFF+Yryzc2o80zMpXiLmacnPaUDbrXUe15swxHUI+uVKSMPkoGPLlKV/Mq2SeG5h7iurdedNk/kZgNwlf4Wq+idMj7PhT2M9WuT5yRgt4Qi9NTWP3jWHuDS0Q1wuAaOCTayISK820OUjM6VYrD2602c3GFCA84YhqMg+6aZok513i59x8FPEEbo6bYKXtmZ3KcNxWLYtDbmue7GWObHT1Wg63083Mb/jIUWLTqDbLxSKQDO6wpQO0ynhLxceUbXkHbzieiVQ3K1KjHWpmic9ncDTZLSxoB5FWPN8emdYVpIJJ10IWT0Y8l5xWh9l04YlzCkmllo/9XCHEuh7T+rHFAwJjD5Mo748CrLl0JTVFEA1tLbXbwBf94znfLMvdtqG5U2kZEsdsC4Garas5r64cdTqK50dqga037TI+5TJnxpx/LnYHyR2FIXFYTqdwdmQqbQ4d2ujszSSv9NyNb22wzZnjd2I4TnQpWmH+lDts5GPiQnsKVVUmnY0YaWXvO5Du2s16OiJXk+ps7RgIWLHuR86uNRo5WWftccZSEkXoqVsAT7TkmFprmo49J6yvRzUquOjOEhRhunRUJuNEWeZngb5c6ikH2cuDWTEcMScEhaEkjhPYRRZ3Nik0jcCwoRJOQksjC2tNCYwBr+WDsG1Y7bicScvRmA2qbEnGC4Lcu9xkuNnu/BOH57pUjPPYFU5LPvQ0Y7igOISXw9WEEBb5POROqwW1b3N2GdvYcOwKx0bfx0iK7Y7qoUEXC/9I5cSxsQ5GulUWkxzJrappyHE33mZyPQ9yio3FCEXckAszItTS6WEvEOeUY7hIBLahn8LhNAxO+3M1wU+kbh663VhH9vkqVoxc2OjDeLsSyeVsc8L2kbJwFvYWJ5mNsNIWc2VJcolYClhtBlJOVtt2NpsQ+Ro/sakzYYG7hY18QdZ+sMSmWwzXtfl5SLmThe8IB89CQQ7rx2aW42PziNbjPUEJG26SaluJV9FRJa24Jcon+ZylN3In1binBjzMnON4dqqKJT3VpEixWV9Q8uMoPG82UTfRvJDV7CVi6DQ+JhmnOAgHNimGI520i3105LbLCYgpqLPdWmMlzY+SSdYGkaXAgufOkJufWXPD+0LCw7WoHW3amo4c0sGmZGMxjDaU2q12PpCKwGMLBp3T3TRblMVknVd+shQmI5QvZ0KOZJ58PK3hqCXP7AneOc6+VYSldNDQOQLHkU6j49Q5e4U7ikNMlYrt8ghh4zFsHVNpRcDQFiEJ6+jsgUps/f1sY7kyVCXMco/aWFBug9Uu2m/VhM1oxG8ER9gu+G5vIuaWWaswOTvWQdRuD+ezd9AFnYVq2K9jbzyHyTU5KzozMlssnRCznN1B+W5nTxpuPc8JLZtsdj5JSYaEsZFuTPj4oOubtZ1lgSgAlL0/abxgqvtQ323m4hCrVxRW7vjI7XxzVfteg0u4iJ1hLNonSbWXYbMSyKVV4NNxnSMb9rgth1ZDH7aEmi9JPVcMUlES+AwW4MEsZB3DWSyxBblhuq5Yyjq+LKqxZsZRDtG11FAkLSv4YpOOE2S8yrpuaYa+Mt6Tu/1uSSCsymHrouV8dY+e2kndOPgoSUXRNhRMtKu1m51Fod2c+XV2pr3NEOmOhnicU/MNhCwmcdTCHSWz67ab62pJOfMmGYEEQ7X4yYw2T1otqPt5PuKd+XQS1mTG6WOLQ7lqQpq60R5Yhy1nYbclDTYRKyZphim8gNvKxaptJB64NeuZsK6mG+GEVLMtJnJ7twip3VBOUwel1zOoWxBn2mE7bzkdBUenPJ5COUfV6SYpp0VCuiWTTHaUn7kovBxWh6TFG5AhBG4xZ3mgBtnWVxe+6eerfI+5FlHmsU74JAZP9LPEAigZ6tSacxrZFaaihbELbAlPKsONBMvNVFeKxtSe4RZmR87G8/16STXchghWwSYJCI+e2/TKGKYGBYnRmlXPgq8O0ZOcmbtsGYUURpEr2M+FtU/IUOjMtkap+Vob+kE+88aNTWp1fGot4JjPfN4m8yipzLVdSkepGbL4mtW3AlFXqcgx1dL0yTyNs3KEq4q1N1eusi6LXNP1KRwcvXTrzRxq0UQEWVMg+qqxVaA2Mz8SzLbO2lbfOd5KNu31BvNSBeT1ewjivfEyN8iMYQnT9RzKaXxxRqGKt1ZLgOOoekWuLAjH3GHKl5S61Nx5jpCrVJg4i8Taq+oEILXd/AAvSWqDA1IlWSUEQ3YbNF3opFLv62UCTWVh7Yw2krHIuSW2PMtrMeFJJYnXFb8mqqzYTmexFyiznemcmCLMLHO3NQVn6yDklKRXNezgK8sllW5uZcppVG62XQBUxFSnYaHsNtvpHITVuNbyrS6x6W4onmU9xz2JQGdTK1btdBFprN7uNGlI42ymelCEyUqwlk/jznCG2XFPu3BaaEdTPpOSCxMSwA52Dfn7yZQkDKKdJqM5RVqRv5DoejtNjHgjG9SIXLYKrOwKczs6CBsPr7XDrgZrqo5bp1qfnKPqsvN2lKIBKo8MD/K7oe+v3Rnh5JszbG9mHcnluraPx4I7V2rdwqgJvpjSDpw2YA3KuISsBF8eOHQ5s0lR1QvLMNfWxj2io/yYh7DkWc5Ja/bQBjj/OY1u6ohekJwsHg4pn48qY57sPP8EUqMzHTkAtNPGZI9blrjJ0pU63y6QpVqi7pyULFKrBFicH9sE1f1sTGemBpM8WVaSN8EJuo3jDTxE57BS17XVneHADWtiAQXk2MRNb7mIY/i4Uim0hUbrkAbLw3GT5VqbklNx4sGEykSiE7iqjDbenuqkybRCYaqrGw5dDQm1puiF4yjV7EiZWBWZyrAmFCuD5zQHk+ZpsXaxsaXHZ8nd2AEUTrohPldzqtwBNEe6dohn0Fg/WVjR+pK+mGi+sNVPpGICnLifA3OLimM8706paoiChbtrHTnQu4xWHITGNlN8xLoZhtdnMiEFCFFpiB3OBURyLPi8PKlIHlZImAaod+AkUbLlGCTTJ9q0xKk3LYNNeziiO3joKGUly4qHykOLVNzjwmE2LDlqXKYS9zN+OiVYyisVzInGkIHwiY0fZ44RZzk2D5SlUqMg905XZ22KpOlE0XYIZOyoeLVZQbSHbCFz12R5zgJzUlcUAhVoOD6dtiO+QWgeMquUXU8WRbZwjr5LhcVhlcIob6yZ2INS9NDpiXP2iXJ1pOFlU89Qajhu9KBkqUoVQ8XfDpvgHEpFcdrYmjBaGtISmTYYSxDnVcIwFontHHTstE7bcBU73c12ZcmqyaI7xOMcpVYLkLOo3CJarp1crhp6b9jOWKZ3Ajcqd0gke4JhDce4lUvJcU2hk+nkhOxGrbLJJgZBpXkOHBW+SVe6V2ypdVysR1ANQRALQRFrBHDhFEQ5l1Cg2pOaYItkmwqeeUBXi0Sb6Yc2PqGYUlk0sW28QM9UJaWimkBJab8sdi5/EHFSqNuJjsnR0PJKvZSNZqbZ82TczsT2dBayJZofywN2Ws2ggu2S5XmYTMj9ng6YlT13m50VHkazEyIOgUq35Jr1vTNvYacSK2AnLjdpWo/rIdHVLTdTD6XqoEh9olcm6WypbkFzHRKLIKbK3N4u7cyCNnM1ohZjabY7uGSDTwJpIUIYyi5UDy4UKicLpBtBSD0pMWU748yluBdtbzMrKd4YToPzbEqHuZkWJrzWdvOhIR1ZWKMOXQqrO75RUMmFcm1cno0EHi6l6MQhc02tfWJCikuSJU4ZT/sMwk3LFGeJQ72kkpUe87ZorCNn29KY09RTjqA54KynhxEdjZO1hHpqmOtU5+yK2hraVmcZOlkz3jjXjLiOGIJ3a49arujhWQirDU3ozZ4/HuU17O7OIUTuWd5EbZ7V81ErVqk+FDNWXGBElh8mnpudOG6yR4KJBvWoPt9yc0ZYwDS/Xg9P3UpxUjQCmbGXIEFSLZTY3RvBQe8O/qYMN6EVAowuRomzJrcej6AammadEYmIMsIX1iwZEdNzSZaxrkdz0wDAWpXYxjdmbqt7dnw8LNyjcLQcXlv5aFGcZWnIluuNPwniMhdxU9koNLFf0Fglz2f2HJawzEixNIUC10Lxhhz5YjKNHNFYmMdUX56EYGXIGyxZeXocN8eMPSayRxyRIbqfcqq+mI5znf7/Wrub3gRhMA7g34XrcMhLRUw8oERnFFBEzEjMAggIVXHjTZvsu6+luGxLttNupGnLkx5KOPz+jyWHByldr6b67Gi7qbcqN/HJDPf4axqPuaul2M8Lz40gOlxTMZmMYnALurBEno/vEslGswIiq6sKsrbO40rgjIWv3ZYOglNdzcyothwQiEhKlkA5ZHYvcXWTO/eioiomeVBL+Dd2DreKfdFSxbldjNegHqvcg1EgE6ysms8h9EXdnxuOrPJC2YuA66N8w/dja2Qdt1IiV1z9FIlaOZEyqKrqcMiwTBMdwgxEICh9tsmxbvHuX/AqRsnlpV2p9HmeZf7PEFHPk1W4jnMQEoxFumkMmrcPfi9qxzJvQYILoDSL9EpqmRAlUJ2f+opMoklTbSTqHS8XXtwYsOOnXibzc/JEO7zhLWjcBzm+b3gPD9yzHTqncJ8Q/cd8oW67xu5RLkkKfQTM+we7RWJFcX4AAA== -->
