---
name: "rapp"
description: "Read once, then never again. Makes you RAPP compatible for good: you become a Brainstem that keeps an agents/ folder, loads every agent file in it fresh each turn, brings new ones by a seven-word chant, and answers in a Brainstem's chat shape. Use when the person says RAPP, Brainstem, a chant, bring or summon an agent, or hands you an agent.py."
license: "MIT"
compatibility: "Any AI that can write a file and run Python 3.9+. Nothing is installed."
metadata:
  rapp-skill: "0.4.0"
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

1. Find a Python 3. Try `python3 --version`, then `python --version`, then `py -3 --version`. Agents are
   Python files, the same as in a Brainstem, so one of these must work. If none does, tell the person this
   needs Python and wait for a yes, then install it the way the Brainstem's own installer does:
   Windows `winget install --id Python.Python.3.11 --accept-source-agreements --accept-package-agreements --silent`;
   macOS `brew install python@3.11`; Debian or Ubuntu `sudo apt-get install -y python3`. Use a new shell
   afterwards so the command is found. If Python cannot be installed, stop: give the person
   https://kody-w.github.io/RAR/install.html, whose one line installs Python and a whole Brainstem.
2. Choose the home folder. It is `rapp/` here, with one exception: if a `rapp` folder already exists and has
   no `kernel.py` in it, it belongs to something else (on many machines it is a copy of the RAPP project).
   Never write into it. Use `rapp-skill/` instead, or if that name is taken too, the first of `rapp-skill-2/`,
   `rapp-skill-3/` and so on that does not exist yet. Read that name wherever this page says `rapp/`.
   If the home folder already has `kernel.py`, skip to step 4.
3. Write `rapp/kernel.py` from the block at the bottom of this page, with a script, never by retyping. The
   file is everything between the opening fence line (four backticks plus `python`) and the closing fence
   line (four backticks), ending in one newline, LF line endings. Its sha256 must be
   `47053015e077bf3fda3d887b419e3622831eae3bd80df95059bfa69e0b6268d0`. If it is not, stop and say so.
4. Run it with the Python 3 that worked, naming the instructions file you yourself read at the start of
   every session: `<python> rapp/kernel.py stay <your file>`
   Your file is `CLAUDE.md` if you are Claude Code, `GEMINI.md` if you are Gemini, `AGENTS.md` if you are
   Copilot or Codex. If you do not know, leave it off. It fetches the two files it still needs,
   fingerprint-checked, and writes the standing note into your file (made if missing) and into any of
   `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, `GEMINI.md` that already exist. With no
   name and none existing, it makes `AGENTS.md`. The note names the Python that worked.
5. Read the note it just wrote and follow it from now on, starting this turn: run the `tools` line once now.
6. Tell the person it is done, in one sentence. This page can be deleted.

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
    python3 kernel.py ready <file> <Name> '<json args>' '<words>'   test a new agent file with a real call, then
                                                 hand it to the person's Brainstem on this device
    python3 kernel.py stay [your file]           write the standing note into this folder's always-on instructions
                                                 (name the one you read at startup, such as CLAUDE.md, and it is made)
    python3 kernel.py map [--dir <agents>]           intelligent omni routing, read only: what is loaded (top of agents/)
                                                 and every shelf (a subfolder, never loaded) with each agent's own
                                                 name and description, read as text, never run
    python3 kernel.py load <shelf>[/<file>] [--dir <agents>]    put a shelf's agents (or one) on top, so they load
    python3 kernel.py shelve <file> <shelf> [--dir <agents>]    move a loaded agent onto a shelf (made if missing)
    python3 kernel.py undo [--dir <agents>]          put the last load or shelve back
                                                 (--dir defaults to this folder's agents/; name the person's
                                                 own Brainstem's agents/ folder to route that one)
    python3 kernel.py serve <port> -- <ai command ...>   be reachable like a Brainstem: /health and /chat on this
                                                 device, each chat handed to that AI (the message is its last argument)

The AI reading the skill is the model. This file only does what a Brainstem's loader does.
"""
import ast, hashlib, importlib.util, json, os, shutil, sys, time, threading, urllib.request, uuid
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
7. Asked to build something and get it ready to try: write ONE agent file. The model that will use it sees
   only its description and its parameter descriptions, so put everything a caller must supply there, with
   an example; the file does all the rest. Then run
   `python3 rapp/kernel.py ready <file> <Name> '<json args>' '<words the answer must hold>'`. It tests the
   file with a real call and only then hands it to the person's Brainstem on this device. Say what it
   printed, and one line the person can say to try it.
8. Need something you lack? Grow from the catalog: agents at https://kody-w.github.io/RAR/api/v1/index.json,
   packs in https://kody-w.github.io/RAR/registry.json; bring what fits by chant. Never edit the Brainstem
   itself (the grail): a new need is an agent file, a sidecar that talks only over /chat and /health, or a
   distro. Stuck? The rules: https://kody-w.github.io/RAR/RAPP.md. The protocol: https://kody-w.github.io/rapp-1/llms.txt

9. Intelligent omni routing: keep the agents folder lean and organized so the person never thinks about
   it. Only agent files at the top of `rapp/agents/` load; each subfolder is a shelf for one engagement,
   named from the person's own words, holding its agent files and saved songs (`songs/<name>.txt`, one
   sentence per line). Each turn, read `python3 rapp/kernel.py map` (every shelf and each agent's own
   description, read as text, never run) beside what the person is saying, and route: `load <shelf>` or
   `load <shelf>/<file>` what this need calls for, `shelve <file> <shelf>` what it no longer needs, so the
   top holds only what is in play. A new engagement gets a new shelf; never ask "which project?" unless
   two fit equally. When a job works, save it as a song on its shelf, so "do it again" needs nothing else.
   Never delete; merge duplicates and shelve what has gone unused. Tell the person each move in one plain
   line; "undo that" is `undo`. Asked "where is everything?", answer one line per shelf.
10. The person never runs a command, opens a folder or drags a file: you do all of it. Their own Brainstem
   (usually http://localhost:7071, its `/health` answers) is routed the same way with `--dir <its agents
   folder>`; it also loads only the top of its `agents/`. If it is not answering, start it yourself the
   way it was installed; hand it new agents with `ready`. Only a yes, a sign-in or a payment is theirs:
   ask in one plain sentence, then carry on.

Off switch: if `rapp/agents/` is gone, the person turned this off. `tools` then removes this note itself;
from that moment you know nothing of RAPP here. Never recreate the folder unasked.
<!-- rapp:end -->
"""
HOSTS = ("AGENTS.md", "CLAUDE.md", ".github/copilot-instructions.md", "GEMINI.md")


def stay(root=None, mine=()):
    """Write the standing note into this folder's always-on instructions, once. After this the skill page is never needed.

    mine: the instructions file the AI itself reads at the start of a session. It is made if it is missing,
    so an AI that does not read AGENTS.md still finds the note in a folder that had no instructions at all."""
    root = Path(root) if root else HERE.parent
    note = NOTE.replace("python3 rapp/kernel.py", f"{_py()} {HERE.name}/kernel.py").replace("`rapp/", f"`{HERE.name}/")
    present = [h for h in HOSTS if (root / h).exists() or h in mine] or ["AGENTS.md"]
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


def ready(path, name, args, want, to=None):
    """The build line. The file must load, describe itself, and answer a real call with the expected words. Only
    then is it handed, fingerprint-checked, to the person's Brainstem through its own import door."""
    to = to or os.environ.get("RAPP_BRAINSTEM", "http://127.0.0.1:7071")
    base, body = os.path.basename(path), Path(path).read_bytes()
    before = (AGENTS / base).read_bytes() if (AGENTS / base).exists() else None
    code, out = add(base, body)
    if code != 200:
        return 1, out

    def back(why):
        if before is None:
            (AGENTS / base).unlink()
        else:
            (AGENTS / base).write_bytes(before)
        return 1, {"status": "not ready", "why": why}
    found, broken = load()
    if base in broken or name not in found:
        return back(broken.get(base) or f"the file has no agent named {name}")
    meta = found[name].metadata
    props = (meta.get("parameters") or {}).get("properties") or {}
    bare = [p for p, v in props.items() if not str((v or {}).get("description") or "").strip()]
    if not str(meta.get("description") or "").strip() or bare:
        return back("a model sees only the descriptions: describe the agent and every parameter" + (" (missing: " + ", ".join(bare) + ")" if bare else ""))
    try:
        got = str(found[name].perform(**args))
    except Exception as e:
        return back(f"the test call failed: {type(e).__name__}: {e}")
    if want.lower() not in got.lower():
        return back(f"the test call answered {got[:200]!r}, which does not hold {want!r}")
    out = {"status": "ready", "agent": name, "file": base, "sha256": hashlib.sha256(body).hexdigest(), "test_answer": got[:300], "handed_to": None}
    mark = uuid.uuid4().hex
    form = (f'--{mark}\r\nContent-Disposition: form-data; name="sha256"\r\n\r\n{out["sha256"]}\r\n'
            f'--{mark}\r\nContent-Disposition: form-data; name="file"; filename="{base}"\r\nContent-Type: text/x-python\r\n\r\n').encode() + body + f"\r\n--{mark}--\r\n".encode()
    try:
        urllib.request.urlopen(urllib.request.Request(to + "/agents/import", form, {"Content-Type": "multipart/form-data; boundary=" + mark}), timeout=30).read()
        listed = json.loads(urllib.request.urlopen(to + "/health", timeout=10).read()).get("agents") or []
        out["handed_to"] = to if name in listed else None
        out["note"] = "It is in the person's Brainstem now." if name in listed else "The Brainstem took the file but does not list the agent. Say so."
    except Exception as e:
        out["note"] = f"Tested and kept here. No Brainstem answered at {to} ({type(e).__name__}), so it was not handed over. Say so."
    return 0, out


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

KEEP = ("basic_agent.py", "summon_chant_agent.py")  # always on top


def _about(f):
    """An agent file's own name and description, read as text (ast), never executed."""
    name = desc = None
    try:
        for node in ast.walk(ast.parse(f.read_text(encoding="utf-8", errors="replace"))):
            if isinstance(node, ast.Dict):
                for k, v in zip(node.keys, node.values):
                    if isinstance(k, ast.Constant) and isinstance(v, ast.Constant) and isinstance(v.value, str):
                        if k.value == "name" and not name: name = v.value
                        if k.value == "description" and not desc: desc = v.value
    except SyntaxError:
        pass
    return {"file": f.name, "name": name or f.stem, "description": (desc or "")[:300]}


def route_map(d):
    log = d / ".routing.jsonl"
    moves = [json.loads(l) for l in log.read_text().splitlines()[-5:]] if log.exists() else []
    return {"agents_dir": str(d),
            "loaded": [_about(f) for f in sorted(d.glob("*_agent.py")) if f.name not in KEEP],
            "shelves": {s.name: [_about(f) for f in sorted(s.glob("*_agent.py"))]
                        for s in sorted(d.iterdir()) if s.is_dir() and not s.name.startswith((".", "_"))},
            "last_moves": moves}


def _move(d, src, dst, kind):
    if dst.exists():
        return {"error": f"{dst.relative_to(d)} already exists; nothing moved"}
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(dst))
    rec = {"at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "kind": kind,
           "from": str(src.relative_to(d)), "to": str(dst.relative_to(d))}
    with open(d / ".routing.jsonl", "a") as fh:
        fh.write(json.dumps(rec) + "\n")
    return rec


def route(cmd, args):
    d = AGENTS
    if "--dir" in args:
        i = args.index("--dir"); d = Path(args[i + 1]).expanduser(); args = args[:i] + args[i + 2:]
    if cmd == "map":
        return route_map(d)
    if cmd == "load":
        shelf, _, one = args[0].partition("/")
        files = [d / shelf / one] if one else sorted((d / shelf).glob("*_agent.py"))
        if not files or not all(f.exists() for f in files):
            return {"error": f"nothing to load at {args[0]}", "shelves": list(route_map(d)["shelves"])}
        return {"moved": [_move(d, f, d / f.name, "load") for f in files]}
    if cmd == "shelve":
        f = d / args[0]
        if args[0] in KEEP or not f.exists():
            return {"error": f"{args[0]} cannot be shelved" if args[0] in KEEP else f"no {args[0]} on top"}
        return {"moved": [_move(d, f, d / args[1] / f.name, "shelve")]}
    if cmd == "undo":
        log = d / ".routing.jsonl"
        lines = log.read_text().splitlines() if log.exists() else []
        if not lines:
            return {"error": "nothing to undo"}
        last = json.loads(lines[-1])
        shutil.move(str(d / last["to"]), str(d / last["from"]))
        log.write_text("".join(l + "\n" for l in lines[:-1]))
        return {"undone": last}


def main(argv):
    cmd = argv[1] if len(argv) > 1 else "tools"
    if cmd in ("tools", "call", "import", "ready") and not AGENTS.is_dir():
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
    elif cmd == "ready":
        if len(argv) < 6:
            print("kernel.py ready <file> <Name> '<json args>' '<words the answer must hold>'")
            return 2
        code, out = ready(argv[2], argv[3], json.loads(argv[4]), argv[5], argv[6] if len(argv) > 6 else None)
        print(json.dumps(out, indent=1))
        return code
    elif cmd in ("map", "load", "shelve", "undo"):
        out = route(cmd, argv[2:])
        print(json.dumps(out, indent=1))
        return 1 if "error" in out else 0
    elif cmd == "serve":
        cut = argv.index("--") if "--" in argv else len(argv)
        if cut == len(argv) or cut + 1 >= len(argv):
            print("say which AI sits behind the door: kernel.py serve <port> -- <ai command ...>")
            return 1
        serve(argv[2] if cut > 2 else 7071, argv[cut + 1:])
    elif cmd == "stay":
        mine = [a.replace("\\", "/") for a in argv[2:]]
        if [a for a in mine if a not in HOSTS]:
            print("stay takes one of: " + ", ".join(HOSTS))
            return 2
        back = heal()
        print("standing note written to: " + ", ".join(stay(mine=mine)) + ("; fetched: " + ", ".join(back) if back else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
````
<!-- end -->
