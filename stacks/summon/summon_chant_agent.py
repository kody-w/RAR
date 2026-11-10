"""Summon by chant — say a card's seven words and it lands in this Brainstem.

No phone, no pairing, no sidecar. The seven words are a 64-bit seed (the same word list
every RAR card uses). The seed is looked up in the RAR catalog: one agent, or a whole
stack of agents, or a stack that carries an egg (an egg can hold anything under
rapp/1; the catalog's own egg hatcher opens it). Each file is downloaded, its sha256 is checked against the catalog, and
it is installed through this Brainstem's own /agents/import, which checks it again.
Everything is ready on the next message. Nothing in the Brainstem kernel changes.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/summon_chant_agent",
    "version": "1.0.0",
    "display_name": "Summon by chant",
    "description": "Say a card's seven-word chant (or its seed or @publisher/name) and the agent, or the whole stack, is installed into this Brainstem, fingerprint-checked, ready on the next message.",
    "author": "kody-w",
    "tags": ["summon", "chant", "install", "stack"],
    "category": "core",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": "Summon by chant: SAGE ZAP SENTINEL PIVOT CRUX EXTINGUISH BIND",
}

import hashlib
import json
import os
import re
import time
import urllib.error
import urllib.request
import uuid
from pathlib import Path

from agents.basic_agent import BasicAgent

RAR_BASE = os.getenv("RAR_BASE", "https://raw.githubusercontent.com/kody-w/RAR/main")
EGG_HATCHER = "@rapp/egg_hatcher"


def _brain():
    return os.getenv("BRAINSTEM_URL") or f"http://127.0.0.1:{os.getenv('PORT', '7071')}"


def _home():
    d = Path(os.getenv("CHANT_HOME") or (Path.home() / ".brainstem" / "chant"))
    d.mkdir(parents=True, exist_ok=True)
    return d


def _get(url, keep=None, max_age=300):
    """Fetch bytes. With keep=<name>, the last good copy is remembered: stale beats gone."""
    f = (_home() / keep) if keep else None
    if f and f.exists() and time.time() - f.stat().st_mtime < max_age:
        return f.read_bytes()
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            b = r.read()
        if f:
            f.write_bytes(b)
        return b
    except Exception:
        if f and f.exists():
            return f.read_bytes()
        raise


def words():
    """The chant word list is the protocol: read it from RAR's rapp_sdk.py, never keep a second copy."""
    src = _get(f"{RAR_BASE}/rapp_sdk.py", keep="rapp_sdk.py", max_age=86400).decode("utf-8", "replace")
    m = re.search(r'MNEMONIC_WORDS = """(.*?)"""', src, re.S)
    if not m:
        raise RuntimeError("the chant word list could not be loaded")
    return m.group(1).split()


def chant_to_seed(chant):
    idx = {w: i for i, w in enumerate(words())}
    ws = re.sub(r"[+,.\-]", " ", str(chant).upper()).split()
    if len(ws) != 7:
        raise ValueError("A chant is exactly 7 words.")
    seed = 0
    for i, w in enumerate(ws):
        if w not in idx:
            raise ValueError(f'"{w}" is not a chant word.')
        seed |= idx[w] << (10 * i)
    return str(seed)


def seed_to_chant(seed):
    w = words()
    return " ".join(w[(int(seed) >> (10 * i)) & 1023] for i in range(7))


def parse(text):
    """-> ('seed', '123…') or ('name', '@pub/slug'). Accepts a chant, a seed, or a card name."""
    t = str(text or "").strip().lstrip("#")
    for p in ("incant=", "seed=", "add="):
        if t.startswith(p):
            t = t[len(p):]
    if re.fullmatch(r"@[^/\s]+/\S+", t):
        return "name", t
    if re.fullmatch(r"0x[0-9a-fA-F]+", t):
        return "seed", str(int(t, 16))
    if re.fullmatch(r"\d{6,}", t):
        return "seed", t
    return "seed", chant_to_seed(t)


def catalog():
    return json.loads(_get(f"{RAR_BASE}/registry.json", keep="registry.json"))


def in_catalog(kind, key):
    key_ = key.replace("-", "_")
    for e in catalog().get("agents", []):
        if kind == "name" and e.get("name", "").replace("-", "_") in (key_, key_ + "_agent"):
            return e
        if kind == "seed" and (str(e.get("_seed")) == key or key in [str(s) for s in e.get("_seed_aliases", [])]):
            return e
    return None


def install(filename, payload, sha):
    """Multipart POST to this Brainstem's own /agents/import over loopback; it re-checks the sha256."""
    b = uuid.uuid4().hex
    body = (f"--{b}\r\nContent-Disposition: form-data; name=\"sha256\"\r\n\r\n{sha}\r\n"
            f"--{b}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{filename}\"\r\n"
            f"Content-Type: text/x-python\r\n\r\n").encode() + payload + f"\r\n--{b}--\r\n".encode()
    req = urllib.request.Request(f"{_brain()}/agents/import", body,
                                 {"Content-Type": f"multipart/form-data; boundary={b}"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read() or b"{}")


def in_stacks(kind, key):
    for p in catalog().get("stack_packs", []):
        if (kind == "seed" and str(p.get("_seed")) == key) or (kind == "name" and p.get("name") == key.lstrip("@").split("/")[-1]):
            return p
    return None


def _put(filename, url, sha):
    payload = _get(url)
    got = hashlib.sha256(payload).hexdigest()
    if got != sha:
        return {"file": filename, "ok": False, "error": "did not match its catalog fingerprint"}
    code, body = install(filename, payload, got)
    ok = code == 200 and body.get("status") == "ok"
    return {"file": filename, "ok": ok, "sha256": got, "error": None if ok else body.get("error", f"the Brainstem answered {code}")}


def _keep_egg(filename, url, sha):
    """Download an egg, check its catalog fingerprint, keep it on this device for the hatcher."""
    payload = _get(url)
    got = hashlib.sha256(payload).hexdigest()
    if got != sha:
        return {"file": filename, "ok": False, "error": "did not match its catalog fingerprint"}
    d = _home() / "eggs"
    d.mkdir(exist_ok=True)
    f = d / os.path.basename(filename)
    f.write_bytes(payload)
    return {"file": filename, "ok": True, "sha256": got, "path": str(f), "error": None}


def summon(text):
    """Resolve one chant, seed or name in the catalog and install it. One agent, or a whole stack."""
    kind, key = parse(text)
    e = in_catalog(kind, key)
    if e:
        if e.get("_lifecycle") != "notarized":
            return {"ok": False, "error": f"{e['name']} is not notarized in the catalog, so I won't install it."}
        r = _put(e["_install_filename"], f"{RAR_BASE}/{e['_file']}", e["_sha256"])
        return {"ok": r["ok"], "kind": "agent", "display": e.get("display_name", e["name"]), "name": e["name"],
                "files": [r], "error": None if r["ok"] else f"{e['name']}: {r['error']}"}
    p = in_stacks(kind, key)
    if p:
        if not p.get("_verified"):
            return {"ok": False, "error": f"The {p['name']} stack is not verified in the catalog, so I won't install it."}
        if p.get("status") == "retired":
            why = (p.get("retired") or {})
            return {"ok": False, "error": f"The {p['name']} stack is retired. {why.get('reason', '')} "
                                          f"{('Use ' + why['replacement'] + ' instead.') if why.get('replacement') else ''}".strip()}
        if p.get("kernel"):
            return {"ok": False, "error": f"{p.get('display_name', p['name'])} is a whole Brainstem, not an add-on. Scan its card to hatch it beside this one."}
        files = [(n, m) for n, m in p["files"].items() if n.endswith("_agent.py")]
        done = [_put(n, f"{RAR_BASE}/{p['path']}/{n}", m["sha256"]) for n, m in files]
        eggs = []
        for n, m in p["files"].items():
            if n.endswith(".egg"):
                eggs.append(_keep_egg(n, f"{RAR_BASE}/{p['path']}/{n}", m["sha256"]))
        if eggs:  # an egg can carry anything under rapp/1: the catalog's own hatcher opens it
            h = in_catalog("name", EGG_HATCHER)
            if h and h.get("_lifecycle") == "notarized":
                done.append(_put(h["_install_filename"], f"{RAR_BASE}/{h['_file']}", h["_sha256"]))
        parts = done + eggs
        ok = bool(parts) and all(d["ok"] for d in parts)
        bad = "; ".join(f"{d['file']} {d['error']}" for d in parts if not d["ok"])
        return {"ok": ok, "kind": "stack", "display": re.sub(r"\s+stack$", "", p.get("display_name", p["name"]), flags=re.I), "name": p["name"],
                "files": done, "eggs": eggs, "error": None if ok else (bad or "that stack carries nothing I can install")}
    return {"ok": False, "error": "No card answers to that chant." if kind == "seed" else f"No card named {key} in the catalog."}


_hop = {"busy": False}


def carry_on(then):
    """What was brought is live on the next message. Send that message ourselves, once."""
    if _hop["busy"]:
        return None
    _hop["busy"] = True
    try:
        req = urllib.request.Request(f"{_brain()}/chat", json.dumps({"user_input": then}).encode(),
                                     {"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=240) as r:
            return json.loads(r.read() or b"{}").get("response") or None
    except Exception:
        return None
    finally:
        _hop["busy"] = False


class SummonChantAgent(BasicAgent):
    def __init__(self):
        self.name = "SummonByChant"
        self.metadata = {
            "name": self.name,
            "description": ("Install an agent or a whole stack into this Brainstem from its chant. Use when the person "
                            "says a seven-word chant, a card seed, or a name like @publisher/name, or asks to summon, "
                            "bring or add a card. Everything is fingerprint-checked against the catalog and ready on "
                            "the next message."),
            "parameters": {
                "type": "object",
                "properties": {
                    "chant": {"type": "string",
                              "description": "the seven words exactly as said, or a seed number, or @publisher/name"},
                    "then": {"type": "string",
                             "description": ("everything the person asked for after the bring, in their words "
                                             "(for example 'Check it answers. Show me.'). It runs once what was "
                                             "brought is live. Leave out if they only asked to bring.")},
                },
                "required": ["chant"],
            },
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs) -> str:
        try:
            r = summon(kwargs.get("chant", ""))
        except ValueError as e:
            return str(e)
        except Exception as e:
            return f"I couldn't summon that: {e}"
        if not r["ok"]:
            return r["error"]
        if r["kind"] == "stack" and r.get("eggs"):
            said = (f"Summoned the {r['display']} stack: {len(r['files'])} agents and an egg, every fingerprint "
                    f"matched. Nothing is hatched yet. The egg is kept at {r['eggs'][0]['path']}; ask the egg "
                    f"hatcher to open it.")
        elif r["kind"] == "stack":
            said = f"Summoned the {r['display']} stack: {len(r['files'])} agents, every fingerprint matched."
        else:
            said = (f"Summoned {r['display']} from the catalog. Its fingerprint matched "
                    f"({r['files'][0]['sha256'][:12]}).")
        then = str(kwargs.get("then") or "").strip()
        then = re.sub(r"\W*\b(and\s+)?seal\W*$", "", then, flags=re.I).strip()  # the seal closes the song; it is not a step
        brought = ", ".join(f["file"] for f in r["files"])
        answer = carry_on(f"(Just installed and live now: {brought}.) {then}") if then else None
        if answer:
            return f"{said} Then I carried on with what you asked, and this came back: {answer}"
        return f"{said} It is ready on your next message."


if __name__ == "__main__":
    import sys
    print(json.dumps(summon(" ".join(sys.argv[1:])), indent=1, default=str)[:900])
