---
name: "rar-kody-w-flight-recorder"
description: "Records both sides of every brainstem /chat conversation to append-only local JSONL files, with search, export, pause, and wipe controls."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/flight_recorder", "rar_sha256": "6a3976cfba0492a585ccab318125caed4ca0820e05dddf4119e98d5f22dea659", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["flight-recorder", "black-box", "logging", "observability", "privacy", "conversations", "audit", "local-first", "ownership"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/flight_recorder`. The original RAPP
agent is preserved byte-for-byte in `flight_recorder_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

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

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `flight_recorder_agent.py` and embedded as the fenced Python below (sha256 6a3976cfba0492a5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `flight_recorder_agent.py` first:

```bash
python3 flight_recorder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 flight_recorder_agent.py   # or on stdin
python3 flight_recorder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
