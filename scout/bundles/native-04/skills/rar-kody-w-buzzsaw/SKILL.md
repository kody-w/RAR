---
name: "rar-kody-w-buzzsaw"
description: "Set up a buzzsaw: an adversarial build-and-verify loop. Generates the seed prompt, the disjoint region split for parallel builders, the harsh critic brief, and an acceptance-gate skeleton. Actions: seed, critic, plan, gate, rules."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/buzzsaw", "rar_sha256": "b14a4f23984fbc61acc1bde61ae592e16e8732ba287a78134d71361130011663", "source_kind": "rar-agent", "source_commit": "working-tree", "author": "Kody Wildfeuer", "tags": ["buzzsaw", "verification", "adversarial", "testing", "determinism", "ark"]}
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
