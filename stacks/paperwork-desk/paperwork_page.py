"""Local metadata-only page at /api/paperwork/."""
import json
import logging
import os
from contextlib import nullcontext
from datetime import date, timedelta
from pathlib import Path

name = "paperwork"


def _papers():
    folder = Path(os.environ.get("PAPERWORK_DIR") or "~/.brainstem/paperwork").expanduser()
    path = folder / "desk.jsonl"
    if not path.exists():
        return []
    lock_path = folder / ".lock"
    with lock_path.open("r") if lock_path.exists() else nullcontext() as lock:
        if lock is not None:
            import fcntl
            fcntl.flock(lock, fcntl.LOCK_SH)
        state = {"papers": []}
        with path.open(encoding="utf-8") as stream:
            for line in stream:
                if line.strip():
                    state = json.loads(line)
        if not isinstance(state, dict) or not isinstance(state.get("papers"), list):
            raise ValueError("The filing list is damaged")
        return [{key: paper[key] for key in ("file", "sha256", "title", "dates", "added")}
                for paper in state["papers"]]


def handle(method, path, body):
    if method != "GET":
        return {"error": "This page only shows papers; use chat to file one."}, 405
    if path not in ("", "/", None):
        return {"error": "That paperwork page was not found."}, 404
    try:
        papers = _papers()
        today = date.today()
        end = (today + timedelta(days=30)).isoformat()
        upcoming = sorted(
            [{"file": paper["file"], "title": paper["title"], "sha256": paper["sha256"], **deadline}
             for paper in papers for deadline in paper["dates"]
             if today.isoformat() <= deadline["date"] <= end],
            key=lambda item: (item["date"], item["file"], item["label"]))
        return {"upcoming_deadlines": upcoming, "papers": papers}, 200
    except Exception:
        logging.exception("Paperwork page could not read the desk")
        return {"error": "Your filing list could not be read; please check the filing folder."}, 500
