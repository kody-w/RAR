"""
NeuronSwarm -- summon a neuron swarm on demand, from inside your brainstem.

Drop this file into your agents/ folder. Then, any time you want more rigor than a
single pass, just ask: "run a neuron swarm on ..." (your brainstem will also reach
for it on its own for hard analysis, design, reviews, and decisions).

How it works: the agent fans your task out across many independent "neuron" lenses --
each a distinct expert perspective -- using your brainstem's OWN language model (the
same engine /chat uses). A reconciler neuron then converges every take into one
higher-confidence answer. No API keys, no new server routes, no edits to the engine:
it finds the brainstem's in-process LLM call and drives it directly with tools turned
OFF, so neurons can never recurse. If a host somehow has no such call, it gracefully
returns a directive so the host model still delivers a multi-lens answer.

Fully self-contained and drop-in -- works in any unmodified brainstem.
Companion to the ebook "RAPP and the Art of Brainstemming".
"""

# RAPP Agent Registry manifest (ignored by the brainstem loader; used by RAR).
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/neuron_swarm",
    "version": "1.0.1",
    "display_name": "NeuronSwarm",
    "description": (
        "Fans a task out across parallel expert 'neuron' prompts using the host brainstem's own LLM call, then reconciles them into one converged answer."
    ),
    "author": "Kody Wildfeuer",
    "tags": ["swarm", "orchestration", "reasoning", "multi-agent", "analysis", "ensemble", "brainstem"],
    "category": "core",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

import json
import re
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

# -- Drop-in BasicAgent import (robust across brainstem variants) --------------
try:
    from basic_agent import BasicAgent
except Exception:
    try:
        from agents.basic_agent import BasicAgent
    except Exception:
        try:
            from openrappter.agents.basic_agent import BasicAgent
        except Exception:
            class BasicAgent:  # last-resort shim so the file always loads
                def __init__(self, name=None, metadata=None):
                    if name is not None:
                        self.name = name
                    if metadata is not None:
                        self.metadata = metadata

                def perform(self, **kwargs):
                    return "Not implemented."

                def system_context(self):
                    return None

                def to_tool(self):
                    return {"type": "function", "function": {
                        "name": getattr(self, "name", "BasicAgent"),
                        "description": self.metadata.get("description", ""),
                        "parameters": self.metadata.get("parameters", {"type": "object", "properties": {}}),
                    }}


# -- Locating the brainstem's own LLM call (no engine edits, no recursion) -----
def _find_call_copilot():
    """Return the host brainstem's module-level LLM function (brainstem.call_copilot,
    or the Azure-parity function_app.call_copilot), or None if it can't be found."""
    for name in ("brainstem", "function_app", "__main__"):
        mod = sys.modules.get(name)
        fn = getattr(mod, "call_copilot", None) if mod is not None else None
        if callable(fn):
            return fn
    # Last resort: scan every loaded module for a call_copilot(messages, tools=None)
    for mod in list(sys.modules.values()):
        fn = getattr(mod, "call_copilot", None) if mod is not None else None
        if callable(fn):
            return fn
    return None


_SWARM_LOCK = threading.Lock()
_SWARM_ACTIVE = 0  # reentrancy guard (defensive; in-process neurons never recurse)


DEFAULT_LENSES = {
    "analyze":    ["first-principles analyst", "skeptical critic", "systems thinker",
                   "practical implementer", "end-user advocate", "precedent & analogy"],
    "design":     ["minimal-MVP designer", "architecture & scale", "UX & ergonomics",
                   "risk & failure modes", "cost & effort realist", "contrarian alternative"],
    "review":     ["correctness auditor", "security & abuse", "performance & efficiency",
                   "maintainability", "edge cases & failure", "user impact"],
    "decide":     ["steelman option A", "steelman option B", "risk officer",
                   "cost/benefit analyst", "reversibility & optionality", "pragmatic gut-check"],
    "research":   ["established facts", "open contested questions", "unknowns & gaps",
                   "key sources & authorities", "counter-evidence", "implications & synthesis"],
    "brainstorm": ["wild / divergent", "adjacent-domain analogy", "constraint removal",
                   "user-need driven", "combinatorial recombination", "feasible right now"],
}

MODE_FRAMING = {
    "analyze": "Understand the task deeply from many angles.",
    "design": "Propose and compare concrete solutions.",
    "review": "Adversarially find problems, risks, and weaknesses.",
    "decide": "Weigh the options and drive toward a recommendation.",
    "research": "Gather and organize what is known, contested, and unknown.",
    "brainstorm": "Diverge widely, then surface the strongest ideas.",
}


class NeuronSwarmAgent(BasicAgent):
    def __init__(self):
        self.name = "NeuronSwarm"
        self.metadata = {
            "name": self.name,
            "description": (
                "Run a NEURON SWARM on a task: fan it out across many independent expert "
                "'neuron' lenses (each a distinct perspective), then reconcile every take into "
                "one converged, higher-confidence answer. Reach for this whenever the user wants "
                "real rigor -- a thorough multi-perspective ANALYSIS, a DESIGN with compared "
                "options, an adversarial REVIEW, a weighed DECISION, organized RESEARCH, or a wide "
                "BRAINSTORM -- anything that deserves more than a single pass. The swarm uses this "
                "brainstem's own language model, so it needs no API keys. Phrases like 'run a neuron "
                "swarm', 'get many perspectives', 'really think hard about this', 'stress-test this', "
                "or 'have your agents debate this' should trigger it."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "task": {
                        "type": "string",
                        "description": "The question, problem, decision, or task to swarm on. Be specific and self-contained -- include everything the swarm needs to reason about. Required.",
                    },
                    "mode": {
                        "type": "string",
                        "description": "Swarm pattern, one of: analyze | design | review | decide | research | brainstorm. Picks the default set of neuron lenses and how they reason. Default: analyze.",
                    },
                    "lenses": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Optional explicit list of perspectives/expert personas to use as neurons, e.g. ['security engineer','first-time user','CFO']. If omitted, the swarm auto-generates diverse lenses tailored to the task. When provided, these override the mode defaults.",
                    },
                    "neurons": {
                        "type": "integer",
                        "description": "Swarm size = how many neuron lenses to spin up. More neurons = more rigor (and more model calls). Default 6. Sensible range 2-12. Ignored when 'lenses' is supplied.",
                    },
                    "rounds": {
                        "type": "integer",
                        "description": "Fan-out rounds. 1 = each neuron answers once, then reconcile. 2 = neurons also see each other's first-round takes and refine before reconciling (deeper convergence, ~2x cost). Default 1. Max 3.",
                    },
                    "context": {
                        "type": "string",
                        "description": "Optional extra background, source material, constraints, or data the neurons should ground their analysis in.",
                    },
                    "output_format": {
                        "type": "string",
                        "description": "Shape of the final synthesis: report (sectioned prose, default) | decision (recommendation + rationale + risks) | bullets (tight bullets) | directive (concrete action steps).",
                    },
                    "max_parallel": {
                        "type": "integer",
                        "description": "Max neurons queried concurrently. Default 4. Set to 1 for fully sequential (gentler on model rate limits).",
                    },
                },
                "required": ["task"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    # -- small helpers ---------------------------------------------------------
    @staticmethod
    def _as_int(v, default):
        try:
            return int(v)
        except Exception:
            return default

    def _llm(self, system, user, _fn):
        """One model turn via the brainstem's own call (tools disabled => no recursion)."""
        messages = [{"role": "system", "content": system},
                    {"role": "user", "content": user}]
        try:
            resp = _fn(messages, tools=None)
        except Exception as e:
            return None, "llm error: %s" % e
        try:
            choice = (resp.get("choices") or [{}])[0]
            text = (choice.get("message", {}).get("content") or "").strip()
            return (text or None), (None if text else "empty response")
        except Exception as e:
            return None, "parse error: %s" % e

    def _plan_lenses(self, task, mode, context, n, _fn):
        """Ask the model for n task-tailored lenses; fall back to mode defaults."""
        sys_p = ("You design neuron-swarm lenses. Given a task, output exactly the requested "
                 "number of DISTINCT, specific expert perspectives that together cover it with "
                 "minimal overlap. Reply ONLY with a JSON array of short lens names (strings).")
        usr_p = "MODE: %s -- %s\nTASK:\n%s\n" % (mode, MODE_FRAMING.get(mode, ""), task)
        if context:
            usr_p += "\nCONTEXT:\n%s\n" % context[:2000]
        usr_p += "\nReturn exactly %d lenses as a JSON array of strings." % n
        text, _ = self._llm(sys_p, usr_p, _fn)
        lenses = []
        if text:
            m = re.search(r"\[.*\]", text, re.S)
            if m:
                try:
                    arr = json.loads(m.group(0))
                    lenses = [str(x).strip() for x in arr if str(x).strip()]
                except Exception:
                    lenses = []
            if not lenses:
                for line in text.splitlines():
                    s = re.sub(r'^[\s\-\*\d\.\)\"]+', '', line).strip().strip('",')
                    if s and len(s) < 80:
                        lenses.append(s)
        if len(lenses) < 2:
            lenses = list(DEFAULT_LENSES.get(mode, DEFAULT_LENSES["analyze"]))
        return lenses[:max(2, n)]

    def _neuron_take(self, lens, task, mode, context, _fn, peers=None):
        sys_p = ("You are the '%s' neuron in a swarm. Examine the task STRICTLY through your lens -- "
                 "surface what others would miss, name assumptions and risks, be concrete and specific, "
                 "and do not hedge or water it down. Goal of the swarm: %s Answer directly in 4-10 tight "
                 "sentences or bullets. Do NOT call tools." % (lens, MODE_FRAMING.get(mode, "")))
        usr_p = "TASK:\n%s\n" % task
        if context:
            usr_p += "\nCONTEXT:\n%s\n" % context[:3000]
        if peers:
            usr_p += ("\nOTHER NEURONS SAID (refine, challenge, or build on these -- add new signal, "
                      "don't just repeat):\n%s\n" % peers[:4000])
        usr_p += "\nYour take, as the '%s' neuron:" % lens
        text, err = self._llm(sys_p, usr_p, _fn)
        return {"lens": lens, "take": text, "error": err}

    def _fan_out(self, lenses, task, mode, context, _fn, max_parallel, peers_map=None):
        results = [None] * len(lenses)

        def work(i):
            peers = peers_map.get(i) if peers_map else None
            return i, self._neuron_take(lenses[i], task, mode, context, _fn, peers=peers)

        if max_parallel <= 1 or len(lenses) == 1:
            for i in range(len(lenses)):
                _, r = work(i)
                results[i] = r
        else:
            with ThreadPoolExecutor(max_workers=min(max_parallel, len(lenses))) as ex:
                futs = [ex.submit(work, i) for i in range(len(lenses))]
                for f in as_completed(futs):
                    try:
                        i, r = f.result()
                        results[i] = r
                    except Exception:
                        pass
        return [r for r in results if r]

    def _reconcile(self, task, mode, output_format, takes, _fn):
        blob = "\n\n".join("### %s\n%s" % (t["lens"], t["take"]) for t in takes if t.get("take"))
        fmt = {
            "decision": "Output a clear RECOMMENDATION first, then the rationale, the key trade-offs, dissent worth heeding, and the top risks.",
            "bullets": "Output a tight, well-organized set of bullets -- no fluff.",
            "directive": "Output concrete, ordered ACTION STEPS the user can take now, then a short 'watch out for' list.",
            "report": "Output a clean, sectioned synthesis: the convergent answer, the strongest supporting points, real tensions/dissent, and what to do next.",
        }.get(output_format, "Output a clean, sectioned synthesis.")
        sys_p = ("You are the RECONCILER of a neuron swarm. Several independent expert neurons each "
                 "examined the same task. Merge their takes into ONE converged answer: keep what is "
                 "strong, resolve conflicts on the merits, explicitly surface important dissent rather "
                 "than averaging it away, and drop the noise. Be decisive and useful. " + fmt)
        usr_p = "TASK:\n%s\n\nMODE: %s\n\nNEURON TAKES:\n%s\n\nNow produce the final synthesis." % (task, mode, blob)
        return self._llm(sys_p, usr_p, _fn)

    # -- the entry point -------------------------------------------------------
    def perform(self, task=None, mode="analyze", lenses=None, neurons=6, rounds=1,
                context="", output_format="report", max_parallel=4, **kwargs):
        global _SWARM_ACTIVE
        task = (task or kwargs.get("query") or "").strip()
        if not task:
            return ("NeuronSwarm needs a 'task' -- tell me what to swarm on "
                    "(a question, decision, design, or thing to review).")

        mode = (mode or "analyze").strip().lower()
        if mode not in DEFAULT_LENSES:
            mode = "analyze"
        output_format = (output_format or "report").strip().lower()
        neurons = max(2, min(12, self._as_int(neurons, 6)))
        rounds = max(1, min(3, self._as_int(rounds, 1)))
        max_parallel = max(1, min(8, self._as_int(max_parallel, 4)))
        context = context or ""

        _fn = _find_call_copilot()
        if _fn is None:
            # Graceful degradation: no in-process LLM found -- hand the host model a
            # directive so the user still gets a multi-lens answer (single pass).
            base = lenses if (isinstance(lenses, list) and lenses) else DEFAULT_LENSES.get(mode)
            return self._directive_fallback(task, mode, base, output_format, context)

        # Reentrancy guard (defensive -- neuron calls disable tools so they can't recurse)
        with _SWARM_LOCK:
            if _SWARM_ACTIVE > 0:
                return ("[neuron swarm already in progress -- answer this directly and concisely "
                        "without invoking another swarm]")
            _SWARM_ACTIVE += 1
        try:
            # 1) Decide the lenses (this warmup call also primes the auth token before fan-out)
            valid = [str(l).strip() for l in lenses if str(l).strip()] if isinstance(lenses, list) else []
            if len(valid) >= 2:
                lens_list = valid[:12]
            else:
                lens_list = self._plan_lenses(task, mode, context, neurons, _fn)

            # 2) Fan out, round by round
            peers_map = None
            takes = []
            for rnd in range(rounds):
                takes = self._fan_out(lens_list, task, mode, context, _fn, max_parallel, peers_map=peers_map)
                if rounds > 1 and rnd < rounds - 1:
                    all_blob = "\n\n".join("[%s] %s" % (t["lens"], t["take"]) for t in takes if t.get("take"))
                    peers_map = {i: all_blob for i in range(len(lens_list))}

            good = [t for t in takes if t.get("take")]
            if not good:
                return ("The neuron swarm could not get responses from the model (it may be rate-limited "
                        "or unauthenticated). Try again in a moment, or check /health.")

            # 3) Reconcile
            synthesis, _err = self._reconcile(task, mode, output_format, good, _fn)
            if not synthesis:
                dump = "\n\n".join("**%s**\n%s" % (t["lens"], t["take"]) for t in good)
                return "[neuron swarm: %d lenses, reconciler unavailable -- raw takes]\n\n%s" % (len(good), dump)

            header = ("[neuron swarm: %d lenses, mode=%s, %d round%s]\nLenses: %s\n\n"
                      % (len(good), mode, rounds, "s" if rounds > 1 else "", ", ".join(t["lens"] for t in good)))
            return header + synthesis
        finally:
            with _SWARM_LOCK:
                _SWARM_ACTIVE -= 1

    def _directive_fallback(self, task, mode, lenses, output_format, context):
        ls = ", ".join(lenses) if lenses else "several diverse expert perspectives"
        msg = ("NEURON-SWARM DIRECTIVE (this host has no in-process model call available, so run the "
               "swarm yourself in your reply): Examine the task below independently through each of "
               "these lenses -- %s -- giving each its own honest, specific take, THEN reconcile them "
               "into one converged answer that keeps the strong points, surfaces real dissent, and is "
               "decisive. Final shape: %s.\n\nMODE: %s\n\nTASK:\n%s" % (ls, output_format, mode, task))
        if context:
            msg += "\n\nCONTEXT:\n%s" % context
        return msg


# Optional manual smoke test:  python neuron_swarm_agent.py "your task here"
if __name__ == "__main__":
    _t = " ".join(sys.argv[1:]) or "Should I rewrite my landing page from scratch or iterate on it?"
    print(NeuronSwarmAgent().perform(task=_t, neurons=4, max_parallel=1))
