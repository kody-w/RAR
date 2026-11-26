"""The Hatchery app: one page on this computer for your Brainstem egg.

    python3 hatch_app.py               opens http://127.0.0.1:7199

1. Hatch it here: drop your .egg, it is checked and your Brainstem starts on this computer.
2. Take it to any AI: the same .egg, plus one sentence to paste (claude.ai or any AI that runs Python).
3. Bring it home: the AI hands you chat.json; your Brainstem's Import button continues the chat here.

Loopback only. Nothing leaves this computer unless you carry it. Stdlib only.
"""
import json
import os
import socket
import subprocess
import sys
import time
import urllib.request
import webbrowser
import zipfile
import io
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rapp1  # noqa: E402  (the rapp/1 reference, vendored beside this file)

HOME = Path(os.getenv("HATCHERY_HOME", Path.home() / ".hatchery")) / "eggs"
SENTENCE = "Open this egg and follow its skill.md. You are my Brainstem's model."
STATE = {"egg": None, "name": None, "port": None, "proc": None, "error": None}


def check_egg(blob):
    """(ok, why). A wake egg is a verified rapp/1 egg that carries brainstem.py and skill.md."""
    ok, step, *rest = rapp1.verify_egg(blob)
    if not ok:
        return False, f"this egg did not pass its check ({step}: {rest[0] if rest else ''})"
    try:
        names = set(zipfile.ZipFile(io.BytesIO(blob)).namelist())
    except zipfile.BadZipFile:
        return False, "this egg holds no files"
    if not {"brainstem.py", "skill.md"} <= names:
        return False, "this egg has no Brainstem inside to wake (no brainstem.py and skill.md)"
    return True, "checked"


def _free_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


def _up(port, seconds):
    end = time.time() + seconds
    while time.time() < end:
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{port}/health", timeout=3) as r:
                if r.status == 200:
                    return True
        except OSError:
            time.sleep(1)
    return False


def hatch(blob, filename):
    ok, why = check_egg(blob)
    if not ok:
        raise ValueError(why)
    stop()
    stem = Path(filename).name.removesuffix(".egg") or "brainstem"
    folder = HOME / stem
    folder.mkdir(parents=True, exist_ok=True)
    (folder / f"{stem}.egg").write_bytes(blob)
    zipfile.ZipFile(io.BytesIO(blob)).extract("brainstem.py", folder)
    port = _free_port()
    log = open(folder / "brainstem.log", "w")
    proc = subprocess.Popen([sys.executable, "brainstem.py", "--port", str(port), "--no-browser"],
                            cwd=folder, stdout=log, stderr=subprocess.STDOUT)
    if not _up(port, 240):
        proc.terminate()
        tail = (folder / "brainstem.log").read_text(errors="replace")[-300:]
        raise ValueError("your Brainstem did not start: " + tail.strip().splitlines()[-1] if tail.strip() else "no output")
    STATE.update(egg=folder / f"{stem}.egg", name=stem, port=port, proc=proc, error=None)


def stop():
    if STATE["proc"] and STATE["proc"].poll() is None:
        STATE["proc"].terminate()
        try:
            STATE["proc"].wait(30)
        except subprocess.TimeoutExpired:
            STATE["proc"].kill()
    STATE.update(proc=None, port=None)


PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Hatchery</title><style>
:root{--bg:#0f1115;--card:#181b22;--ink:#e8eaf0;--soft:#9aa3b2;--go:#4c8dff;--ok:#3fb27f;--bad:#e5534b}
@media (prefers-color-scheme:light){:root{--bg:#f6f7f9;--card:#fff;--ink:#161a22;--soft:#5b6472}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.5 system-ui,-apple-system,sans-serif}
main{max-width:640px;margin:0 auto;padding:28px 16px}h1{font-size:26px;margin:0 0 4px}p.sub{color:var(--soft);margin:0 0 24px}
.step{background:var(--card);border-radius:14px;padding:20px;margin:0 0 14px}.step h2{font-size:19px;margin:0 0 6px}
.step p{margin:0 0 12px;color:var(--soft)}.btn{display:inline-block;background:var(--go);color:#fff;border:0;border-radius:10px;
padding:12px 18px;font:inherit;font-weight:600;cursor:pointer;text-decoration:none}.btn.alt{background:transparent;color:var(--go);border:2px solid var(--go)}
.drop{display:block;border:2px dashed var(--soft);border-radius:12px;padding:26px;text-align:center;cursor:pointer}.drop.on{border-color:var(--go)}
.ok{color:var(--ok)}.bad{color:var(--bad)}.say{background:var(--bg);border-radius:10px;padding:12px;margin:0 0 10px;font-style:italic}
.dim{opacity:.45;pointer-events:none}
</style></head><body><main>
<h1>Your Brainstem, anywhere</h1><p class="sub">Hatch it here. Take it to any AI. Bring it home.</p>

<section class="step" id="s1"><h2>1. Hatch your egg</h2>
<p id="s1p">Drop your <b>.egg</b> file here.</p>
<label class="drop" id="drop">Choose or drop your egg<input type="file" accept=".egg" id="file" hidden></label>
<p id="status" style="margin-top:12px"></p>
<a class="btn" id="open" href="#" target="_blank" hidden>Open my Brainstem</a></section>

<section class="step" id="s2"><h2>2. Take it to any AI</h2>
<p>Attach your egg in claude.ai (or any AI that can run Python) and say:</p>
<div class="say" id="sentence">__SENTENCE__</div>
<button class="btn" id="copy">Copy the sentence</button> <a class="btn alt" id="egg" href="/egg">Download my egg</a></section>

<section class="step" id="s3"><h2>3. Bring it home</h2>
<p>When you're done there, ask the AI for <b>chat.json</b>. Then open your Brainstem, click <b>Import</b>, and choose it. The conversation carries on here.</p>
<a class="btn alt" id="open2" href="#" target="_blank">Open my Brainstem</a></section>

<script>
const $=id=>document.getElementById(id);
function show(s){const on=!!s.port;["s2","s3"].forEach(i=>$(i).classList.toggle("dim",!on));
 for(const b of ["open","open2"]){$(b).href=on?`http://127.0.0.1:${s.port}/`:"#";} $("open").hidden=!on;
 if(on){$("status").innerHTML=`<span class="ok">Hatched: ${s.name}</span>`;$("s1p").textContent="Your Brainstem is running on this computer.";}
 else if(s.error){$("status").innerHTML=`<span class="bad">${s.error}</span>`;}}
fetch("/state").then(r=>r.json()).then(show);
async function send(f){$("status").textContent="Checking and hatching… (the first time can take a minute)";
 const r=await fetch("/hatch?name="+encodeURIComponent(f.name),{method:"POST",body:f});show(await r.json());}
$("file").onchange=e=>e.target.files[0]&&send(e.target.files[0]);
const d=$("drop");d.ondragover=e=>{e.preventDefault();d.classList.add("on")};d.ondragleave=()=>d.classList.remove("on");
d.ondrop=e=>{e.preventDefault();d.classList.remove("on");e.dataTransfer.files[0]&&send(e.dataTransfer.files[0])};
$("copy").onclick=async()=>{try{await navigator.clipboard.writeText($("sentence").textContent);$("copy").textContent="Copied"}catch(e){$("copy").textContent="Select the sentence and copy it"}};
</script></main></body></html>"""


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code, body, ctype="application/json", extra=None):
        data = body if isinstance(body, bytes) else body.encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(data)

    def _state(self):
        return json.dumps({"name": STATE["name"], "port": STATE["port"], "error": STATE["error"]})

    def do_GET(self):
        if self.path == "/":
            self._send(200, PAGE.replace("__SENTENCE__", SENTENCE), "text/html; charset=utf-8")
        elif self.path == "/state":
            self._send(200, self._state())
        elif self.path == "/egg" and STATE["egg"]:
            self._send(200, STATE["egg"].read_bytes(), "application/octet-stream",
                       {"Content-Disposition": f'attachment; filename="{STATE["egg"].name}"'})
        else:
            self._send(404, '{"error":"not here"}')

    def do_POST(self):
        if not self.path.startswith("/hatch"):
            return self._send(404, '{"error":"not here"}')
        if self.headers.get("Origin") not in (None, f"http://127.0.0.1:{self.server.server_port}",
                                              f"http://localhost:{self.server.server_port}"):
            return self._send(403, '{"error":"only this page may hatch"}')
        n = int(self.headers.get("Content-Length") or 0)
        if n > 64 * 1024 * 1024:
            return self._send(413, '{"error":"that file is too big to be an egg"}')
        from urllib.parse import parse_qs, urlparse
        name = (parse_qs(urlparse(self.path).query).get("name") or ["brainstem.egg"])[0]
        try:
            hatch(self.rfile.read(n), name)
        except ValueError as e:
            STATE["error"] = str(e)
        self._send(200, self._state())


def main(port=7199, open_browser=True):
    try:
        srv = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    except OSError:                                   # that door is taken: any free one will do
        srv = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    url = f"http://127.0.0.1:{srv.server_port}/"
    print(f"Hatchery at {url}  (Ctrl-C to stop)", flush=True)
    if open_browser:
        webbrowser.open(url)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        stop()
        srv.server_close()


if __name__ == "__main__":
    import argparse
    a = argparse.ArgumentParser(description="Hatch your egg here, take it to any AI, bring it home.")
    a.add_argument("--port", type=int, default=7199)
    a.add_argument("--no-browser", action="store_true")
    args = a.parse_args()
    main(args.port, not args.no_browser)
