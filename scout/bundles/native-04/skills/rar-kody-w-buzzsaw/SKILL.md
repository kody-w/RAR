---
name: "rar-kody-w-buzzsaw"
description: "Set up a buzzsaw: an adversarial build-and-verify loop. Generates the seed prompt, the disjoint region split for parallel builders, the harsh critic brief, and an acceptance-gate skeleton. Actions: seed, critic, plan, gate, rules."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/buzzsaw", "rar_sha256": "68ffa820bc89cd8966f9929725bd9befd616ac26ad26867b828dc790b9cf13bb", "source_kind": "rar-agent", "source_commit": "ae1d6143f70e0182abd968e9c1c80ead38750484", "author": "Kody Wildfeuer", "tags": ["buzzsaw", "verification", "adversarial", "testing", "determinism", "ark"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `buzzsaw_agent.py` and embedded as the fenced Python below (sha256 68ffa820bc89cd89…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `buzzsaw_agent.py` first:

```bash
python3 buzzsaw_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 buzzsaw_agent.py   # or on stdin
python3 buzzsaw_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
