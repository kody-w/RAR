---
name: "rar-kody-w-flight-recorder"
description: "Records both sides of every brainstem /chat conversation to append-only local JSONL files, with search, export, pause, and wipe controls."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/flight_recorder", "rar_sha256": "6a3976cfba0492a585ccab318125caed4ca0820e05dddf4119e98d5f22dea659", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "flight_recorder_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/flight-recorder:e2f78f98124b0571827913346c11afd1b040b4adbffc14cb46ba40722876cb82", "kind": "skill"}, "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["flight-recorder", "black-box", "logging", "observability", "privacy", "conversations", "audit", "local-first", "ownership"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/flight_recorder`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `flight_recorder_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
