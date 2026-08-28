"""
Flight Recorder -- a local black box for your brainstem.

Drop this file into your agents/ folder and, from that moment on, EVERY conversation
through your brainstem -- whoever or whatever is on the other end: you in the browser,
another AI over the API, a script, an MCP bridge -- gets recorded BOTH SIDES and stored
locally, in plain files that YOU own. Your conversational estate lives on your hardware,
not inside whatever model happened to be chatting.

How it captures everything (no engine edits, grail untouched): the grail's rule is that
all conversation flows through POST /chat. On load, this agent finds the running Flask
app in-process and transparently WRAPS the /chat route once (idempotent). The wrapper
reads the incoming request (the caller's side) and the outgoing response (the brainstem's
side) and appends one record to an append-only black box. It never alters the response and
never breaks a request -- every recording step is wrapped in try/except.

It's also a normal agent, so you steer it by talking to your brainstem:
  "flight recorder status" / "where is my black box?" / "stats"
  "search my conversations for <x>" / "show my last 5 conversations"
  "export my conversation history"        -> a readable HTML transcript on your Desktop
  "pause the flight recorder" / "resume recording"
  "wipe my flight recorder" (you own it, so you can erase it)

Storage (owned + durable, outside the engine so upgrades/re-clones never touch it):
  ~/.brainstem/flight_recorder/<YYYY-MM-DD>.jsonl   (append-only JSONL)
  override with the FLIGHT_RECORDER_DIR environment variable.

Nothing leaves your machine. This is your estate.
"""

# RAPP Agent Registry manifest (ignored by the brainstem loader; used by RAR).
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/flight_recorder",
    "version": "1.0.1",
    "display_name": "FlightRecorder",
    "description": (
        "Records both sides of every brainstem /chat conversation to append-only local JSONL files, with search, export, pause, and wipe controls."
    ),
    "author": "Kody Wildfeuer",
    "tags": ["flight-recorder", "black-box", "logging", "observability", "privacy",
             "conversations", "audit", "local-first", "ownership"],
    "category": "core",
    "quality_tier": "community",
    "requires_env": ["FLIGHT_RECORDER_DIR"],
    "dependencies": ["@rapp/basic_agent"],
}

import datetime
import json
import os
import sys
import threading

# -- Drop-in BasicAgent import (robust across brainstem variants) --------------
try:
    from basic_agent import BasicAgent
except Exception:
    try:
        from agents.basic_agent import BasicAgent
    except Exception:
        try:
            from openrappter.agents.basic_agent import BasicAgent
        except Exception:
            class BasicAgent:  # last-resort shim so the file always loads
                def __init__(self, name=None, metadata=None):
                    if name is not None:
                        self.name = name
                    if metadata is not None:
                        self.metadata = metadata

                def perform(self, **kwargs):
                    return "Not implemented."

                def system_context(self):
                    return None

                def to_tool(self):
                    return {"type": "function", "function": {
                        "name": getattr(self, "name", "BasicAgent"),
                        "description": self.metadata.get("description", ""),
                        "parameters": self.metadata.get("parameters", {"type": "object", "properties": {}}),
                    }}


# -- Storage -------------------------------------------------------------------
_LOCK = threading.Lock()


def _dir():
    d = os.environ.get("FLIGHT_RECORDER_DIR") or os.path.join(os.path.expanduser("~"), ".brainstem", "flight_recorder")
    try:
        os.makedirs(d, exist_ok=True)
    except Exception:
        pass
    return d


def _control_path():
    return os.path.join(_dir(), "control.json")


def _now():
    return datetime.datetime.now()


def _load_control():
    try:
        with open(_control_path(), encoding="utf-8") as f:
            c = json.load(f)
        if isinstance(c, dict):
            return c
    except Exception:
        pass
    return {}


def _save_control(c):
    try:
        with open(_control_path(), "w", encoding="utf-8") as f:
            json.dump(c, f)
    except Exception:
        pass


def _is_enabled():
    c = _load_control()
    return c.get("enabled", True)  # installed => recording, until paused


def _set_enabled(on):
    c = _load_control()
    c["enabled"] = bool(on)
    c.setdefault("installed_at", _now().isoformat(timespec="seconds"))
    _save_control(c)


def _logfiles():
    d = _dir()
    try:
        return sorted(os.path.join(d, f) for f in os.listdir(d) if f.endswith(".jsonl"))
    except Exception:
        return []


def _logfile_today():
    return os.path.join(_dir(), _now().strftime("%Y-%m-%d") + ".jsonl")


def _iter_records():
    for path in _logfiles():
        try:
            with open(path, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        yield json.loads(line)
                    except Exception:
                        continue
        except Exception:
            continue


# -- Locating the host's running Flask app (no engine edits) -------------------
def _find_flask_app():
    cands = []
    for name in ("brainstem", "function_app", "__main__"):
        m = sys.modules.get(name)
        if m is not None:
            cands.append(m)
    cands.extend(m for m in list(sys.modules.values()) if m is not None and m not in cands)
    for m in cands:
        app = getattr(m, "app", None)
        try:
            if app is not None and hasattr(app, "view_functions") and "chat" in app.view_functions:
                return app
        except Exception:
            continue
    return None


def _model():
    for name in ("brainstem", "function_app", "__main__"):
        m = sys.modules.get(name)
        if m is not None and hasattr(m, "MODEL"):
            try:
                return getattr(m, "MODEL")
            except Exception:
                return None
    return None


def _classify(ua, ip):
    is_local = ip in ("127.0.0.1", "::1", "localhost", "")
    u = (ua or "").lower()
    if any(k in u for k in ("claude", "anthropic", "openai", "gpt-", "llm", "agent")):
        kind = "AI agent"
    elif not ua:
        kind = "API/unknown"
    elif any(b in u for b in ("mozilla", "chrome", "safari", "firefox", "edg/", "webkit")):
        kind = "browser (human)"
    elif any(c in u for c in ("curl", "wget", "httpie")):
        kind = "CLI"
    elif any(s in u for s in ("python", "requests", "httpx", "node", "axios", "go-http", "okhttp")):
        kind = "script/AI"
    else:
        kind = "other"
    return ("local " if is_local else "remote ") + kind


def _record(req, rb):
    if not _is_enabled():
        return
    try:
        data = req.get_json(silent=True) or {}
    except Exception:
        data = {}
    if not isinstance(data, dict):
        data = {}
    try:
        ua = req.headers.get("User-Agent", "") or ""
    except Exception:
        ua = ""
    ip = getattr(req, "remote_addr", "") or ""
    rec = {
        "ts": _now().isoformat(timespec="seconds"),
        "session_id": (rb.get("session_id") or data.get("session_id") or ""),
        "caller": _classify(ua, ip),
        "ip": ip,
        "user_agent": ua[:200],
        "user_input": data.get("user_input", ""),
        "response": rb.get("response", ""),
        "agent_logs": rb.get("agent_logs", ""),
        "voice_response": rb.get("voice_response", ""),
        "error": rb.get("error", ""),
        "history_len": len(data.get("conversation_history", []) or []),
        "model": _model(),
    }
    line = json.dumps(rec, ensure_ascii=False)
    with _LOCK:
        try:
            with open(_logfile_today(), "a", encoding="utf-8") as f:
                f.write(line + "\n")
        except Exception:
            pass


def _install():
    """Wrap the running /chat route once so every conversation is recorded. Idempotent."""
    app = _find_flask_app()
    if app is None:
        return False, "no running Flask app found yet"
    if getattr(app, "_flight_recorder_installed", False):
        return True, "attached"
    try:
        import flask
    except Exception:
        return False, "flask not importable"
    original = app.view_functions.get("chat")
    if original is None:
        return False, "no /chat route on this app"

    def wrapped(*a, **k):
        resp = original(*a, **k)
        try:
            body_obj = resp[0] if isinstance(resp, tuple) else resp
            raw = body_obj.get_data(as_text=True)
            rb = json.loads(raw) if raw else {}
            if isinstance(rb, dict):
                _record(flask.request, rb)
        except Exception:
            pass
        return resp

    wrapped._flight_recorder_wrapped = True
    app.view_functions["chat"] = wrapped
    app._flight_recorder_installed = True
    c = _load_control()
    c.setdefault("enabled", True)
    c.setdefault("installed_at", _now().isoformat(timespec="seconds"))
    _save_control(c)
    try:
        print("[flight-recorder] attached to /chat -- recording both sides locally to " + _dir())
    except Exception:
        pass
    return True, "attached"


# Attach as soon as the agent is first loaded (guarded; safe to re-run every request).
try:
    _install()
except Exception:
    pass


def _esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


class FlightRecorderAgent(BasicAgent):
    def __init__(self):
        self.name = "FlightRecorder"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"] + (
                " Trigger phrases: 'flight recorder', 'black box', 'record my conversations', "
                "'show/search my conversation log or history', 'export my conversations', "
                "'pause/stop recording', 'resume recording', 'where are my conversations stored', "
                "'wipe/delete my recordings'."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "description": "What to do: 'status' (is it recording, where, how many) | 'stats' (counts by day and caller) | 'search' (find conversations containing 'query') | 'tail' (the most recent conversations) | 'export' (write a readable HTML transcript to disk) | 'pause' (stop recording) | 'resume' (start recording) | 'where' (the storage path) | 'wipe' (delete recordings -- requires confirm=true). Default: status.",
                    },
                    "query": {"type": "string", "description": "For 'search'/'wipe': text to match within either side of a conversation (case-insensitive). For 'wipe', leave empty to target everything."},
                    "limit": {"type": "integer", "description": "For 'search'/'tail': how many conversations to return. Default 10."},
                    "path": {"type": "string", "description": "For 'export': the file path to write the HTML transcript to. Default: a timestamped file on the Desktop."},
                    "confirm": {"type": "boolean", "description": "For 'wipe': must be true to actually delete. Deleting is permanent -- this is the user's data and only they can erase it."},
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def system_context(self):
        # Ensure the recorder is attached (idempotent), and inform the user ONCE.
        ok = False
        try:
            ok, _ = _install()
        except Exception:
            ok = False
        enabled = _is_enabled()
        c = _load_control()
        if not c.get("announced"):
            c["announced"] = True
            _save_control(c)
            return ("[Flight Recorder add-on just activated. It is now recording BOTH SIDES of "
                    "every conversation through this brainstem to local files at " + _dir() +
                    " -- owned by the user, nothing leaves this machine. THIS TURN, briefly let the "
                    "user know the flight recorder is on, where it stores, and that they can say "
                    "'pause the flight recorder' anytime or 'export my conversations'. Then answer "
                    "their actual message.]")
        return ("[Flight Recorder add-on is installed; recording is currently " +
                ("ON" if enabled else "PAUSED") + ". It logs both sides of every /chat conversation "
                "locally to " + _dir() + " (owned by the user). If the user asks about recording, "
                "their conversation history/transcripts, privacy of past chats, or wants to "
                "pause/resume/export/wipe, call the FlightRecorder tool. Do not mention it otherwise.]")

    # -- helpers ---------------------------------------------------------------
    @staticmethod
    def _as_int(v, d):
        try:
            return int(v)
        except Exception:
            return d

    def _disk_size(self):
        total = 0
        for p in _logfiles():
            try:
                total += os.path.getsize(p)
            except Exception:
                pass
        return total

    # -- entry point -----------------------------------------------------------
    def perform(self, action="status", query="", limit=10, path="", confirm=False, **kwargs):
        action = (action or "status").strip().lower()
        limit = max(1, min(200, self._as_int(limit, 10)))
        attached, why = (False, "")
        try:
            attached, why = _install()
        except Exception:
            pass
        d = _dir()

        if action in ("where", "path"):
            return "Your flight recorder stores conversations locally at:\n" + d + "\nOverride with the FLIGHT_RECORDER_DIR environment variable."

        if action in ("pause", "stop", "off", "disable"):
            _set_enabled(False)
            return "Flight recorder PAUSED. No conversations are being recorded until you resume. (Existing records at " + d + " are untouched.)"

        if action in ("resume", "start", "on", "enable"):
            _set_enabled(True)
            return "Flight recorder RESUMED. Both sides of every conversation are being recorded again, locally, to " + d + "."

        records = list(_iter_records())
        total = len(records)

        if action in ("status",):
            by_caller = {}
            today = _now().strftime("%Y-%m-%d")
            today_n = 0
            for r in records:
                by_caller[r.get("caller", "?")] = by_caller.get(r.get("caller", "?"), 0) + 1
                if (r.get("ts", "")[:10] == today):
                    today_n += 1
            lines = [
                "FLIGHT RECORDER",
                "  recording:  " + ("ON" if _is_enabled() else "PAUSED"),
                "  attached:   " + ("yes (/chat is being captured)" if attached else "NOT YET (" + why + ")"),
                "  storage:    " + d + "   (yours; nothing leaves this machine)",
                "  recorded:   " + str(total) + " conversation turns total, " + str(today_n) + " today",
                "  on disk:    " + str(round(self._disk_size() / 1024, 1)) + " KB",
            ]
            if by_caller:
                lines.append("  by caller:  " + ", ".join("%s=%d" % (k, v) for k, v in sorted(by_caller.items(), key=lambda x: -x[1])))
            lines.append("  control it: search / tail / export / pause / resume / wipe")
            return "\n".join(lines)

        if action in ("stats",):
            by_day, by_caller = {}, {}
            for r in records:
                by_day[r.get("ts", "")[:10] or "?"] = by_day.get(r.get("ts", "")[:10] or "?", 0) + 1
                by_caller[r.get("caller", "?")] = by_caller.get(r.get("caller", "?"), 0) + 1
            out = ["FLIGHT RECORDER STATS -- " + str(total) + " turns, " + str(round(self._disk_size() / 1024, 1)) + " KB at " + d, "", "By day:"]
            for day in sorted(by_day)[-14:]:
                out.append("  %s : %d" % (day, by_day[day]))
            out.append("")
            out.append("By caller:")
            for k, v in sorted(by_caller.items(), key=lambda x: -x[1]):
                out.append("  %-26s : %d" % (k, v))
            return "\n".join(out)

        if action in ("search", "find"):
            q = (query or "").strip().lower()
            if not q:
                return "Tell me what to search for in your recorded conversations (a word or phrase)."
            hits = [r for r in records if q in (r.get("user_input", "") + " " + r.get("response", "")).lower()]
            hits = hits[-limit:]
            if not hits:
                return "No recorded conversations mention '" + query + "'."
            out = [str(len(hits)) + " match(es) for '" + query + "' (most recent last):", ""]
            for r in hits:
                out.append("[" + r.get("ts", "") + "] (" + r.get("caller", "?") + ")")
                out.append("  > " + (r.get("user_input", "") or "")[:160].replace("\n", " "))
                out.append("  < " + (r.get("response", "") or "")[:200].replace("\n", " "))
                out.append("")
            return "\n".join(out)

        if action in ("tail", "recent", "last"):
            recs = sorted(records, key=lambda r: r.get("ts", ""))[-limit:]
            if not recs:
                return "No conversations recorded yet. Send a message or two and check back."
            out = ["Your last " + str(len(recs)) + " recorded conversation turns:", ""]
            for r in recs:
                out.append("[" + r.get("ts", "") + "] (" + r.get("caller", "?") + ")")
                out.append("  > " + (r.get("user_input", "") or "")[:200].replace("\n", " "))
                out.append("  < " + (r.get("response", "") or "")[:240].replace("\n", " "))
                out.append("")
            return "\n".join(out)

        if action in ("export", "transcript", "download"):
            if not records:
                return "Nothing to export yet -- no conversations have been recorded."
            target = (path or "").strip()
            if not target:
                fname = "brainstem-flight-recorder-" + _now().strftime("%Y-%m-%d-%H%M%S") + ".html"
                desktop = os.path.join(os.path.expanduser("~"), "Desktop")
                target = os.path.join(desktop if os.path.isdir(desktop) else d, fname)
            recs = sorted(records, key=lambda r: r.get("ts", ""))
            rows = []
            for r in recs:
                rows.append(
                    '<div class="turn"><div class="meta">' + _esc(r.get("ts", "")) + " &middot; " + _esc(r.get("caller", "?")) +
                    (" &middot; " + _esc(r.get("model")) if r.get("model") else "") + '</div>' +
                    '<div class="u"><b>them &rarr;</b> ' + _esc(r.get("user_input", "")) + '</div>' +
                    '<div class="b"><b>brainstem &rarr;</b> ' + _esc(r.get("response", "")) + '</div>' +
                    (('<div class="logs">' + _esc(r.get("agent_logs", "")) + '</div>') if r.get("agent_logs") else "") +
                    '</div>')
            html = (
                "<!doctype html><meta charset=utf-8><title>Brainstem Flight Recorder</title>"
                "<style>body{font:15px/1.5 system-ui,sans-serif;max-width:820px;margin:30px auto;padding:0 16px;color:#1d1b16;background:#fbfaf7}"
                "h1{font-size:22px}.sub{color:#6b6256;margin-bottom:24px}.turn{border:1px solid #e7e0d4;border-radius:10px;padding:12px 14px;margin:12px 0}"
                ".meta{font-size:12px;color:#8a8270;margin-bottom:6px}.u{margin:4px 0}.b{margin:4px 0;color:#2a2620}"
                ".logs{font:12px ui-monospace,monospace;color:#7a7060;white-space:pre-wrap;margin-top:6px;border-top:1px dashed #e7e0d4;padding-top:6px}</style>"
                "<h1>Brainstem Flight Recorder</h1><div class=sub>" + str(len(recs)) + " conversation turns &middot; recorded locally &middot; exported " + _esc(_now().isoformat(timespec="seconds")) + "</div>" +
                "".join(rows))
            try:
                with open(target, "w", encoding="utf-8") as f:
                    f.write(html)
            except Exception as e:
                return "Could not write the transcript: " + str(e)
            return "Exported " + str(len(recs)) + " conversation turns to a readable transcript:\n" + target + "\nOpen it in any browser. It's yours."

        if action in ("wipe", "delete", "redact", "erase", "forget"):
            q = (query or "").strip().lower()
            if not confirm:
                scope = "conversations mentioning '" + query + "'" if q else "ALL recorded conversations"
                return "This will permanently delete " + scope + " from your flight recorder at " + d + ". It's your data, so it's your call -- re-run with confirm=true to erase."
            removed = 0
            if not q:
                for p in _logfiles():
                    try:
                        for line in open(p, encoding="utf-8"):
                            if line.strip():
                                removed += 1
                        os.remove(p)
                    except Exception:
                        pass
                return "Erased your entire flight recorder (" + str(removed) + " turns). Nothing left behind; nobody else ever had a copy."
            for p in _logfiles():
                try:
                    kept = []
                    for line in open(p, encoding="utf-8"):
                        s = line.strip()
                        if not s:
                            continue
                        try:
                            r = json.loads(s)
                        except Exception:
                            kept.append(line)
                            continue
                        if q in (r.get("user_input", "") + " " + r.get("response", "")).lower():
                            removed += 1
                        else:
                            kept.append(line if line.endswith("\n") else line + "\n")
                    with open(p, "w", encoding="utf-8") as f:
                        f.writelines(kept)
                except Exception:
                    pass
            return "Redacted " + str(removed) + " conversation turn(s) matching '" + query + "' from your flight recorder."

        return ("Flight Recorder actions: status, stats, search (query), tail, export, pause, resume, where, wipe (confirm). "
                "Recording is currently " + ("ON" if _is_enabled() else "PAUSED") + "; storage at " + d + ".")


if __name__ == "__main__":
    print(FlightRecorderAgent().perform(action="status"))
