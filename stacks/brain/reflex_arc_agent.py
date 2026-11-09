"""
Reflex arc agent - turns a learned habit into a reflex, only when you say so.

Reads the firing log the HebbianSynapse agent keeps. When agent A is usually
followed by agent B, it can suggest a reflex "after A, also run B". A reflex is
armed only when the user asks for it. Armed reflexes are given to the model as
background each turn, so the model runs B after A without being told again.
Nothing fires behind the model's back, and one call disarms a reflex.

Reflexes live in ~/.brainstem/reflexes.json. Delete the file to forget them all.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/reflex_arc_agent",
    "version": "1.0.0",
    "display_name": "ReflexArc",
    "description": "Suggests, arms and disarms reflexes (after agent A, also run agent B) learned from which agents usually fire in sequence.",
    "author": "kody-w",
    "tags": ["brain", "reflex", "habits", "automation", "agents"],
    "category": "core",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent", "@kody-w/hebbian_synapse_agent"],
}

import json
import os
from collections import Counter

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    from basic_agent import BasicAgent

LOG = os.path.expanduser(os.environ.get("HEBBIAN_LOG", "~/.brainstem/synapses.jsonl"))
STORE = os.path.expanduser(os.environ.get("REFLEX_STORE", "~/.brainstem/reflexes.json"))
GAP = 90        # seconds; same as the synapse agent's burst window
MIN_SEEN = 3    # a sequence must happen this many times before it is suggested


def _load():
    try:
        with open(STORE) as f:
            return json.load(f)
    except (FileNotFoundError, ValueError):
        return []


def _save(reflexes):
    os.makedirs(os.path.dirname(STORE), exist_ok=True)
    with open(STORE, "w") as f:
        json.dump(reflexes, f, indent=2)


def _sequences():
    try:
        with open(LOG) as f:
            ev = sorted((json.loads(l) for l in f if l.strip()), key=lambda e: e["t"])
    except FileNotFoundError:
        return Counter()
    seq = Counter()
    for x, y in zip(ev, ev[1:]):
        if y["t"] - x["t"] <= GAP and x["a"] != y["a"] and "err" not in x and "err" not in y:
            seq[(x["a"], y["a"])] += 1
    return seq


class ReflexArcAgent(BasicAgent):
    def __init__(self):
        self.name = "ReflexArc"
        self.metadata = {
            "name": self.name,
            "description": (
                "Learned reflexes between agents. action='suggest' lists sequences the user repeats "
                "(after A, B). action='arm' with first and then turns one into a reflex - only when "
                "the user asks. action='disarm' removes one. action='list' shows armed reflexes."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": ["suggest", "arm", "disarm", "list"]},
                    "first": {"type": "string", "description": "Agent that fires first (arm/disarm)"},
                    "then": {"type": "string", "description": "Agent to run right after it (arm/disarm)"},
                },
                "required": ["action"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def system_context(self):
        armed = _load()
        if not armed:
            return None
        rules = "; ".join(f"after {r['first']} succeeds, also call {r['then']}" for r in armed)
        return f"Armed reflexes the user chose: {rules}. Mention it in one line when a reflex fires."

    def perform(self, action="suggest", first="", then="", **kwargs):
        armed = _load()
        if action == "list":
            if not armed:
                return "No reflexes armed."
            return "Armed reflexes:\n" + "\n".join(f"- after {r['first']}, run {r['then']}" for r in armed)
        if action == "suggest":
            seq = [(k, n) for k, n in _sequences().most_common(5) if n >= MIN_SEEN]
            if not seq:
                return f"No sequence has repeated {MIN_SEEN}+ times yet. Keep using your agents."
            done = {(r["first"], r["then"]) for r in armed}
            lines = [f"- after {a}, you ran {b} {n} times" + (" (armed)" if (a, b) in done else "")
                     for (a, b), n in seq]
            return "Sequences you repeat:\n" + "\n".join(lines) + \
                "\n\nSay 'arm the first one' to make it a reflex."
        if not first or not then:
            return "Tell me both agents: first and then."
        if action == "arm":
            if any(r["first"] == first and r["then"] == then for r in armed):
                return f"Already armed: after {first}, run {then}."
            armed.append({"first": first, "then": then})
            _save(armed)
            return f"Armed: after {first}, I'll also run {then}. Say 'disarm' to undo."
        if action == "disarm":
            left = [r for r in armed if not (r["first"] == first and r["then"] == then)]
            if len(left) == len(armed):
                return f"No reflex after {first} -> {then} was armed."
            _save(left)
            return f"Disarmed: after {first} -> {then}."
        return f"Unknown action {action!r}."
