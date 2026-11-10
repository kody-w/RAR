"""Summon by chant — say a card's seven words and its agent lands in this Brainstem.

No phone, no pairing, no sidecar. The seven words are a 64-bit seed (the same word list
every RAR card uses). The seed is looked up in the RAR catalog first, then across the
card federation (any GitHub repo that publishes a seed-index.json). The agent file is
downloaded, its sha256 is checked against the catalog, and it is installed through this
Brainstem's own /agents/import, which checks it again. It is ready on the next message.

An agent from a repo outside the catalog has no notary behind it, so it is never
installed unasked: this agent says where it comes from and waits for a clear yes.
Nothing in the Brainstem kernel changes.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/summon_chant_agent",
    "version": "1.0.0",
    "display_name": "Summon by chant",
    "description": "Say a card's seven-word chant (or its seed or @publisher/name) and the agent is installed into this Brainstem, fingerprint-checked, ready on the next message.",
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
import urllib.parse
import urllib.request
import uuid
from pathlib import Path

from agents.basic_agent import BasicAgent

RAR_BASE = os.getenv("RAR_BASE", "https://raw.githubusercontent.com/kody-w/RAR/main")
PEERS_URL = os.getenv("CHANT_PEERS_URL", "https://raw.githubusercontent.com/kody-w/RAPPcards/main/peers.json")
_REPO = re.compile(r"^[A-Za-z0-9][A-Za-z0-9-]*/[A-Za-z0-9._-]+$")


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


def dials():
    f = _home() / "dials.json"
    try:
        return [d for d in json.loads(f.read_text()) if _REPO.match(d)]
    except Exception:
        return []


def dial(repo):
    """Any GitHub repo with a seed-index.json at its root is a peer. Remember one the owner names."""
    if not _REPO.match(repo or ""):
        return False
    d = [repo] + [x for x in dials() if x != repo]
    (_home() / "dials.json").write_text(json.dumps(d[:24]))
    return True


def is_brainstem_agent(source):
    return bool(re.search(r"class\s+\w+\s*\(\s*BasicAgent\s*\)", source)) and "def perform" in source


def in_federation(seed):
    """Walk the owner's dialed repos, then the canonical peers. -> dict or None."""
    peers = [{"binder": r, "seed_index": f"https://raw.githubusercontent.com/{r}/main/seed-index.json"} for r in dials()]
    try:
        peers += json.loads(_get(PEERS_URL, keep="peers.json")).get("peers", [])
    except Exception:
        pass
    seen = set()
    for peer in peers:
        binder, url = peer.get("binder") or peer.get("id") or "", peer.get("seed_index")
        if not url or binder in ("rar", "rappcards") or url in seen:  # the catalog was checked first
            continue
        seen.add(url)
        try:
            idx = json.loads(_get(url, keep="idx-" + hashlib.sha256(url.encode()).hexdigest()[:16] + ".json"))
        except Exception:
            continue
        entry = (idx.get("seeds") or {}).get(seed)
        if not entry:
            continue
        if isinstance(entry, str):
            entry = {"url": entry}
        base = url.rsplit("/", 1)[0] + "/"
        card = {}
        try:
            blob = json.loads(_get(urllib.parse.urljoin(base, entry["url"])))
            card = (blob.get("cards", blob).get(entry.get("bundle_key") or entry.get("id"), {})
                    if (entry.get("url_is_bundle") or "cards" in blob) else blob)
        except Exception:
            pass
        cid = entry.get("id") or card.get("id") or ""
        slug = re.sub(r"_agent$", "", cid.split("/")[-1])
        meta = card.get("meta") or {}
        tries = [entry.get("agent_url"), card.get("agent_url"), meta.get("agent_url"), meta.get("_file"),
                 slug and f"agents/{slug}_agent.py", slug and f"agents/{slug}.py"]
        hit = {"binder": binder, "id": cid, "name": card.get("name") or entry.get("name") or cid,
               "source": None, "sha256": entry.get("sha256") or meta.get("sha256"),
               "file": re.sub(r"[^A-Za-z0-9_]", "_", slug or "card") + "_agent.py"}
        for t in [t for t in tries if t]:
            try:
                src = _get(urllib.parse.urljoin(base, t))
            except Exception:
                continue
            hit["source"] = src
            break
        return hit
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


def summon(text, yes=False, from_repo=None):
    """Resolve one chant, seed or card name and install it. Returns a result dict."""
    if from_repo:
        dial(from_repo)
    kind, key = parse(text)
    e = in_catalog(kind, key)
    if e:
        if e.get("_lifecycle") != "notarized":
            return {"ok": False, "error": f"{e['name']} is not notarized in the catalog, so I won't install it."}
        payload = _get(f"{RAR_BASE}/{e['_file']}")
        got = hashlib.sha256(payload).hexdigest()
        if got != e["_sha256"]:
            return {"ok": False, "error": f"{e['name']} did not match its catalog fingerprint, so I stopped."}
        code, body = install(e["_install_filename"], payload, got)
        ok = code == 200 and body.get("status") == "ok"
        return {"ok": ok, "from": "catalog", "name": e["name"], "display": e.get("display_name", e["name"]),
                "file": e["_install_filename"], "sha256": got, "kernel": body,
                "error": None if ok else body.get("error", f"the Brainstem answered {code}")}
    if kind == "name":
        return {"ok": False, "error": f"No card named {key} in the catalog."}
    hit = in_federation(key)
    if not hit:
        return {"ok": False, "seed": key, "error": "No card answers to that chant."}
    if not hit["source"]:
        return {"ok": False, "from": hit["binder"], "name": hit["id"],
                "error": f"{hit['name']} is in {hit['binder']}, but that card carries no agent file."}
    src = hit["source"].decode("utf-8", "replace")
    if not is_brainstem_agent(src):
        return {"ok": False, "from": hit["binder"], "name": hit["id"],
                "error": f"{hit['name']} is in {hit['binder']}, but its file is not a Brainstem agent, so it cannot run here."}
    got = hashlib.sha256(hit["source"]).hexdigest()
    if hit["sha256"] and hit["sha256"] != got:
        return {"ok": False, "from": hit["binder"], "name": hit["id"],
                "error": f"{hit['name']} did not match the fingerprint its own repo lists, so I stopped."}
    if not yes:
        return {"ok": False, "ask": True, "from": hit["binder"], "name": hit["id"], "display": hit["name"],
                "error": None}
    code, body = install(hit["file"], hit["source"], got)
    ok = code == 200 and body.get("status") == "ok"
    return {"ok": ok, "from": hit["binder"], "name": hit["id"], "display": hit["name"], "file": hit["file"],
            "sha256": got, "kernel": body, "error": None if ok else body.get("error", f"the Brainstem answered {code}")}


class SummonChantAgent(BasicAgent):
    def __init__(self):
        self.name = "SummonByChant"
        self.metadata = {
            "name": self.name,
            "description": ("Install an agent into this Brainstem from its chant. Use when the person says a "
                            "seven-word chant, a card seed, or a card name like @publisher/name, or asks to summon, "
                            "bring or add a card. The agent is fingerprint-checked and ready on the next message. "
                            "If the result says it is waiting for a yes, ask the person exactly that and call again "
                            "with yes=true only after they clearly agree."),
            "parameters": {
                "type": "object",
                "properties": {
                    "chant": {"type": "string",
                              "description": "the seven words exactly as said, or a seed number, or @publisher/name"},
                    "yes": {"type": "boolean",
                            "description": "true only after the person clearly agreed to add an agent from outside the catalog"},
                    "from_repo": {"type": "string",
                                  "description": "optional owner/repo to also look in (a GitHub repo with a seed-index.json)"},
                },
                "required": ["chant"],
            },
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs) -> str:
        try:
            r = summon(kwargs.get("chant", ""), yes=bool(kwargs.get("yes")), from_repo=kwargs.get("from_repo"))
        except ValueError as e:
            return str(e)
        except Exception as e:
            return f"I couldn't summon that: {e}"
        if r.get("ask"):
            return (f"{r['display']} comes from {r['from']}, not from the catalog, so nobody has checked it. "
                    f"Should I add it to this Brainstem?")
        if not r["ok"]:
            return r["error"]
        where = "the catalog" if r["from"] == "catalog" else r["from"]
        return (f"Summoned {r['display']} from {where}. Its fingerprint matched ({r['sha256'][:12]}). "
                f"It is ready on your next message.")


if __name__ == "__main__":
    import sys
    print(json.dumps(summon(" ".join(sys.argv[1:])), indent=1, default=str)[:900])
