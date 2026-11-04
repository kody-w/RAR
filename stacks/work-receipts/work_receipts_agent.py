"""Read-only counts from the Journal's frames.jsonl; exports contain no chat text."""
import csv
import hashlib
import io
import json
import logging
import os
import uuid
from collections import Counter
from datetime import date, datetime, time, timedelta
from pathlib import Path

from agents.basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0", "name": "@kody-w/work_receipts_agent",
    "version": "1.0.0", "display_name": "Work Receipts",
    "description": "Summarises recorded tool use by day and saves local CSV work receipts.",
    "author": "kody-w", "tags": ["journal", "receipts", "local"],
    "category": "productivity", "quality_tier": "community",
    "requires_env": [], "dependencies": ["@rapp/basic_agent"],
}


def _bound(value, end=False):
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Use a date or an ISO timestamp")
    value = value.strip()
    if len(value) == 10:
        parsed = datetime.combine(date.fromisoformat(value), time.max if end else time.min)
    else:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return parsed.astimezone()


def _requested_range(days, since, until):
    if days is not None:
        if isinstance(days, bool) or not isinstance(days, int) or not 1 <= days <= 36500:
            raise ValueError("Days must be a whole number from 1 to 36500")
        if since is not None or until is not None:
            raise ValueError("Use days or explicit dates, not both")
        today = date.today()
        return (today - timedelta(days=days - 1)).isoformat(), today.isoformat()
    return since, until


def _coverage(since, until, turns):
    start, end = _bound(since), _bound(until, True)
    first = start.date() if start else min(
        (date.fromisoformat(turn["_day"]) for turn in turns),
        default=min(date.today(), end.date()) if end else date.today())
    last = end.date() if end else max(
        (date.fromisoformat(turn["_day"]) for turn in turns),
        default=max(date.today(), first))
    lower = start.isoformat() if since is not None and len(since.strip()) != 10 else first.isoformat()
    upper = end.isoformat() if until is not None and len(until.strip()) != 10 else last.isoformat()
    return f"Date range: {lower} through {upper} (local time). "


def read_turns(since=None, until=None):
    start, end = _bound(since), _bound(until, True)
    if start and end and start > end:
        raise ValueError("The start is after the end")
    store = Path(os.environ.get("JOURNAL_STORE") or "~/.brainstem/journal").expanduser()
    path = store if store.name == "frames.jsonl" else store / "frames.jsonl"
    if not path.is_file():
        raise FileNotFoundError("The journal file was not found")
    frames, reactions = {}, {}
    with path.open(encoding="utf-8", errors="replace") as stream:
        for number, line in enumerate(stream, 1):
            if not line.strip():
                continue
            try:
                item = json.loads(line)
            except ValueError as error:
                raise ValueError(f"The journal has an unreadable line at {number}") from error
            if not isinstance(item, dict):
                raise ValueError(f"The journal has a non-record line at {number}")
            fid = item.get("frame_id")
            if not fid:
                continue
            if item.get("kind") == "reaction":
                old = reactions.get(fid)
                if not old or old.get("inferred") or not item.get("inferred"):
                    reactions[fid] = item
            elif item.get("kind") == "turn":
                frames[fid] = item
    selected = []
    for fid, frame in frames.items():
        at = _bound(frame.get("at"))
        if at is None:
            raise ValueError("A recorded turn has no date")
        if (start and at < start) or (end and at > end):
            continue
        frame = dict(frame)
        if fid in reactions:
            frame["edit"] = reactions[fid].get("edit")
        calls = frame.get("agent_calls") or []
        if not isinstance(calls, list) or any(not isinstance(call, dict) for call in calls):
            raise ValueError("A recorded turn has an unreadable tool list")
        frame["agent_calls"] = calls
        frame["_day"] = at.date().isoformat()
        selected.append(frame)
    return sorted(selected, key=lambda frame: (frame["_day"], frame["at"], frame["frame_id"]))


def daily_counts(turns):
    counts = Counter()
    for frame in turns:
        for call in frame["agent_calls"]:
            agent = call.get("agent")
            if agent:
                if not isinstance(agent, str):
                    raise ValueError("A recorded tool name is not text")
                counts[(frame["_day"], agent)] += 1
            else:
                counts[(frame["_day"], "Unidentified tool")] += 1
    return [{"day": day, "tool": tool, "runs": runs}
            for (day, tool), runs in sorted(counts.items())]


def _csv_bytes(rows):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=["day", "tool", "runs"])
    writer.writeheader()
    for row in rows:
        # A journal tool name is untrusted text when opened in a spreadsheet.
        tool = row["tool"]
        if tool.lstrip().startswith(("=", "+", "-", "@")) or tool.startswith(("\t", "\r", "\n")):
            tool = "'" + tool
        writer.writerow({**row, "tool": tool})
    return stream.getvalue().encode("utf-8")


class WorkReceiptsAgent(BasicAgent):
    def __init__(self):
        self.name = "WorkReceipts"
        self.metadata = {
            "name": self.name,
            "description": ("Read the local journal: count recorded tool runs by day, export counts, or find turns; "
                            "use days=7 for the last seven local calendar days including today."),
            "parameters": {"type": "object", "properties": {
                "action": {"type": "string", "enum": ["report", "export", "find"]},
                "since": {"type": "string", "description": "Inclusive YYYY-MM-DD or ISO timestamp; default all recorded days."},
                "until": {"type": "string", "description": "Inclusive YYYY-MM-DD or ISO timestamp."},
                "days": {"type": "integer", "minimum": 1, "maximum": 36500,
                         "description": "Last N local calendar days including today; do not combine with since or until."},
                "text": {"type": "string"}}, "required": ["action"]},
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        try:
            action = kwargs.get("action")
            if action not in ("report", "export", "find"):
                return "Please choose report, export or find. No date range was covered."
            if action == "find":
                text = kwargs.get("text")
                if not isinstance(text, str) or not text.strip():
                    return "Please give a few words to find in the work record. No date range was covered."
            since, until = _requested_range(kwargs.get("days"), kwargs.get("since"), kwargs.get("until"))
            turns = read_turns(since, until)
            coverage = _coverage(since, until, turns)
            if action == "find":
                query = text.strip().casefold()
                hits = []
                for frame in turns:
                    fields = [str(frame.get(key) or "") for key in ("request", "response", "edit")]
                    fields.extend(str(call.get("result") or "") for call in frame["agent_calls"])
                    fields.extend(str(call.get("agent") or "") for call in frame["agent_calls"])
                    match = next((field for field in fields if query in field.casefold()), None)
                    if match is not None:
                        pos = match.casefold().find(query)
                        snippet = " ".join(match[max(0, pos - 60):pos + len(query) + 100].split()).rstrip(".")
                        hits.append(f"{frame['_day']} ({frame['frame_id']}): {snippet}")
                return coverage + (
                    f"Found {len(hits)} matching {'turn' if len(hits) == 1 else 'turns'}: " + "; ".join(hits[:5]) + "."
                    if hits else "No recorded turn mentions those words.")
            rows = daily_counts(turns)
            if action == "report":
                days = Counter(frame["_day"] for frame in turns)
                summaries = []
                for day, count in sorted(days.items()):
                    tools = ", ".join(
                        f"{row['tool']} {row['runs']} {'time' if row['runs'] == 1 else 'times'}"
                        for row in rows if row["day"] == day)
                    summaries.append(f"{day}: {count} turns, {tools or 'no tool runs recorded'}")
                return coverage + (f"Recorded work across {len(turns)} turns: " + "; ".join(summaries) + "."
                                   if turns else "No turns were recorded in that period.")
            output = Path(os.environ.get("WORK_RECEIPTS_DIR") or "~/.brainstem/work-receipts").expanduser()
            journal = Path(os.environ.get("JOURNAL_STORE") or "~/.brainstem/journal").expanduser()
            journal_folder = journal.parent if journal.name == "frames.jsonl" else journal
            if output.resolve() == journal_folder.resolve() or journal_folder.resolve() in output.resolve().parents:
                raise ValueError("Exports must be outside the journal")
            output.mkdir(parents=True, exist_ok=True)
            target = output / ("work-" + uuid.uuid4().hex + ".csv")
            blob = _csv_bytes(rows)
            with target.open("xb") as stream:
                stream.write(blob)
                stream.flush()
                os.fsync(stream.fileno())
            fingerprint = hashlib.sha256(blob).hexdigest()
            with target.with_suffix(".csv.sha256").open("x", encoding="ascii") as stream:
                stream.write(f"{fingerprint}  {target.name}\n")
                stream.flush()
                os.fsync(stream.fileno())
            return coverage + f"Saved daily tool counts to {target}; its check file is {target}.sha256."
        except Exception:
            logging.exception("Work Receipts could not finish")
            return ("Work Receipts could not finish; please check the dates, journal file and export folder."
                    " No date range was covered.")
