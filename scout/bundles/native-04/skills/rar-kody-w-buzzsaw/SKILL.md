---
name: "rar-kody-w-buzzsaw"
description: "Set up a buzzsaw: an adversarial build-and-verify loop. Generates the seed prompt, the disjoint region split for parallel builders, the harsh critic brief, and an acceptance-gate skeleton. Actions: seed, critic, plan, gate, rules."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/buzzsaw", "rar_sha256": "68ffa820bc89cd8966f9929725bd9befd616ac26ad26867b828dc790b9cf13bb", "source_kind": "rar-agent", "source_commit": "ae1d6143f70e0182abd968e9c1c80ead38750484", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "buzzsaw_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/buzzsaw:d3d8eee224c2ef7a0252edd49ca4a8fa5fdec86d9aff6eceb7ad4b946da5ae68", "kind": "skill"}, "author": "Kody Wildfeuer", "tags": ["buzzsaw", "verification", "adversarial", "testing", "determinism", "ark"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/buzzsaw`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `buzzsaw_agent.py` is
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
