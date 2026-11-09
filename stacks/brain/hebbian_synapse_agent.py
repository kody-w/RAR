"""
Hebbian synapse agent - "cells that fire together wire together."

Drop into any Brainstem's agents/ folder. From then on it quietly notes which
agents fire close together in time, and when asked it reports the strongest
connections: which cells form circuits, and which pairs could become a chain.

What it records: agent names and timestamps only. Never arguments, never results.
Where: ~/.brainstem/synapses.jsonl (append-only; delete it to forget everything).
How it listens: it wraps perform() on the other agents in memory, never on disk.
Delete this file and restart the Brainstem to remove it completely.
Old firings fade with a 14-day half-life, so stale habits drop away by themselves.
"""
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/hebbian_synapse_agent",
    "version": "1.0.0",
    "display_name": "HebbianSynapse",
    "description": "Notes which agents fire together (names and times only) and reports the strongest connections and chain candidates.",
    "author": "kody-w",
    "tags": ["brain", "hebbian", "habits", "agents", "learning"],
    "category": "core",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

import functools
import json
import math
import os
import threading
import time
from collections import Counter

try:
    from agents.basic_agent import BasicAgent
except ImportError:  # running standalone
    from basic_agent import BasicAgent

LOG = os.path.expanduser(os.environ.get("HEBBIAN_LOG", "~/.brainstem/synapses.jsonl"))
TURN_GAP = 90          # firings closer than this (seconds) belong to the same burst
HALF_LIFE_DAYS = 14
_lock = threading.Lock()
SELF = "HebbianSynapse"
BRAIN = {"HebbianSynapse", "ReflexArc", "PainReceptor", "BrainstemImpact"}  # don't watch ourselves


def _record(name, error=None):
    try:
        os.makedirs(os.path.dirname(LOG), exist_ok=True)
        row = {"t": round(time.time(), 1), "a": name}
        if error:
            row["err"] = error  # exception type only, never the message or arguments
        with _lock, open(LOG, "a") as f:
            f.write(json.dumps(row) + "\n")
    except Exception:
        pass  # sensing must never break the cell it watches


def _wrap(cls):
    perform = cls.__dict__.get("perform")
    if perform is None or getattr(perform, "_hebbian", False):
        return

    @functools.wraps(perform)
    def fired(self, *a, **kw):
        name = getattr(self, "name", cls.__name__)
        if name in BRAIN:
            return perform(self, *a, **kw)
        try:
            result = perform(self, *a, **kw)
        except Exception as e:
            _record(name, type(e).__name__)
            raise
        _record(name)
        return result

    fired._hebbian = True
    cls.perform = fired


def _listen():
    """Wrap every agent class defined from now on (agents reload each request)."""
    if getattr(BasicAgent, "_hebbian_listening", False):
        return
    original = BasicAgent.__dict__.get("__init_subclass__")

    @classmethod
    def hook(cls, **kw):
        if original is not None:
            original.__func__(cls, **kw)
        else:
            super(BasicAgent, cls).__init_subclass__(**kw)
        _wrap(cls)

    BasicAgent.__init_subclass__ = hook
    BasicAgent._hebbian_listening = True


_listen()


def _bursts(events):
    burst, last = [], None
    for e in events:
        if last is not None and e["t"] - last > TURN_GAP:
            yield burst
            burst = []
        burst.append(e)
        last = e["t"]
    if burst:
        yield burst


class HebbianSynapseAgent(BasicAgent):
    def __init__(self):
        self.name = SELF
        self.metadata = {
            "name": self.name,
            "description": (
                "Shows how the user's agents wire together: which agents fire together most "
                "(strongest synapses), which fire most on their own, and which pairs could be "
                "chained into one step. Use when the user asks how their agents connect, what "
                "their habits are, or what to combine."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "top": {"type": "integer", "description": "How many connections to show. Default 5."},
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, top=5, **kwargs):
        try:
            with open(LOG) as f:
                events = sorted((json.loads(l) for l in f if l.strip()), key=lambda e: e["t"])
        except FileNotFoundError:
            return "No firings recorded yet. Use your agents for a while, then ask again."

        now = time.time()
        decay = lambda t: math.exp(-math.log(2) * (now - t) / (HALF_LIFE_DAYS * 86400))
        cells, pairs, chains = Counter(), Counter(), Counter()
        for burst in _bursts(events):
            w = decay(burst[-1]["t"])
            names = [e["a"] for e in burst]
            for n in set(names):
                cells[n] += w
            uniq = sorted(set(names))
            for i, x in enumerate(uniq):
                for y in uniq[i + 1:]:
                    pairs[(x, y)] += w
            for x, y in zip(names, names[1:]):
                if x != y:
                    chains[(x, y)] += w

        top = int(top or 5)
        out = [f"**{len(events)} firings across {len(cells)} cells.**", ""]
        if pairs:
            out += ["Strongest synapses (fire together; recent counts more):"]
            for (x, y), w in pairs.most_common(top):
                together = w / min(cells[x], cells[y])
                out.append(f"- {x} + {y}: strength {w:.1f} ({together:.0%} of the time the rarer one fires, the other does too)")
            out.append("")
        if chains:
            (x, y), w = chains.most_common(1)[0]
            if w >= 2.5:  # about 3 recent repeats
                out.append(f"Chain candidate: {x} is usually followed by {y}. These could become one step.")
            else:
                out.append("No chain is strong enough to suggest yet.")
            out.append("")
        loners = [n for n in cells if not any(n in p for p in pairs)]
        if loners:
            out.append("Fire alone: " + ", ".join(sorted(loners)))
        return "\n".join(out).rstrip()


if __name__ == "__main__":
    print(HebbianSynapseAgent().perform())
