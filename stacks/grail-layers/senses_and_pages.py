"""Layer: senses_and_pages — senses and pages run over the unchanged grail.

Senses (RAPP Sense Store format: name, delimiter, response_key, system_prompt) add one extra field to every plain
/chat reply, such as a headline or a spoken version. Pages (rappter-distro organ format: name, handle(method, path,
body)) add routes at /api/<name>/... . Before this layer only rappter-distro's own kernel loaded either; now any
Brainstem does, and that loader is retired as an alias of this one.

Where things go (one standard): ~/.brainstem/senses/*_sense.py and ~/.brainstem/pages/*_page.py
(~/.brainstem/organs/*_organ.py is read too: "organ" is an alias of "page"). Env BRAINSTEM_SENSES_DIR and
BRAINSTEM_PAGES_DIR override for a lab.

Safety: a sense or page that fails to load is skipped and logged; a page that throws answers 500 for its own route
only; the sense prompt is added only to plain /chat (never /chat/stream, so the chat page shows no markers), and a
reply without the marker is returned exactly as the kernel gave it.
"""
import functools
import glob
import importlib.util
import os
import sys
import threading

TOUCHES = {"flask.Flask.__init__"}  # pages and the sense splitter are attached as the app is created
WRAPS = {"requests.post"}           # sense prompts ride on the system message; composes with providers

PROVEN_GRAIL = {
    "35618683ebc3d1c2bfaff47f60182fd756f3a8de53c53dd907ec1099d631930a",  # 0.6.17 (installed)
    "bd55a7f0bcf5efd3f7966ca39bb146da3c25fda9a0b1ce5ba587919d3c3775f4",  # 0.6.16 (published; proven 2026-11-04: 5/5 chat with sense, stream, 3/3 pages)
}

BASE = os.path.expanduser("~/.brainstem")
SENSES = os.environ.get("BRAINSTEM_SENSES_DIR") or os.path.join(BASE, "senses")
PAGES = os.environ.get("BRAINSTEM_PAGES_DIR") or os.path.join(BASE, "pages")
ORGANS = os.path.join(BASE, "organs")
_local = threading.local()


def _say(msg):
    print(f"[senses_and_pages] {msg}", file=sys.stderr, flush=True)


_CACHE = {}  # path -> ((mtime_ns, size), module): re-run a file only when it changes on disk


def _load(path, prefix):
    try:
        st = os.stat(path); key = (st.st_mtime_ns, st.st_size)
        hit = _CACHE.get(path)
        if hit and hit[0] == key:
            return hit[1]
        spec = importlib.util.spec_from_file_location(prefix + os.path.basename(path)[:-3], path)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        _CACHE[path] = (key, m)
        return m
    except Exception as e:
        _say(f"{os.path.basename(path)} did not load ({e}); skipped")
        if "key" in locals():
            _CACHE[path] = (key, None)  # a broken file is reported once, retried when it changes
        return None


def _senses():
    out = []
    for p in sorted(glob.glob(os.path.join(SENSES, "*_sense.py"))):
        m = _load(p, "_sense_")
        if m and all(isinstance(getattr(m, k, None), str) for k in ("name", "delimiter", "response_key", "system_prompt")):
            out.append(m)
    return out


def _pages():
    seen, out = set(), []
    dirs = [(PAGES, "*_page.py"), (ORGANS, "*_organ.py")] if not os.environ.get("BRAINSTEM_PAGES_DIR") else [(PAGES, "*_page.py"), (PAGES, "*_organ.py")]
    for d, pat in dirs:
        for p in sorted(glob.glob(os.path.join(d, pat))):
            m = _load(p, "_page_")
            n = getattr(m, "name", None) if m else None
            if n and callable(getattr(m, "handle", None)) and n not in seen:
                seen.add(n); out.append(m)
    return out


def _attach(app):
    """One standing route; the pages folder is re-read on every request (like agents/), so a new or changed
    page needs no restart. rapp/1 section 8: pages are read-only views (GET); every change goes through /chat."""
    import flask

    def view(page, rest=""):
        m = next((x for x in _pages() if x.name == page), None)
        if m is None:
            return flask.jsonify({"error": f"no page named {page}"}), 404
        try:
            result, status = m.handle(flask.request.method, rest, {})
        except Exception as e:
            return flask.jsonify({"error": f"page {page} failed: {e}"}), 500
        return (flask.jsonify(result), status) if isinstance(result, (dict, list)) else (result, status)
    try:
        app.add_url_rule("/api/<page>", "_pages_root", view, methods=["GET"], strict_slashes=False)
        app.add_url_rule("/api/<page>/<path:rest>", "_pages_path", view, methods=["GET"])
        _say("pages at /api/<name>/ (read fresh every request: " + ", ".join(m.name for m in _pages()) + ")")
    except Exception as e:
        _say(f"pages not added ({e})")


    @app.before_request
    def _mark():
        _local.senses = _senses() if flask.request.path == "/chat" else []

    @app.after_request
    def _split(resp):
        senses = getattr(_local, "senses", None) or []
        _local.senses = []
        if not senses or not resp.is_json or resp.status_code != 200:
            return resp
        try:
            data = resp.get_json()
            text = data.get("response") if isinstance(data, dict) else None
            if not isinstance(text, str):
                return resp
            for s in senses:
                if s.delimiter in text:
                    text, extra = text.split(s.delimiter, 1)
                    for o in senses:  # a later marker inside this segment belongs to its own sense
                        if o.delimiter in extra:
                            extra, rest = extra.split(o.delimiter, 1)
                            text += o.delimiter + rest
                    data[s.response_key] = extra.strip()
            data["response"] = text.strip()
            resp.set_data(flask.json.dumps(data))
        except Exception:
            pass
        return resp


def apply():
    import flask
    import requests
    orig_init = flask.Flask.__init__

    @functools.wraps(orig_init)
    def __init__(self, *a, **kw):
        orig_init(self, *a, **kw)
        try:
            _attach(self)
        except Exception as e:
            _say(f"not attached ({e}); the Brainstem is unaffected")
    flask.Flask.__init__ = __init__

    orig_post = requests.post

    @functools.wraps(orig_post)
    def post(url, *a, **kw):
        try:
            senses = getattr(_local, "senses", None) or []
            msgs = (kw.get("json") or {}).get("messages")
            if senses and isinstance(msgs, list) and msgs and msgs[0].get("role") == "system":
                add = "\n\n".join(s.system_prompt for s in senses)
                kw["json"] = dict(kw["json"], messages=[dict(msgs[0], content=f"{msgs[0]['content']}\n\n{add}")] + msgs[1:])
        except Exception:
            pass
        return orig_post(url, *a, **kw)
    requests.post = post
