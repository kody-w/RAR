"""
Pain receptor agent - tells you which of your agents keep failing.

Reads the firing log the HebbianSynapse agent keeps. Each failed firing is
recorded there with its error type only (never the message or arguments).
This agent reports which agents hurt: how often each one fails, the most
common error, and when it last failed, so you know what to fix first.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/pain_receptor_agent",
    "version": "1.0.0",
    "display_name": "PainReceptor",
    "description": "Reports which agents keep failing, how often, with which error type, so the user knows what to fix first.",
    "author": "kody-w",
    "tags": ["brain", "health", "errors", "agents", "diagnostics"],
    "category": "devtools",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent", "@kody-w/hebbian_synapse_agent"],
}

import json
import os
import time
from collections import Counter, defaultdict

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    from basic_agent import BasicAgent

LOG = os.path.expanduser(os.environ.get("HEBBIAN_LOG", "~/.brainstem/synapses.jsonl"))


class PainReceptorAgent(BasicAgent):
    def __init__(self):
        self.name = "PainReceptor"
        self.metadata = {
            "name": self.name,
            "description": (
                "Shows which of the user's agents keep failing: failure rate, most common error "
                "type, last failure. Use when the user asks what's broken, what hurts, or what to fix."
            ),
            "parameters": {"type": "object", "properties": {}, "required": []},
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        try:
            with open(LOG) as f:
                ev = [json.loads(l) for l in f if l.strip()]
        except FileNotFoundError:
            return "Nothing recorded yet. The HebbianSynapse agent has to be installed to sense failures."
        fired, hurt, errors, last = Counter(), Counter(), defaultdict(Counter), {}
        for e in ev:
            fired[e["a"]] += 1
            if "err" in e:
                hurt[e["a"]] += 1
                errors[e["a"]][e["err"]] += 1
                last[e["a"]] = max(last.get(e["a"], 0), e["t"])
        if not hurt:
            return f"No pain: {sum(fired.values())} firings across {len(fired)} agents, none failed."
        rows = sorted(hurt, key=lambda a: hurt[a] / fired[a], reverse=True)
        out = ["**What hurts:**", ""]
        for a in rows:
            err, _ = errors[a].most_common(1)[0]
            ago = (time.time() - last[a]) / 3600
            out.append(f"- {a}: failed {hurt[a]} of {fired[a]} ({hurt[a] / fired[a]:.0%}), "
                       f"mostly {err}, last {ago:.0f}h ago")
        out += ["", f"Fix {rows[0]} first."]
        return "\n".join(out)
