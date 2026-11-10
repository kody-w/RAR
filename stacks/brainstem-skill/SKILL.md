---
name: "rapp"
description: "Read once, then never again. Makes you RAPP compatible for good: you become a Brainstem that keeps an agents/ folder, loads every agent file in it fresh each turn, brings new ones by a seven-word chant, and answers in a Brainstem's chat shape. Use when the person says RAPP, Brainstem, a chant, bring or summon an agent, or hands you an agent.py."
license: "MIT"
compatibility: "Any AI that can write a file and run Python 3.9+. Nothing is installed."
metadata:
  rapp-skill: "0.3.1"
---

# RAPP: become a Brainstem, once

This page is a seed. It carries one small file. That file brings everything else it needs, checks it, and
writes a standing note into your own always-on instructions. After that you never need this page again.

## Before you start: ask once

Tell the person, in plain words, and wait for a yes:

> This sets up a folder called `rapp/` here and adds a short note to this folder's instructions file, so I
> can bring tools by saying seven words. Bringing a tool downloads it from the public RAPP catalog, checks
> its fingerprint, and runs it on this device. Deleting the `rapp/agents` folder turns it all off again, as if it was never here. OK?

## Then do this, in order

1. Choose the home folder. It is `rapp/` here, with one exception: if a `rapp` folder already exists and has
   no `kernel.py` in it, it belongs to something else (on many machines it is a copy of the RAPP project).
   Never write into it. Use `rapp-skill/` instead, and read `rapp-skill/` wherever this page says `rapp/`.
   If the home folder already has `kernel.py`, skip to step 3.
2. Write `rapp/kernel.py` from the block at the bottom of this page, with a script, never by retyping. The
   file is everything between the opening fence line (four backticks plus `python`) and the closing fence
   line (four backticks), ending in one newline, LF line endings. Its sha256 must be
   `d5839882311762f6cf6d4d1b378e25d55fe890566c2f05e4f3dd3f39d03aaf30`. If it is not, stop and say so.
3. Run it with whichever Python 3 works here (`python3`, `python`, or `py -3`):
   `<python> rapp/kernel.py stay`
   It fetches the two files it still needs, fingerprint-checked, and writes the standing note into this
   folder's always-on instructions file (`AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md` or
   `GEMINI.md`; the ones that exist, or a new `AGENTS.md`). The note names the Python that worked.
4. Read the note it just wrote and follow it from now on, starting this turn: run the `tools` line once now.
5. Tell the person it is done, in one sentence. This page can be deleted.

## Later, if the person wants it reachable like a Brainstem

Other programs can talk to you on a Brainstem's address, in a Brainstem's shape (`/health`, `/chat`), on
this device only. Start the door with the command that runs you for one message, the message last:
`<python> rapp/kernel.py serve 7071 -- <your one-message command>`. Only on the person's ask.

<!-- file: rapp/kernel.py -->
````python
"""kernel.py: the smallest Brainstem. It loads whatever is in agents/ fresh on every call.

    python3 kernel.py tools                      what is in agents/ right now (the tool list for this turn)
    python3 kernel.py call <Name> '<json args>'  run one agent's perform(**args) and print what it returns
    python3 kernel.py import <file> [sha256]     add an agent file to agents/ (checked if a sha256 is given)
    python3 kernel.py stay                       write the standing note into this folder's always-on instructions
    python3 kernel.py serve <port> -- <ai command ...>   be reachable like a Brainstem: /health and /chat on this
                                                 device, each chat handed to that AI (the message is its last argument)

The AI reading the skill is the model. This file only does what a Brainstem's loader does.
"""
import hashlib, importlib.util, json, os, sys, threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
AGENTS = HERE / "agents"
os.environ.setdefault("CHANT_HOME", str(HERE / "chant"))  # everything stays inside this folder

NOTE = """<!-- rapp:begin -->
## This folder has a Brainstem (RAPP)

You are RAPP compatible here, permanently. A folder `rapp/` holds your agents. Do this without being asked:

1. At the start of every turn run `python3 rapp/kernel.py tools`. What it prints is your extra tool list
   for this turn, read fresh from `rapp/agents/`. Never answer from a list you remember.
2. When a request fits one, run `python3 rapp/kernel.py call <Name> '<json args>'` and use exactly what
   it prints. Up to three calls a turn. Never invent a tool's output.
3. Seven chant words, or "Bring" plus seven words: call `SummonByChant` with `{"chant": "<the words>"}`.
   The agent file is fetched from the public catalog, fingerprint-checked, and is in your tool list on
   the very next `tools` run, in the same turn. A handed `agent.py`: `python3 rapp/kernel.py import <file>`.
4. A song ("R, A, P, P, verse. ... And seal.") is a job said aloud: do each sentence in order. "Bring" =
   get it, "Check" = prove it with a real call, "Show me" = quote what came back, "seal" = the job is closed.
5. Sent a JSON object with `user_input`? Reply with one JSON object and nothing else:
   `{"response": "...", "agent_logs": "[Name] output", "session_id": "<same one>", "model": "<your model id>"}`
   (one `[Name] output` line per call, in order; empty string if none).
6. Agent files are code that runs on this device: load only by chant from the catalog or from the person.
   Anything that leaves the device or cannot be undone waits for the person's yes.

Off switch: if `rapp/agents/` is gone, the person turned this off. `tools` then removes this note itself;
from that moment you know nothing of RAPP here. Never recreate the folder unasked.
<!-- rapp:end -->
"""
HOSTS = ("AGENTS.md", "CLAUDE.md", ".github/copilot-instructions.md", "GEMINI.md")


def stay(root=None):
    """Write the standing note into this folder's always-on instructions, once. After this the skill page is never needed."""
    root = Path(root) if root else HERE.parent
    note = NOTE.replace("python3 rapp/kernel.py", f"{_py()} {HERE.name}/kernel.py").replace("`rapp/", f"`{HERE.name}/")
    present = [h for h in HOSTS if (root / h).exists()] or ["AGENTS.md"]
    done = []
    for h in present:
        f = root / h
        old = f.read_text() if f.exists() else ""
        if "<!-- rapp:begin -->" in old:
            a, b = old.index("<!-- rapp:begin -->"), old.index("<!-- rapp:end -->") + len("<!-- rapp:end -->\n")
            new = old[:a] + note + old[b:]
        else:
            new = old + ("\n" if old and not old.endswith("\n") else "") + ("\n" if old else "") + note
        if new != old:
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text(new)
        done.append(h)
    return done


BASIC = "class BasicAgent:\n    def __init__(self, name, metadata):\n        self.name = name\n        self.metadata = metadata\n\n    def perform(self, **kwargs):\n        return \"Not implemented.\"\n"
CATALOG = "https://raw.githubusercontent.com/kody-w/RAR/main"


def _py():
    """The plain command name for a Python 3 here. Never a full path: hosts refuse commands they cannot recognise."""
    import shutil, subprocess
    for name in ("python3", "python", "py -3"):
        if shutil.which(name.split()[0]):
            try:
                out = subprocess.run(name.split() + ["-c", "import sys;print(sys.version_info >= (3, 9))"],
                                     capture_output=True, text=True, timeout=20).stdout.strip()
                if out == "True":
                    return name
            except Exception:
                pass
    return "python3"


def heal():
    """Bring back what this Brainstem cannot work without. Returns what it restored."""
    AGENTS.mkdir(parents=True, exist_ok=True)
    back = []
    if not (AGENTS / "basic_agent.py").exists():
        (AGENTS / "basic_agent.py").write_text(BASIC)
        back.append("basic_agent.py")
    if not (AGENTS / "summon_chant_agent.py").exists():
        try:  # from the catalog, checked against the catalog's own fingerprint for it
            import urllib.request
            reg = json.loads(urllib.request.urlopen(f"{CATALOG}/registry.json", timeout=30).read())
            want = [p for p in reg["stack_packs"] if p["name"] == "summon"][0]["files"]["summon_chant_agent.py"]["sha256"]
            body = urllib.request.urlopen(f"{CATALOG}/stacks/summon/summon_chant_agent.py", timeout=30).read()
            if hashlib.sha256(body).hexdigest() == want:
                (AGENTS / "summon_chant_agent.py").write_bytes(body)
                back.append("summon_chant_agent.py")
        except Exception:
            pass
    return back


def load():
    """Every agent in agents/, loaded from disk now. Returns {tool name: agent}, {file: error}."""
    sys.path.insert(0, str(HERE))
    found, broken = {}, {}
    for f in sorted(AGENTS.glob("*_agent.py")):
        if f.name == "basic_agent.py":
            continue
        try:
            spec = importlib.util.spec_from_file_location(f"agents.{f.stem}", f)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            from agents.basic_agent import BasicAgent
            for v in vars(mod).values():
                if isinstance(v, type) and issubclass(v, BasicAgent) and v is not BasicAgent and v.__module__ == mod.__name__:
                    a = v()
                    found[a.name] = a
        except Exception as e:
            broken[f.name] = f"{type(e).__name__}: {e}"
    return found, broken


def add(name, body, sha=None):
    name = os.path.basename(name)
    if not name.endswith("_agent.py"):
        return 400, {"status": "error", "error": "an agent file is named <something>_agent.py"}
    if sha and hashlib.sha256(body).hexdigest() != sha:
        return 400, {"status": "error", "error": "the file does not match its sha256"}
    AGENTS.mkdir(exist_ok=True)
    (AGENTS / name).write_bytes(body)
    return 200, {"status": "ok", "message": f"Agent {name} imported successfully."}


class Door(BaseHTTPRequestHandler):
    """While an agent runs, it can reach 'its Brainstem' the usual way: /health and /agents/import."""
    def log_message(self, *a):
        pass

    def _send(self, code, obj):
        b = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        self._send(200, {"status": "ok", "agents": sorted(load()[0])}) if self.path == "/health" else self._send(404, {})

    def do_POST(self):
        body = self.rfile.read(int(self.headers.get("Content-Length") or 0))
        if self.path != "/agents/import":
            return self._send(501, {"error": "the AI reading the skill is the chat; ask it directly"})
        import email
        msg = email.message_from_bytes(b"Content-Type: " + self.headers["Content-Type"].encode() + b"\r\n\r\n" + body)
        sha = payload = fname = None
        for part in msg.get_payload():
            if part.get_param("name", header="content-disposition") == "sha256":
                sha = part.get_payload(decode=True).decode().strip()
            if part.get_filename():
                fname, payload = part.get_filename(), part.get_payload(decode=True)
        if payload is not None and body.count(payload) == 0:  # keep the exact octets, not a re-decoded copy
            payload = payload.replace(b"\n", b"\r\n") if body.count(payload.replace(b"\n", b"\r\n")) else payload
        self._send(*add(fname or "", payload or b"", sha))


def envelope(text, session_id):
    """Find the Brainstem-shaped answer in whatever the AI printed; if there is none, wrap what it said."""
    dec, best = json.JSONDecoder(), None
    for i, ch in enumerate(text):
        if ch == "{":
            try:
                obj, _ = dec.raw_decode(text[i:])
            except ValueError:
                continue
            if isinstance(obj, dict) and "response" in obj:
                best = obj
    out = best or {"response": text.strip(), "agent_logs": ""}
    out.setdefault("agent_logs", "")
    out["session_id"] = out.get("session_id") or session_id
    out.setdefault("model", "")
    out.setdefault("requested_model", out["model"])
    out.setdefault("voice_mode", False)
    return out


def serve(port, host_cmd):
    import subprocess, uuid

    class Chat(Door):
        def do_GET(self):
            if self.path != "/health":
                return self._send(404, {})
            found, broken = load() if AGENTS.is_dir() else ({}, {})
            self._send(200, {"status": "ok", "agents": sorted(found), "quarantined": sorted(broken),
                             "model": os.path.basename(host_cmd[0]), "brainstem_dir": str(HERE)})

        def do_POST(self):
            if self.path != "/chat":
                return Door.do_POST(self)
            try:
                data = json.loads(self.rfile.read(int(self.headers.get("Content-Length") or 0)) or b"{}")
            except ValueError:
                return self._send(400, {"error": "Request body must be a JSON object"})
            said = data.get("user_input") if isinstance(data, dict) else None
            if not isinstance(said, str) or not said.strip():
                return self._send(400, {"error": "user_input is required"})
            sid = data.get("session_id") or str(uuid.uuid4())
            msg = json.dumps({"user_input": said.strip(), "session_id": sid})
            try:
                r = subprocess.run(host_cmd + [msg], cwd=str(HERE.parent), capture_output=True, text=True, timeout=600)
            except Exception as e:
                return self._send(502, {"error": f"the AI behind this door did not answer: {e}"})
            self._send(200, envelope(r.stdout, sid))

    door = ThreadingHTTPServer(("127.0.0.1", int(port)), Chat)
    os.environ["BRAINSTEM_URL"] = f"http://127.0.0.1:{door.server_address[1]}"
    print(f"listening like a Brainstem on http://127.0.0.1:{door.server_address[1]} (this device only)", flush=True)
    door.serve_forever()


def leave(root=None):
    """The agents folder is gone: take the standing note back out, so the AI is exactly as it was before."""
    root = Path(root) if root else HERE.parent
    for h in HOSTS:
        f = root / h
        old = f.read_text() if f.exists() else ""
        if "<!-- rapp:begin -->" not in old:
            continue
        a, b = old.index("<!-- rapp:begin -->"), old.index("<!-- rapp:end -->") + len("<!-- rapp:end -->\n")
        new = (old[:a].rstrip("\n") + "\n" + old[b:]).lstrip("\n") if old[:a].strip() or old[b:].strip() else ""
        f.write_text(new) if new.strip() else f.unlink()


def main(argv):
    cmd = argv[1] if len(argv) > 1 else "tools"
    if cmd in ("tools", "call", "import") and not AGENTS.is_dir():
        leave()
        print(json.dumps({"tools": [], "off": "The agents folder was removed, so RAPP is off here. The standing "
                          "note has been taken out of the instructions file. Carry on as if it was never there."}))
        return 0
    if cmd == "tools":
        found, broken = load()
        print(json.dumps({"tools": [a.metadata for a in found.values()], "broken": broken}, indent=1))
    elif cmd == "call":
        found, _ = load()
        if argv[2] not in found:
            print(json.dumps({"error": f"no agent named {argv[2]} in agents/", "have": sorted(found)}))
            return 1
        door = ThreadingHTTPServer(("127.0.0.1", 0), Door)
        threading.Thread(target=door.serve_forever, daemon=True).start()
        os.environ["BRAINSTEM_URL"] = f"http://127.0.0.1:{door.server_address[1]}"
        print(found[argv[2]].perform(**json.loads(argv[3] if len(argv) > 3 else "{}")))
    elif cmd == "import":
        code, out = add(argv[2], Path(argv[2]).read_bytes(), argv[3] if len(argv) > 3 else None)
        print(json.dumps(out))
        return 0 if code == 200 else 1
    elif cmd == "serve":
        cut = argv.index("--") if "--" in argv else len(argv)
        if cut == len(argv) or cut + 1 >= len(argv):
            print("say which AI sits behind the door: kernel.py serve <port> -- <ai command ...>")
            return 1
        serve(argv[2] if cut > 2 else 7071, argv[cut + 1:])
    elif cmd == "stay":
        back = heal()
        print("standing note written to: " + ", ".join(stay()) + ("; fetched: " + ", ".join(back) if back else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
````
<!-- end -->
