#!/usr/bin/env python3
"""Federation catalog — consolidate the RAPP ecosystem stores into RAR.

RAR is the single storefront; content keeps its constitutional home
(RAPP Constitution Articles XXVII/XXXI — each artifact has one home):

  rapplications  kody-w/RAPP_Store        bundles (agent + UI/service/state)
  senses         kody-w/RAPP_Sense_Store  per-channel output overlays
  skills         kody-w/rapp-skills, kody-w/rapp-claude-skills

This snapshots those public catalogs into ``state/federation.json`` at
refresh time so the web store reads ONE static file — no client-side API
rate limits, offline-capable after clone. Non-fatal per source: a failed
fetch keeps that section from the previous snapshot instead of erasing
it, and no timestamps are written so the file only changes when the
content changes (lets the refresh workflow skip no-op commits).

Usage:
  python scripts/build_federation.py
"""

from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
FEDERATION_FILE = REPO_ROOT / "state" / "federation.json"

FEDERATION_SCHEMA = "rar-federation/1.0"

RAPP_STORE_INDEX = (
    "https://raw.githubusercontent.com/kody-w/RAPP_Store/main/index.json"
)
SENSE_STORE_INDEX = (
    "https://raw.githubusercontent.com/kody-w/RAPP_Sense_Store/main/index.json"
)
SKILL_REPOS = [
    # (repo, subdirectory holding skill folders, "" = repo root)
    ("kody-w/rapp-skills", ""),
    ("kody-w/rapp-claude-skills", "skills"),
]

MAX_DESCRIPTION = 300


def warn(msg: str) -> None:
    print(f"[federation] {msg}", file=sys.stderr)


def fetch_json(url: str):
    req = urllib.request.Request(
        url, headers={"User-Agent": "rar-federation/1.0"}
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_text(url: str) -> str:
    req = urllib.request.Request(
        url, headers={"User-Agent": "rar-federation/1.0"}
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def clip(text: str) -> str:
    text = " ".join(str(text or "").split())
    if len(text) > MAX_DESCRIPTION:
        return text[: MAX_DESCRIPTION - 1].rstrip() + "…"
    return text


def build_rapplications() -> list[dict] | None:
    """Slim projection of the RAPP_Store catalog."""
    try:
        index = fetch_json(RAPP_STORE_INDEX)
    except (OSError, ValueError, urllib.error.URLError) as exc:
        warn(f"RAPP_Store fetch failed: {exc}")
        return None
    out = []
    for app in index.get("rapplications", []):
        out.append(
            {
                "id": str(app.get("id", "")),
                "name": str(app.get("name", "")),
                "version": str(app.get("version", "")),
                "summary": clip(app.get("summary") or app.get("tagline")),
                "category": str(app.get("category", "")),
                "tags": [str(t) for t in (app.get("tags") or [])][:6],
                "manifest_name": str(app.get("manifest_name", "")),
                "access": str(app.get("access", "public")),
                "singleton_url": str(app.get("singleton_url", "")),
                "singleton_sha256": str(app.get("singleton_sha256", "")),
                "store_url": "https://kody-w.github.io/RAPP_Store/",
                "repo_url": "https://github.com/kody-w/RAPP_Store",
            }
        )
    return sorted(out, key=lambda a: a["id"])


def build_senses() -> list[dict] | None:
    """Slim projection of the RAPP_Sense_Store catalog."""
    try:
        index = fetch_json(SENSE_STORE_INDEX)
    except (OSError, ValueError, urllib.error.URLError) as exc:
        warn(f"RAPP_Sense_Store fetch failed: {exc}")
        return None
    out = []
    for sense in index.get("senses", []):
        out.append(
            {
                "name": str(sense.get("name", "")),
                "publisher": str(sense.get("publisher", "")),
                "version": str(sense.get("version", "")),
                "description": clip(sense.get("description")),
                "delimiter": str(sense.get("delimiter", "")),
                "surfaces": [str(s) for s in (sense.get("surfaces") or [])],
                "url": str(sense.get("url", "")),
                "sha256": str(sense.get("sha256", "")),
                "repo_url": "https://github.com/kody-w/RAPP_Sense_Store",
            }
        )
    return sorted(out, key=lambda s: (s["publisher"], s["name"]))


FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---", re.DOTALL)


def parse_frontmatter(markdown: str) -> dict[str, str]:
    """Minimal YAML frontmatter reader (name/description lines only)."""
    match = FRONTMATTER_RE.match(markdown)
    if not match:
        return {}
    fields: dict[str, str] = {}
    key = None
    for line in match.group(1).splitlines():
        if re.match(r"^[A-Za-z_-]+:", line):
            key, _, value = line.partition(":")
            value = value.strip().strip("\"'")
            # YAML block-scalar markers start a multi-line value
            if value in {">", "|", ">-", "|-", ">+", "|+"}:
                value = ""
            fields[key.strip()] = value
        elif key and line.startswith(("  ", "\t")):
            # folded continuation of a multi-line scalar
            fields[key] = (fields[key] + " " + line.strip()).strip()
    return fields


def build_skills() -> list[dict] | None:
    """Enumerate SKILL.md-bearing folders in the skills repos."""
    out = []
    any_source_ok = False
    for repo, subdir in SKILL_REPOS:
        listing_url = f"https://api.github.com/repos/{repo}/contents/{subdir}"
        try:
            entries = fetch_json(listing_url)
        except (OSError, ValueError, urllib.error.URLError) as exc:
            warn(f"{repo} listing failed: {exc}")
            continue
        any_source_ok = True
        for entry in entries:
            if entry.get("type") != "dir":
                continue
            folder = entry.get("name", "")
            base = f"{subdir}/{folder}" if subdir else folder
            raw = (
                f"https://raw.githubusercontent.com/{repo}/main/"
                f"{base}/SKILL.md"
            )
            try:
                fm = parse_frontmatter(fetch_text(raw))
            except (OSError, urllib.error.URLError):
                continue  # folder without a SKILL.md — not a skill
            out.append(
                {
                    "name": fm.get("name") or folder,
                    "description": clip(fm.get("description")),
                    "repo": repo,
                    "url": f"https://github.com/{repo}/tree/main/{base}",
                    "skill_md_url": raw,
                }
            )
    if not any_source_ok:
        return None
    return sorted(out, key=lambda s: (s["repo"], s["name"]))


def main() -> int:
    previous = {}
    if FEDERATION_FILE.exists():
        try:
            previous = json.loads(FEDERATION_FILE.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            previous = {}

    sections = {
        "rapplications": build_rapplications(),
        "senses": build_senses(),
        "skills": build_skills(),
    }
    snapshot = {"schema": FEDERATION_SCHEMA}
    for key, value in sections.items():
        if value is None:
            kept = previous.get(key, [])
            warn(f"keeping previous '{key}' section ({len(kept)} entries).")
            snapshot[key] = kept
        else:
            snapshot[key] = value

    FEDERATION_FILE.parent.mkdir(parents=True, exist_ok=True)
    FEDERATION_FILE.write_text(
        json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        "[federation] wrote "
        + ", ".join(f"{len(snapshot[k])} {k}" for k in sections)
        + f" to {FEDERATION_FILE.relative_to(REPO_ROOT)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
