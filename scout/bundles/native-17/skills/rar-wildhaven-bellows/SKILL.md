---
name: "rar-wildhaven-bellows"
description: "Builds a paste-ready self-critique 'doubledown' prompt for ten escalating ideas, persisting a local kill log so each loop learns from the last."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@wildhaven/bellows_agent", "rar_sha256": "b80d52b3ed24ff6b50e1be11b08117c7581b0b6563f7a4ad01738963c901bc00", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.1.1", "author": "Wildhaven of America", "tags": ["bellows", "doubledown", "self-judge", "creative", "loop", "daemon", "construct", "show-off-the-power"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bellows_agent.py` and embedded as the fenced Python below (sha256 b80d52b3ed24ff6b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bellows_agent.py` first:

```bash
python3 bellows_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bellows_agent.py   # or on stdin
python3 bellows_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@wildhaven/bellows_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/bellows_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@wildhaven/bellows_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
