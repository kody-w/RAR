#!/usr/bin/env python3
"""Stage every agent.py as a flat GitHub Release asset.

Why this exists
---------------
Release assets are the only download path GitHub counts for us. A public
repo's release asset needs no token to fetch, and GitHub increments
``download_count`` server-side on every fetch — anonymous ones included.
That is exactly how npm's registry produces its public download numbers,
and it is the one mechanism available to us without any infrastructure.

``raw.githubusercontent.com`` is invisible by comparison: GitHub keeps that
log, we never see it. The reaction-based tally in
``scripts/discussion_ratings.py`` was the workaround, and it costs a
GitHub token — which is why it reads ~0 across the whole catalog. Keep the
reactions for *upvotes*, where a per-user identity is the point, and let
release assets carry downloads.

Assets are a FLAT namespace — no directories — so each agent ships under
its ``_install_filename`` (``rar_<publisher>_<slug>_agent.py``), which
``build_registry.py`` already computes to be collision-safe and is the
same name the agent lands under on disk. One name, three places: the
asset, the install target, and the stats key.

Usage
-----
    python scripts/stage_release_assets.py [--out dist/release-assets]

Writes the staged tree and prints the count. The release workflow then
uploads the directory with ``gh release upload``.
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY_FILE = REPO_ROOT / "registry.json"
DEFAULT_OUT = REPO_ROOT / "dist" / "release-assets"


def load_agents() -> list[dict]:
    if not REGISTRY_FILE.exists():
        print("[stage-assets] registry.json missing — run build_registry.py first.",
              file=sys.stderr)
        return []
    data = json.loads(REGISTRY_FILE.read_text(encoding="utf-8"))
    return data.get("agents", []) if isinstance(data, dict) else list(data)


def stage(out_dir: Path) -> int:
    agents = load_agents()
    if not agents:
        print("[stage-assets] no agents in registry; nothing to stage.", file=sys.stderr)
        return 1

    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    seen: dict[str, str] = {}
    staged = 0
    skipped_stub = 0
    missing: list[str] = []

    for agent in agents:
        name = agent.get("name", "")
        # Private stubs point at bytes in another repo. There is nothing
        # here to publish, and publishing the pointer would be misleading.
        if agent.get("type") == "stub" or agent.get("_stub_sha256"):
            skipped_stub += 1
            continue

        src_rel = agent.get("_file")
        asset = agent.get("_install_filename")
        if not src_rel or not asset:
            missing.append(name)
            continue

        # Belt: build_registry.py already guarantees this is a bare filename.
        # Suspenders: an asset name with a path separator would silently
        # nest and break every client URL.
        if Path(asset).name != asset:
            print(f"[stage-assets] FATAL: '{name}' has a non-flat asset name "
                  f"{asset!r}.", file=sys.stderr)
            return 1

        # A collision would mean two agents share one download counter and
        # one on-disk install target. Fail the build rather than publish a
        # number that silently merges two agents.
        if asset in seen:
            print(f"[stage-assets] FATAL: asset name collision {asset!r} — "
                  f"'{seen[asset]}' and '{name}' both map to it.", file=sys.stderr)
            return 1
        seen[asset] = name

        src = REPO_ROOT / src_rel
        if not src.exists():
            missing.append(f"{name} ({src_rel})")
            continue

        shutil.copy2(src, out_dir / asset)
        staged += 1

    if missing:
        print(f"[stage-assets] FATAL: {len(missing)} agent(s) have no readable "
              f"source: {', '.join(missing[:5])}"
              f"{' …' if len(missing) > 5 else ''}", file=sys.stderr)
        return 1

    # The manifest lets fetch_download_counts.py map an asset back to an
    # agent without re-deriving the naming rule, and lets a client resolve
    # a download URL from the release alone.
    manifest = {
        "schema": "rar-release-assets/1.0",
        "assets": {seen[a]: a for a in sorted(seen)},
    }
    (out_dir / "release-assets.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(f"[stage-assets] staged {staged} agent asset(s) into {out_dir} "
          f"({skipped_stub} private stub(s) skipped).")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", default=str(DEFAULT_OUT),
                    help="staging directory (default: dist/release-assets)")
    args = ap.parse_args()
    return stage(Path(args.out))


if __name__ == "__main__":
    raise SystemExit(main())
