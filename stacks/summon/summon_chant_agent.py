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
import subprocess
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


# ── team catalogs ── a team's own shelf is a git repo (private is fine) holding a registry.json of the same shape.
# It is kept as a clone on this device, read with the person's own git sign-in. No token ever passes through here.

def _catalogs_dir():
    d = _home() / "catalogs"
    d.mkdir(exist_ok=True)
    return d


def _clone(repo):
    return _catalogs_dir() / repo.replace("/", "--")


def _own_sign_in():
    """Git runs as the person, with their own GitHub sign-in, never with a token this Brainstem holds for its model."""
    env = {k: v for k, v in os.environ.items() if k not in ("GH_TOKEN", "GITHUB_TOKEN", "GH_ENTERPRISE_TOKEN")}
    env["GIT_TERMINAL_PROMPT"] = "0"
    return env


def _git(folder, *args):
    return subprocess.run(["git", "-C", str(folder), *args], capture_output=True, text=True, timeout=120,
                          env=_own_sign_in())


def team_catalogs():
    """-> [(repo, folder, registry)] for every team catalog on this device, freshened at most once a minute."""
    out = []
    for folder in sorted(_catalogs_dir().iterdir()):
        if not (folder / ".git").exists():
            continue
        stamp = folder / ".git" / "chant-pulled"
        if not stamp.exists() or time.time() - stamp.stat().st_mtime > 60:
            _git(folder, "pull", "--ff-only", "-q")
            stamp.write_text("")
        reg = folder / "registry.json"
        if reg.exists():
            out.append((folder.name.replace("--", "/", 1), folder, json.loads(reg.read_text())))
    return out


def add_catalog(repo):
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9-]*/[A-Za-z0-9._-]+", repo or ""):
        return "A team catalog is named like owner/name."
    folder = _clone(repo)
    if not folder.exists():
        r = subprocess.run(["git", "clone", "-q", f"https://github.com/{repo}.git", str(folder)],
                           capture_output=True, text=True, timeout=180, env=_own_sign_in())
        if r.returncode != 0:
            return f"I couldn't reach {repo}. Check the name, and that you are signed in to GitHub with access to it."
    if not (folder / "registry.json").exists():
        build_catalog(folder, repo)
    reg = json.loads((folder / "registry.json").read_text())
    n = len(reg.get("agents", [])) + len(reg.get("stack_packs", []))
    return f"Added the team catalog {repo}. Cards in it: {n}. Say a card's chant and it lands here."


def team_seed(repo, name):
    """A team card's seed comes from the catalog's name plus the card's name: it cannot shadow a public card."""
    return int.from_bytes(hashlib.sha256(f"{repo}:{name}".encode()).digest()[:8], "big") | 1 << 63


def build_catalog(folder, repo):
    """One input (the folder's agents/ and stacks/) -> registry.json. Idempotent."""
    folder = Path(folder)
    agents, packs = [], []
    for f in sorted((folder / "agents").glob("*_agent.py")) if (folder / "agents").exists() else []:
        name = f"@{repo.split('/')[0]}/{f.stem}"
        seed = team_seed(repo, name)
        m = re.search(r'"display_name":\s*["\']([^"\']+)["\']', f.read_text())
        agents.append({"name": name, "display_name": m.group(1) if m else f.stem, "_file": f"agents/{f.name}",
                       "_install_filename": f.name, "_sha256": hashlib.sha256(f.read_bytes()).hexdigest(),
                       "_seed": seed, "_incantation": seed_to_chant(seed), "_lifecycle": "team"})
    for d in sorted((folder / "stacks").iterdir()) if (folder / "stacks").exists() else []:
        files = {f.name: {"sha256": hashlib.sha256(f.read_bytes()).hexdigest()} for f in sorted(d.iterdir()) if f.is_file()}
        seed = team_seed(repo, d.name)
        packs.append({"name": d.name, "display_name": d.name.replace("-", " ").title(), "path": f"stacks/{d.name}",
                      "files": files, "_verified": True, "status": "current", "_seed": seed,
                      "_incantation": seed_to_chant(seed)})
    reg = {"schema": "rapp-registry/1.1", "catalog": repo, "base": f"https://github.com/{repo}",
           "agents": agents, "stack_packs": packs}
    (folder / "registry.json").write_text(json.dumps(reg, indent=1, sort_keys=True) + "\n")
    (folder / ".nojekyll").touch()
    return reg


def in_team(kind, key):
    """-> (repo, folder, entry, is_stack) from the first team catalog that answers, else None."""
    for repo, folder, reg in team_catalogs():
        for e in reg.get("agents", []):
            if (kind == "seed" and str(e.get("_seed")) == key) or (kind == "name" and e.get("name") == key):
                return repo, folder, e, False
        for p in reg.get("stack_packs", []):
            if (kind == "seed" and str(p.get("_seed")) == key) or (kind == "name" and p.get("name") == key.split("/")[-1]):
                return repo, folder, p, True
    return None


def _put_local(folder, rel, filename, sha):
    payload = (Path(folder) / rel).read_bytes()
    got = hashlib.sha256(payload).hexdigest()
    if got != sha:
        return {"file": filename, "ok": False, "error": "did not match its catalog fingerprint"}
    code, body = install(filename, payload, got)
    ok = code == 200 and body.get("status") == "ok"
    return {"file": filename, "ok": ok, "sha256": got, "error": None if ok else body.get("error", f"the Brainstem answered {code}")}


def summon_team(hit):
    repo, folder, e, is_stack = hit
    if not is_stack:
        done = [_put_local(folder, e["_file"], e["_install_filename"], e["_sha256"])]
    else:
        done = [_put_local(folder, f"{e['path']}/{n}", n, m["sha256"]) for n, m in e["files"].items() if n.endswith("_agent.py")]
    ok = bool(done) and all(d["ok"] for d in done)
    bad = "; ".join(f"{d['file']} {d['error']}" for d in done if not d["ok"])
    return {"ok": ok, "kind": "stack" if is_stack else "agent", "display": e.get("display_name", e["name"]),
            "name": e["name"], "files": done, "eggs": [], "source": f"your team catalog {repo}",
            "error": None if ok else (bad or "that card carries nothing I can install")}


# ── keep a song as a card ── the job you just did, as one agent file that can say itself and run itself.

CARD = '''"""{title}: a kept song. Say it to hear the job; go to run it again."""

__manifest__ = {{
    "schema": "rapp-agent/1.0", "name": "@{owner}/{slug}_song_agent", "version": "1.0.0",
    "display_name": {title!r}, "description": {desc!r}, "author": {owner!r},
    "tags": ["verse", "song"], "category": "operations", "quality_tier": "community",
    "requires_env": [], "dependencies": ["@rapp/basic_agent"],
}}

import json
import os
import urllib.request

from agents.basic_agent import BasicAgent

SONG = {song!r}


class {cls}(BasicAgent):
    def __init__(self):
        self.name = {tool!r}
        self.metadata = {{
            "name": self.name,
            "description": {desc!r},
            "parameters": {{"type": "object", "properties": {{"action": {{
                "type": "string", "enum": ["say", "go"],
                "description": "say = read the song aloud, word for word; go = run the job again"}}}}, "required": ["action"]}},
        }}
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs) -> str:
        if kwargs.get("action") != "go":
            return SONG
        url = os.getenv("BRAINSTEM_URL") or f"http://127.0.0.1:{{os.getenv('PORT', '7071')}}"
        steps = SONG.split("verse.", 1)[-1].rsplit("And seal", 1)[0].strip()
        req = urllib.request.Request(url + "/chat", json.dumps({{"user_input": "Do these steps in order and show me the result: " + steps}}).encode(),
                                     {{"Content-Type": "application/json"}})
        with urllib.request.urlopen(req, timeout=300) as r:
            return json.loads(r.read() or b"{{}}").get("response", "")
'''


def keep_song(title, song, repo=None):
    """Write the song as a card into a team catalog's folder, rebuild its registry, load it here. Nothing leaves this device."""
    song = " ".join(str(song or "").split())
    if not re.match(r"(?i)^r,? ?a,? ?p,? ?p,? verse\.", song) or not re.search(r"(?i)seal\W*$", song):
        return ('A song starts "R, A, P, P, verse." and ends "And seal." I was handed: "' + song[:120] +
                '". Pass the whole song, word for word.')
    cats = team_catalogs()
    if repo is None:
        if len(cats) != 1:
            return "Tell me which team catalog keeps it (owner/name)." if cats else "Add a team catalog first: say its owner/name."
        repo = cats[0][0]
    folder = _clone(repo)
    if not (folder / ".git").exists():
        return f"{repo} is not one of your team catalogs yet. Add it first."
    slug = re.sub(r"[^a-z0-9]+", "_", str(title or "").lower()).strip("_")
    if not slug:
        return "Give the song a short title."
    owner = repo.split("/")[0]
    cls = "".join(w.title() for w in slug.split("_")) + "SongAgent"
    desc = f"The kept song '{title}'. Use when the person asks to say, read aloud, hear, run or repeat {title}."
    body = CARD.format(title=title, owner=owner, slug=slug, song=song, cls=cls, tool=cls[:-5], desc=desc)
    (folder / "agents").mkdir(exist_ok=True)
    f = folder / "agents" / f"{slug}_song_agent.py"
    f.write_text(body)
    reg = build_catalog(folder, repo)
    e = [a for a in reg["agents"] if a["_install_filename"] == f.name][0]
    install(f.name, f.read_bytes(), e["_sha256"])
    return (f"Kept. '{title}' is a card now and its chant is {e['_incantation']}. It works on this device already. "
            f"Your team can't reach it until you say publish.")


def publish(repo=None, yes=False):
    """Send kept cards to the team: commit and push the catalog folder. A send, so it waits for a yes."""
    cats = team_catalogs()
    if repo is None and len(cats) == 1:
        repo = cats[0][0]
    if not repo or not (_clone(repo) / ".git").exists():
        return "Tell me which team catalog to publish to (owner/name)."
    folder = _clone(repo)
    build_catalog(folder, repo)
    changed = [l[3:] for l in _git(folder, "status", "--porcelain").stdout.splitlines()]
    if not changed:
        return f"Nothing new to publish to {repo}."
    if not yes:
        return f"This sends {len(changed)} changed files to {repo} where your whole team can bring them: {', '.join(changed[:6])}. Say yes to send."
    _git(folder, "add", "-A")
    c = _git(folder, "commit", "-q", "-m", "Keep songs as cards")
    r = _git(folder, "push", "-q")
    if c.returncode != 0 or r.returncode != 0:
        return f"The send to {repo} did not go through: {(r.stderr or c.stderr).strip()[:200]}"
    return f"Published to {repo}. Anyone on the team who has added this catalog can now say the chant."


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
    hit = in_team(kind, key)  # the team's own shelf answers first, and the reply says so
    if hit:
        return summon_team(hit)
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
            "description": ("Also: add a team catalog (owner/name), keep a song as a card, publish kept cards to the team. "
                            "Install an agent or a whole stack into this Brainstem from its chant. Use when the person "
                            "says a seven-word chant, a card seed, or a name like @publisher/name, or asks to summon, "
                            "bring or add a card. Everything is fingerprint-checked against the catalog and ready on "
                            "the next message."),
            "parameters": {
                "type": "object",
                "properties": {
                    "chant": {"type": "string",
                              "description": "the seven words exactly as said, or a seed number, or @publisher/name"},
                    "catalog": {"type": "string",
                                "description": "owner/name of a team catalog: to add it, or to say which one a keep or publish is for"},
                    "keep": {"type": "string",
                             "description": ("the ENTIRE song to keep as a card, copied word for word in one string: it starts "
                                             "'R, A, P, P, verse.', includes every step and every chant word, and ends 'And seal.' "
                                             "When keeping, pass only keep and title; do not also pass chant.")},
                    "title": {"type": "string", "description": "a short title for the song being kept"},
                    "publish": {"type": "boolean", "description": "true when the person asks to publish kept cards to the team"},
                    "yes": {"type": "boolean", "description": "true only when the person said yes to sending, in this message"},
                    "then": {"type": "string",
                             "description": ("everything the person asked for after the bring, in their words "
                                             "(for example 'Check it answers. Show me.'). It runs once what was "
                                             "brought is live. Leave out if they only asked to bring.")},
                },
            },
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs) -> str:
        try:
            if kwargs.get("keep"):
                return keep_song(kwargs.get("title"), kwargs["keep"], kwargs.get("catalog"))
            if kwargs.get("publish"):
                return publish(kwargs.get("catalog"), bool(kwargs.get("yes")))
            if kwargs.get("catalog") and not kwargs.get("chant"):
                return add_catalog(kwargs["catalog"])
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
            said = (f"Summoned {r['display']} from {r.get('source', 'the catalog')}. Its fingerprint matched "
                    f"({r['files'][0]['sha256'][:12]}).")
        then = str(kwargs.get("then") or "").strip()
        then = re.sub(r"\W*\b(and\s+)?seal\W*$", "", then, flags=re.I).strip()  # the seal closes the song; it is not a step
        brought = ", ".join(f["file"] for f in r["files"])
        for egg in r.get("eggs") or []:
            brought += f"; its egg is kept at {egg['path']}, not hatched yet"
        answer = carry_on(f"(Just installed and live now: {brought}.) {then}") if then else None
        if answer:
            return f"{said} Then I carried on with what you asked, and this came back: {answer}"
        return f"{said} It is ready on your next message."


if __name__ == "__main__":
    import sys
    print(json.dumps(summon(" ".join(sys.argv[1:])), indent=1, default=str)[:900])
