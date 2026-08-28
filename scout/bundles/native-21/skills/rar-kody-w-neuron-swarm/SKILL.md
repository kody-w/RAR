---
name: "rar-kody-w-neuron-swarm"
description: "Run a NEURON SWARM on a task: fan it out across many independent expert 'neuron' lenses (each a distinct perspective), then reconcile every take into one converged, higher-confidence answer. Reach for this whenever the user wants real rigor -- a thorough multi-perspective ANALYSIS, a DESIGN with compared options, an adversarial REVIEW, a weighed DECISION, organized RESEARCH, or a wide BRAINSTORM -- anything that deserves more than a single pass. The swarm uses this brainstem's own language model, so it needs no API keys. Phrases like 'run a neuron swarm', 'get many perspectives', 'really think hard about this', 'stress-test this', or 'have your agents debate this' should trigger it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/neuron_swarm", "rar_sha256": "911cbdf5536d55be0da3f49cf86f6b96fb4dde7eeb05fdd1ae7f67ea945e0498", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["swarm", "orchestration", "reasoning", "multi-agent", "analysis", "ensemble", "brainstem"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/neuron_swarm`. The original RAPP
agent is preserved byte-for-byte in `neuron_swarm_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "context": {
      "description": "Optional extra background, source material, constraints, or data the neurons should ground their analysis in.",
      "type": "string"
    },
    "lenses": {
      "description": "Optional explicit list of perspectives/expert personas to use as neurons, e.g. ['security engineer','first-time user','CFO']. If omitted, the swarm auto-generates diverse lenses tailored to the task. When provided, these override the mode defaults.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "max_parallel": {
      "description": "Max neurons queried concurrently. Default 4. Set to 1 for fully sequential (gentler on model rate limits).",
      "type": "integer"
    },
    "mode": {
      "description": "Swarm pattern, one of: analyze | design | review | decide | research | brainstorm. Picks the default set of neuron lenses and how they reason. Default: analyze.",
      "type": "string"
    },
    "neurons": {
      "description": "Swarm size = how many neuron lenses to spin up. More neurons = more rigor (and more model calls). Default 6. Sensible range 2-12. Ignored when 'lenses' is supplied.",
      "type": "integer"
    },
    "output_format": {
      "description": "Shape of the final synthesis: report (sectioned prose, default) | decision (recommendation + rationale + risks) | bullets (tight bullets) | directive (concrete action steps).",
      "type": "string"
    },
    "rounds": {
      "description": "Fan-out rounds. 1 = each neuron answers once, then reconcile. 2 = neurons also see each other's first-round takes and refine before reconciling (deeper convergence, ~2x cost). Default 1. Max 3.",
      "type": "integer"
    },
    "task": {
      "description": "The question, problem, decision, or task to swarm on. Be specific and self-contained -- include everything the swarm needs to reason about. Required.",
      "type": "string"
    }
  },
  "required": [
    "task"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `neuron_swarm_agent.py` and embedded as the fenced Python below (sha256 911cbdf5536d55be…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `neuron_swarm_agent.py` first:

```bash
python3 neuron_swarm_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 neuron_swarm_agent.py   # or on stdin
python3 neuron_swarm_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
