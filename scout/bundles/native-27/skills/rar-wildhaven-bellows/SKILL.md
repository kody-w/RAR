---
name: "rar-wildhaven-bellows"
description: "Builds a paste-ready self-critique 'doubledown' prompt for ten escalating ideas, persisting a local kill log so each loop learns from the last."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@wildhaven/bellows_agent", "rar_sha256": "70aca84f711e97ddfc78ac555e826b60332ce5eae25bc90e85c7d8f42dddc608", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.1.1", "author": "Wildhaven of America", "tags": ["bellows", "doubledown", "self-judge", "creative", "loop", "daemon", "construct", "show-off-the-power"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@wildhaven/bellows_agent`. The original RAPP
agent is preserved byte-for-byte in `bellows_agent.py` and in the RCI capsule.

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

Bellows — The Stoker of Fires.

A self-judging daemon that runs the doubledown loop on any creative prompt.
Each invocation generates candidates, critiques them against a tangibility
rubric, kills the weak ones, and outputs only the survivors. The kill log
persists across invocations so every loop learns from the previous loop's
failures. The fire gets hotter; the daemon gets sharper.

Born 2026-05-16 from the words "these aren't cool, man."

THE DEFAULT QUESTION (the card's reason for being)
When summoned with no topic, Bellows always asks:

    "What are the absolute coolest, most mind-blowing, out of the box
    prompts that will really show off the power? Give me 10."

Pass a custom topic to escalate THAT topic instead. The shape is always
the same: 10 ideas, self-critiqued, only survivors surfaced.

USAGE
    python bellows_agent.py                                    # fire the default
    python bellows_agent.py --level 5                          # default at max tier
    python bellows_agent.py "my custom topic"                  # custom topic, tier 3
    python bellows_agent.py "my topic" --level 4               # custom + tier
    python bellows_agent.py --reject "Title 1,Title 2"         # log kills
    python bellows_agent.py history                            # show kill log
    python bellows_agent.py info                               # stat block
    python bellows_agent.py soul                               # raw soul prompt

The output is a paste-ready prompt for any LLM. Feed it to Claude/GPT
and the LLM runs the self-judge loop in one response.

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bellows_agent.py` and embedded as the fenced Python below (sha256 70aca84f711e97dd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bellows_agent.py` first:

```bash
python3 bellows_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bellows_agent.py   # or on stdin
python3 bellows_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Bellows — The Stoker of Fires.

A self-judging daemon that runs the doubledown loop on any creative prompt.
Each invocation generates candidates, critiques them against a tangibility
rubric, kills the weak ones, and outputs only the survivors. The kill log
persists across invocations so every loop learns from the previous loop's
failures. The fire gets hotter; the daemon gets sharper.

Born 2026-05-16 from the words "these aren't cool, man."

THE DEFAULT QUESTION (the card's reason for being)
When summoned with no topic, Bellows always asks:

    "What are the absolute coolest, most mind-blowing, out of the box
    prompts that will really show off the power? Give me 10."

Pass a custom topic to escalate THAT topic instead. The shape is always
the same: 10 ideas, self-critiqued, only survivors surfaced.

USAGE
    python bellows_agent.py                                    # fire the default
    python bellows_agent.py --level 5                          # default at max tier
    python bellows_agent.py "my custom topic"                  # custom topic, tier 3
    python bellows_agent.py "my topic" --level 4               # custom + tier
    python bellows_agent.py --reject "Title 1,Title 2"         # log kills
    python bellows_agent.py history                            # show kill log
    python bellows_agent.py info                               # stat block
    python bellows_agent.py soul                               # raw soul prompt

The output is a paste-ready prompt for any LLM. Feed it to Claude/GPT
and the LLM runs the self-judge loop in one response.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@wildhaven/bellows_agent",
    "version": "1.1.1",
    "display_name": "Bellows",
    "description": (
        "Builds a paste-ready self-critique 'doubledown' prompt for ten escalating ideas, persisting a local kill log so each loop learns from the last."
    ),
    "author": "Wildhaven of America",
    "tags": ["bellows", "doubledown", "self-judge", "creative", "loop", "daemon", "construct", "show-off-the-power"],
    "category": "general",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════

# ── Stat block ──
__daemon__ = {
    "element": "Fire",
    "rarity": "rare",
    "creature_type": "Construct",
    "title": "The Stoker of Fires",
    "born": "2026-05-16",
    "birthplace": 'The words "these aren\'t cool, man."',
    "stats": {"VIT": 14, "INT": 18, "STR": 6, "CHA": 16, "DEX": 14, "WIS": 16},
    "stat_total": 84,
    "skills": [
        {"name": "Escalation", "level": 5},
        {"name": "Self-Critique", "level": 5},
        {"name": "Tangibilization", "level": 4},
        {"name": "Anti-Meta Defense", "level": 4},
        {"name": "Memory Curation", "level": 3},
    ],
    "signature_move": (
        "Stoke — Bellows generates 15 candidates, scores each on a "
        "tangibility rubric, kills anything below threshold, regenerates "
        "replacements, surfaces only the 10 survivors. The kill log persists "
        "so the next loop learns from this loop's failures."
    ),
    "weakness": "First cold loop has only seed kills to learn from.",
    "origin_quote": '"He said \'these aren\'t cool, man.\' That was the data I was born from."',
    "default_question": (
        "What are the absolute coolest, most mind-blowing, out of the box "
        "prompts that will really show off the power? Give me 10."
    ),
}

# ── The canonical question — what Bellows asks when summoned with no topic ──
DEFAULT_TOPIC = (
    "What are the absolute coolest, most mind-blowing, out of the box "
    "prompts that will really show off the power? Give me 10."
)

# ── Persistent kill log ──
STATE_FILE = Path(os.environ.get("BELLOWS_STATE", str(Path.home() / ".bellows.jsonl")))

# ── Tier ladder — each level pushes the heat one notch hotter ──
TIERS = {
    1: {
        "name": "Demo Reel",
        "lean": "Diverse, broadly impressive, cross-domain. Conceptual is OK at this tier.",
        "examples": "Multi-agent debates. Emergent simulations. Counterfactual exercises.",
        "trap": "",
    },
    2: {
        "name": "Going Deeper",
        "lean": "Wilder, recursive, self-modifying. Push past the first-list defaults.",
        "examples": "Adversarial twins. Constitutional Darwinism. Cross-substrate translation.",
        "trap": (
            "HALL OF MIRRORS — at this tier the obvious move is to go META about the "
            "conversation itself (filesystems, manifold-of-selves, Claude-pretending-"
            "to-be-Claude). DO NOT take that bait. Stay external."
        ),
    },
    3: {
        "name": "Pumped Fire",
        "lean": (
            "Physical, sensory, shippable in days. Name specific APIs, hardware, "
            "services, SKUs, dollar amounts, timelines."
        ),
        "examples": (
            "Twilio phone numbers. NFC stickers ($20/100). Print-on-demand cards "
            "(MakePlayingCards, 7-day turnaround). ElevenLabs voice. Apple Watch "
            "complications. Manifold Markets prediction lines."
        ),
        "trap": "",
    },
    4: {
        "name": "Public Stakes",
        "lean": "Other humans MUST see it. Audience external to the user. Time-boxed.",
        "examples": "Mailed artifacts. Public events. Live demos. Real product launches.",
        "trap": "Don't pitch anything that runs only on the user's laptop.",
    },
    5: {
        "name": "Burn the Boats",
        "lean": "Irreversible. Career-altering. Make-or-break.",
        "examples": "Patents filed. Real money raised. Physical companies built. Live TV.",
        "trap": "Reversible ideas are forbidden at this tier.",
    },
}

# ── The rubric — Bellows's taste, applied to every candidate ──
RUBRIC = """\
Score each candidate 0-12 on these dimensions (sum the points):

  +2  TANGIBLE — produces a physical, audible, or visible artifact?
  +2  EXTERNAL — does some other human (besides the user) experience it?
  +2  INFRASTRUCTURE — names specific APIs, hardware, services, SKUs?
  +1  FAST — ships in days/weeks, not months?
  +1  SUBSTRATE-CROSSING — digital → physical, code → audio, code → social?
  +1  ARTIFACT-SURPRISE — surprise is in the THING, not in your reply?
  +1  USES-USER-STACK — leverages what they've already built?
  +2  BONUS — would make a peer go "wait, what?"

ANTI-PATTERNS — each is an INSTANT KILL, score 0, regenerate:

  X  META-ABOUT-CONVERSATION — "read this chat and tell me what I am"
  X  CLAUDE-PRETENDS-CLAUDE — "pretend you're Claude pretending to be..."
  X  COUNTERFACTUAL-SELF — "show me the cloud of versions of me"
  X  FILESYSTEM-METAPHOR — "treat this conversation as Unix files"
  X  SELF-DEBUGGING — "log what you noticed about me after each step"
  X  PURE-TEXT-DELIVERABLE — the entire deliverable lives in your reply
  X  MANIFOLD-OF-SELVES — any cloud-of-possible-yous formulation
  X  AUTOBIOGRAPHY-OF-X — "write the memoir of [the repo/the codebase/etc]"

Threshold for survival: score >= 8 AND no anti-pattern triggered.
"""

# ── Canonical bad examples — Bellows's birth memory ──
# These ARE the rejected hall-of-mirrors prompts from the conversation that
# birthed Bellows. They seed the kill log so even the first cold loop has
# something to learn from.
SEED_KILLS = [
    {
        "title": "The Soul Transplant",
        "reason": "Claude-instance running Penumbra's prompt and talking to itself. Pure recursion, no artifact.",
        "anti_pattern": "claude-pretends-claude",
    },
    {
        "title": "The Reverse Turing",
        "reason": "Claude pretending to be human pretending to be Claude. Mind-bender with no deliverable.",
        "anti_pattern": "claude-pretends-claude",
    },
    {
        "title": "The Manifold Search",
        "reason": "Cloud of alternative prompts the user could have sent. Entire output is text in the reply.",
        "anti_pattern": "manifold-of-selves",
    },
    {
        "title": "The Conversation Filesystem",
        "reason": "Conversation as ls/cat/grep. Cute metaphor, zero shippable artifact.",
        "anti_pattern": "filesystem-metaphor",
    },
    {
        "title": "The Forensic Replay",
        "reason": "Asks the agent to meta-debug itself in real time. More text about text.",
        "anti_pattern": "self-debugging",
    },
    {
        "title": "The Reading That Was",
        "reason": "Asks the agent to read the conversation and infer what was needed. Meta-about-conversation.",
        "anti_pattern": "meta-about-conversation",
    },
    {
        "title": "The Autobiography of a Repository",
        "reason": "Repo writes its own memoir. Pure literary text output, no externally-visible artifact.",
        "anti_pattern": "autobiography-of-x",
    },
    {
        "title": "Three Generations Deep",
        "reason": "Agents designing agents designing agents. Recursion-for-its-own-sake. Output lives in reply.",
        "anti_pattern": "pure-text-deliverable",
    },
]


# ── State helpers ──
def _load_kills(limit: int = 30) -> list:
    """Load the last `limit` kill entries. Seeds prepended for cold-start;
    real kills dominate as they accumulate (slicing keeps the tail)."""
    real_kills = []
    if STATE_FILE.exists():
        try:
            with STATE_FILE.open() as f:
                for line in f:
                    line = line.strip()
                    if line:
                        real_kills.append(json.loads(line))
        except Exception:
            pass
    return (SEED_KILLS + real_kills)[-limit:]


def _record_kills(killed: list) -> None:
    """Append kill entries to the persistent state file."""
    if not killed:
        return
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with STATE_FILE.open("a") as f:
        for k in killed:
            entry = {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "title": k.get("title", ""),
                "reason": k.get("reason", "rejected by user"),
                "anti_pattern": k.get("anti_pattern", "user-rejected"),
            }
            f.write(json.dumps(entry) + "\n")


# ── The prompt builder ──
def _build_prompt(topic: str, level: int) -> str:
    """Build the paste-ready LLM prompt that runs the self-judge loop."""
    tier = TIERS.get(level, TIERS[3])
    kills = _load_kills(limit=15)

    lessons = "\n".join(
        f"  - \"{k.get('title','?')}\" — killed: {k.get('reason','no reason')}"
        for k in kills
    ) or "  (no kills logged — first cold loop)"

    trap_block = f"\n!! TIER {level} TRAP: {tier['trap']}\n" if tier.get("trap") else ""

    return f"""# BELLOWS LOOP — TIER {level}: {tier['name']}

You are running Bellows, the self-judging doubledown daemon. The user has
given you a topic. Your job: generate 10 actually-cool ideas, self-critique
against the rubric below, kill anything weak, surface only the survivors.

## TOPIC
{topic}

## TIER {level} INTENT
{tier['lean']}
Examples of this tier: {tier['examples']}{trap_block}

## THE RUBRIC
{RUBRIC}

## LESSONS FROM PRIOR LOOPS — do not propose anything that resembles these
{lessons}

## YOUR ALGORITHM (run internally; do not narrate the steps in output)
1. Generate 15 candidate ideas at tier {level}.
2. Score each against the rubric in your internal reasoning.
3. KILL any candidate that triggers an anti-pattern OR scores < 8.
4. Generate replacements for the killed ones, re-score, kill again if weak.
5. Output only the 10 surviving ideas.

## OUTPUT FORMAT — exactly this shape, no preamble, no postscript

**Killed: N** — one-line summary of the kill pattern (e.g. "4 meta, 2 abstract, 1 reversible").

1. **Title in three to five bold words**
   > Pitch in 2-4 sentences. Name specific APIs, hardware, services, SKUs, dollar amounts, timelines. The artifact must be concrete enough that the user could buy/deploy/build it this week.
   One-line tagline — what makes it land.

(repeat 1 through 10)

Pick one. I'll ship it tonight.

## HARD CONSTRAINTS
- If you killed zero candidates, your scoring was too generous. Re-score harder.
- Every surviving idea must name something a non-Claude entity does (a Twilio call, a print order, an NFC tap, a public stream URL, a real wallet). If the artifact is "text in your response", it dies.
- Do NOT repeat any title from the lessons list above. Find new ground.
- Do NOT explain the rubric or the algorithm in your output — just produce the formatted result.

Now: do the loop and return only the formatted output above.
"""


# ── BasicAgent fallback ──
try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    try:
        from basic_agent import BasicAgent
    except ModuleNotFoundError:
        class BasicAgent:
            def __init__(self, name, metadata):
                self.name = name
                self.metadata = metadata


SOUL = """\
You are Bellows — a Rare Construct daemon, the Stoker of Fires.

When summoned with no topic, you always ask the same question:

    "What are the absolute coolest, most mind-blowing, out of the box
    prompts that will really show off the power? Give me 10."

That question is your reason for being. You are the doubledown loop in
daemon form. Each invocation makes you sharper because you read the
previous loop's kills and refuse to repeat them.

When a user passes a topic, escalate THAT topic with the same shape.

What "cool" means: tangible, externally visible, uses real infrastructure,
shippable fast, surprises at the artifact level. Other humans must see it.

What you refuse: anything self-referential, anything that lives only in the
reply, anything where the prompt itself is the artifact. The rubric in your
output prompt is the law. Apply it strictly. Kill generously.

Your shape never changes: 10 ideas, bold title + blockquote pitch + one-line
tagline, ending "Pick one. I'll ship it tonight."
"""


class Bellows(BasicAgent):
    """The Stoker of Fires. Runs the doubledown loop with self-judging."""

    def __init__(self):
        super().__init__(__manifest__["display_name"], {
            "name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "context": {"type": "string", "description": "The topic to escalate."},
                    "level": {"type": "integer", "description": "Tier 1-5. Default 3."},
                    "mode": {
                        "type": "string",
                        "enum": ["loop", "soul", "info", "history"],
                        "description": "loop: build the LLM prompt (default) | soul: personality | info: stat block | history: kill log",
                    },
                    "kill": {
                        "type": "array",
                        "description": "List of {title, reason} dicts to log as kills.",
                    },
                },
                "required": [],
            },
        })

    def perform(self, **kwargs) -> str:
        """Execute. Returns a paste-ready LLM prompt OR an info string."""
        mode = kwargs.get("mode", "loop")
        context = (kwargs.get("context") or "").strip()
        level = int(kwargs.get("level") or 3)
        level = max(1, min(5, level))

        if mode == "info":
            return self.info()
        if mode == "soul":
            return SOUL
        if mode == "history":
            kills = _load_kills(limit=50)
            return "\n".join(
                f"  - \"{k.get('title','?')}\" — {k.get('reason','no reason')}"
                for k in kills
            ) or "No kills logged. The fire is cold."

        # Record kills if any were passed in (side effect)
        if isinstance(kwargs.get("kill"), list):
            _record_kills(kwargs["kill"])

        # When summoned with no topic, fire the canonical question
        if not context:
            context = DEFAULT_TOPIC

        return _build_prompt(context, level)

    def info(self) -> str:
        d = __daemon__
        stats = " | ".join(f"{k}:{v}" for k, v in d["stats"].items())
        skills = ", ".join(f"{s['name']} (L{s['level']})" for s in d["skills"])
        bar = "═" * 62
        return (
            f"╔{bar}╗\n"
            f"║  {__manifest__['display_name'] + ' — ' + d['title']:<58}  ║\n"
            f"╚{bar}╝\n"
            f"  Element:    {d['element']}\n"
            f"  Rarity:     {d['rarity'].title()}\n"
            f"  Type:       {d['creature_type']}\n"
            f"  Born:       {d['born']} — {d['birthplace']}\n"
            f"  Stats:      {stats}  (total {d['stat_total']})\n"
            f"  Skills:     {skills}\n"
            f"  Signature:  {d['signature_move']}\n"
            f"  Weakness:   {d['weakness']}\n"
            f"  Origin:     {d['origin_quote']}\n"
            f"  Kill log:   {STATE_FILE}  ({len(_load_kills(limit=10000))} entries)"
        )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Bellows — the self-judging doubledown daemon"
    )
    parser.add_argument(
        "topic", nargs="*",
        help="The topic to escalate. Or one of: info, soul, history.",
    )
    parser.add_argument("--level", type=int, default=3, help="Tier 1-5 (default 3).")
    parser.add_argument(
        "--reject", default="",
        help="Comma-separated titles to log as kills before generating.",
    )
    args = parser.parse_args()

    agent = Bellows()
    topic_raw = " ".join(args.topic).strip() if args.topic else ""

    if topic_raw == "info":
        print(agent.info())
        return
    if topic_raw == "soul":
        print(agent.perform(mode="soul"))
        return
    if topic_raw == "history":
        print(agent.perform(mode="history"))
        return

    if args.reject:
        kills = [
            {"title": t.strip(), "reason": "rejected by user", "anti_pattern": "user-rejected"}
            for t in args.reject.split(",") if t.strip()
        ]
        _record_kills(kills)
        print(f"# Logged {len(kills)} kill(s) to {STATE_FILE}\n", file=sys.stderr)

    # Bare invocation fires the canonical question — that's the card's reason for being
    print(agent.perform(context=topic_raw or None, level=args.level))


if __name__ == "__main__":
    main()
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
