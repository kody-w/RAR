"""Rooms — a group chat of AI seats inside this Brainstem. The kernel is never edited.

Each seat has its own personality and its own private memory. One helper Brainstem (the
same pinned kernel, hardlinked, fingerprint-checked) plays every seat in turn by swapping
three links before each answer:
    soul.md         -> seats/<seat>/soul.md      (personality)
    .brainstem_data -> seats/<seat>/memory       (private memory)
    agents/         -> the room's agents          (SeatNotes)

The conversation is an append-only log (rooms/<room>.jsonl) with a bookmark per room, so
work picks up where it stopped. Every message has an id and is answered once. A hop limit
and a turn budget stop AI-to-AI reply storms; a seat that starts with ASK_OWNER hands
control back to the owner.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/rooms_agent",
    "version": "1.0.0",
    "display_name": "Rooms",
    "description": "Group chat of AI seats on one Brainstem: each seat has its own personality and private memory, with turn budgets, pick-up-where-it-stopped and hand-back to the owner.",
    "author": "kody-w",
    "tags": ["rooms", "multiplayer", "multi-agent", "pair", "queue"],
    "category": "core",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

import fcntl
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.request
import uuid
from pathlib import Path

from agents.basic_agent import BasicAgent

KERNEL_FILES = ["brainstem.py", "local_storage.py", "VERSION", "requirements.txt", "index.html"]
MAX_HOPS = 6
NAME = re.compile(r"^[a-z][a-z0-9_-]{0,23}$")


def _home():
    # This agent lives in <distro>/agents/; the distro folder holds the pinned kernel.
    return Path(__file__).resolve().parent.parent


def _base():
    d = _home() / "rooms-data"
    for sub in ("seats", "rooms"):
        (d / sub).mkdir(parents=True, exist_ok=True)
    return d


def _owners(port):
    out = subprocess.run(["lsof", "-tnP", f"-iTCP:{port}", "-sTCP:LISTEN"],
                         capture_output=True, text=True).stdout.split()
    return {int(p) for p in out}


def _relink(link, target):
    tmp = link.with_name(link.name + ".swap")
    if tmp.is_symlink() or tmp.exists():
        tmp.unlink()
    os.symlink(target, tmp)
    os.replace(tmp, link)  # atomic: never a moment with no link


def _write_json(p, obj):
    tmp = p.with_suffix(".tmp")
    tmp.write_text(json.dumps(obj, indent=1))
    os.replace(tmp, p)


class Worker:
    """The helper Brainstem that plays the seats."""

    def __init__(self):
        self.kd, self.b = _home(), _base()
        self.w = self.b / "worker"
        self.state = self.b / "worker.json"

    def up(self):
        w, kd = self.w, self.kd
        (w / "agents").mkdir(parents=True, exist_ok=True)
        (self.b / "room-agents").mkdir(exist_ok=True)
        for f in KERNEL_FILES:
            if (kd / f).exists() and not (w / f).exists():
                os.link(kd / f, w / f)
        if hashlib.sha256((w / "brainstem.py").read_bytes()).hexdigest() != \
           hashlib.sha256((kd / "brainstem.py").read_bytes()).hexdigest():
            raise RuntimeError("the helper's kernel does not match this Brainstem's kernel")
        for f in ("basic_agent.py", "seat_notes_agent.py"):
            src, dst = kd / "agents" / f, self.b / "room-agents" / f
            if src.exists():
                if dst.exists():
                    dst.unlink()
                os.link(src, dst)
        if not (w / "agents" / "basic_agent.py").exists():
            os.link(kd / "agents" / "basic_agent.py", w / "agents" / "basic_agent.py")
        (w / "agents" / "__init__.py").touch()
        for f in (".copilot_token", ".copilot_session"):
            if (kd / f).exists():
                shutil.copy2(kd / f, w / f)
                os.chmod(w / f, 0o600)
        if self.state.exists():
            st = json.loads(self.state.read_text())
            if st["pid"] in _owners(st["port"]):
                return st["port"]
        port = next(p for p in range(7600, 7700) if not _owners(p))
        if not (w / "soul.md").is_symlink():
            (self.b / "blank-soul.md").write_text("You are a seat in a group room.\n")
            _relink(w / "soul.md", self.b / "blank-soul.md")
            (self.b / "blank-memory").mkdir(exist_ok=True)
            _relink(w / ".brainstem_data", self.b / "blank-memory")
        env = {**os.environ, "PORT": str(port), "PYTHONUNBUFFERED": "1",
               "AGENTS_PATH": str(self.b / "room-agents"), "SOUL_PATH": str(w / "soul.md")}
        env.pop("BRAINSTEM_LAN_MODE", None)  # the helper is loopback-only
        proc = subprocess.Popen([sys.executable, str(w / "brainstem.py")], cwd=w, env=env,
                                stdout=open(self.b / "worker.log", "w"), stderr=subprocess.STDOUT,
                                start_new_session=True)
        for _ in range(450):
            if proc.poll() is not None:
                raise RuntimeError(f"the helper Brainstem exited; see {self.b / 'worker.log'}")
            if proc.pid in _owners(port):
                _write_json(self.state, {"port": port, "pid": proc.pid})
                return port
            time.sleep(0.2)
        proc.kill()
        raise RuntimeError("the helper Brainstem did not start in time")

    def ask(self, seat, prompt, history):
        port = self.up()
        sd = self.b / "seats" / seat
        _relink(self.w / "soul.md", sd / "soul.md")
        _relink(self.w / ".brainstem_data", sd / "memory")
        body = json.dumps({"user_input": prompt, "conversation_history": history}).encode()
        req = urllib.request.Request(f"http://127.0.0.1:{port}/chat", body,
                                     {"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=300) as r:
            return json.load(r).get("response", "")

    def stop(self):
        if self.state.exists():
            st = json.loads(self.state.read_text())
            if st["pid"] in _owners(st["port"]):  # only ever stop the process we started
                os.kill(st["pid"], 15)
            self.state.unlink()
            return True
        return False


def _log(room):
    return _base() / "rooms" / f"{room}.jsonl"


def _read(room):
    p = _log(room)
    return [json.loads(l) for l in p.read_text().splitlines() if l.strip()] if p.exists() else []


def _post(room, sender, text, hop=0, reply_to=None):
    msg = {"id": uuid.uuid4().hex[:12], "at": time.strftime("%H:%M:%S"), "from": sender,
           "text": text, "hop": hop, "reply_to": reply_to}
    with open(_log(room), "a") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.write(json.dumps(msg) + "\n")
        fcntl.flock(f, fcntl.LOCK_UN)
    return msg


def _meta(room):
    p = _base() / "rooms" / f"{room}.room.json"
    return json.loads(p.read_text()) if p.exists() else None


class RoomsAgent(BasicAgent):
    def __init__(self):
        self.name = "Rooms"
        self.metadata = {
            "name": self.name,
            "description": (
                "Run a group chat of AI seats. Actions: 'add_seat' (seat + personality), "
                "'start' a room (room + seats, optional goal), 'say' something into a room as the owner "
                "(use @seat to wake one seat), 'run' the room so the seats talk (optional budget = max "
                "turns, default 6), 'show' the room's transcript, 'list' rooms and seats, 'stop' the helper."),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string",
                               "enum": ["add_seat", "start", "say", "run", "show", "list", "stop"]},
                    "seat": {"type": "string", "description": "seat name, lowercase, e.g. alice"},
                    "personality": {"type": "string", "description": "who this seat is and how it talks"},
                    "room": {"type": "string", "description": "room name, lowercase"},
                    "seats": {"type": "array", "items": {"type": "string"},
                              "description": "seats in the room"},
                    "goal": {"type": "string", "description": "what the room is trying to reach"},
                    "text": {"type": "string", "description": "what the owner says"},
                    "budget": {"type": "integer", "description": "max seat turns for this run"},
                },
                "required": ["action"],
            },
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kw) -> str:
        try:
            return getattr(self, "_" + kw.get("action", "list"))(**kw)
        except (AttributeError, TypeError):
            return "Unknown action. Use add_seat, start, say, run, show, list or stop."
        except Exception as e:
            return f"Rooms hit a problem: {e}"

    def _add_seat(self, seat="", personality="", **_):
        seat = seat.strip().lower()
        if not NAME.match(seat) or not personality.strip():
            return "A seat needs a short lowercase name and a personality."
        sd = _base() / "seats" / seat
        (sd / "memory").mkdir(parents=True, exist_ok=True)
        (sd / "soul.md").write_text(
            f"You are {seat}, a seat in a group room with other AIs and their owner.\n{personality.strip()}\n"
            "Your SeatNotes notebook is private to you. Keep answers under 80 words.\n")
        return f"Seat {seat} is ready, with its own private memory."

    def _start(self, room="", seats=None, goal="", **_):
        room = room.strip().lower()
        seats = [s.strip().lower() for s in (seats or [])]
        if not NAME.match(room) or not seats:
            return "A room needs a short lowercase name and at least one seat."
        missing = [s for s in seats if not (_base() / "seats" / s / "soul.md").exists()]
        if missing:
            return f"Add these seats first: {', '.join(missing)}."
        _write_json(_base() / "rooms" / f"{room}.room.json", {"seats": seats, "goal": goal})
        if goal:
            _post(room, "owner", goal)
        return f"Room {room} is open with {', '.join(seats)}." + (" Say 'run' to let them talk." if goal else "")

    def _say(self, room="", text="", **_):
        if not _meta(room):
            return f"There is no room called {room}."
        if not text.strip():
            return "Say what?"
        _post(room, "owner", text.strip())
        return f"Posted to {room}. Say 'run' to let the seats answer."

    def _run(self, room="", budget=6, **_):
        meta = _meta(room)
        if not meta:
            return f"There is no room called {room}."
        seats, goal = meta["seats"], meta.get("goal", "")
        sp = _base() / "rooms" / f"{room}.state.json"
        st = json.loads(sp.read_text()) if sp.exists() else {"offset": 0, "done": []}
        worker, turns, said, why = Worker(), 0, [], "the room is quiet"
        budget = max(1, min(int(budget or 6), 20))
        while True:
            log = _read(room)
            if st["offset"] >= len(log):
                break
            i, msg = st["offset"], log[st["offset"]]
            mentioned = [s for s in seats if f"@{s}" in msg["text"]]
            if msg["from"] == "owner":
                wake = mentioned or seats
            else:  # a seat speaks: wake who it named, else the next seat in order
                wake = mentioned or [seats[(seats.index(msg["from"]) + 1) % len(seats)]] \
                    if msg["from"] in seats and len(seats) > 1 else mentioned
            wake = [s for s in wake if s != msg["from"]]
            stop = False
            for seat in wake:
                key = f'{msg["id"]}:{seat}'
                if key in st["done"]:
                    continue
                if msg["hop"] >= MAX_HOPS:
                    why = f"hop limit {MAX_HOPS} reached"
                    continue
                if turns >= budget:
                    why, stop = f"turn budget {budget} spent; say 'run' to continue", True
                    break
                hist = [{"role": "assistant" if m["from"] == seat else "user",
                         "content": m["text"] if m["from"] == seat else f'{m["from"]}: {m["text"]}'}
                        for m in log[:i]]
                prompt = (f"[Room '{room}'. You are {seat}. Others: {', '.join(x for x in seats if x != seat)}. "
                          f"Goal: {goal or 'help the owner'}. Under 80 words. Name a seat with @name to hand "
                          f"it the turn. If the goal is reached start with DONE:. If the owner must decide, "
                          f"start with ASK_OWNER:]\n{msg['from']}: {msg['text']}")
                try:
                    reply = worker.ask(seat, prompt, hist).strip()
                except Exception as e:
                    with open(_base() / "rooms" / f"{room}.dead.jsonl", "a") as f:
                        f.write(json.dumps({"key": key, "error": str(e)}) + "\n")
                    reply = ""
                st["done"].append(key)
                turns += 1
                if reply:
                    _post(room, seat, reply, msg["hop"] + 1, msg["id"])
                    said.append(f"{seat}: {reply}")
                    head = reply.upper()
                    if head.startswith("ASK_OWNER"):
                        why, stop = f"{seat} is asking you to decide", True
                    elif head.startswith("DONE"):
                        why, stop = f"{seat} says the goal is reached", True
                if stop:
                    break
            if stop:
                if not why.startswith("turn budget"):
                    # DONE or ASK_OWNER closes the old queue: the owner's next message comes first.
                    st["offset"] = len(_read(room))
                break
            st["offset"] = i + 1
            _write_json(sp, st)
        _write_json(sp, st)
        return "\n\n".join(said + [f"(Stopped: {why}.)"]) if said else f"Nothing new to answer ({why})."

    def _show(self, room="", **_):
        log = _read(room)
        if not log:
            return f"Room {room} is empty or does not exist."
        return "\n".join(f'{m["at"]} {m["from"]}: {m["text"]}' for m in log[-30:])

    def _list(self, **_):
        b = _base()
        rooms = sorted(p.name[:-10] for p in (b / "rooms").glob("*.room.json"))
        seats = sorted(p.name for p in (b / "seats").iterdir() if p.is_dir())
        return f"Rooms: {', '.join(rooms) or 'none'}. Seats: {', '.join(seats) or 'none'}."

    def _stop(self, **_):
        return "The helper Brainstem is stopped." if Worker().stop() else "The helper was not running."
