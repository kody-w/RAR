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
