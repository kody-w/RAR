---
name: "rar-wildhaven-bellows"
description: "Builds a paste-ready self-critique 'doubledown' prompt for ten escalating ideas, persisting a local kill log so each loop learns from the last."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@wildhaven/bellows_agent", "rar_sha256": "b80d52b3ed24ff6b50e1be11b08117c7581b0b6563f7a4ad01738963c901bc00", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.1.1", "author": "Wildhaven of America", "tags": ["bellows", "doubledown", "self-judge", "creative", "loop", "daemon", "construct", "show-off-the-power"]}
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
