"""Layer: journal_tap — every completed chat turn is recorded in the owner's journal, by default.

Simon Willison's `llm` lesson: the log people keep a tool for is the one that is on by default and searchable
later. The Brainstem Journal (a sidecar on :7074) already keeps that record, but only for turns routed through
its proxy; the chat page talks to the kernel on :7071 directly, so the record stayed nearly empty.

This layer wraps, inside the Brainstem process only, the registration of the kernel's two chat routes:
  POST /chat         -> after the kernel answers (200, JSON), the turn is posted to <journal>/journal/record
  POST /chat/stream  -> the event stream is passed through untouched; when its "done" event has gone by, the
                        same record is posted
The post runs on a daemon thread with a short timeout; the answer to the person is never delayed or changed.
No journal running, journal refusing, bad network: nothing happens and the kernel is unaffected.
The owner pauses it with a file (`<journal store>/paused`; the JournalRecall agent toggles it in chat).

Env: JOURNAL_URL (default http://127.0.0.1:7074), JOURNAL_STORE (default ~/.brainstem/journal).
"""
import functools
import hashlib
import json
import os
import sys
import threading
import time
import urllib.request

# Hook points this layer wraps. Two enabled layers touching the same point conflict; the pack's order wins.
TOUCHES = {"flask.Flask.add_url_rule"}

# sha256 of every grail brainstem.py this layer was PROVEN against (a real /chat and /chat/stream recorded through it).
PROVEN_GRAIL = {
    "35618683ebc3d1c2bfaff47f60182fd756f3a8de53c53dd907ec1099d631930a",  # 0.6.17 (installed)
    "bd55a7f0bcf5efd3f7966ca39bb146da3c25fda9a0b1ce5ba587919d3c3775f4",  # 0.6.16 (public rapp-installer main)
}

JOURNAL = os.environ.get("JOURNAL_URL", "http://127.0.0.1:7074").rstrip("/")
STORE = os.path.expanduser(os.environ.get("JOURNAL_STORE", "~/.brainstem/journal"))
PAUSED = os.path.join(STORE, "paused")
_said_down = [False]


def _post(frame):
    req = urllib.request.Request(JOURNAL + "/journal/record", data=json.dumps(frame, ensure_ascii=False).encode(),
                                 headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=3) as r:
            r.read()
        _said_down[0] = False
    except Exception as e:  # the journal is optional; say so once, never again until it is back
        if not _said_down[0]:
            _said_down[0] = True
            print(f"[journal_tap] turn not recorded ({e}); the Brainstem is unaffected", file=sys.stderr, flush=True)


def _record(body, reply, t0, streamed):
    try:
        if os.path.exists(PAUSED) or not isinstance(reply, dict) or not reply.get("response"):
            return
        request = body.get("user_input")
        if not isinstance(request, str) or not request.strip():
            return
        session = reply.get("session_id") or body.get("session_id")
        minute = time.strftime("%Y-%m-%dT%H:%M", time.gmtime())
        tap_id = hashlib.sha256(f"{session}|{request}|{reply['response']}|{minute}".encode()).hexdigest()[:16]
        frame = {"request": request, "response": reply.get("response"), "agent_logs": reply.get("agent_logs"),
                 "session_id": session, "model": reply.get("model"), "latency_s": round(time.time() - t0, 2),
                 "streamed": bool(streamed), "upstream": "tap:" + (os.environ.get("PORT") or "7071"), "tap_id": tap_id}
        threading.Thread(target=_post, args=(frame,), daemon=True).start()
    except Exception:
        pass


def _wrap_chat(view):
    @functools.wraps(view)
    def chat(*a, **kw):
        import flask
        body = flask.request.get_json(silent=True) or {}
        t0 = time.time()
        out = view(*a, **kw)
        try:
            resp = out[0] if isinstance(out, tuple) else out
            if getattr(resp, "status_code", None) == 200 and getattr(resp, "is_json", False):
                _record(body if isinstance(body, dict) else {}, resp.get_json(silent=True), t0, False)
        except Exception:
            pass
        return out
    return chat


def _wrap_stream(view):
    @functools.wraps(view)
    def chat_stream(*a, **kw):
        import flask
        body = flask.request.get_json(silent=True) or {}
        t0 = time.time()
        out = view(*a, **kw)
        try:
            if isinstance(out, flask.Response) and "text/event-stream" in out.headers.get("Content-Type", ""):
                orig = out.response

                def tee():
                    done, buf = None, ""
                    for chunk in orig:
                        yield chunk
                        try:
                            buf += chunk.decode("utf-8", "replace") if isinstance(chunk, bytes) else str(chunk)
                            while "\n\n" in buf:
                                event, buf = buf.split("\n\n", 1)
                                for line in event.splitlines():
                                    if line.startswith("data:"):
                                        ev = json.loads(line[5:].strip())
                                        if isinstance(ev, dict) and ev.get("type") == "done":
                                            done = ev
                        except Exception:
                            pass
                    if done:
                        _record(body if isinstance(body, dict) else {}, done, t0, done.get("streamed"))
                out.response = tee()
        except Exception:
            pass
        return out
    return chat_stream


def apply():
    import flask
    orig = flask.Flask.add_url_rule

    @functools.wraps(orig)
    def add_url_rule(self, rule, endpoint=None, view_func=None, **options):
        if view_func is not None and rule == "/chat":
            view_func = _wrap_chat(view_func)
        elif view_func is not None and rule == "/chat/stream":
            view_func = _wrap_stream(view_func)
        return orig(self, rule, endpoint, view_func, **options)
    flask.Flask.add_url_rule = add_url_rule
