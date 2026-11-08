"""TrustGate: your Brainstem's credit score for its own claims (rapp-trust/1).

Before it says "done", it bets part of its score that the claim is true. A judge or a person settles the bet from
evidence. A wrong confident claim costs the stake; a right one pays a little. The score gates what it may do alone:
  80+  ordinary          act as usual
  50-79 no-irreversible-alone   ask before anything that cannot be undone
  <50  owner-verifies    the owner checks every claim
Nothing is stored but the frames; the score is recomputed from them every time (rapp-trust/1, kody-w/rapp-1).

Userland route 1: an agent file. The kernel is untouched. The three public MIT reference files (rapp.py, rapp_profile.py, rapp_trust.py)
are streamed from kody-w/rapp-1 at a pinned commit, checked against pinned sha256 and cached; never vendored.
Drop this file into your brainstem's agents/ ; the ledger lives at <brainstem data>/trust/ledger.jsonl.
"""
import os, sys, json, hashlib, pathlib, importlib.util, urllib.request, datetime
from agents.basic_agent import BasicAgent

PIN = {"commit": "fe141f4643f11fbee3f80edc386b7d2af0db2b6f",
       "rapp.py": "76154a2b2e0a71cceda92c2c1b50a1cd8f7878b1892d0d093d523c4e5256eb87",
       "rapp_profile.py": "23c2ee228bfbe2d18880a7a57df118d96b185caca20dadc6998cee192c9a9008",
       "rapp_trust.py": "d4fe019075b0954cd87401f1fe0fa59f364852f519e4e41bc6b73bfbb79683f3"}
RAW = "https://raw.githubusercontent.com/kody-w/rapp-1/{commit}/{name}"
HOME = pathlib.Path(os.environ.get("BRAINSTEM_DATA", pathlib.Path.home() / ".brainstem/data")) / "trust"
LEDGER = HOME / "ledger.jsonl"
CACHE = HOME / "ref"

def _ref(name):
    """The public reference file, pinned by hash: fetch once, verify, cache, import. Refuses a mismatch."""
    CACHE.mkdir(parents=True, exist_ok=True); p = CACHE / f"{PIN['commit'][:12]}-{name}"
    if not p.exists():
        data = urllib.request.urlopen(RAW.format(commit=PIN["commit"], name=name), timeout=20).read()
        if hashlib.sha256(data).hexdigest() != PIN[name]: raise RuntimeError(f"{name}: sha256 mismatch against the pin; refusing")
        p.write_bytes(data)
    if hashlib.sha256(p.read_bytes()).hexdigest() != PIN[name]: raise RuntimeError(f"{name}: cached copy does not match the pin; refusing")
    if name == "rapp_trust.py":
        for dep in ("rapp.py", "rapp_profile.py"):
            if dep[:-3] not in sys.modules: _ref(dep)
    spec = importlib.util.spec_from_file_location(name[:-3], p); m = importlib.util.module_from_spec(spec)
    sys.modules[name[:-3]] = m; spec.loader.exec_module(m); return m

def _now():
    n = datetime.datetime.now(datetime.timezone.utc); return n.strftime("%Y-%m-%dT%H:%M:%S.") + f"{n.microsecond // 1000:03d}Z"

def _stake(T, conf, klass, score):
    lo = T.MIN_STAKE[klass]; hi = min(T.MAX_STAKE, score)
    if conf < 0.5: raise ValueError("confidence below 0.5 is a bet against yourself: do not claim, say 'unverified'")
    if conf > 1.0: raise ValueError("confidence above 1.0")
    return max(lo, min(hi, round(lo + (hi - lo) * (conf - 0.5) / 0.5)))

class TrustGate(BasicAgent):
    def __init__(self):
        self.name = "TrustGate"
        self.metadata = {
            "name": self.name,
            "description": ("Your own credit score for claims. action='score' shows the score, band and open bets. action='wager' bets "
                            "part of the score that a claim is true BEFORE you call it done (confidence 0.5-1.0 sets the stake; "
                            "all_in=true stakes the table max). action='settle' closes a bet won/lost/void with evidence a stranger "
                            "can open. action='board' prints the ledger summary. Use wager before any 'done', 'fixed' or 'released'."),
            "parameters": {"type": "object", "properties": {
                "action": {"type": "string", "enum": ["score", "wager", "settle", "board"]},
                "claim": {"type": "string", "description": "wager: the exact claim being made, as a stranger would check it"},
                "confidence": {"type": "number", "description": "wager: 0.5-1.0; sets the stake"},
                "klass": {"type": "string", "enum": ["statement", "done", "release", "destructive"], "description": "wager: what kind of claim (minimum stakes 1/5/10/20)"},
                "needs": {"type": "string", "description": "wager: what evidence settles it (a path:, https://, sha256: or log: entry a stranger can open)"},
                "hours": {"type": "number", "description": "wager: hours until the bet expires unsettled (expired = lost); default 24"},
                "all_in": {"type": "boolean"},
                "spread": {"type": "string", "description": "wager: your own stated uncertainty, kept with the bet"},
                "wager": {"type": "string", "description": "settle: the bet's hash or prefix"},
                "outcome": {"type": "string", "enum": ["won", "lost", "void"]},
                "evidence": {"type": "string", "description": "settle: path:/https:///sha256:/log: a stranger can open"},
                "note": {"type": "string"}},
                "required": ["action"]}}
        # caller-side extras per bet (confidence, spread, all_in) are not trust fields; they are kept in tiles.jsonl beside the ledger

    def _ledger(self):
        T = _ref("rapp_trust.py")
        if not LEDGER.exists():
            owner = os.environ.get("RAPP_OWNER", "kody-w"); LEDGER.parent.mkdir(parents=True, exist_ok=True)
            T.write_frame(LEDGER, T.genesis_frame(owner, "brainstem", _now()))
        return T, T.load(LEDGER, _now())

    def system_context(self):
        try:
            T, led = self._ledger()
            return (f"[TrustGate] Your trust score is {led.score} ({led.autonomy}); {len(led.open)} open bet(s), "
                    f"{len(led.settled)} settled. Before you say done/fixed/released, call TrustGate(action='wager', ...). "
                    + ("Band rule: no irreversible action without the owner's yes. " if led.score < 80 else "")
                    + ("Band rule: the owner verifies every claim. " if led.score < 50 else ""))
        except Exception as e:
            return f"[TrustGate] ledger unavailable ({e}); treat every claim as unverified."

    def perform(self, action="score", **k):
        try:
            T, led = self._ledger()
            if action == "score":
                opens = [f"{h[:12]} stake {w['stake']} '{w['claim'][:60]}' by {w['settles_by'][:16]}" for h, w in led.open.items()]
                return json.dumps({"score": led.score, "band": led.autonomy, "open": opens, "settled": len(led.settled)}, indent=1)
            if action == "board":
                rows = [f"{'won' if s['outcome']=='won' else s['outcome']:5s} {w['stake']:3d} {w['claim'][:70]} | {s['evidence'][0][:60]}" for w, s in led.settled]
                return f"score {led.score} ({led.autonomy}); open {len(led.open)}\n" + "\n".join(rows[-12:])
            if action == "wager":
                conf = float(k.get("confidence", 0.75)); klass = k.get("klass", "statement"); hours = float(k.get("hours", 24))
                stake = min(T.MAX_STAKE, led.score) if k.get("all_in") else _stake(T, conf, klass, led.score)
                by = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=hours)).strftime("%Y-%m-%dT%H:%M:%S.000Z")
                payload = {"schema": "trust.wager", "plug": os.environ.get("RAPP_PLUG", "brainstem"), "claim": k["claim"], "class": klass,
                           "stake": stake, "counter": 0, "evidence_required": [k.get("needs", "path: or https:// a stranger can open")], "settles_by": by}
                frame = led.append("trust.wager", payload, _now()); T.write_frame(LEDGER, frame)
                tile = {"wager": frame["frame_hash"], "confidence": conf, "all_in": bool(k.get("all_in")), "spread": k.get("spread", ""), "stake": stake, "score_before": led.score, "utc": _now()}
                with open(HOME / "tiles.jsonl", "a") as fh: fh.write(json.dumps(tile) + "\n")
                return f"bet {frame['frame_hash'][:12]}: staked {stake} of {led.score} at confidence {conf}{' (ALL IN)' if tile['all_in'] else ''}; settle by {by[:16]}Z with {payload['evidence_required'][0]}"
            if action == "settle":
                full = [h for h in led.open if h.startswith(k["wager"])]
                if len(full) != 1: return f"refused: '{k['wager']}' matches {len(full)} open bets"
                before = led.score
                frame = led.append("trust.settle", {"schema": "trust.settle", "wager": full[0], "outcome": k["outcome"], "evidence": [k["evidence"]], "note": k.get("note", "")}, _now())
                T.write_frame(LEDGER, frame); after = T.load(LEDGER, _now())
                return f"settled {full[0][:12]} {k['outcome']}: score {before} -> {after.score} ({after.autonomy})"
            return "unknown action"
        except Exception as e:
            return f"refused: {e}"
