---
name: "rar-kody-w-flight-recorder"
description: "Records both sides of every brainstem /chat conversation to append-only local JSONL files, with search, export, pause, and wipe controls."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/flight_recorder", "rar_sha256": "f07d76a30266eab0a367c47a6dacf9403cb08cae684c0e02b0252c0cea79da02", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["flight-recorder", "black-box", "logging", "observability", "privacy", "conversations", "audit", "local-first", "ownership"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `flight_recorder_agent.py` and embedded as the fenced Python below (sha256 f07d76a30266eab0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `flight_recorder_agent.py` first:

```bash
python3 flight_recorder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 flight_recorder_agent.py   # or on stdin
python3 flight_recorder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/flight_recorder_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/flight_recorder_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/flight_recorder/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
