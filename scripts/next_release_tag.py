#!/usr/bin/env python3
"""Derive the next release tag from the tags that already exist.

Why this is a script and not three lines of shell
-------------------------------------------------
It used to be `EXISTING=$(git tag -l 'v*' | wc -l); NEXT=$((EXISTING + 1))`.
Counting tags is not versioning, and every way it was wrong could only be
discovered by cutting a real release:

  * Canary and hotfix tags match `v*` too, so each one inflated the count and
    the next seasonal release silently skipped a major number.
  * Delete any tag and the count walks *backwards* onto a version that already
    exists — `createRef` then 422s partway through the job, after the registry
    has already been stamped and pushed.
  * `hotfix` produced `v{count+1}.0.1`, minting a brand new major for a patch.
    A hotfix to v3.0.0 has to be v3.0.1; that is the whole point of a hotfix.

So the rule is now derived from the highest version that actually exists, and
it is unit-tested — a release tag is not something you get to test in
production.

Rules
-----
  seasonal  next major after the highest stable release  (v3.0.0 -> v4.0.0)
  hotfix    patch bump of the highest stable release      (v3.0.0 -> v3.0.1)
  canary    prerelease of the *upcoming* major, dated     (v4.0.0-canary.20260801)

Stable means "no prerelease suffix". Canaries never advance the stable line:
they are named for the major they preview, so cutting canaries all week does
not push the eventual seasonal release into a different number.

Usage
-----
    python scripts/next_release_tag.py --type seasonal
    python scripts/next_release_tag.py --type canary --date 20260801
    python scripts/next_release_tag.py --type hotfix --tags v1.0.0,v2.0.0
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys

# v1.2.3 with an optional prerelease suffix (v4.0.0-canary.20260801).
# Build metadata (+foo) is not used by this repo and is deliberately not parsed:
# accepting a shape we never emit would only widen what counts as a valid tag.
TAG_RE = re.compile(r"^v(\d+)\.(\d+)\.(\d+)(?:-(.+))?$")


def parse(tag: str):
    """(major, minor, patch, prerelease|None), or None if not a version tag."""
    m = TAG_RE.match(tag.strip())
    if not m:
        return None
    return (int(m.group(1)), int(m.group(2)), int(m.group(3)), m.group(4))


def read_tags() -> list[str]:
    """Every tag in the repo. Requires fetch-depth: 0 to be meaningful."""
    out = subprocess.run(["git", "tag", "-l"], capture_output=True, text=True, check=True)
    return [t for t in out.stdout.split() if t]


def next_tag(tags: list[str], release_type: str, date: str | None) -> str:
    parsed = [p for p in (parse(t) for t in tags) if p]
    stable = [p for p in parsed if p[3] is None]
    existing = {t.strip() for t in tags}

    if release_type == "hotfix":
        if not stable:
            # Nothing to patch. Silently promoting this to v1.0.0 would publish
            # a first release labelled "hotfix", so make the operator pick.
            raise SystemExit(
                "no stable release exists to patch — use --type seasonal for the "
                "first release"
            )
        maj, minor, patch, _ = max(stable)
        return f"v{maj}.{minor}.{patch + 1}"

    # seasonal and canary both target the next major after the stable line.
    base = max(stable)[0] if stable else 0
    if release_type == "seasonal":
        tag = f"v{base + 1}.0.0"
        if tag in existing:
            # Only reachable if the stable line is not contiguous, which means
            # a tag was deleted or hand-created. Refuse rather than collide.
            raise SystemExit(f"{tag} already exists — refusing to reissue a version")
        return tag

    if release_type == "canary":
        if not date:
            raise SystemExit("--date is required for a canary (YYYYMMDD)")
        stem = f"v{base + 1}.0.0-canary.{date}"
        if stem not in existing:
            return stem
        # Second and later canary on the same day. Suffix rather than fail:
        # cutting two canaries in one day is normal and must not need a human.
        n = 2
        while f"{stem}.{n}" in existing:
            n += 1
        return f"{stem}.{n}"

    raise SystemExit(f"unknown release type: {release_type}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--type", required=True,
                    choices=["seasonal", "hotfix", "canary"])
    ap.add_argument("--date", help="YYYYMMDD, canary only (defaults to today UTC)")
    ap.add_argument("--tags", help="comma-separated tags; defaults to `git tag -l`")
    args = ap.parse_args()

    tags = args.tags.split(",") if args.tags else read_tags()

    date = args.date
    if args.type == "canary" and not date:
        # Only consulted for canaries, and only when the caller did not pin it,
        # so the tested path stays deterministic.
        from datetime import datetime, timezone
        date = datetime.now(timezone.utc).strftime("%Y%m%d")

    print(next_tag(tags, args.type, date))
    return 0


if __name__ == "__main__":
    sys.exit(main())
