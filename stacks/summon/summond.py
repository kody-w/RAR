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
import hmac, html, json, hashlib, os, re, secrets, shutil, subprocess, sys, threading, time, urllib.request, uuid
from urllib.parse import parse_qs, urlsplit
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


HOME = Path(os.getenv("SUMMON_HOME") or Path(__file__).resolve().parent)
NAME_OK = re.compile(r"^[a-z0-9][a-z0-9_-]{0,63}$")


def pair_key():
    """One secret per sidecar, given to a phone once through the pairing QR on this Mac.
    Every request from the tailnet must carry it; delete pair.key to un-pair every phone."""
    f = HOME / "pair.key"
    if not f.exists():
        f.write_text(secrets.token_urlsafe(24))
        os.chmod(f, 0o600)
    return f.read_text().strip()


def key_matches(given):
    return bool(given) and hmac.compare_digest(given.encode(), pair_key().encode())


def pair_page():
    ip, name = tailnet()
    if not ip:
        return "<p>Tailscale is not running on this Mac, so phones can't reach it yet. Start Tailscale, then reload.</p>"
    link = f"{PAGES}/s.html#pair=http://{name}:{PORT}&k={pair_key()}"
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


def _gate(c):
    """Read one request head from the tailnet. Let it through only with the pairing key:
    ?k=<key> once (answered with a cookie and a redirect), then the cookie on every request."""
    buf = b""
    while b"\r\n\r\n" not in buf and len(buf) < 65536:
        d = c.recv(65536)
        if not d:
            return None
        buf += d
    head = buf.split(b"\r\n\r\n", 1)[0].decode("latin-1")
    parts = head.split("\r\n", 1)[0].split(" ")
    target = urlsplit(parts[1] if len(parts) > 1 else "/")
    cookie = re.search(r"(?:^|[;\s])summon_k=([A-Za-z0-9_-]+)", head)
    if key_matches(parse_qs(target.query).get("k", [""])[0]):
        rest = "&".join(f"{k}={v[0]}" for k, v in parse_qs(target.query).items() if k != "k")
        loc = target.path + ("?" + rest if rest else "")
        c.sendall((f"HTTP/1.1 302 Found\r\nLocation: {loc}\r\nSet-Cookie: summon_k={pair_key()}; Path=/; "
                   "HttpOnly; SameSite=Strict; Max-Age=2592000\r\nContent-Length: 0\r\nConnection: close\r\n\r\n").encode())
        return None
    if cookie and key_matches(cookie.group(1)):
        return buf
    msg = b"This device is not paired. Open /pair on the Mac running your Brainstem and scan it."
    c.sendall(b"HTTP/1.1 403 Forbidden\r\nContent-Type: text/plain\r\nConnection: close\r\nContent-Length: "
              + str(len(msg)).encode() + b"\r\n\r\n" + msg)
    return None


def forward(listen_ip, port):
    """Tailnet-only, key-gated door to a distro Brainstem that itself listens only on loopback.
    (The kernel trusts loopback callers, so without this gate the tailnet would inherit that trust.)"""
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

    def serve(c):
        try:
            c.settimeout(30)
            first = _gate(c)
            c.settimeout(None)
        except OSError:
            first = None
        if first is None:
            try: c.close()
            except OSError: pass
            return
        try:
            u = socket.create_connection(("127.0.0.1", port))
        except OSError:
            c.close(); return
        u.sendall(first)
        threading.Thread(target=pipe, args=(c, u), daemon=True).start()
        pipe(u, c)

    def loop():
        while True:
            try:
                c, _ = srv.accept()
            except OSError:  # the door was closed (dismiss)
                return
            threading.Thread(target=serve, args=(c,), daemon=True).start()
    threading.Thread(target=loop, daemon=True).start()
    return srv


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
        return {"card": card, "ok": True, "already": True, "results": [],
                "chat_url": _live[name]["url"] + (f"?k={pair_key()}" if _live[name].get("srv") else "")}
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
    (seat / "pack.json").write_text(json.dumps(pk, indent=1))
    results += seed_layers(seat, pk)
    if not all(r["ok"] for r in results):
        return {"card": card, "ok": False, "results": results}
    return {"card": card, "results": results, **launch(seat, name, have)}


SUPERVISOR = Path.home() / ".brainstem" / "layers" / "grail_layers.py"
PART_KEYS = ("id", "kind", "point", "file", "sha256", "locator")


def seed_layers(seat, pk):
    """A distro that lists grail layers (pack >= 1.2: install.parts + seed) gets them seeded into its OWN chain
    under <seat>/layers, every part's bytes checked against the pack's sha256. The same supervisor that runs the
    main Brainstem applies them in memory over the unchanged kernel and falls back to plain grail on any failure.
    No parts, or no supervisor installed: the seat boots plain grail exactly as before."""
    inst = pk.get("install") or {}
    parts = inst.get("parts") or []
    seed = inst.get("seed")
    if seed is not None:
        parts = [x for x in parts if x.get("id") in seed]
    if not parts:
        return []
    home = seat / "layers"
    (home / "parts").mkdir(parents=True, exist_ok=True)
    results, seeded = [], []
    for part in parts:
        try:
            part = {k: part[k] for k in PART_KEYS}
            body = get(part["locator"], binary=True)
            ok = hashlib.sha256(body).hexdigest() == part["sha256"]
        except Exception as e:  # a missing key or an unreachable locator is a refusal, never a half-install
            results.append({"file": str(part.get("id")), "ok": False, "error": str(e)[:120]}); continue
        results.append({"file": part["id"], "ok": ok, **({} if ok else {"error": "sha mismatch"})})
        if ok:
            pub, nm = part["id"][1:].split("/", 1)
            target = home / "parts" / pub / nm / part["file"]
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(body)
            seeded.append(part)
    (home / "parts.json").write_text(json.dumps(seeded, indent=1) + "\n")
    return results


def launch(seat, name, have):
    """Start a distro's Brainstem from its folder and open its key-gated tailnet door."""
    ip, dns = tailnet()
    port = next(p for p in range(7500, 7600) if port_owner(p) is None)
    env = {**os.environ, "PORT": str(port), "PYTHONUNBUFFERED": "1",
           "AGENTS_PATH": str(seat / "agents"), "SOUL_PATH": str(seat / "soul.md"),
           "BRAINSTEM_ALLOWED_HOSTS": ",".join(h for h in (dns, ip) if h)}
    env.pop("BRAINSTEM_LAN_MODE", None)  # the distro listens on loopback only; the gated door is its only way in
    py = brain_python() or sys.executable  # the main Brainstem's own Python has the kernel's packages
    layered = (seat / "layers" / "parts.json").is_file() and SUPERVISOR.is_file()
    if layered:  # grail + the pack's layers, applied in memory; the supervisor falls back to plain grail itself
        env["GRAIL_LAYERS_HOME"] = str(seat / "layers")
        cmd = [py, str(SUPERVISOR), "--kernel", str(seat / "brainstem.py"), "--port", str(port),
               "--lab-port", str(port + 10000), "--python", py]
    else:
        cmd = [py, str(seat / "brainstem.py")]
    proc = subprocess.Popen(cmd, cwd=seat, env=env,
                            stdout=open(seat / "brainstem.log", "w"), stderr=subprocess.STDOUT,
                            start_new_session=True)
    owner = None
    for _ in range(600):  # a layered boot proves itself in the lab first: up to 2 minutes
        if proc.poll() is not None:
            raise RuntimeError(f"the distro's Brainstem exited; see {seat / 'brainstem.log'}")
        owner = next((p for p in port_owners(port) if p == proc.pid or _parent(p) == proc.pid), None)
        if owner:
            break
        time.sleep(0.2)
    else:
        proc.kill(); raise RuntimeError("the distro's Brainstem did not come up in time")
    srv = forward(ip, port) if ip else None
    url = f"http://{dns}:{port}/" if ip else f"http://127.0.0.1:{port}/"
    _live[name] = {"port": port, "pid": owner, "url": url, "srv": srv}
    (seat / "state.json").write_text(json.dumps({"port": port, "pid": owner, "url": url, "kernel": have,
                                                 "layered": layered}))
    return {"ok": True, "chat_url": url + (f"?k={pair_key()}" if ip else ""),
            "local_url": f"http://127.0.0.1:{port}/"}


ATTIC = DISTROS.parent / "distros-attic"


def _parent(pid):
    out = subprocess.run(["ps", "-o", "ppid=", "-p", str(pid)], capture_output=True, text=True).stdout.strip()
    return int(out) if out.isdigit() else None


def _seat_pids(seat):
    """Processes running a kernel from inside this distro's folder (its Brainstem and any helpers)."""
    out = subprocess.run(["ps", "-axo", "pid=,command="], capture_output=True, text=True).stdout
    mark = str(seat) + "/"
    return [int(l.split(None, 1)[0]) for l in out.splitlines()
            if mark in l and int(l.split(None, 1)[0]) != os.getpid()]


def list_distros():
    rows = []
    for d in sorted(DISTROS.iterdir()) if DISTROS.is_dir() else []:
        st = json.loads((d / "state.json").read_text()) if (d / "state.json").exists() else {}
        on = bool(st) and st.get("pid") in port_owners(st.get("port", 0))
        rows.append({"name": d.name, "running": on, "url": st.get("url") if on else None})
    attic = sorted(p.name for p in ATTIC.iterdir()) if ATTIC.is_dir() else []
    return {"ok": True, "summoned": rows, "dismissed": attic}


def dismiss(name):
    """Stop a distro and move its folder (memory included) to the attic. Never deletes; restore undoes it."""
    seat = DISTROS / name
    if not NAME_OK.match(name) or not seat.is_dir():
        return {"ok": False, "error": f"no summoned distro called {name}"}
    live = _live.pop(name, None)
    if live and live.get("srv"):
        live["srv"].close()
    pids = _seat_pids(seat)
    for pid in pids:
        try: os.kill(pid, 15)
        except ProcessLookupError: pass
    for _ in range(100):
        if not _seat_pids(seat):
            break
        time.sleep(0.1)
    for pid in _seat_pids(seat):  # still running after 10s: force it (only processes inside this folder)
        try: os.kill(pid, 9)
        except ProcessLookupError: pass
    time.sleep(0.5)
    if _seat_pids(seat):
        return {"ok": False, "error": "some of its processes would not stop, so nothing was moved"}
    ATTIC.mkdir(parents=True, exist_ok=True)
    dest = ATTIC / f"{name}-{time.strftime('%Y%m%d-%H%M%S')}"
    shutil.move(str(seat), dest)
    return {"ok": True, "stopped": pids, "moved_to": str(dest)}


def restore(name):
    """Bring back the newest dismissed copy of a distro, memory and all, and start it."""
    if not NAME_OK.match(name):
        return {"ok": False, "error": "bad name"}
    if (DISTROS / name).exists():
        return {"ok": False, "error": f"{name} is already summoned"}
    copies = sorted(ATTIC.glob(f"{name}-*")) if ATTIC.is_dir() else []
    if not copies:
        return {"ok": False, "error": f"no dismissed copy of {name}"}
    seat = DISTROS / name
    shutil.move(str(copies[-1]), seat)
    kd = Path(get(f"{BRAIN}/health").get("brainstem_dir") or "")
    have = hashlib.sha256((seat / "brainstem.py").read_bytes()).hexdigest()
    pin = (json.loads((seat / "pack.json").read_text()).get("kernel") or {}).get("sha256") \
        if (seat / "pack.json").exists() else have
    if have != pin or have != hashlib.sha256((kd / "brainstem.py").read_bytes()).hexdigest():
        return {"ok": False, "error": "its kernel no longer matches this Brainstem's; summon it fresh instead"}
    return {"name": name, **launch(seat, name, have)}


def adopt():
    """On restart, re-open the doors of distros that are still running."""
    ip, _ = tailnet()
    for d in DISTROS.iterdir() if DISTROS.is_dir() else []:
        st = json.loads((d / "state.json").read_text()) if (d / "state.json").exists() else {}
        if st and st.get("pid") in port_owners(st["port"]):
            srv = forward(ip, st["port"]) if ip else None
            _live[d.name] = {**st, "srv": srv}


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
const r=await fetch(location.pathname+location.search,{{method:'POST'}});const j=await r.json();
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
        p = urlsplit(self.path).path.strip("/").split("/")
        if len(p) == 2 and p[0] == "s":
            return "seed", p[1]
        if len(p) == 3 and p[:2] == ["s", "stack"]:
            return "stack", p[2]
        return None

    def reply(self, code, ctype, body):
        self.send_response(code); self.send_header("Content-Type", ctype); self.end_headers()
        self.wfile.write(body.encode() if isinstance(body, str) else body)

    def local(self):
        return self.client_address[0] == "127.0.0.1"

    def paired(self):
        if self.local():
            return True
        return key_matches(parse_qs(urlsplit(self.path).query).get("k", [""])[0])

    def not_paired(self):
        return self.reply(403, "text/html; charset=utf-8",
                          "<meta name=viewport content='width=device-width'><body style='font-family:-apple-system,sans-serif;max-width:420px;margin:24px auto'>"
                          "<h2>Pair this phone first</h2><p>Open <b>/pair</b> on the Mac running your Brainstem and scan its code, then scan the card again.</p>")

    def do_GET(self):
        if urlsplit(self.path).path == "/distros":
            if not self.local():
                return self.reply(403, "application/json", '{"error":"only on this Mac"}')
            return self.reply(200, "application/json", json.dumps(list_distros()))
        if urlsplit(self.path).path.rstrip("/") == "/pair":
            if self.client_address[0] != "127.0.0.1":  # pairing is shown only on this Mac
                return self.reply(403, "text/plain", "open /pair on the Mac running your Brainstem")
            return self.reply(200, "text/html; charset=utf-8",
                              "<meta name=viewport content='width=device-width'><body style='font-family:-apple-system,sans-serif;max-width:420px;margin:24px auto'>" + pair_page())
        r = self.route()
        if not r:
            return self.reply(404, "text/plain", "scan a card: /s/<seed> or /s/stack/<name>")
        if not self.paired():
            return self.not_paired()
        try:
            card, files = plan(*r)
        except Exception as e:
            return self.reply(404, "text/plain", f"not found: {e}")
        esc = {k: html.escape(str(v)) for k, v in card.items()}
        self.reply(200, "text/html; charset=utf-8", PAGE.format(brain=html.escape(BRAIN), **esc))

    def do_POST(self):
        p = urlsplit(self.path).path.strip("/").split("/")
        if len(p) == 2 and p[0] in ("dismiss", "restore"):
            if not self.local():
                return self.reply(403, "application/json", '{"error":"only on this Mac"}')
            try:
                out = (dismiss if p[0] == "dismiss" else restore)(p[1])
            except Exception as e:
                out = {"ok": False, "error": str(e)}
            return self.reply(200, "application/json", json.dumps(out))
        if not self.paired():
            return self.reply(403, "application/json", '{"ok":false,"error":"this phone is not paired"}')
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
    pair_key(); adopt()
    ip, name = tailnet()
    binds = ["127.0.0.1"] + ([ip] if ip else [])
    for addr in binds[1:]:
        threading.Thread(target=Server((addr, PORT), H).serve_forever, daemon=True).start()
    print(f"summond on {', '.join(binds)}:{PORT} -> {BRAIN}  (RAR {RAR})  pair: http://127.0.0.1:{PORT}/pair", flush=True)
    Server(("127.0.0.1", PORT), H).serve_forever()
