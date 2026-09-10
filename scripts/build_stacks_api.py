#!/usr/bin/env python3
"""build_stacks_api.py — generate api/v1/stacks.json from stacks/*/pack.json.

Additive, read-only over the rest of the registry: does NOT touch
registry.json, agents/, or anything build_registry.py / build_static_api.py
produce. Run it whenever a stack under stacks/ is added, removed, or its
pack.json changes; commit the regenerated api/v1/stacks.json alongside.

    python3 scripts/build_stacks_api.py [--check]
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STACKS_DIR = ROOT / "stacks"
OUT_PATH = ROOT / "api" / "v1" / "stacks.json"
RAW_BASE = "https://raw.githubusercontent.com/kody-w/RAR/main"


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def build() -> dict:
    stacks = []
    for stack_dir in sorted(p for p in STACKS_DIR.iterdir() if p.is_dir()):
        pack_path = stack_dir / "pack.json"
        if not pack_path.exists():
            continue
        pack = json.loads(pack_path.read_text(encoding="utf-8"))
        slug = stack_dir.name
        files = {}
        for fname, meta in pack.get("files", {}).items():
            files[fname] = {
                **meta,
                "raw_url": f"{RAW_BASE}/stacks/{slug}/{fname}",
            }
        stacks.append({
            "name": pack.get("name", slug),
            "display_name": pack.get("display_name", slug),
            "version": pack.get("version"),
            "purpose": pack.get("purpose"),
            "slug": slug,
            "directory_url": f"{RAW_BASE}/stacks/{slug}/",
            "pack_url": f"{RAW_BASE}/stacks/{slug}/pack.json",
            "readme_url": f"{RAW_BASE}/stacks/{slug}/README.md",
            "files": files,
            "install": pack.get("install"),
            "workspace_spec": pack.get("workspace_spec"),
            "egg_variant": pack.get("egg_variant"),
            "modes": pack.get("modes"),
            "agents_in_pack": pack.get("agents_in_pack"),
            "agents_in_template": pack.get("agents_in_template"),
            "see_also": pack.get("see_also", []),
        })

    return {
        "schema": "rar-stacks/1.0",
        "description": (
            "Every RAR stack — a drop-in pack (agent(s) + optional .egg + "
            "pack.json sha256 manifest) that plants something bigger than a "
            "single agent: a neighborhood, a fleet controller, a lifecycle "
            "kit, or a private rapp-workspace/1.1 vault. Each stack's files "
            "are individually sha256-pinned and independently fetchable — "
            "a client can take a whole stack or cherry-pick files across "
            "stacks since every entry is a content-addressed manifest."
        ),
        "generated": now(),
        "count": len(stacks),
        "self_url": f"{RAW_BASE}/api/v1/stacks.json",
        "stacks": stacks,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true",
                        help="compute everything but write nothing")
    args = parser.parse_args()

    doc = build()
    if args.check:
        print(json.dumps(doc, indent=2))
        return 0

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {OUT_PATH} ({doc['count']} stacks)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
