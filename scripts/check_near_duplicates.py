#!/usr/bin/env python3
"""Rhyme check: block agents that near-duplicate what the registry already has.

Two agents "rhyme" when their slug tokens or their description/tags/display-name
tokens overlap strongly (Jaccard similarity over content words). The registry
already blocks exact display-name duplicates; this catches the family that rhymes
without being identical -- deploy / parity_deploy / forge / transpiler for the
same target, for example.

Gate (CI, `--base <sha>`): every agent ADDED or MODIFIED since `base` is compared
against every other agent in registry.json. A rhyme is only allowed when the
changed agent's `__manifest__` says how it relates:

    "supersedes":    ["@pub/older_agent"],              # this replaces it
    "distinct_from": {"@pub/lookalike": "one-line why"} # deliberately different

Pairs designed together are exempt automatically: one lists the other in
`dependencies`, or both belong to the same declared stack directory.

Report (`--report`): cluster the whole registry and print the rhymes it already
holds -- the cleanup list. Never fails; that is what `--base` is for.

Exit 0 = OK, 1 = undeclared rhymes (with the exact declarations that would clear
them), 2 = usage/registry error.
"""

from __future__ import annotations

import argparse
import ast
import itertools
import json
import re
import subprocess
import sys
from pathlib import Path

DEFAULT_REPO_ROOT = Path(__file__).resolve().parent.parent

# Thresholds calibrated on the live registry (2026-09-07, 1,698 agents): they flag
# the copilot_studio_* family and the generated cookbook families, and stay quiet
# for ordinary same-category neighbours.
NAME_THRESHOLD = 0.5
DESC_THRESHOLD = 0.45
MIN_SHARED = 2

STOPWORDS = {
    "agent", "agents", "the", "a", "an", "and", "or", "of", "for", "to", "in", "with",
    "from", "via", "by", "on", "at", "is", "as", "into", "your", "this", "that", "it",
    "be", "use", "uses", "using", "rapp", "you", "are", "one", "any", "all", "each",
    "when", "then", "than", "not", "can", "its", "their", "them", "they", "these",
    "those", "also", "get", "gets", "return", "returns", "run", "runs", "make",
}


def tokens(text: str) -> set[str]:
    return {t for t in re.findall(r"[a-z0-9]+", (text or "").lower())
            if len(t) > 2 and t not in STOPWORDS}


def jaccard(a: set[str], b: set[str]) -> float:
    return len(a & b) / len(a | b) if (a | b) else 0.0


def profile(entry: dict) -> dict:
    """Token profile of one registry entry / manifest."""
    name = str(entry.get("name", ""))
    slug = name.split("/")[-1]
    return {
        "name": name,
        "slug_tokens": tokens(slug.replace("_", " ")),
        "desc_tokens": (tokens(entry.get("description", ""))
                        | tokens(entry.get("display_name", ""))
                        | {str(t).lower() for t in (entry.get("tags") or [])}),
        "dependencies": {str(d) for d in (entry.get("dependencies") or [])},
        "supersedes": {str(d) for d in (entry.get("supersedes") or [])},
        "distinct_from": {str(k): str(v) for k, v in (entry.get("distinct_from") or {}).items()}
                         if isinstance(entry.get("distinct_from"), dict) else {},
        "stack": _stack_dir(str(entry.get("_file", ""))),
    }


def _stack_dir(file_path: str) -> str:
    """agents/@pub/<something>_stacks/<stack>/x.py -> '<pub>/<stack>'; else ''."""
    parts = file_path.split("/")
    if len(parts) >= 5 and parts[0] == "agents" and parts[2].endswith("_stacks"):
        return f"{parts[1]}/{parts[3]}"
    return ""


def rhyme(p: dict, q: dict) -> dict | None:
    """Return the rhyme record for two profiles, or None when they do not rhyme."""
    if p["name"] == q["name"]:
        return None
    shared_slug = p["slug_tokens"] & q["slug_tokens"]
    shared_desc = p["desc_tokens"] & q["desc_tokens"]
    name_j = jaccard(p["slug_tokens"], q["slug_tokens"])
    desc_j = jaccard(p["desc_tokens"], q["desc_tokens"])
    by_name = name_j >= NAME_THRESHOLD and len(shared_slug) >= MIN_SHARED
    by_desc = desc_j >= DESC_THRESHOLD and len(shared_desc) >= MIN_SHARED
    if not (by_name or by_desc):
        return None
    return {
        "a": p["name"], "b": q["name"],
        "name_similarity": round(name_j, 2), "description_similarity": round(desc_j, 2),
        "shared": sorted(shared_slug | shared_desc)[:12],
    }


def declared(p: dict, q: dict) -> str | None:
    """Why a rhyme between p (the changed agent) and q is acceptable, or None."""
    if q["name"] in p["supersedes"]:
        return f"supersedes {q['name']}"
    reason = p["distinct_from"].get(q["name"], "")
    if len(reason.strip()) >= 10:
        return f"distinct_from {q['name']}: {reason.strip()}"
    if q["name"] in p["dependencies"] or p["name"] in q["dependencies"]:
        return "designed together (dependencies)"
    if p["stack"] and p["stack"] == q["stack"]:
        return f"same stack {p['stack']}"
    if q["name"] in q.get("_superseded_by", set()):
        return "already superseded"
    return None


# ── inputs ─────────────────────────────────────────────────────────────────

def load_registry(path: Path) -> list[dict]:
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise SystemExit(f"cannot read registry {path}: {exc}")
    agents = doc.get("agents", doc) if isinstance(doc, dict) else doc
    if not isinstance(agents, list):
        raise SystemExit(f"registry {path} has no 'agents' list")
    return [a for a in agents if isinstance(a, dict) and a.get("name")]


def extract_manifest(py_path: Path) -> dict | None:
    """AST-only read of __manifest__ -- no code execution, same as the registry build."""
    try:
        tree = ast.parse(py_path.read_text(encoding="utf-8"), filename=str(py_path))
    except (OSError, SyntaxError):
        return None
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__manifest__":
                    try:
                        value = ast.literal_eval(node.value)
                    except (ValueError, TypeError):
                        return None
                    return value if isinstance(value, dict) else None
    return None


def _git(repo_root: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(repo_root), *args], capture_output=True,
                          text=True, check=True).stdout


def changed_agent_files(repo_root: Path, base: str) -> list[Path]:
    if not base or set(base) == {"0"}:
        base = _git(repo_root, "rev-parse", "HEAD^").strip()
    out = _git(repo_root, "diff", "--name-status", base, "HEAD")
    files = []
    for line in out.splitlines():
        cols = line.split("\t")
        status, paths = cols[0], cols[1:]
        if not paths:
            continue
        path = paths[-1]  # renames: the new path
        if status[0] in "AMR" and path.startswith("agents/") and path.endswith(".py") \
                and not path.endswith("/basic_agent.py") and "/templates/" not in path:
            files.append(repo_root / path)
    return files


# ── modes ──────────────────────────────────────────────────────────────────

def gate(repo_root: Path, base: str, registry: list[dict]) -> tuple[int, dict]:
    catalog = [profile(e) for e in registry]
    by_name = {c["name"]: c for c in catalog}
    findings, cleared, checked = [], [], []
    for py_path in changed_agent_files(repo_root, base):
        manifest = extract_manifest(py_path)
        if not manifest or not manifest.get("name"):
            continue  # the registry build reports malformed manifests itself
        manifest = dict(manifest)
        manifest.setdefault("_file", str(py_path.relative_to(repo_root)))
        p = profile(manifest)
        checked.append(p["name"])
        for target in p["supersedes"]:
            if target not in by_name:
                findings.append({"agent": p["name"], "error": f"supersedes unknown agent {target!r}"})
        for q in catalog:
            r = rhyme(p, q)
            if not r:
                continue
            why = declared(p, q)
            if why:
                cleared.append({**r, "declared": why})
            else:
                findings.append({"agent": p["name"], "rhymes_with": q["name"], **r})
    return (1 if findings else 0), {"checked": checked, "findings": findings, "cleared": cleared}


def report(registry: list[dict]) -> dict:
    catalog = [profile(e) for e in registry]
    pairs = []
    for p, q in itertools.combinations(catalog, 2):
        r = rhyme(p, q)
        if r and not (declared(p, q) or declared(q, p)):
            pairs.append(r)
    parent: dict[str, str] = {}

    def find(x: str) -> str:
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for r in pairs:
        parent[find(r["a"])] = find(r["b"])
    members: dict[str, set[str]] = {}
    for r in pairs:
        members.setdefault(find(r["a"]), set()).update((r["a"], r["b"]))
    clusters = sorted(members.values(), key=lambda s: (-len(s), sorted(s)[0]))
    publishers: dict[str, int] = {}
    for c in clusters:
        for n in c:
            pub = n.split("/")[0]
            publishers[pub] = publishers.get(pub, 0) + 1
    return {
        "agents": len(catalog), "rhyming_pairs": len(pairs), "clusters": len(clusters),
        "agents_in_clusters": sum(len(c) for c in clusters),
        "by_publisher": dict(sorted(publishers.items(), key=lambda kv: -kv[1])),
        "cluster_list": [{"size": len(c), "members": sorted(c)} for c in clusters],
        "thresholds": {"name": NAME_THRESHOLD, "description": DESC_THRESHOLD, "min_shared": MIN_SHARED},
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--base", help="git ref to diff against (CI gate mode)")
    parser.add_argument("--report", action="store_true", help="cluster the whole registry; never fails")
    parser.add_argument("--repo-root", default=str(DEFAULT_REPO_ROOT))
    parser.add_argument("--registry", default="registry.json")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument("--top", type=int, default=12, help="report: clusters to print")
    args = parser.parse_args()
    repo_root = Path(args.repo_root).resolve()
    registry = load_registry(repo_root / args.registry)

    if args.report:
        doc = report(registry)
        if args.json:
            print(json.dumps(doc, indent=2))
            return 0
        print(f"Rhyme report: {doc['agents']} agents, {doc['rhyming_pairs']} rhyming pairs, "
              f"{doc['clusters']} clusters covering {doc['agents_in_clusters']} agents")
        print("by publisher: " + ", ".join(f"{k} {v}" for k, v in doc["by_publisher"].items()))
        for c in doc["cluster_list"][: args.top]:
            print(f"\n[{c['size']}] " + ", ".join(c["members"][:10]) + (" ..." if c["size"] > 10 else ""))
        return 0

    if not args.base:
        parser.error("pass --base <sha> (gate) or --report")
    code, doc = gate(repo_root, args.base, registry)
    if args.json:
        print(json.dumps(doc, indent=2))
        return code
    if not doc["checked"]:
        print("OK no changed agent artifacts to rhyme-check")
        return 0
    for c in doc["cleared"]:
        print(f"ok  {c['a']} ~ {c['b']} ({c['declared']})")
    for f in doc["findings"]:
        if "error" in f:
            print(f"ERROR {f['agent']}: {f['error']}")
            continue
        print(f"ERROR {f['agent']} rhymes with {f['rhymes_with']} "
              f"(name {f['name_similarity']}, description {f['description_similarity']}; shared: {', '.join(f['shared'])})")
        print(f"      declare in __manifest__ either  \"supersedes\": [\"{f['rhymes_with']}\"]"
              f"  or  \"distinct_from\": {{\"{f['rhymes_with']}\": \"<why this is a different agent>\"}}")
    if code:
        print(f"FAIL {len(doc['findings'])} undeclared rhyme(s) across {len(doc['checked'])} changed agent(s)")
    else:
        print(f"OK {len(doc['checked'])} changed agent(s) carry no undeclared rhymes")
    return code


if __name__ == "__main__":
    sys.exit(main())
