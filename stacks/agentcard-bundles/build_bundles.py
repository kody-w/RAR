#!/usr/bin/env python3
"""Build one .agentcard for every RAR agent that needs something a phone's Python lacks (status: staging).

Writes stacks/agentcard-bundles/cards/<publisher path>/<agent stem>.agentcard and index.json
(rapp-static-api style: one input = agents/, one idempotent build, one JSON index).
Agents that need nothing extra get no card (the bare agent.py already works).
Run in a job with NO write token: bundling loads each agent to read its metadata.
"""
import json, sys, traceback
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
import bundle_card as B


def main(out=HERE / "cards", cache=None):
    reg = json.loads((ROOT / "registry.json").read_text())
    rows = []
    for a in reg["agents"]:
        src = ROOT / a["_file"]
        try:
            groups = B.import_groups(src.read_text(encoding="utf-8"))
        except Exception as e:
            rows.append({"agent": a["name"], "status": "unreadable", "why": str(e)[:200]}); continue
        if not any(B.needs(m) for mods, _, _ in groups for m in mods):
            continue
        if not src.name.endswith("_agent.py"):
            rows.append({"agent": a["name"], "status": "file name is not *_agent.py (cards need it)"}); continue
        try:
            card, rep = B.bundle(src, author=a["name"].split("/")[0].lstrip("@"), cache=cache)
        except ModuleNotFoundError as e:
            pure = B.pure_wheels(B.DIST.get(e.name, e.name), cache) if cache else None
            rows.append({"agent": a["name"], "status": "needs compiled code (not for iPhone)" if pure is None else "failed",
                         "why": f"cannot start without {e.name}"}); continue
        except BaseException as e:
            rows.append({"agent": a["name"], "status": "failed", "why": (str(e) or type(e).__name__)[:200]}); continue
        row = {"agent": a["name"], "file": a["_file"], "carried": rep["carried"], "left_out": rep["left_out"],
               "skipped_optional": rep["skipped_optional"]}
        if len([x for x in card.get("files", [])]) and not rep["left_out"]:
            rel = Path(a["_file"]).relative_to("agents").with_suffix(".agentcard")
            dest = out / rel; dest.parent.mkdir(parents=True, exist_ok=True)
            sys.path.insert(0, str(HERE / "vendor")); import agentcard_core as cards
            dest.write_text(cards.to_json(card))
            row.update(status="card", agentcard=str(dest.relative_to(ROOT)))
        elif rep["left_out"]:
            row["status"] = "needs compiled code (not for iPhone)"
        else:
            row["status"] = "nothing to carry"
        rows.append(row)
    idx = {"schema": "rapp-agentcard-bundles/1", "status": "staging", "count": sum(r.get("status") == "card" for r in rows), "agents": rows}
    (HERE / "index.json").write_text(json.dumps(idx, indent=1) + "\n")
    return idx


if __name__ == "__main__":
    idx = main(cache=Path(sys.argv[1]) if len(sys.argv) > 1 else None)
    from collections import Counter
    print(json.dumps(Counter(r["status"] for r in idx["agents"])))
