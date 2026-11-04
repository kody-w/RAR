"""A local filing desk; dates are hints from labelled text, not legal advice."""
import hashlib
import json
import logging
import os
import re
import threading
from contextlib import contextmanager
from datetime import date, datetime, timedelta
from pathlib import Path

from agents.basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0", "name": "@kody-w/paperwork_desk_agent",
    "version": "1.0.0", "display_name": "Paperwork Desk",
    "description": "Files papers on this computer and finds labelled deadlines and matching passages.",
    "author": "kody-w", "tags": ["papers", "deadlines", "local"],
    "category": "productivity", "quality_tier": "community",
    "requires_env": [], "dependencies": ["@rapp/basic_agent"],
}

_LOCK = threading.RLock()
_MONTH = (r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|"
          r"Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)")
_DATE = re.compile(
    rf"\b(?:\d{{4}}-\d{{1,2}}-\d{{1,2}}|\d{{1,2}}[/-]\d{{1,2}}[/-]\d{{4}}|"
    rf"{_MONTH}\s+\d{{1,2}}(?:st|nd|rd|th)?[,]?\s+\d{{4}}|"
    rf"\d{{1,2}}(?:st|nd|rd|th)?\s+{_MONTH}[,]?\s+\d{{4}})\b", re.I)
_LABEL = re.compile(
    r"\b(renewal|renews?|expiry|expires?|expiration|due|claim\s+by|submit\s+by|file\s+(?:a\s+)?claim)\b", re.I)
_POLICY_PERIOD = re.compile(
    r"\bpolicy\s+period\s*:\s*(" + _DATE.pattern + r")\s+(?:to|through)\s+(" + _DATE.pattern + r")", re.I)


def desk_dir():
    return Path(os.environ.get("PAPERWORK_DIR") or "~/.brainstem/paperwork").expanduser()


@contextmanager
def _locked():
    import fcntl
    with _LOCK:
        desk_dir().mkdir(parents=True, exist_ok=True)
        with (desk_dir() / ".lock").open("a") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            yield


def load_state():
    path = desk_dir() / "desk.jsonl"
    state = {"papers": [], "told": {}}
    if path.exists():
        with path.open(encoding="utf-8") as stream:
            for line in stream:
                if line.strip():
                    state = json.loads(line)
    if not isinstance(state, dict) or not isinstance(state.get("papers"), list) or not isinstance(state.get("told"), dict):
        raise ValueError("The filing list is damaged")
    return state


def _save(state):
    with (desk_dir() / "desk.jsonl").open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(state, ensure_ascii=True) + "\n")
        stream.flush()
        os.fsync(stream.fileno())


def parse_date(value):
    value = re.sub(r"(\d)(st|nd|rd|th)\b", r"\1", value, flags=re.I).replace(",", "")
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%m-%d-%Y",
                "%B %d %Y", "%b %d %Y", "%d %B %Y", "%d %b %Y"):
        try:
            return datetime.strptime(value, fmt).date().isoformat()
        except ValueError:
            pass
    return None


def extract_dates(text):
    found = []
    for line in text.splitlines():
        periods = list(_POLICY_PERIOD.finditer(line))
        for period in periods:
            for label, raw in (("start", period.group(1)), ("expiry", period.group(2))):
                parsed = parse_date(raw)
                item = {"date": parsed, "label": label}
                if parsed and item not in found:
                    found.append(item)
        labels = list(_LABEL.finditer(line))
        for match in _DATE.finditer(line):
            if any(period.start() <= match.start() < period.end() for period in periods):
                continue
            parsed = parse_date(match.group())
            nearby = [label for label in labels
                      if min(abs(match.start() - label.end()), abs(label.start() - match.end())) <= 65]
            if not parsed or not nearby:
                continue
            label = min(nearby, key=lambda item: min(
                abs(match.start() - item.end()), abs(item.start() - match.end()))).group().lower()
            label = ("renewal" if label.startswith("renew") else
                     "expiry" if label.startswith("expir") else
                     "claim by" if label.startswith(("claim", "submit", "file")) else "due")
            item = {"date": parsed, "label": label}
            if item not in found:
                found.append(item)
    return sorted(found, key=lambda item: (item["date"], item["label"]))


def upcoming(state, days=30, today=None):
    if isinstance(days, bool) or not isinstance(days, int) or not 0 <= days <= 36500:
        raise ValueError("Days must be a whole number from zero to 36500")
    today = today or date.today()
    end = (today + timedelta(days=days)).isoformat()
    return sorted(
        [{"file": paper["file"], "title": paper["title"], "sha256": paper["sha256"], **deadline}
         for paper in state["papers"] for deadline in paper["dates"]
         if today.isoformat() <= deadline["date"] <= end],
        key=lambda item: (item["date"], item["file"], item["label"]))


def _extract(path):
    suffix = path.suffix.lower()
    if suffix in {".txt", ".text", ".md"}:
        return path.read_text(encoding="utf-8-sig"), ""
    if suffix == ".pdf":
        try:
            from pypdf import PdfReader
        except ImportError:
            return "", "Only plain text can be read here until the optional PDF reader is installed"
        try:
            text = "\n".join(page.extract_text() or "" for page in PdfReader(str(path)).pages)
        except Exception:
            logging.exception("Paperwork Desk could not read PDF text")
            return "", "The paper was saved, but its PDF text could not be read"
        return text, "" if text.strip() else "The paper has no readable text; scanned pages need a text copy"
    return "", "The image was saved, but images need a text copy to find dates or passages"


class PaperworkDeskAgent(BasicAgent):
    def __init__(self):
        self.name = "PaperworkDesk"
        self.metadata = {
            "name": self.name,
            "description": "File a local paper, list papers, find deadlines, or ask for matching passages; no uploads.",
            "parameters": {"type": "object", "properties": {
                "action": {"type": "string", "enum": ["file", "list", "due", "ask"]},
                "path": {"type": "string"}, "days": {"type": "integer", "minimum": 0, "maximum": 36500, "default": 30},
                "question": {"type": "string"}}, "required": ["action"]},
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        try:
            with _locked():
                state = load_state()
                action = kwargs.get("action")
                if action == "file":
                    path = kwargs.get("path")
                    if not isinstance(path, str) or not path.strip():
                        return "Please give the path to a PDF, text file or image."
                    source = Path(path).expanduser()
                    if not source.is_file():
                        return "That paper could not be found; please check its path."
                    if source.suffix.lower() not in {
                            ".txt", ".text", ".md", ".pdf", ".png", ".jpg", ".jpeg",
                            ".gif", ".webp", ".tif", ".tiff", ".bmp"}:
                        return "Please choose a PDF, plain text file or image."
                    blob = source.read_bytes()
                    sha = hashlib.sha256(blob).hexdigest()
                    existing = next((paper for paper in state["papers"] if paper["sha256"] == sha), None)
                    if existing is not None:
                        dates = extract_dates(existing["text"])
                        if dates != existing["dates"]:
                            existing["dates"] = dates
                            _save(state)
                            return f"Updated {source.name} to {len(dates)} labelled dates; the saved paper was kept."
                        return f"{source.name} is already filed; no second copy was added."
                    folder = desk_dir() / "papers"
                    folder.mkdir(exist_ok=True)
                    target = folder / (sha + source.suffix.lower())
                    try:
                        with target.open("xb") as stream:
                            stream.write(blob)
                            stream.flush()
                            os.fsync(stream.fileno())
                    except FileExistsError:
                        if target.read_bytes() != blob:
                            raise ValueError("A saved paper does not match its fingerprint")
                    text, note = _extract(target)
                    record = {"file": source.name, "sha256": sha, "title": source.stem,
                              "dates": extract_dates(text), "added": datetime.now().astimezone().isoformat(),
                              "text": text, "saved_file": target.name}
                    state["papers"].append(record)
                    _save(state)
                    count = len(record["dates"])
                    return (f"Filed {source.name} with {count} labelled {'date' if count == 1 else 'dates'} on this computer."
                            + (" " + note + "." if note else ""))
                if action == "list":
                    return "Filed papers: " + ("; ".join(p["file"] for p in state["papers"]) or "none yet") + "."
                if action == "due":
                    today = date.today()
                    days = kwargs.get("days", 30)
                    found = upcoming(state, days, today=today)
                    end = today + timedelta(days=days)
                    return (f"Counted from {today.isoformat()} (today, local time) through {end.isoformat()}. "
                            "Upcoming deadlines: " + ("; ".join(
                                f"{item['file']}: {item['label']} {item['date']}" for item in found)
                                or "none in that period") + ".")
                if action == "ask":
                    question = kwargs.get("question")
                    if not isinstance(question, str) or not question.strip():
                        return "Please give a few words to look for in your papers."
                    words = set(re.findall(r"\w+", question.casefold())) - {
                        "the", "a", "an", "is", "my", "what", "when", "where", "does", "do", "of", "to", "in"}
                    hits = []
                    for paper in state["papers"]:
                        text = paper["text"]
                        for start in range(0, len(text), 300):
                            snippet = " ".join(text[start:start + 400].split())
                            score = len(words & set(re.findall(r"\w+", snippet.casefold())))
                            if score:
                                hits.append((score, paper["file"], snippet))
                    hits.sort(key=lambda hit: (-hit[0], hit[1], hit[2]))
                    return ("Matching passages: " + "; ".join(
                        f"{file}: {snippet.rstrip('.')}" for _, file, snippet in hits[:3]) + "."
                            if hits else "No matching passage was found in the readable papers.")
                return "Please choose file, list, due or ask."
        except Exception:
            logging.exception("Paperwork Desk could not finish")
            return "Paperwork Desk could not finish; please check the file, date range and filing folder."

    def system_context(self):
        try:
            with _locked():
                state = load_state()
                today = date.today().isoformat()
                fresh = []
                for item in upcoming(state, 7):
                    key = f"{item['sha256']}:{item['label']}:{item['date']}"
                    if state["told"].get(key) != today:
                        fresh.append(item)
                        state["told"][key] = today
                if not fresh:
                    return None
                _save(state)
                return "Paperwork needs you: " + "; ".join(
                    f"{item['file']} has {item['label']} on {item['date']}" for item in fresh) + "."
        except Exception:
            logging.exception("Paperwork Desk could not check reminders")
            return "Paperwork Desk could not check your deadlines; please check the filing folder."
