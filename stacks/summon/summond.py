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
import html, json, hashlib, shutil, subprocess, sys, threading, time, urllib.request, uuid
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
        if not e:
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
    return ({"name": pk["display_name"], "by": "stack", "what": pk["purpose"], "id": pk["path"]}, files)


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


def summon(kind, key):
    card, files = plan(kind, key)
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
