#!/usr/bin/env python3
"""summond — scan a RAR card's QR, summon it into your Brainstem. Kernel never edited.

The phone (on your tailnet) opens  http://<this-mac>:7390/s/<seed>  (what the QR encodes).
It sees the card and one button. On tap it sends ONLY the seed. This sidecar resolves the
seed in RAR's registry, fetches the file, checks the sha256, then hands it to the kernel's
own /agents/import (loopback, with the sha256 so the kernel re-checks it). Stacks: /s/stack/<name>.

  python3 summond.py BRAINSTEM_URL [port] [rar_base]

Listens ONLY on loopback and this Mac's Tailscale address (never 0.0.0.0), so only your
own tailnet devices can reach it. Pair a phone once: open /pair on this Mac and scan.
"""
PAGES = "https://kody-w.github.io/RAR"
import html, json, hashlib, os, shutil, subprocess, sys, threading, time, urllib.request, uuid
from pathlib import Path
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

BRAIN = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:7071"
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 7390
RAR = sys.argv[3] if len(sys.argv) > 3 else "https://raw.githubusercontent.com/kody-w/RAR/main"
_reg = {}


def get(url, binary=False):
    with urllib.request.urlopen(url, timeout=30) as r:
        b = r.read()
    return b if binary else json.loads(b)


def registry():
    if _reg and time.time() - _reg.get("_at", 0) > 300:  # re-read RAR every 5 minutes
        _reg.clear()
    if not _reg:
        _reg["_at"] = time.time()
        for e in get(f"{RAR}/registry.json")["agents"]:
            if "_seed" in e:
                _reg[str(e["_seed"])] = e
    return _reg


def plan(kind, key):
    """What would be installed: list of (install_name, url, sha256), plus a card to show."""
    if kind == "seed":
        e = registry().get(key)
        if not e:  # a distro's seed: summon the whole stack
            pk = next((p for p in get(f"{RAR}/registry.json").get("stack_packs", [])
                       if str(p.get("_seed")) == key), None)
            if pk:
                return plan("stack", pk["name"])
            raise LookupError(f"no card with seed {key}")
        if e.get("_lifecycle") != "notarized":
            raise PermissionError(f"{e['name']} is not notarized; refusing to summon")
        return ({"name": e["display_name"], "by": e.get("author", "?"), "what": e["description"],
                 "id": e["name"]}, [(e["_install_filename"], f"{RAR}/{e['_file']}", e["_sha256"])])
    reg = get(f"{RAR}/registry.json")
    packs = [p for p in reg.get("stack_packs", []) if p["name"] == key]
    if not packs:
        raise LookupError(f"no stack named {key}")
    pk = packs[0]
    if not pk.get("_verified"):  # RAR could not vouch for these bytes: refuse
        raise PermissionError(f"stack {key} is not verified in RAR; refusing to summon")
    files = [(n, f"{RAR}/{pk['path']}/{n}", m["sha256"]) for n, m in pk["files"].items() if n.endswith("_agent.py")]
    return ({"name": pk["display_name"], "by": "stack", "what": pk["purpose"], "id": pk["path"],
             "_pack": pk}, files)


def tailnet():
    """(ip, magicdns name) of this machine on Tailscale, or (None, None)."""
    ts = shutil.which("tailscale") or "/Applications/Tailscale.app/Contents/MacOS/Tailscale"
    try:
        st = json.loads(subprocess.run([ts, "status", "--json"], capture_output=True, text=True, timeout=10).stdout)
        me = st["Self"]
        ip = next(a for a in me["TailscaleIPs"] if "." in a)
        return ip, me.get("DNSName", "").rstrip(".") or ip
    except Exception:
        return None, None


def pair_page():
    ip, name = tailnet()
    if not ip:
        return "<p>Tailscale is not running on this Mac, so phones can't reach it yet. Start Tailscale, then reload.</p>"
    link = f"{PAGES}/s.html#pair=http://{name}:{PORT}"
    svg = ""
    if shutil.which("qrencode"):
        svg = subprocess.run(["qrencode", "-t", "SVG", "-m", "2", "-o", "-", link],
                             capture_output=True, text=True).stdout
    return (f"<h2>Pair your phone</h2><p>Scan this with your phone's camera. Your phone must be on your Tailscale network.</p>"
            f"<div style='background:#fff;padding:12px;border-radius:12px;max-width:300px'>{svg}</div>"
            f"<details><summary>Can't scan?</summary><p>Open this on the phone: <code>{html.escape(link)}</code></p></details>")


def import_file(name, payload, sha):
    """Multipart POST to the kernel's own /agents/import. Loopback, no Origin header."""
    b = uuid.uuid4().hex
    body = (f"--{b}\r\nContent-Disposition: form-data; name=\"sha256\"\r\n\r\n{sha}\r\n"
            f"--{b}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{name}\"\r\n"
            f"Content-Type: text/x-python\r\n\r\n").encode() + payload + f"\r\n--{b}--\r\n".encode()
    req = urllib.request.Request(f"{BRAIN}/agents/import", body,
                                 {"Content-Type": f"multipart/form-data; boundary={b}"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read() or b"{}")


DISTROS = Path.home() / ".brainstem" / "distros"
KERNEL_FILES = ["brainstem.py", "local_storage.py", "VERSION", "requirements.txt", "index.html"]
_live = {}  # name -> {"port", "pid", "proxy"}


def port_owners(port):
    out = subprocess.run(["lsof", "-tnP", f"-iTCP:{port}", "-sTCP:LISTEN"], capture_output=True, text=True).stdout.split()
    return {int(x) for x in out}


def port_owner(port):
    """Some PID listening on the port, or None (use port_owners to test a specific PID:
    a distro's port is held by both its Brainstem and this sidecar's tailnet forwarder)."""
    o = port_owners(port)
    return min(o) if o else None


def forward(listen_ip, port):
    """Tailnet-only door to a distro Brainstem that itself listens only on loopback."""
    import socket
    srv = socket.socket(); srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((listen_ip, port)); srv.listen(32)

    def pipe(a, b):
        try:
            while (d := a.recv(65536)):
                b.sendall(d)
        except OSError:
            pass
        finally:
            for x in (a, b):
                try: x.close()
                except OSError: pass

    def loop():
        while True:
            c, _ = srv.accept()
            try:
                u = socket.create_connection(("127.0.0.1", port))
            except OSError:
                c.close(); continue
            threading.Thread(target=pipe, args=(c, u), daemon=True).start()
            threading.Thread(target=pipe, args=(u, c), daemon=True).start()
    threading.Thread(target=loop, daemon=True).start()


def brain_python():
    """The interpreter of the process serving the main Brainstem's port."""
    port = BRAIN.rsplit(":", 1)[-1].strip("/")
    for pid in port_owners(port):
        exe = subprocess.run(["ps", "-o", "comm=", "-p", str(pid)], capture_output=True, text=True).stdout.strip()
        if exe and os.path.isabs(exe) and os.access(exe, os.X_OK):
            return exe
    return None


def summon_distro(card, pk):
    """A distro gets its OWN fresh Brainstem: the same pinned kernel (hardlinked, sha-checked),
    its own agents, soul and memory. The owner's main Brainstem is never touched."""
    name = pk["name"]
    if name in _live and _live[name]["pid"] in port_owners(_live[name]["port"]):
        return {"card": card, "ok": True, "already": True, "chat_url": _live[name]["url"], "results": []}
    pin = (pk.get("kernel") or {}).get("sha256", "")
    health = get(f"{BRAIN}/health")
    kd = Path(health.get("brainstem_dir") or "")
    if not (kd / "brainstem.py").is_file():
        raise RuntimeError("could not locate this Brainstem's kernel (is it signed in?)")
    have = hashlib.sha256((kd / "brainstem.py").read_bytes()).hexdigest()
    if have != pin:
        raise PermissionError(f"this distro pins kernel {pin[:12]}, but this Brainstem runs {have[:12]}; refusing")
    seat = DISTROS / name
    (seat / "agents").mkdir(parents=True, exist_ok=True)
    for f in KERNEL_FILES:  # same bytes, same fingerprint, never edited
        if not (seat / f).exists():
            os.link(kd / f, seat / f)
    if not (seat / "agents" / "basic_agent.py").exists():
        os.link(kd / "agents" / "basic_agent.py", seat / "agents" / "basic_agent.py")
    (seat / "agents" / "__init__.py").touch()  # beat any same-named site-packages 'agents'
    for f in (".copilot_token", ".copilot_session"):
        if (kd / f).exists() and not (seat / f).exists():
            shutil.copy2(kd / f, seat / f); os.chmod(seat / f, 0o600)
    results = []
    for fname, meta in pk["files"].items():
        if not (fname.endswith("_agent.py") or fname == "soul.md"):
            continue
        body = get(f"{RAR}/{pk['path']}/{fname}", binary=True)
        ok = hashlib.sha256(body).hexdigest() == meta["sha256"]
        results.append({"file": fname, "ok": ok, **({} if ok else {"error": "sha mismatch"})})
        if ok:
            (seat / ("soul.md" if fname == "soul.md" else f"agents/{fname}")).write_bytes(body)
    if not all(r["ok"] for r in results):
        return {"card": card, "ok": False, "results": results}
    ip, dns = tailnet()
    port = next(p for p in range(7500, 7600) if port_owner(p) is None)
    env = {**os.environ, "PORT": str(port), "PYTHONUNBUFFERED": "1",
           "AGENTS_PATH": str(seat / "agents"), "SOUL_PATH": str(seat / "soul.md"),
           "BRAINSTEM_ALLOWED_HOSTS": ",".join(h for h in (dns, ip) if h)}
    py = brain_python() or sys.executable  # the main Brainstem's own Python has the kernel's packages
    proc = subprocess.Popen([py, str(seat / "brainstem.py")], cwd=seat, env=env,
                            stdout=open(seat / "brainstem.log", "w"), stderr=subprocess.STDOUT,
                            start_new_session=True)
    for _ in range(300):
        if proc.poll() is not None:
            raise RuntimeError(f"the distro's Brainstem exited; see {seat / 'brainstem.log'}")
        if proc.pid in port_owners(port):
            break
        time.sleep(0.2)
    else:
        proc.kill(); raise RuntimeError("the distro's Brainstem did not come up in time")
    if ip:
        forward(ip, port)
    url = f"http://{dns}:{port}/" if ip else f"http://127.0.0.1:{port}/"
    _live[name] = {"port": port, "pid": proc.pid, "url": url}
    (seat / "state.json").write_text(json.dumps({"port": port, "pid": proc.pid, "url": url, "kernel": have}))
    return {"card": card, "ok": True, "results": results, "chat_url": url}


def summon(kind, key):
    card, files = plan(kind, key)
    pk = card.pop("_pack", None)
    if pk and pk.get("kernel"):
        return summon_distro(card, pk)
    results = []
    for name, url, sha in files:
        payload = get(url, binary=True)
        got = hashlib.sha256(payload).hexdigest()
        if got != sha:  # refuse before the kernel ever sees it
            results.append({"file": name, "ok": False, "error": f"sha mismatch {got[:12]} != {sha[:12]}"})
            continue
        code, body = import_file(name, payload, sha)
        results.append({"file": name, "ok": code == 200, "status": code, "kernel": body})
    return {"card": card, "results": results, "ok": all(r["ok"] for r in results)}


PAGE = """<!doctype html><meta name=viewport content="width=device-width,initial-scale=1">
<title>Summon</title><style>body{{font:17px -apple-system,sans-serif;max-width:420px;margin:24px auto;padding:0 16px}}
.card{{border-radius:16px;padding:20px;background:#111827;color:#fff}}.by{{opacity:.7;font-size:14px}}
button{{width:100%;padding:16px;margin-top:18px;font-size:18px;border:0;border-radius:12px;background:#2563eb;color:#fff}}
#out{{margin-top:14px}}</style>
<div class=card><h2>{name}</h2><div class=by>by {by} &middot; {id}</div><p>{what}</p>
<div class=by>Installs into your Brainstem at {brain}</div></div>
<button onclick="go()">Summon</button><div id=out></div>
<script>async function go(){{const o=document.getElementById('out');o.textContent='Summoning…';
const r=await fetch(location.pathname,{{method:'POST'}});const j=await r.json();
if(j.ok&&j.chat_url){{o.textContent='Summoned: '+j.card.name+' — opening its Brainstem…';location.href=j.chat_url;return}}
o.textContent=j.ok?('Summoned: '+j.card.name+' — ready in your next chat'):('Not installed: '+JSON.stringify(j.results||j.error))}}</script>"""


class Server(ThreadingHTTPServer):
    """Skip HTTPServer's reverse-DNS lookup of its own address (getfqdn): on a Tailscale
    address it can hang for a long time, and the name is never used."""
    def server_bind(self):
        import socketserver
        socketserver.TCPServer.server_bind(self)
        self.server_name, self.server_port = self.server_address[:2]


class H(BaseHTTPRequestHandler):
    def route(self):
        p = self.path.strip("/").split("/")
        if len(p) == 2 and p[0] == "s":
            return "seed", p[1]
        if len(p) == 3 and p[:2] == ["s", "stack"]:
            return "stack", p[2]
        return None

    def reply(self, code, ctype, body):
        self.send_response(code); self.send_header("Content-Type", ctype); self.end_headers()
        self.wfile.write(body.encode() if isinstance(body, str) else body)

    def do_GET(self):
        if self.path.rstrip("/") == "/pair":
            if self.client_address[0] != "127.0.0.1":  # pairing is shown only on this Mac
                return self.reply(403, "text/plain", "open /pair on the Mac running your Brainstem")
            return self.reply(200, "text/html; charset=utf-8",
                              "<meta name=viewport content='width=device-width'><body style='font-family:-apple-system,sans-serif;max-width:420px;margin:24px auto'>" + pair_page())
        r = self.route()
        if not r:
            return self.reply(404, "text/plain", "scan a card: /s/<seed> or /s/stack/<name>")
        try:
            card, files = plan(*r)
        except Exception as e:
            return self.reply(404, "text/plain", f"not found: {e}")
        esc = {k: html.escape(str(v)) for k, v in card.items()}
        self.reply(200, "text/html; charset=utf-8", PAGE.format(brain=html.escape(BRAIN), **esc))

    def do_POST(self):
        r = self.route()
        if not r:
            return self.reply(404, "application/json", '{"error":"bad path"}')
        try:
            out = summon(*r)
        except Exception as e:
            out = {"ok": False, "error": str(e)}
        self.reply(200, "application/json", json.dumps(out))

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    ip, name = tailnet()
    binds = ["127.0.0.1"] + ([ip] if ip else [])
    for addr in binds[1:]:
        threading.Thread(target=Server((addr, PORT), H).serve_forever, daemon=True).start()
    print(f"summond on {', '.join(binds)}:{PORT} -> {BRAIN}  (RAR {RAR})  pair: http://127.0.0.1:{PORT}/pair", flush=True)
    Server(("127.0.0.1", PORT), H).serve_forever()
