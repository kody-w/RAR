---
name: "rar-wildhaven-bellows"
description: "Builds a paste-ready self-critique 'doubledown' prompt for ten escalating ideas, persisting a local kill log so each loop learns from the last."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@wildhaven/bellows_agent", "rar_sha256": "70aca84f711e97ddfc78ac555e826b60332ce5eae25bc90e85c7d8f42dddc608", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bellows_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@wildhaven/bellows:84ce546eeddd950dc88ec1e3f2870980c46f997b652d0a22882661e6be38fbab", "kind": "skill"}, "version": "1.1.1", "author": "Wildhaven of America", "tags": ["bellows", "doubledown", "self-judge", "creative", "loop", "daemon", "construct", "show-off-the-power"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@wildhaven/bellows_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bellows_agent.py` is
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
