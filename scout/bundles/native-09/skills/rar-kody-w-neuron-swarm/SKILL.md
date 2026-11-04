---
name: "rar-kody-w-neuron-swarm"
description: "Run a NEURON SWARM on a task: fan it out across many independent expert 'neuron' lenses (each a distinct perspective), then reconcile every take into one converged, higher-confidence answer. Reach for this whenever the user wants real rigor -- a thorough multi-perspective ANALYSIS, a DESIGN with compared options, an adversarial REVIEW, a weighed DECISION, organized RESEARCH, or a wide BRAINSTORM -- anything that deserves more than a single pass. The swarm uses this brainstem's own language model, so it needs no API keys. Phrases like 'run a neuron swarm', 'get many perspectives', 'really think hard about this', 'stress-test this', or 'have your agents debate this' should trigger it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/neuron_swarm", "rar_sha256": "271579577537088ee30aa14aa9bc28887d9f564cda195bdeb777d5a0da897815", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["swarm", "orchestration", "reasoning", "multi-agent", "analysis", "ensemble", "brainstem"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/618B7ObaNbmX1F5asr26NoIEMm7/dWiQJJEFELQ7nKTcxBJoNnZ374vknwd2jNfbdW6un0leMN5T3jOcw5c//ON3bVRWb/59GZXeuPMiDMv8Du/fvPyxvMbt46rNi4LcFvtipk9E7e6KokzzaDVw6ycrrR2k36aBXYxi9tZ2bUz263LppnldjHO4sLzKx/8VbQzf6j8up29LfyuLou3s8wvGr+ZvfNtNwLreHHTxoXbzsCopvLdNu799y+zNvKLWe27ZeHGmT/ze78ewZ6pD9ZuSyCCPwP3wNXQ915mURxGfv0BXAlisKnrz+yiufr1x5l63yYoa7Bi3MyuYNlprWn9WdeAD1e7aBuwk53N6jgE4z58mE4HdFN2YTTLu6yNP3wn24wW6b2p8doLGLbZajwrzq5xGwFx8squfW9W3lXXgPtATx7YrLHrGCyvbk/81pimXf1JXg9MX/MaL4kvs7IO7SK+gWvqVtvS6pqbrk1DwXlmK5XmRe0oAd1P0hUjOEsRAiHtdgas5dc9UGhe1v50aTJOA24DrVV203ycHcFRm6td59OBm4cenNqOi6b187fNrLwWs8wuws4OfbCK52cvs6aczFr4vtfMinJGy/ws9UewmBzV9rRKFgNTvK3vzvGw7GOPty+zt6HfPtzgO7U1041Jy9k4SVCks8iuvZntTK4ziTTdb9rab5oPrd+8XgNKeBvZQO1j2QF9hP5kLc937NZ/DJk1Udll3qwF1guBPeP2I/Bhf7DzKvObN59+/+PlTQw+v/n0zzduBhQCfFq8C6xN8tLTimDCpABwpwKqBW7/8gaIDpwmB5c8P5g9v71r/Cx4ubv+byJwwZe7un77/MYu7Gy8+Z/fvDzd+3n7oZnmN/xlBtyp8Jrf4JfPxeynP8BtW39owTrTAkAhVdd+mfazp2u1X5V1O93J7eELcDGgQz/7bfky+8c/UnCEsHn/6duaYVY6wNe+3CP1C70+8qftt7uT5LPfZu/uP4FqH/M/AoO9+/zmAsJ//Pzm/XRjEuX9R2CPuHr3/tv8OADe0D5i/8dz1H7b1cUMLPOdcp8OZM/eTjPeTs7b+lk2y30QiMB3QSA/HBN4D9jxL4qZ/nx+886eAdGaKahegOnduHl+auKwuHvIMxxKIEUf+9f3H4Hwn4tv601Wmo59/3k/3avBXg/5MSsBYPx02PuE6cRxAYKVofX98ct+K2pb7afjP3f4buFv938w6CTGjxfu8nw18n8Q5+lLYAHgB+8Q4A5x8Q4GPyen/PjFbr4AZHz3HPUyw9+//27yw/uec+HHXPSnqY8xLzP4h5nfO92P88mf5n8/8mW2/GGVp4uDBb5+ejrZ92b6EhRgwJcAZI8vLljmi1tWcVa2PxllGgYgbIqwn6zwtxlb264fdBnwjrC2PXtymk8TgsXFh6ouXQAvs/3+ABICOOvkjwAvvXsyiEoAOnf0m9k/r+rF9RP8AS6+Zg7gkcCXQexMHv7IE1PwP1PP7N13IAw88oclHYCh4KjPVAjO9A44NcBjG6Sud4+rAElAZnw/m+R7XHk/8zMw7Uc/vMfuJPb7X8bjw0Cv8n8JgFod203vCPCAr5e7ND/hzstXO/0QR38D6RTAZQ3EHGcgXwAAfwfgEUg36QZo85kJJuM1U2a3HaCAtizBt4fmRnCveNtOmb2rm++FvufQJ2ztpfXuJ9NOdv8e02b/NVt8+itifIOh37/PSjM7A7nHm4jJDLhBOKWZRyq9m+qeEh9KAulp0viddwDljf8Wlx7YNEk9ZbC46Mt0AiEboEU0Oce07R93HPp+xo9nmP82g78D53r8iz/D72cbgHief3e7r9TpQWXABl111zU4HlBvVcf5Pb8D9gPIHdB7CjiU4wcTMQBE7QMQ9CdxejuLPeCIvwPUeZe9gs+dL2WTsr556I8j/pgu/Vufvfvp73/8xYJg1Lv7lu9n//XbDPmF/aZ1vkyLAKHuI3//BCM/LTSt/t9Mfbh9BZL6l4dkP/j707Vf0/PLBCk/OPpD+cj7GQPoFFDbM33PnPHx4ceRlQ94zpfcrsDOEyr9eHcirRPy/qyPScc1WBNoGQRU6D/x9/0vjvZ1icexgCm/AJnevR74wUj+cjpwqB85w8s3SX97/fT+r9sBSz3zxX/N4Hs4THL+z68XP8zgT7+OiQmzHUBA7pnwM1Ao+O/Nx6QEyQIE5N+bP2Z/bz6/mf0dePDvn99M8n9+8weQHnyZjgi+PFzvnm8fhwaytE9+8hjy/v2v9/7eCP+MP32TZVow/qblyQdfNff+/b9+NntYlveIaP97Sf7q4BNVmBb4j8g08fEfwMm9E9j7XH+CxqYq71EX1GV+D+dHWnoXT7R6BBENjtL6H7I4j1tQMfxnhAKH6IoJDwBwxy6Y570HJQEopuwQlADT8UDyKnNw906l3Mh30xkUAabeRj/zqEdYoO9BGngWZj/ea8YC7NPEU0T5df3qsa913A9h+FPCmfT2NRJ/odbXtX+hW6/Lq1/63D/+8ffmH/8Al/4f/G6S4/2/td9PieXT7O9f0/PLt3L1rvLejrN7/gN5pravDy/64yHhV3EmZ7zv93I/w1+UDczg+ZMe3/2nfe9FyN/BB3DtHqN/v++zv9/+NMXcUy3/zk9+lORhna9s8PObSdYfIeGO749q5fH/Q9/fKfcndb7/NTt5Hm/+zbjfhgEWOBWLP1n7v2EJf02xH0CKffMvUAKCTFV37r0yB0Xd3/42O8RTw6IM2pnmTikc1LItSKCTCY5Tfo0fqbSe2gVNPBnyMQ7wh8S/LzQrg9mf/ystvfHDFXpY58vdOn8+iu4SlKTTKWYqLcufi3vxOi1b1Y+afconII6Bqj5MHyZt/fn9Ml/uMz5W4593EJ6QCKyqrnmQ9Kumy/yPk7DG1Cl5iAa41cwfALUCi2UlYAZAi9nDM5sy6x8V86xJJ976oDtl/eA74PCfpsX+/PNPwAajz8WjEEZnj1ZQA4EBr+IAjwZHCLI4jNrPhe9G5eztP//1dva/Z/9p1n3xaQ8ZEOKnaoGEgiaJM1CFdvm9tL93JWzvrtp//uupSLBMAfwEGCIO4ifFyeIi9b2vWtU4+gOC4V/ZDij4QTk18bG4/Tjjg9mrvLNHpTVR9jvj/9qncsd7O+Vz8arJO+iAAqIJxpeJ8N93/fO1cfLFBcP/nB3W8p3g3qvP7mEhMLksANZmrzYvXquGt81s9XWJjzPx3oua8nN176vchwX2wy7ls9/x6HhNbZbr52JqZfiTqu6lzUM9YBDQjPs06YfJ5lM3KreneH3ufR8zof/sWNpg8/ozAIeHF9u1f4eue4st7GJvYnT/4+lSz+7KpL9n1+xpBe9plbsPfl/zA7hrujwvf+4MTUW+509CvTwyG1DCRGzvjZ1Xtd6X29Rl9fDV+1nu5/+u/wMBdMm8qbsHTl9MfTZgPBC605h7P+/RC3u08x4dMXDab9XYyyzpgOnvDUxQene/kvTjR5D8Zu9+FA7Az1eyXU99xc/FnVy004S4fXTSpiuP1tbUCbjnwq+dikd34t4Y9F4bGffa8HPBlddpoWtZpwCy7xz+bntA9prH2R89m//QaP385nEIIPeTtn/4AMLzpzbrsx37fUcTWKyb1POTKYCrSob4U2twKj4ARjY2ULdfAHjzZ9AUCffeImAW9PdZ8KnUey/3a7e2+VUv93Px7zu44rf248tUyYMwmN3hs55SUus/rvreZID2UZ4/BAOABjQ6dRMeiPH9wX5qBzyKqMkq9dSrnCzxWg7eU86jhp2S1oQ5EsPcW6RfWzIT7j7ays+69o45T4RpALmKgHUj+95KbTpgj2m/l2mX8NmvyAA8PpJiczfWT/2G75oTj64D+BRPeelXnYe7PzHTmnf6Nem0BSf3vecJy+oDAAVg9Luz3Rkg8KSuAOs/Avv7YFxPXe1igomvunXKMgW+NuW02dfmCQ08CiD2K7LlwJsAK5j6qrE7+eKbTwUQ6OVNAfzmxwbs1GsF+Jf7AJOaqUkL7DJ5aOzfvz2rmenjj88lpPsHkEDA3dqeTU2N8E5RJst0NXAgwCr9qfF+L4lA9geytc2d5Hp2a9/l/mrAJ8o9FpjuxPVr/AIFTQdpx2qSfKp/i3BiFI8Y+4+CVeD0wMj3orQMfmiHQ9/FIRh9d90pyUxO8rUq9T+GH2e/v20mn4rb8enWIIe8vA3iumk/3EHvnlVe3q4Z6e0fd78rQVnQTk9F2tfGP+D/5YevKWBqdUy+89pPAN6RldOTi6eJJ6T5OLvzCmCMHsTjYzEwY0oS9dd2xL3p6fmBDTywmXQEypH8rpG/KOt5wa5re5y+f1+W/lWFB3t4Nc3UlZ6ccgKVrq4B0GXjx9nmsets+XGm+fdGMnxH3uDp9mAWYHPACO8mFJ2wCHjwI4AmFczutRPAq2+GBc7hh359Fw6M+6tQj+xW2UC39dR2BshXBp9mz4YvID8PmAcfHjh/v3Jv3UxXGt+uQeD/76/BBYqejzM5dtMHNj21CCS/e8oTOJ/2maJsQpB7/wwknmZK/E8NvArwSx99KvHfHaaJb1Mbclr7nk1+3HbqzlcAHbrq4+wwJdTvOtDf8uu7Sbr794d6772/998shE8WKh4E+l6Bz5APMAIcNSzuPjc9kZu9fWz5dmLHTVeBuPG9X9vmh6LxF+eK7Gqyy4NI3cn3t8Lxyf1m757Mx594TTn1Pp/qf/+02ZSXZ++mRJYDqvXoIoMqpbYfke1Pn+MmbabxDvC4qQX8rr3Ty+fX+0qvKP5ucl4A7yC8H5QLYGT1g/d9M9mjzPrryZhHA+9Zhn0E/v7b7J7bn0Z7YD/gICB3/vz49OMMAaO/mu/OXxrff0y/tyvfTkxrQpQnAN4bHve6wA+mFP+k1V8XnLjCO88HzKN+zev3bf8PMoALTfud/WHgPCCc0V+bc4Kav551IrXfHvkAGwHnyb9/9lM+6dB3D5A+zlYA7QC8ghzm3mX/KfmBhAcIUNZ5z6fJX5+hfsXIx7Oq+0OkKcIejyanB8iXDhjS+4WxJms977759PvjLH+8jiqdqUycDllldvt4mPjPNyDPTY8l7Geme1aSYHht1x+aiXJD8McF2At8f5RO4N6vasznkCayQd0DxiAEjBEURhAYSixI0vfRhW3DS9umHBchSZLwqADDl65nwxTmeL5DEISH2QvPJimChDGw3iNvfpm8Pp62ddxFAOMUTAa+TzkIguIL0l8EKIUTgY37KOJ75GKxcL5NTQHZep7lIfuko9dydzrz80j/fOPgSzCSWzY8/fizhuYnFzrvnaE+Q8ViPtBLsl6szWgk8wVnW7sLFY1lahuysNfEtVy7mbNNU2VLx1dje0BwvB25bksti/lxfkvy/X4QdEJscyKizsuFojdci1DoAO2teQlBeA+RCuSduQVRobuSzL3Rbbn5cRztqGbUjkWziMGtSiArcb+9iDo52F2yRc59mUSG7goyiqM336qv7YFezZsT1GvBxdrVhm2xVQWAvcpbwloIeNkL+mCn0slS5GxLGK2AB1kn4/Zld6Q1xLvdxCQ7oOKiXNJEvFJQRMG1fhWWwbVCwwVtXfZJeKrLMSgyKM91ZjWf6wnFalbcEduE8rnC3iDhmbwNQdI7qB/QZBsUwGWouUfQkHirJWysDsnpJOT5ofByfTTKDBJS3bjMOf1cEWNAN7SH5Evugq8N6yjHVBNqvXvrT1fJ1l08SRGEuC0Z70LMSwOHC0U2xsWKyubWRupIesSTg7m9sh7TUg5Wpxq/PgUscTnMMatUrmzFccv82BHSvjYzqiACbHeeL9OqSRQLwc4Sk4tzZryd7Sq+BPMl186NeH6zHXLPsZR24CpUmhNSupsviEMEDyKWVOc1cmjR6OCdDGZoNze6WZNrSpEhWsec/KI5O/rAyEWEBkWeUVGhq1eSbgpW3/O9y45pv6b3/VLrWR2xDdK6LFnhFtN2vxfBniV28nFD6U9wrl62OW5IYdoe6rOdnzrr3HICtIAuOZmYe0golFXFOQcGjxBEhkoG45zYU6F9gO9oSIZIGDqQNRqw7L5Jo10R6SIghNqGKmntGCdbYbDFtUIpzoXNjX26ytmlIVnRqV/VqI+Pg+c0pbpBhQbHlYJfW6IqQunC5FcX6yRdd1i1yvGd1a3JgMYN+LhwhKNEG3lVr+Z1ce3stCNX1MDsnW7U/BOHEWekYvBM5rJQ9Y9zm9rZK05SEJkXN9W6LfXj3MTXwLE4m2qj3Wlt4geLqmJrTsbNnl0gw0EUrPXh6g1zDtIwbwuEzVt4dbW2JrkuTsyh2h8rOLmMZdtIJyHLyj1shhtlPNgjM/DKDbV63IvpJTvw27XslfEmsjixRDRtBx1WSsXerPVNFNaeSlvpTmkaFrqwya0gSZ1gJCs0BGjNi0d7IJ3dUIjWqkmzdEuP+/WG4VjeU9Rb4gnpNS8z68wPtKbB3dG3NnIz+jQ67o49t4GjiKtv9sZEEXW9qbr1xmJ37jUkdMO+SGiFlBIhITXLHxt4r7DlOjrkm/XIHI7bzvbS6kQl55rGjkq80rdyjvu7tNuO2hgollQvqDWssxZ7vAjbFQtCYLs1l2q4PLW84NPidbGqlFhb3EwJhW7WZdXgIVYY6jaPei8p92Nr2l3K2CmVMJ0puSEOIxrL02O40hZouT3luYWbtspxOIzl632VSbkh7TJLuqL0lrLp0Csr2RdQdbnVVYxiFZtB4wvlEcp1vSqLaIcfhsGOJHyBn9LbMrFv7C41lhkUh0elRPKtqaCqj+ldllyEmLtKF8Kr/ItLulpJJ9XSCy1Osw30xOR0bLOZRlPrkyxrvBEk69thBfGbZilW9VqLAYqFG2sQ6losUNO/bawTqarQytyxHj9wlXccEBG+bAhk3KiYl+w4NuaSq2fbmHGGeC6JNr5K0QmetTB66VfDpjsomK1G+SoMMneRHA6tU7tKnoDy9cK7ltTksTWiGlRRo0wtzNvhGGSend7c2In1MEGtDUWsu3Fp8LuNqlzrJvGtrFV3o73YpHa2g4WEYTB9eXJ5I8tvEek5uNN2eHjozgsrn6/gOtTJcwSvlHy3nJ9wrGAQpJeXeobZirUNl2s7uZVhjg+RwRfufCubqcDIAWbiyQ0/slntDqUJJgaD0w7rLbZwLpIJO4a+duIQJffeeoDZOdf56ugfPTPbpj7DS+PhFqzDeMdZfVoUFq4PzFaUtumh2K3lgQmIg+jFoxPD7cbeELDfMnHOHzaytD1i0lHOBKJDMN0bddTgXcgxjxE7j8drQiGRrbCqYJAJvRuI5aaq4zktLxQByxfyCkmERW9i4sZZ0CHP5X2hrubKrdGQM01D65GyjCatmf3+SqASX4UjQgYklpIymRxjE5INNncbxbP31GHk4lOR41UEhaY5NqagKCpLsMlVSrYWSlPXtRFu8xZblal5cGQ0V4fBi71bznIGdWDHAl6tnD2WykqUp1gyAGPleqAA6tg7dmMZ1z0jI1vrUrPkNkzsVR546xikhSNE0oMW6ckW29R655vQHJdaJFCOx3PKzu2l7lEbnii5hTI2W1keFWuOrI01QbKndb0zgxPBEIVrs/xyt2hQNg9kp9vcDlCTtJJQmHx3FLK0OaU0NtrboMu3G327Xi0hYROz9HKt+6vFlcOv9qlCDuMVI+klLp1rzG8a22W4FV40u1rmEZfoCmzn37aboedJ9xarFRR5DVYUJzYt0r11spltQrMaJCqrkLueWCGUbqYt4ebx7G+GijsiFBRF7WrBMvYo2rzS35bkfpU0iluqJ0atrolNtvyBcAR6jP1eGwbaqzEX2ja+vlWH/hKWWeyN18YE1As4h8QvqGGxWmqeuz4s8L1KuGkMJGWhzjwy1dLaseOF9DLNciU1J+b9SoRCApZpFTc39iU3xLIUbV0O/WzgzNRCNzshGgI0Faxqq6+H3tl6grDZozsRVjujPjDWSujnQkpmWmMlNcnmEg3g0+eVcbdttkuSpvKeypEVP55TU4w3hCGReskUbbNZ0h1vXvS1xfqHblzAtC0yxYaS66O1FcNitzpsUQJXBXh9Hms1m9ODmyeMinjynlMX5kotYXuXgNqYnkvXOIbxhjwYxJFRDjeS6rke9oelMQT1fLhA87ohAv2YU+Tcl9XB6wc8yGuCYL2xV7iUD4kens/looK9YHc2r8NScZL9RlRXVSULRsyAvHYswnkQUe6KgfDSsoVjpMStjrOyCpNenxTLZa9eAq6iPC6DjDqGCf1MFqbryO3RFw9RDFumae6zizaMns+U3bLX5GO8OdSX1YlcsoB3N+mQCDtirM/OIl7yiqHmtbu4geXXvHEqMproNZU0de2Um0kiQfSiL0jCOHcwpp/DuiNPyFbJtuthIaMQkRVmS65snOWHItO3C+WY0qtmmfXzgxiQqufCiSowFLcl2qhjGjaAwsV6Gcf5XFVOjeVivGes5p5USdzO9reYv+U4PljuvYHaakebObVGDvhQK16vRrZcN5HfpWsjRjP51MRMnqrFquzyywoEpZ3rgn5OutUYhhniCNcFXZ7ieWLvEHPBRKkslRkLuC3CF4lsKMpCqUrOXbv72K7mYc3ng1hdL6fS4/pDJ0bU/JovlryGZKgE57S79yB74G9JwOc6YrD0KFuHvVmanIEF543k0ExzbDbIXN2oV1/rwpNVx+KaXBqdnF52aHkI3S7XduaNE6QtyifhFuEuF0jRDkrAYWeBc4WEXkTWxT53WBLdgNGOZttco1jP11Yskf52v4xP0UhfsUEuWYdZAqwHuOeYni5giqtUmIN7Ruh50tkyeQ3T5suElyxrbHR0eVjuEWE1Z3ceu9iGciSaF0Vho+tyvWOythtce389bDhWUK9a7ozL1bkNCSVZazzrQQyM768xynfhTcvPojvGUGa2CVrhkBzhUHeMQPG3Rxwr6EgOoyX6KOq603ACy0atVBOCd1un2VFrrix6MRt/DoXy7mi4h5VcmjdJ2seuAlh9GPMdK+SrdsxkNGN4dCtpKpXyZEiXQ6MLTEIboITraMcc5yWR1o6Bm6jTq0v5SNY2MzdGrzK5lXFm5sczzQyqPjZR5VzOiTKHzY3a2McFMubpPOlP9E2VvFTFanV1M/Nx7/orxlEMC437SJP1dd8d4HFptgudxQBEnoPVKm+u5c3cqnlJsUSlb3fLBUn3nRZ0sCFlHcyY+sJhwpvFxpnAXQhUniMd3OHdynDFEqiJzXR6XC6PgExCB5mZW1kc4+Gyx9obWxiX7QJn5GqXePtUdoZ2kSnYgOgtdEADS2NqREQPoYEWDCj+7M5iV0gFw720PlXzYRemmQG4RStG7Jk5KlmGoOdtrpLnA2/1yVGhL4jO5KtEs/jFAsc4a+EXMoz4Z36fwVKfjJjY38ajh9NKS2zG1ZoWhp1V5Hrj6EPABMcSg4RtWG+j6hAUKIl3xxGTgVVkhowZ9jws3HNNgCoMdm8QCkChQZmFW1iYp2Pati000UlVhiZpwH8DeIPAepWfz/vLpWKOGKyRI0Ydj1moIHuOt/KjekzEWxwZB5W9aDruZdskUoi5aRnkYklfzqiRF0SSn5YC2mxaJej1Ih4URdjvl1FMnkpXsPxFP57nlYke/Wt4Y0RNgbcyVvPNNfcuDk7sO4ytiNLJGXzUbpmAFCtl2G0620zNQg5vtpm464YLsnbAB6c84f2VaOuowD3Tojizb5dHZuzo23DtO+pIw3OZ3bELfClqkDK/5KF7470mWbOt5dKFLs5pP1376xu5u/hr6bgx7e2ujPcLOiNHq8xu12KDMaO9dIF9LB4Qf4k1nVUCXSEvucHxkJGCfOJjY9yn4YnEl/uhlaJFZRH9ScZuQUJT8alPhVy35nxri1rLnmxTKFXhQOzOAR2xYcmxa/kAqZJcDb7gqNpJ4TfwFZPDc9ke8FIM1ni+ku1iqVcFUC0UXS68Gfnr1iz8aAFxBJHdjEMRXqX55nBhy3C/UWF6QyTn0lQTudYZ2DmNnKMIWchckrrXSindj9wYmKw/7AzXRVSC3vk9V936ItiI2mp7SDKC2ZzQawpcl6JFoRT9RhKA8hmOIVbL20ZXTygfLZVET5Bjzm/QdFTK620bDgdN9EuO21brM0P4gXaz0HFxBTQIqfJusRNUInHTpoXH7Y2T6kRMxiOk3ZLjcBQUh8yb7MCNpiPO8UF2yJbSNvbBLBYXKSm4k3MVYc3coh2ZXoXUpgAnI1frk1uaOcgOl6MQBDzlyMy2vA3zYxmV5E2pl/ZVvJVW2ufqSRFgej1exblwFeLlzlk7ZKYvgh1D9ztLbpqDe7LzDhSPkLCi8ERJqmG/FQtrUeiK6Vw317qE06u1VJbh5WQHZXg2L5TQL/MzNA92m7JZD2Gw3Cy2GKQzFLlPLM/to7Ne86JgbsyjiF5GDzncbti10eTlNijRMrUTqVzfHKE3A5IoxGODr2/YbRQ6Z7drdtB+tSvQdtS5zMJYWeKhwcaIuYuPZ4s5BRC/HXTXn/NIPi5BCSlaN1pcIYWx2VbZonCRAd1rrQpXF9/bjeXWJnvLNZPSDuB+25hcv5y77qUuIfYknJDerllG2CuV57jQJXCsGxyhjKX3CDwIzLK7KFAh5IexU2HmuPLh6/4q+HlQCEeL1l1Jh31+wK+pMECegPvKPBauJsNEFn0KM4Mu5K6/cia0i/OEz5UWwXPCLofLkesqszFX5RxCwjixMSQ7c1FxFi7D6UQVTecurqIcNpcVOYjHlbUoF0eMPZIHcksiFaZoWZUXprrY2cu+xQKMulm+fFq1nla5BbWZD3GX5JIUU36nL/dhm6Qp6TWCHly4bQ1oIoYWmZbHBuutIBAEOyHb4mlxVdW9bZQKel56Tovoke513D7Uu5uCU25gnqt4och109c0nhwiSuNkr4l2sqVLCwHjjwPWcY1Ung0BK+RcjTjynDa5cKgQMysulxWkXOYbphIzQa5t39/VIsFgIsamKB8Hq0qG92SaBwaOSXjfE0tXlKCg4I55auSR7/CaUGSblIOb0p/Tc025mjRZD3OlzFAcsnHAlG7Hk4ni9Nw4w5o4v3U6fxtHY36qTonZQ3R5CdHr6kovUjgclyrIhUyFsget5iGTwRaGvZDnOp1x2kCoAnfuWdXZF5sBY7ksCmu3pjS9E6yDMOboxvBvV7sKr5st0DVEZSsro9Y73B2Trr7Sh27L3m6rVMzEaFVurduInRcBug8RId2EbmvvWUxIdALU6PL+gkm3E+xvpNxxiXx+S+uC17EVfquIg+wGQZqjldGsTnsq2Se9oV1Tb5cLeFAEyzQljjg5P2O5zy+j3lzdrqvajQ8GrsOmTHB6JVr1MnIR86pi2V7P7Go/D9g6EGBA3am5jMbBIlWSZg0ZdneCcx3NDpSxZ8976kSqgtbCmcAUo8R4ZFGThFyXBOS3J3NIEYyrYZK0+UhsYKFOBiftrMrgDcWLGs7tdrSy9qkqXK/ndoJrKqh01uUwprSxbewmSvqrzpnozRNbDkFWBysVBPqGHOYQ5QWbBlLg1Iic7YXsEIrZV+6+7c1tL2Ybcslkdghd1rSxOJOqvpqjlAAtfAo9XiJ0kx6X3FiertUeDq2+pTdCLG9OPopcVz416LJpl01PpjcPrQk7X+RWSAZGvVrh5joe6LIaAwOlGMNUkTyGGwiBOhmHAgQKNlQDBdF8vqIgAkZJbNAsOZYVRuPcGkL7A+MHsCfHpOIhO1fGIFrGe7f3En8h7Y0ow1RQU9K5NdC0r1PKubZXp20Ss4VGLNqLcpHtPY5XpNsewtaTd3TP4CsxOAbXnFr39WlsI5iBBR2zlGHjzaO04RAaCavLrhC9yw7hWsNayRlxHFi4i8Lr8qLUF0+hgx1/VsX1pStEzDtzIx5e7F1F7bEqvaWX0SlZHAcLW123ttcHXzhdFkuYybagEhUxxWodhwHlCuNufR/R1U3sCejxupSlzInm6W3H3eqUzjP+IqsezDF7Rj0jwA92Hpymx1Olcpx8NgKnoK9CsAkHbxeWNwkQoFbCuZgXrauuxC510rziNBc40uw2u6Y+z+OFMecQCTsuo5bPAX8lGJk/703dPZon2Ss3I+33JF73yRr29e6kndXR70cdiVPA+6lRuM5ZNV+VvHDJK8Mb+bIf5uwi00V3AUeNGDiMmmfwqt7sgwPP8QjLwkRfnL2lHFw0ryX6dq1DmhIQhc2x4xYxuGh7KJsduzyC4i+BBI85tuerwjoXVIF3hxNp+TRJxeq1gpaQt1bQdU7u9mG0sVM4Iav2AAkLPRl8XAKF5OGwEtZzod1oVHfi5Ly/XJxCSwCAy21EtTi7ZhOpOK2b0dAdKF6fa2Oh7I8bXmE3BSwS/lE3uONtJC8CREHmjirUoStO3HWpErhlacM2WLYZuxkjL9XWFeaOLjokrnk+s41ILtuDyDtELycEu0MtMbtkcG3utmIMIzDhWm4BWfJVypYLAZ7nWC32wdmSIUgB6t/zdo8pvKnSziDTtHvBEwqBhVbyb0MWeETJBKYwD7G6F8XI9Ep+ebFX5SHpiWHE6KUfAFS/ZiSPOHwdea5VjEOoHsMbLWXF8QzS/bgklMrSXXYR524i8R3gzQZp4KtjWc43KbNzFsURw6/aiERpRQXxrQzVmjTOZzoRDrW18vntbpOb2zAYQ94ei5EYwYp4rnIJtNtv91klmgUod7r9Eg4KpyW9ol7OuyOo5lycOAlGitXr9Ghl/LGkcUMWpYi1nePutFDD2sjWSWauzSshLm38dnVOjtmQZ7M+ofr15Ls42R6dbVaw4Sm2pQjVGUQ0NmOsgOCYa5c8c487z1F27eKsiI3t10LGa6yZAuS6iGy46xMP82DfGvD1PtUKXKk9lGjDi0KBAN+p14M97jdc3RYGUu1MdCtcQZQ3R0ZHSJCancoI9jFFbBLLPmiJt8HX+gLG87Q7ZmYBS6oiLsWgkSB7CUpSgaUyhz8iREPyDGaZ4kpGjOR2iq8ImSYQ4MPemd+ZGCaJOJ7oZ0DhcdXvfbiLEwFUCMV8XwR8LDRlcTieW1zDKcEkDE07E7a2yuNAui1x1KnYw3W/yoGBJG9TeYm0WImYzFKLUbfVQcQZ29UOm7UlXpszqM12W/nSb+cYna7PVFpi407tK6SJ7OM19A4gkEUNb9t9rZzPqhbsEVs/nhtnOezLjNqPy4vEqfbAcyPMHTTy4HkdoGWsfTtaVIC4xXkBBUwm+nRzPnG+vB5ciqTYPFuQt53V8QQCY44LakpZx082ttxa54sVC7Az15wW7iDc87LK9RrxvNlFyqXQ9uii5pylQXJ1isH+fu15oMwbdlzh2MntCu/myJLQl5bvUVcqv66cK+Jf5rUDb+MilFYOmkZu1Oi+rdcZ1B+7HAMch8iS+hYcUGTXeudS1P3EoxItXd/CiqyPJ85jfRgpN3AgEmWExzZPZnhJrSp1v5Av6x53JeSCpJyMpCh0TPVagxkGLXbLMqeoETbCBafKbB2huXNRjyuuZFqutvhobFEUo1mU26J7RFaT7HzNrbELMT8r8UqbU2cscAKxObSmRqKUvs6DGhBx0jzAW+ZmNq3g6CgEuc6i7XvUUiXeRLjD/kYOB+qks2e58Fv3FI3myV4pC6y34UILLgbqCgx3vY6EpsOplWYbt7sAdrJid4Tvp5K4xlk8REID83hES/aUt7WQAJEuuLxzUHWgzIMxMG0bH1tXCnWObFiS4hZ8vIOoQ1bGCrXs01vproqV28RyvagymyEEvRuo47IqxluOthcfQYJ5wi+w9VmYV7GHNHPphsUGkYugTGG7XTcHsQ931wFUeh26LGvWMjnVCu0uOMmhTRkqgl/0G3euxzqXdqc6gmi7lHFZOsyLlTkIwx5GTjTG5udNoihii1tUKN10mRDOZK11xFGC+UHqtk2CD9iSOFULb0mavb9BdcMSMBqjThc8LRN5bCwRt8otye6rOvOOe5If48EaT9jZaU3Avm8xW3deuCsWMuGgLn4LdyM2XNADIBeJb8Lrm8UV3AZGM+SgpTescOJsy8Pnmu37hHBva8OYu8rgDVtvbO1Ovbo9gqyRktqIsbtPb64gemSen3gfpuFVAhmnoLcZAxoFdFWFndZLHBEoq+oaSi102Cw7uBUsGrPTfi2V9InwSjWpTBrbrrL1RcfxnswDWKCQEnN351A3oDUsVfRBkAlCgbJrJ2TDZbXH9EPlhf4e1tEOYBOsLmNcD5YDSwU8sQh3h0tBQKWORoZbnocLcTtT1daCdoGVzGPXxi/Z9Pu0a9vF50Cfl/kly8xuLSqZAu5v2hKuzmPlGhyfKL0nANA6IaOa7obj+qp6/LUmQueyJvGq8LhuDfL83jswKkM6o6jus74eCyxY8AgKqREsoJIpGxcS5KKChEHww1HHqii9i+xROiPbVc4ZVocumpZpWrEtaoTYZRTVDUfyOl94oGaqvEtuntQzenXEPZXSQUfBwz7wRkZI/dho3FQi3LoJrU7KVvWt2DjXNWommaQ6Xq/tOHoBDbRLmZhAaOuLp1nFXl1oGGtLFG0zG9xZYYBxWy1Izcf4up+vT2YN6pGwbqFKdZKbvKOE09y77TbaHh7g6lqhOQj8dNOkKZzlzabwMgmDT2XBcgjM96wlsrUOSs1MiAs9LFdH1KiU/W7T7qRL4ScReZTyfan1CpEtGqdOl20imZRpo2aBBr4ucje5A6Xr6Xxjb0Gh+9s5bpp9uSj28kkL1vTA7nfwhix0glqcnRXeOlvqsEC9E8j013XqxUYbU5J0stW5fkblxO7yGy4QbrFaGn2WyZxoyonAncyOZtZs1yfN3IavwdKAFITBcgz1LhpzWFm62vAUo1eW5Z4acZdc8pPR1bviHGVRLCjOqFIKDxMCk6ysEI+1FOdtlrxlZ9r1rgnplg1NutatIiWbsTNWNsqbvtxWAeOT+AV28Z0W7jUovI05LtzYNWdpfeb383Oy66HETLody4tNVmAxZZcahUrGzS0tR0yaDFQsF6vc99tY3vf1lWLFYe+dF1WChRnSHaowpdT4GHiC0hDwwlpoba4iaVpcUvsiovy2PVPFQsW3LGqjImSjjhEg4VFgrm6uuh3IojWSZPthBVH9kjuA/JDaK8Dv6N/evLyZftXh+Xr0L38JaHrL6v/by16P97LKHuxYuP709tr0+9Gf7nt9+vX2f7y8ASUv2PzxflqTdeHzVa/H22kfHtM+fH07rRkfvybz9QXuxwvgrR1O/yjHm6+jytqN/Onl7PtrcNMLddPLd9PrdS9vHm+2289/oePr+9jTv+5RNH7uZD74+Pqu+iTf/Te17m/TARk/wm/+9X8Bkb9ob+dGAAA= -->
