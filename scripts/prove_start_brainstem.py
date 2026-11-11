#!/usr/bin/env python3
"""Prove the Start Brainstem agent on a clean machine: nothing installed -> asks -> installs -> a Brainstem answers.

Run by .github/workflows/prove-start-brainstem.yml on fresh Windows, Linux and macOS machines. It runs the
catalog's own agent file, which downloads the public installer. Not for a machine that already has a Brainstem.
"""
import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "agents" / "@rapp"))
from start_brainstem_agent import LOG, StartBrainstemAgent  # noqa: E402


def main() -> int:
    agent = StartBrainstemAgent()
    first = json.loads(agent.perform())
    print("1 with nothing installed:", first["status"], flush=True)
    if first["status"] != "ask":
        print("this machine is not clean:", first)
        return 1
    second = json.loads(agent.perform(yes=True, wait=900))
    print("2 after yes:", json.dumps(second)[:600], flush=True)
    if second["status"] != "up":
        if LOG.exists():
            print("--- installer log tail ---")
            print(LOG.read_bytes()[-4000:].decode("utf-8", "replace"))
        return 1
    health = json.loads(urllib.request.urlopen("http://localhost:7071/health", timeout=10).read())
    print("3 health:", health.get("status"), "version", health.get("version"), "agents", len(health.get("agents") or []), flush=True)
    third = json.loads(agent.perform())
    print("4 asked again:", third["say"], flush=True)
    if "already running" not in third["say"]:
        return 1
    print("PROVED: nothing installed -> asked -> installed -> a Brainstem answered -> second ask changed nothing")
    return 0


if __name__ == "__main__":
    sys.exit(main())
