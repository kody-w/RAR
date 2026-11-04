---
name: "rar-kody-w-neuron-swarm"
description: "Run a NEURON SWARM on a task: fan it out across many independent expert 'neuron' lenses (each a distinct perspective), then reconcile every take into one converged, higher-confidence answer. Reach for this whenever the user wants real rigor -- a thorough multi-perspective ANALYSIS, a DESIGN with compared options, an adversarial REVIEW, a weighed DECISION, organized RESEARCH, or a wide BRAINSTORM -- anything that deserves more than a single pass. The swarm uses this brainstem's own language model, so it needs no API keys. Phrases like 'run a neuron swarm', 'get many perspectives', 'really think hard about this', 'stress-test this', or 'have your agents debate this' should trigger it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/neuron_swarm", "rar_sha256": "271579577537088ee30aa14aa9bc28887d9f564cda195bdeb777d5a0da897815", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["swarm", "orchestration", "reasoning", "multi-agent", "analysis", "ensemble", "brainstem"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `neuron_swarm_agent.py` and embedded as the fenced Python below (sha256 271579577537088e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `neuron_swarm_agent.py` first:

```bash
python3 neuron_swarm_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 neuron_swarm_agent.py   # or on stdin
python3 neuron_swarm_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/neuron_swarm_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/neuron_swarm_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/neuron_swarm/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
