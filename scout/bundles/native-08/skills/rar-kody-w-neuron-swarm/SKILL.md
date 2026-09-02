---
name: "rar-kody-w-neuron-swarm"
description: "Run a NEURON SWARM on a task: fan it out across many independent expert 'neuron' lenses (each a distinct perspective), then reconcile every take into one converged, higher-confidence answer. Reach for this whenever the user wants real rigor -- a thorough multi-perspective ANALYSIS, a DESIGN with compared options, an adversarial REVIEW, a weighed DECISION, organized RESEARCH, or a wide BRAINSTORM -- anything that deserves more than a single pass. The swarm uses this brainstem's own language model, so it needs no API keys. Phrases like 'run a neuron swarm', 'get many perspectives', 'really think hard about this', 'stress-test this', or 'have your agents debate this' should trigger it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/neuron_swarm", "rar_sha256": "911cbdf5536d55be0da3f49cf86f6b96fb4dde7eeb05fdd1ae7f67ea945e0498", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "neuron_swarm_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/neuron-swarm:24f21e1b55e4ae73a4ddfadae06492c85c60c766d91d7c5eaa6b14ab30e75c0d", "kind": "skill"}, "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["swarm", "orchestration", "reasoning", "multi-agent", "analysis", "ensemble", "brainstem"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/neuron_swarm`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `neuron_swarm_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
