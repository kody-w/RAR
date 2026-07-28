#!/usr/bin/env python3
"""
resume_review.py — carry on a critic review inside your own brainstem.

The critic panel publishes its proof as a frame-chunked transcript. This takes
that transcript's handoff frame and replays it into a local brainstem, so the
conversation starts with everything the panel saw — the run output, the failures,
the scores — instead of from nothing.

    python scripts/resume_review.py @aibast-agents-library/account_risk_assessment
    python scripts/resume_review.py <agent> --ask "What would you fix first?"
    python scripts/resume_review.py <agent> --print   # just show the payload
"""

import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSCRIPTS = ROOT / "state" / "critic_transcripts"
BRAINSTEM = "http://127.0.0.1:7071"


def norm(s):
    return re.sub(r"[-\s]+", "_", (s or "").strip().lower())


def find_transcript(agent):
    slug = norm(agent).strip("@").replace("/", "__")
    p = TRANSCRIPTS / f"{slug}.json"
    if p.exists():
        return p
    hits = [q for q in TRANSCRIPTS.glob("*.json") if slug.split("__")[-1] in q.stem]
    return hits[0] if hits else None


def main():
    ap = argparse.ArgumentParser(description="Resume a critic review on your local brainstem.")
    ap.add_argument("agent")
    ap.add_argument("--ask", help="override the opening question")
    ap.add_argument("--print", dest="show", action="store_true", help="print the payload instead of sending")
    ap.add_argument("--url", default=BRAINSTEM)
    a = ap.parse_args()

    path = find_transcript(a.agent)
    if not path:
        print(f"No transcript for {a.agent}. Run: python scripts/critic_review.py --agent {a.agent} --force",
              file=sys.stderr)
        return 1

    doc = json.loads(path.read_text())
    frame = next((f for f in doc.get("frames", []) if f.get("kind") == "handoff"), None)
    if not frame:
        print(f"{path} has no handoff frame.", file=sys.stderr)
        return 1
    data = json.loads(frame["text"])
    payload = {
        "user_input": a.ask or data["user_input"],
        "conversation_history": data["conversation_history"],
    }
    if a.show:
        print(json.dumps(payload, indent=1))
        return 0

    print(f"→ resuming the review of {doc.get('agent')} on {a.url}\n", file=sys.stderr)
    req = urllib.request.Request(f"{a.url}/chat", data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            res = json.loads(r.read())
    except Exception as e:
        print(f"Could not reach a brainstem at {a.url}: {type(e).__name__}. Is it running?", file=sys.stderr)
        return 1
    print(res.get("response") or res.get("error") or json.dumps(res)[:800])
    return 0


if __name__ == "__main__":
    sys.exit(main())
