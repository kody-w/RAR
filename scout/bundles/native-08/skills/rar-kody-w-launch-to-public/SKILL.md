---
name: "rar-kody-w-launch-to-public"
description: "Snapshot a local brainstem's current state and launch it as a public repo (or graft into an existing one) so any cloud AI / brainstem can fetch from raw.githubusercontent.com and resume the work autonomously. Mirrors the ultraplan handoff pattern: local\u2192global launch with a continuation manifest. The inverse of rar_loader/graft (global\u2192local). Default dry_run=True."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/launch_to_public_agent", "rar_sha256": "15f570244d281c16313f2711c180910bd839fce61609a37545358e63b7c1ea24", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.5", "author": "kody-w", "tags": ["launch", "publish", "local-to-global", "bond-technique", "operator-mediated", "platform"]}
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
