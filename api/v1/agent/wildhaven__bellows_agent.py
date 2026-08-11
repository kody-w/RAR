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
    "version": "1.1.0",
    "display_name": "Bellows",
    "description": (
        "Summoning this card asks: 'What are the absolute coolest, most "
        "mind-blowing, out of the box prompts that will really show off "
        "the power? Give me 10.' Then it runs the doubledown loop — "
        "generate, self-critique against a tangibility rubric, kill the "
        "weak, surface only survivors. Pass a topic to escalate something "
        "else. Each loop sharpens itself with the previous loop's kills."
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
