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
