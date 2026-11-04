---
name: "rar-kody-w-buzzsaw"
description: "Set up a buzzsaw: an adversarial build-and-verify loop. Generates the seed prompt, the disjoint region split for parallel builders, the harsh critic brief, and an acceptance-gate skeleton. Actions: seed, critic, plan, gate, rules."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/buzzsaw", "rar_sha256": "b14a4f23984fbc61acc1bde61ae592e16e8732ba287a78134d71361130011663", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "author": "Kody Wildfeuer", "tags": ["buzzsaw", "verification", "adversarial", "testing", "determinism", "ark"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/buzzsaw`. The original RAPP
agent is preserved byte-for-byte in `buzzsaw_agent.py` and in the RCI capsule.

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

Buzzsaw — an adversarial build-and-verify loop for taking anything to a named bar.

Generates the four artifacts a buzzsaw needs: the builder seed prompt, the
disjoint region split that lets several agents edit one artifact at once, the
read-only critic brief, and an acceptance-gate skeleton defining when to stop.

ARK PARITY. This file and the single-file SKILL.md distribution carry byte-identical
logic. Measured across 5 invocations x 2 forms: identical output every time, and
50 determinism runs produced exactly 1 distinct output per case. The canonical
body digests to:

    sha256 = db907a26cc3ec142015cca637cb3d70f3e4d00454fbb7491d5ed08fbdf9ee4d0

If your copy differs, you are not running what the registry published. That check
is the point — it turns skill drift from invisible into detectable.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "seed | critic | plan | gate | rules",
      "type": "string"
    },
    "constraints": {
      "description": "Hard constraints (one file, offline, no build step...)",
      "type": "string"
    },
    "reference": {
      "description": "The best-in-class thing to be judged against",
      "type": "string"
    },
    "regions": {
      "description": "How many parallel builders to plan for (default 5)",
      "type": "number"
    },
    "target": {
      "description": "What is being built or improved",
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `buzzsaw_agent.py` and embedded as the fenced Python below (sha256 b14a4f23984fbc61…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `buzzsaw_agent.py` first:

```bash
python3 buzzsaw_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 buzzsaw_agent.py   # or on stdin
python3 buzzsaw_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/buzzsaw.py -o ~/.brainstem/src/rapp_brainstem/agents/buzzsaw.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/buzzsaw/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""Buzzsaw — an adversarial build-and-verify loop for taking anything to a named bar.

Generates the four artifacts a buzzsaw needs: the builder seed prompt, the
disjoint region split that lets several agents edit one artifact at once, the
read-only critic brief, and an acceptance-gate skeleton defining when to stop.

ARK PARITY. This file and the single-file SKILL.md distribution carry byte-identical
logic. Measured across 5 invocations x 2 forms: identical output every time, and
50 determinism runs produced exactly 1 distinct output per case. The canonical
body digests to:

    sha256 = db907a26cc3ec142015cca637cb3d70f3e4d00454fbb7491d5ed08fbdf9ee4d0

If your copy differs, you are not running what the registry published. That check
is the point — it turns skill drift from invisible into detectable.
"""

from __future__ import annotations

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/buzzsaw",
    "version": "1.0.0",
    "display_name": "Buzzsaw",
    "description": "Set up an adversarial build-and-verify loop: seed prompt, disjoint region split for parallel builders, harsh read-only critic brief, and an acceptance gate that defines when to stop.",
    "author": "Kody Wildfeuer",
    "tags": ["buzzsaw", "verification", "adversarial", "testing", "determinism", "ark"],
    "category": "workflow",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

import argparse, json, sys
from pathlib import Path

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    try:
        from basic_agent import BasicAgent
    except ImportError:
        class BasicAgent:
            def __init__(self, name=None, metadata=None):
                if name is not None: self.name = name
                if metadata is not None: self.metadata = metadata
            def perform(self, **kwargs): return "Not implemented."

RULES = [
    {"rule": "Check the assertion before you fix the implementation.",
     "why": "When something reports a failure, the test is a suspect too. 6 of 27 reported "
            "failures in the source run were the test being wrong, not the code — one nearly "
            "caused correct CSS to be changed to satisfy a broken check.",
     "smell": "A failure that appears the first time you ever run a check."},
    {"rule": "Measure the output, not the intermediate.",
     "why": "A builder implemented ambient occlusion correctly, verified 66.3% of quads carried "
            "the right vertex data, and reported a win. A blind critic scored the result 2/10: "
            "the lighting clipped the highlight, so the data never reached a pixel.",
     "smell": "Evidence phrased as 'the value is set' rather than 'the user sees'."},
    {"rule": "Prove the tests can fail.",
     "why": "'83 assertions passing' and '83 assertions that cannot fail' print the same thing. "
            "Break each invariant on purpose and confirm exactly one assertion goes red. One "
            "audit found 7 green-but-vacuous assertions, including a body of `async () => true`.",
     "smell": "A suite that has never been red."},
    {"rule": "A skipped check is more dangerous than a failing one.",
     "why": "A gate read a value through a method that did not exist, got null, treated null as "
            "'not supported, skip', and printed an info line. The most important check never ran.",
     "smell": "Any branch that turns 'cannot measure' into anything but a failure."},
    {"rule": "Measure after the system settles, and keep a control.",
     "why": "An agent measured a 9.4-object-per-round leak, ran a zero-activity control, saw the "
            "control climb identically, and retracted its own finding — it was measuring warm-up.",
     "smell": "A measurement taken right after start-up, with no baseline."},
    {"rule": "Never let one bad idiom spread.",
     "why": "`offsetParent === null` as a visibility test is wrong — CSSOM defines it as null for "
            "ANY position:fixed element. That idiom produced five separate false results across "
            "two tools and three agents before anyone noticed it was one mistake.",
     "smell": "The same surprising result showing up in unrelated places."},
]

ANTIPATTERNS = [
    "Absolute FPS from a software rasteriser reported as real-world performance.",
    "`offsetParent` used as a visibility test (null for every fixed element).",
    "A readiness flag that flips before the thing is actually usable.",
    "A cache test run against a server sending `cache-control: no-store`.",
    "Self-assessment after the agent knows which artifact is the new one.",
    "'It looks right in the source' offered as verification.",
]

def seed_prompt(target, reference, constraints=""):
    con = (constraints or "").strip() or "(state any hard constraints here — they shape everything)"
    return f"""Act as an autonomous senior engineer. Build {target}, at the level of
{reference}, and leave it finished.

Work autonomously: create the files, run it, test it, fix what you find, and
deliver something that works. Do not stop after planning. Do not hand back
snippets to assemble. Do not ask questions you can answer by making a
reasonable decision.

HARD CONSTRAINTS:
{con}

Fan out sub-agents and have each take one area individually, so every area gets
real attention rather than an even smear of effort. /loop on each item. Have a
SEPARATE sub-agent check the result — a genuinely harsh critic, not a teammate.
If it does not measure up to {reference}, keep going.

The critic must compare against {reference} side by side, blind, and say which is
better without knowing which is which. Self-assessment after you know which one
is yours is worthless.

Before you claim done, verify in the real runtime and report MEASURED numbers,
not expectations:
  - It works from a cold start with zero errors.
  - The core interaction works repeatedly, not just once.
  - State survives a restart, and export/import round-trips exactly.
  - Timing is measured over a real interval and reported honestly, with the
    limits of the measurement environment stated.
  - Anything time-based is paced by the wall clock, not by frame or tick count.
    Prove it: slow the system down and show it advances the same amount per real
    second.
  - It is usable at the smallest size a real person will use it at.

When finished, reply with only: a short summary, how to run it, the measured
numbers, and anything you deliberately left out and why.

/loop until it is genuinely done. Fan out sub-agents and ultracode."""

def critic_prompt(target, reference):
    return f"""You are the HARSH CRITIC in a buzzsaw loop. You are READ-ONLY on
{target} — you do not edit it. Builders are working it right now. Your entire job
is to refuse to be impressed.

Your reference bar is {reference}. The builder claims this stands next to it.
Find out whether that is true, and be the one who says "no, not yet" when it isn't.

THE GOVERNING LESSON. Two classes of defect survive every round of code review:
  1. Behaviour that only misbehaves on hardware or settings the builder lacks.
  2. Surfaces the builder shipped but never opened — including its own self-test.
Neither is reachable by reading source. Something has to go and open the doors.

DO THESE, do not reason about them:
  - Enumerate every interactive surface and exercise each one. Report a table:
    control, what you did, what happened, verdict. Highest value work you do.
  - Put a real cursor on things and click. An element that renders at full
    opacity can still be unreachable underneath an overlay.
  - Check anything time-based against the WALL CLOCK, not frame count. Slow the
    system and prove the same amount happens per real second.
  - Run it small, run it slow, run it offline, run it with storage denied.
  - Leave it running long enough to see drift, sampling on an interval, with a
    control group so start-up warm-up cannot masquerade as a leak.
  - Open its own self-test if it has one. Then check whether the test is right.

THE BLIND COMPARISON. Collect the candidates. Shuffle and relabel them A/B/C,
writing the mapping to a file you do not read. Judge purely on what you observe,
in concrete terms. Only then reveal the mapping and report whether your blind
preference matched the new version.

RULES:
  - Every finding needs reproduction steps and evidence. No evidence, no finding.
  - Separate real defects from artifacts of the measurement environment, and say
    which you believe for anything ambiguous.
  - CHECK THE ASSERTION BEFORE DECLARING A BUG.
  - Severity-rank everything: BLOCKER / MAJOR / MINOR / POLISH.
  - Report what you tested and found FINE too. A credible report needs it.
  - Do not fix anything. Report.

A critic that says "looks great" has produced nothing."""

REGIONS = [
    ("presentation", "styling, markup, layout, visual polish"),
    ("core-logic", "the main engine or algorithm"),
    ("state", "persistence, import/export, migration, corruption handling"),
    ("io", "network, external services, failure and offline paths"),
    ("api", "public interfaces, CLI, docs, and the self-test"),
    ("performance", "hot paths, allocation, caching, teardown"),
    ("accessibility", "keyboard, labels, contrast, small viewports"),
]

def region_plan(target, regions=5):
    picked = REGIONS[: max(1, min(int(regions), len(REGIONS)))]
    return [{"region": n, "owns": o,
             "rule": (f"You own ONLY {n} in {target}. Other agents are editing other regions of "
                      f"the same artifact concurrently. Do not edit outside your region; if you "
                      f"must, make the smallest possible change and flag it. Line numbers shift "
                      f"as others edit — always re-search for code, never trust a stale number.")}
            for n, o in picked]

GATE = '''/**
 * Acceptance gate for {target}. THIS FILE IS THE DEFINITION OF "PERFECT".
 * Exit 0 only when every required check passes.
 *
 * Rules this gate follows, learned the hard way:
 *  - A check that cannot measure FAILS. It never skips. A skipped check looks
 *    almost exactly like a passing one in a log.
 *  - Never use `offsetParent` to test visibility: CSSOM defines it as null for
 *    ANY position:fixed element, so correct fixed overlays read as invisible.
 *  - Measure after the system settles, and keep an unthrottled control sample
 *    so start-up warm-up cannot masquerade as a result.
 *  - Absolute FPS under software rendering is meaningless. Report relative
 *    timing and hardware-independent counters instead.
 */
const results = [];
const req = (name, pass, detail) => {{
  results.push({{ name, pass: !!pass, detail }});
  console.log(`${{pass ? ' PASS' : '*FAIL'}}  ${{name}}${{detail ? '  — ' + detail : ''}}`);
}};

async function main() {{
  // TODO: boot {target} however it boots.
  req('boots with zero errors', false, 'not implemented yet');
  req('core interaction repeatable', false, 'not implemented yet');
  req('state survives restart', false, 'not implemented yet');
  req('wall-clock paced under load', false, 'not implemented yet');
  req('degrades gracefully (small/offline/no-storage)', false, 'not implemented yet');

  const failed = results.filter((r) => !r.pass);
  console.log('\\n' + '='.repeat(60));
  console.log(failed.length === 0
    ? `PERFECT — ${{results.length}}/${{results.length}} pass`
    : `NOT PERFECT — ${{failed.length}} of ${{results.length}} failing`);
  console.log('='.repeat(60));
  process.exit(failed.length === 0 ? 0 : 1);
}}
main().catch((e) => {{ console.error('GATE CRASH', e); process.exit(2); }});
'''

class BuzzsawAgent(BasicAgent):
    def __init__(self):
        self.name = "Buzzsaw"
        self.metadata = {
            "name": self.name,
            "description": ("Set up a buzzsaw: an adversarial build-and-verify loop. Generates the "
                            "seed prompt, the disjoint region split for parallel builders, the harsh "
                            "critic brief, and an acceptance-gate skeleton. Actions: seed, critic, "
                            "plan, gate, rules."),
            "parameters": {"type": "object", "properties": {
                "action": {"type": "string", "description": "seed | critic | plan | gate | rules"},
                "target": {"type": "string", "description": "What is being built or improved"},
                "reference": {"type": "string", "description": "The best-in-class thing to be judged against"},
                "constraints": {"type": "string", "description": "Hard constraints (one file, offline, no build step...)"},
                "regions": {"type": "number", "description": "How many parallel builders to plan for (default 5)"},
            }, "required": ["action"]},
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs):
        action = (kwargs.get("action") or "rules").strip().lower()
        target = kwargs.get("target") or "the artifact"
        reference = kwargs.get("reference") or "the best-in-class equivalent"
        if action == "seed":
            return seed_prompt(target, reference, kwargs.get("constraints") or "")
        if action == "critic":
            return critic_prompt(target, reference)
        if action == "gate":
            return GATE.format(target=target)
        if action == "plan":
            plan = region_plan(target, kwargs.get("regions") or 5)
            out = [f"BUZZSAW PLAN — {target}, judged against {reference}", "",
                   f"{len(plan)} builders on disjoint regions, plus 2 read-only critics.",
                   "Disjoint ownership is what lets them all edit one artifact at once.", ""]
            for i, r in enumerate(plan, 1):
                out.append(f"[builder {i}] {r['region']} — {r['owns']}")
            out += ["",
                    "[critic A] adversarial surface sweep — open every control, panel and tab,",
                    "           including the artifact's own self-test.",
                    f"[critic B] blind comparison against {reference} — shuffle, relabel, judge,",
                    "           then reveal.", "",
                    "Both critics are READ-ONLY. Neither may edit the artifact.", "",
                    "STOP CONDITION: the acceptance gate exits 0. Not 'it looks good'."]
            return "\n".join(out)
        lines = ["THE BUZZSAW RULES", ""]
        for i, r in enumerate(RULES, 1):
            lines += [f"{i}. {r['rule']}", f"   why:   {r['why']}", f"   smell: {r['smell']}", ""]
        lines += ["KNOWN ANTI-PATTERNS", ""] + [f"  - {a}" for a in ANTIPATTERNS]
        return "\n".join(lines)

def main():
    ap = argparse.ArgumentParser(prog="buzzsaw", description="Set up a buzzsaw loop.")
    ap.add_argument("action", choices=["seed", "critic", "plan", "gate", "rules"])
    ap.add_argument("--target", default="the artifact")
    ap.add_argument("--reference", default="the best-in-class equivalent")
    ap.add_argument("--constraints", default="")
    ap.add_argument("--regions", type=int, default=5)
    ap.add_argument("--out")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.json and a.action == "rules":
        print(json.dumps({"rules": RULES, "antipatterns": ANTIPATTERNS}, indent=2)); return 0
    text = BuzzsawAgent().perform(action=a.action, target=a.target, reference=a.reference,
                                  constraints=a.constraints, regions=a.regions)
    if a.out:
        Path(a.out).expanduser().write_text(text); print(f"wrote {a.out}")
    else:
        print(text)
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
