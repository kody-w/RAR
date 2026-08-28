#!/usr/bin/env python3
"""harvest_orappter_vault.py — snapshot the orappter demo vault listing as static data.

orappter/orappter.html used to directory-list builder-w/orappter-demo via the
GitHub contents API on every page load (one unauthenticated call per visitor).
This harvester makes that call ONCE, here in CI where a token is available,
and commits the listing; the page reads the static snapshot and pulls file
bodies straight from raw.githubusercontent.com — no API in any visitor's path.

Non-fatal by design: an API problem leaves the existing snapshot untouched.
"""

import json
import os
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "state" / "orappter_demo_vault.json"
SRC = "https://api.github.com/repos/builder-w/orappter-demo/contents/"


def main():
    req = urllib.request.Request(SRC, headers={
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "RAR-vault-harvester",
        **({"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"}
           if os.environ.get("GITHUB_TOKEN") else {}),
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            items = json.load(r)
    except Exception as e:
        print(f"· upstream unreadable ({type(e).__name__}) — existing snapshot left untouched")
        return 0
    files = [{"name": i["name"], "download_url": i["download_url"]}
             for i in items
             if isinstance(i, dict) and i.get("type") == "file"
             and str(i.get("name", "")).endswith(".md") and i.get("download_url")]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(
        {"schema": "rar-orappter-vault/1", "source": SRC, "files": files},
        indent=1, sort_keys=True) + "\n")
    print(f"✓ {OUT.relative_to(ROOT)} — {len(files)} vault docs listed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
