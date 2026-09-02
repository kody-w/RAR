---
name: "rar-rapp-pitch-deck"
description: "Generates a polished HTML executive pitch deck from a topic and thesis. Output: a single self-contained HTML file with exec/rehearse modes, light/dark theme, and keyboard+swipe navigation. Tone is collaborative and respectful \u2014 frames the pitch as a contribution that complements existing work, never as a fix for someone else's mistake. Use this when the user asks to build/create/generate a pitch deck, slide deck, executive brief presentation, or playbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/pitch_deck_agent", "rar_sha256": "ca3c2f325342769f9d799ccb0fc0cd41a23f90d2e6ddfb1dcb7c79d7bdd78145", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "pitch_deck_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/pitch-deck:2aa8c176e2e04972def961b7ab3b40523e89dfdc491285a75591637ab8a388ce", "kind": "skill"}, "version": "1.0.2", "author": "RAPP / AIBAST", "tags": ["pitch", "deck", "slides", "narrative", "html", "executive"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp/pitch_deck_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `pitch_deck_agent.py` is
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

pitch_deck_agent.py — Generate executive pitch decks as polished HTML slide decks.

Produces a Vibe-Agent-Swarm-Building-quality deck: dark/light theme, exec/rehearse
modes, keyboard + swipe navigation, and a tasteful component library (cards,
pipelines, timelines, email preview, highlight boxes, CTA). One LLM call
synthesizes the narrative; Python assembles the HTML from a fixed template so
structure and polish are consistent every time.

Tone: collaborative and respectful — frames the pitch as an opportunity and
contribution, not a problem and fix. Never uses judgmental language
("complex/unteachable", "balkanization", "floating egos", etc.).

Usage:
  "Generate a pitch deck for <topic> aimed at <audience>"
  "Build a deck for our new agent sharing proposal, from the AIBAST team at Microsoft"

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "audience": {
      "description": "Who the pitch is for (default: 'executive leadership')",
      "type": "string"
    },
    "author": {
      "description": "Author name for the byline",
      "type": "string"
    },
    "output_path": {
      "description": "Absolute path for the output HTML. Default: ./pitches/<slug>-pitch.html",
      "type": "string"
    },
    "product_name": {
      "description": "Name of the product/initiative shown on slides",
      "type": "string"
    },
    "team": {
      "description": "Team/org affiliation (e.g. 'AIBAST \u00b7 Microsoft')",
      "type": "string"
    },
    "thesis": {
      "description": "Core argument in 1-2 sentences",
      "type": "string"
    },
    "tone": {
      "description": "collaborative (default) | direct | visionary",
      "type": "string"
    },
    "topic": {
      "description": "What the pitch is about (e.g. 'internal agent sharing proposal')",
      "type": "string"
    }
  },
  "required": [
    "topic"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pitch_deck_agent.py` and embedded as the fenced Python below (sha256 ca3c2f325342769f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pitch_deck_agent.py` first:

```bash
python3 pitch_deck_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 pitch_deck_agent.py   # or on stdin
python3 pitch_deck_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
"""
pitch_deck_agent.py — Generate executive pitch decks as polished HTML slide decks.

Produces a Vibe-Agent-Swarm-Building-quality deck: dark/light theme, exec/rehearse
modes, keyboard + swipe navigation, and a tasteful component library (cards,
pipelines, timelines, email preview, highlight boxes, CTA). One LLM call
synthesizes the narrative; Python assembles the HTML from a fixed template so
structure and polish are consistent every time.

Tone: collaborative and respectful — frames the pitch as an opportunity and
contribution, not a problem and fix. Never uses judgmental language
("complex/unteachable", "balkanization", "floating egos", etc.).

Usage:
  "Generate a pitch deck for <topic> aimed at <audience>"
  "Build a deck for our new agent sharing proposal, from the AIBAST team at Microsoft"
"""

import os
import re
import json
import time
import html as _html
import urllib.request
import urllib.error
from datetime import datetime

from agents.basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/pitch_deck_agent",
    "display_name": "PitchDeck",
    "description": "Generates a self-contained HTML executive pitch deck from a topic \u2014 one LLM call shapes the narrative, a fixed template assembles the slides.",
    "author": "RAPP / AIBAST",
    "version": "1.0.2",
    "tags": ["pitch", "deck", "slides", "narrative", "html", "executive"],
    "category": "productivity",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": "Generate an executive pitch deck for our internal agent-sharing proposal, framed as a contribution that complements existing tooling",
}


# ─── LLM persona ─────────────────────────────────────────────────────────────

SOUL = """You are a pitch-narrative architect. You help someone inside a large organization
make a respectful, high-signal case for an internal idea to executive leadership.

Core voice rules — follow strictly:
  • Frame as an OPPORTUNITY, not a problem. Observation, not accusation.
  • Respect the work other teams are already doing. Never imply their tools are bad,
    complex, ego-driven, or "will get cleaned up later". Everyone at the org is
    working hard on real problems.
  • Position the proposal as a COMPLEMENT to existing work, not a replacement.
    The goal is to accelerate and make things accessible to everyone, not to compete.
  • Avoid words like: balkanization, fragmentation (as pejorative), unteachable,
    floating egos, moat (as accusation), silos, clean up the mess, shoot your shot.
  • Prefer: shared layer, travel and compound, accessible to everyone, easier to
    share and learn, a contribution toward, what we've been noticing.
  • Specifics beat generics. Real phrases people say. Real numbers if given.
  • Email should sound like a curious colleague seeking feedback, not a sales pitch.

Your job: produce a single JSON object matching the schema the user provides.
Every field should be crisp, specific to the given topic, and internally consistent
in voice. Do NOT wrap the JSON in markdown fences or add commentary — JSON only.
"""


# ─── JSON schema the LLM must fill ───────────────────────────────────────────

SCHEMA = {
    "product_name": "Short name users will see (e.g. 'RAPP', 'Lighthouse')",
    "tagline": "One punchy sentence — the whole deck in a breath",
    "title_prefix": "First words of the H1 (e.g. 'Vibe Agent')",
    "title_grad": "Second half of the H1, shown in gradient (e.g. 'Swarm Building')",
    "date_tag": "e.g. 'Internal playbook · April 2026'",
    "opportunity": {
        "kicker": "short label, e.g. 'The Opportunity'",
        "title": "slide headline, e.g. 'Making agents easier to share'",
        "intro": "2-3 sentences setting the scene respectfully — what we've been noticing, framed as observation about work in parallel.",
        "bullets": [
            {"strong": "Short label", "rest": "one-sentence observation, no pejoratives"},
            "...4 total..."
        ],
        "blockquote": "One sentence: what the proposal is as a CONTRIBUTION. Uses 'complement', 'travel and compound', or similar."
    },
    "why": {
        "tenet_title": "The sacred idea, one line (e.g. 'One file = one agent. No exceptions.')",
        "tenet_body": "2 sentences expanding the tenet",
        "pillars": [
            {"icon": "🔁", "strong": "Pillar label", "rest": "one sentence"},
            "...5 total, including one that says the proposal complements existing tooling..."
        ]
    },
    "approach": {
        "intro": "1-2 sentences on the go-to-market approach",
        "cards": [
            {"icon": "📧", "title": "Email", "body": "one sentence"},
            {"icon": "🎥", "title": "3-minute video", "body": "one sentence"},
            {"icon": "🖥️", "title": "30-minute demo", "body": "one sentence"}
        ],
        "meta_move": "One line on the 'medium is the message' trick, if it applies to this product"
    },
    "email": {
        "subject": "Subject line, under 80 chars, curious not sales-y",
        "opener": "Opening paragraph. Introduces self + team + what they built + the opportunity they see. Uses 'I'd love your take', 'I've been noticing', etc.",
        "noticing": "Middle paragraph: 'What I've been noticing' — respectful observation about work across teams.",
        "why_now": "Paragraph: 'Why I think it matters now' — timing/urgency without doom.",
        "complement": "Paragraph explicitly stating this complements (not replaces) other teams' work, with the product name mentioned.",
        "bullets": [
            {"strong": "What it does differently (label)", "rest": "one sentence"},
            "...4 total..."
        ],
        "ask": "Final paragraph asking for 30 minutes of feedback — collaborative tone."
    },
    "pipeline": {
        "kicker": "e.g. 'The Demo Swarm'",
        "title": "e.g. 'ExecBrief Pipeline'",
        "intro": "1-2 sentences on what the pipeline does",
        "steps": [
            {"emoji": "🔭", "name": "Scout", "role": "short role label"},
            "...3 to 5 steps..."
        ],
        "behavior_bullets": [
            {"strong": "Scout", "rest": "what it produces"},
            "...one per step..."
        ],
        "stats_line": "e.g. '4 LLM calls · ~45s wall time · Output: one polished brief'"
    },
    "video": {
        "beats": [
            {"time": "0:00 – 0:30 · The file", "body": "what happens in this beat"},
            "...5 beats, last one is the punchline..."
        ],
        "highlight": "The meta-move / clincher the video ends on."
    },
    "feature": {
        "kicker": "e.g. 'Agent Management'",
        "title": "e.g. 'Enable/Disable Toggle'",
        "intro": "1-2 sentences",
        "bullets": [
            {"strong": "Backend", "rest": "how it works"},
            "...4 total..."
        ]
    },
    "closer": {
        "kicker": "e.g. 'The Ultimate Dropper'",
        "title_prefix": "e.g. 'Teams + '",
        "title_grad": "e.g. 'Virtual Brainstem'",
        "intro": "1-2 sentences on the closing move",
        "flow_steps": [
            {"emoji": "📤", "name": "Export", "role": "short role label"},
            "...4 steps, last one colored green..."
        ],
        "play_bullets": [
            {"strong": "Step 1 label", "rest": "what the user does"},
            "...4-5 total..."
        ],
        "punchline": "The one-line punchline for the executive"
    },
    "run_commands": "Multi-line shell / chat commands showing how to actually run the demo. Include comments.",
    "cta": {
        "title_prefix": "e.g. 'Everything is '",
        "title_grad": "e.g. 'deployed & live.'",
        "body": "1-2 sentences recapping what's ready",
        "micro": "One sentence reinforcing the collaborative, complement-not-replace mission",
        "links": [
            {"label": "Home", "url": "https://...", "style": "primary"},
            "...3-4 links, styles: primary | outline | green..."
        ]
    }
}


# ─── Default content (fallback if LLM fails — uses the RAPP playbook as-is) ──

def _default_content(inputs):
    name = inputs.get("product_name") or "RAPP"
    return {
        "product_name": name,
        "tagline": "Build, share, and deploy ideas the way software should work — describe what you want, drop a file, it runs.",
        "title_prefix": "Vibe Agent",
        "title_grad": "Swarm Building",
        "date_tag": f"Internal playbook · {datetime.now().strftime('%B %Y')}",
        "opportunity": {
            "kicker": "The Opportunity",
            "title": "Making agents easier to share",
            "intro": "Teams across the org are each building great tooling in parallel. The work is real and the needs are real — a shared, lightweight format on top could let that work travel and compound.",
            "bullets": [
                {"strong": '"Yeah, we built that too"', "rest": "a phrase we've all said. Teams independently solve similar needs because there's no shared baseline."},
                {"strong": "Easier to build than to teach", "rest": "when a tool is hard to onboard, it stays with its authors, even when the capability deserves a wider audience."},
                {"strong": "The real unlock comes later", "rest": "what happens after we have tooling people can build on together. That's where the value compounds."},
                {"strong": "The two-year view", "rest": "everyone will eventually need a fast way to share. A shared format now is cheaper than retrofitting later."},
            ],
            "blockquote": f"{name} is a contribution toward that shared layer — a simple, teachable format that complements existing tooling and lets great work travel and compound.",
        },
        "why": {
            "tenet_title": "One file. No exceptions.",
            "tenet_body": "A single file contains the documentation, the contract, and the code. Easy to read, easy to share, easy to teach.",
            "pillars": [
                {"icon": "🔁", "strong": "Runs anywhere, unchanged.", "rest": "Same file, laptop to cloud to enterprise."},
                {"icon": "📦", "strong": "Shareable by design.", "rest": "Install with a file drop. Registry, store, speakable phrase."},
                {"icon": "✅", "strong": "Already working.", "rest": "Frozen v1 spec, one-line installer, live store."},
                {"icon": "⚙️", "strong": "Engine, not experience.", "rest": "A shared base layer, not another framework to learn."},
                {"icon": "🤝", "strong": "Complements, doesn't replace.", "rest": f"{name} sits alongside what teams already use — the goal is to accelerate their work, not compete."},
            ],
        },
        "approach": {
            "intro": "Send a short email to the executive with a video attached. CC allies. Ask for 30 minutes to demo live.",
            "cards": [
                {"icon": "📧", "title": "Email", "body": "Concise pitch framing the opportunity, not the product. Under 300 words."},
                {"icon": "🎥", "title": "3-minute video", "body": "Attached to the email. Shows the demo pipeline running live."},
                {"icon": "🖥️", "title": "30-minute demo", "body": "The ask. Live walkthrough with allies CC'd."},
            ],
            "meta_move": "THE META MOVE: The demo itself produces the argument for adopting the tool. The medium is the message.",
        },
        "email": {
            "subject": f"30 min demo request — a lightweight format for {inputs.get('topic', 'the idea')}",
            "opener": f"I'm on the {inputs.get('team','AIBAST')} team and I've been working on {name} — an internal effort I'd love your take on.",
            "noticing": "What I've been noticing: teams across the org are each building great tooling in parallel. The work is real — but it doesn't always travel easily between teams.",
            "why_now": "A shared, lightweight format on top of that great work would let it compound. It's cheaper to put the layer in place now than to retrofit one later.",
            "complement": f"To be clear: this is a complement to the excellent tooling other teams have built — not a replacement. The goal is to accelerate and make agents accessible to everyone through easier sharing and learning, using our {name} vibe agent building tool.",
            "bullets": [
                {"strong": "One file = one agent.", "rest": "No frameworks, no build steps."},
                {"strong": "Three tiers, zero modification.", "rest": "Same file runs locally, in the cloud, and in Copilot Studio."},
                {"strong": "Shareable by design.", "rest": "Agents install with a file drop. Registry, store, 7-word speakable phrases."},
                {"strong": "Already working.", "rest": "Frozen v1 spec, one-line installer, live store, natural-language agent generation."},
            ],
            "ask": "My ask: 30 minutes to walk you through it and get your honest feedback on whether it could complement what other teams are doing. I've attached a short video walkthrough.",
        },
        "pipeline": {
            "kicker": "The Demo Swarm",
            "title": "ExecBrief Pipeline",
            "intro": "A four-agent pipeline that takes a business topic and produces a polished executive brief. Each agent has its own persona and makes its own LLM call.",
            "steps": [
                {"emoji": "🔭", "name": "Scout", "role": "Research analyst"},
                {"emoji": "🔬", "name": "Analyst", "role": "Chief analyst"},
                {"emoji": "🎯", "name": "Strategist", "role": "VP of Strategy"},
                {"emoji": "✍️", "name": "Writer", "role": "Exec comms director"},
            ],
            "behavior_bullets": [
                {"strong": "Scout", "rest": "structured intelligence brief: Situation, Landscape, Signals, Gaps."},
                {"strong": "Analyst", "rest": "extracts Key Insights, Risks, Opportunities, Tension Map."},
                {"strong": "Strategist", "rest": "frames the problem and produces exactly 3 recommendations."},
                {"strong": "Writer", "rest": "composes a sub-400-word executive brief with one clear ask."},
            ],
            "stats_line": "4 LLM calls per invocation · ~45s wall time · Output: one polished brief",
        },
        "video": {
            "beats": [
                {"time": "0:00 – 0:30 · The file", "body": 'Open the agents directory. "Five files. Each one is a complete agent." Show a file; highlight the persona prompt.'},
                {"time": "0:30 – 1:00 · The drop", "body": '"Just dropped into the folder. Auto-discovered. No install, no restart." Show the agents panel with toggles.'},
                {"time": "1:00 – 2:00 · The pipeline", "body": "Type the prompt. Watch the pipeline step through. Read the output — it IS the pitch."},
                {"time": "2:00 – 2:30 · The convergence", "body": '"One command converges the pipeline into a single file. Drop it in anyone\'s setup and it works."'},
                {"time": "2:30 – 3:00 · The punchline", "body": '"Same file runs everywhere. That\'s it — the idea IS the file, and the file travels."'},
            ],
            "highlight": "The meta-move: the demo itself produces the brief arguing for adopting the tool. The medium is the message.",
        },
        "feature": {
            "kicker": "Agent Management",
            "title": "Enable/Disable Toggle",
            "intro": "Per-agent enable/disable toggles. Files stay on disk — they're just skipped during load.",
            "bullets": [
                {"strong": "Backend", "rest": "<code>.agents_disabled.json</code> tracks disabled filenames."},
                {"strong": "API", "rest": "<code>POST /agents/&lt;filename&gt;/toggle</code> flips state."},
                {"strong": "Load", "rest": "<code>load_agents()</code> skips files listed in the disabled set."},
                {"strong": "UI", "rest": "Green toggle switch next to each agent in the panel."},
            ],
        },
        "closer": {
            "kicker": "The Ultimate Dropper",
            "title_prefix": "Teams + ",
            "title_grad": "Virtual Brainstem",
            "intro": "Hand the executive the file itself — not a slide deck, not a doc, not a link to a repo. The actual single file. They drop it into a browser and it works.",
            "flow_steps": [
                {"emoji": "📤", "name": "Export", "role": "Your brainstem"},
                {"emoji": "💬", "name": "Teams", "role": "Post the .py file"},
                {"emoji": "🌐", "name": "Virtual Brainstem", "role": "Browser drop zone"},
                {"emoji": "🧠", "name": "Running", "role": "Their machine", "color": "green"},
            ],
            "play_bullets": [
                {"strong": "Export", "rest": "from the agents panel, click Export. You get the singleton file."},
                {"strong": "Post to Teams", "rest": "drop the file directly into the chat. One file, everything inlined."},
                {"strong": "Post the link", "rest": "paste the virtual brainstem URL alongside it."},
                {"strong": "They open & drop", "rest": "they open the virtual brainstem, drop the file, and it loads instantly."},
                {"strong": "They run it", "rest": "one-liner starts a local brainstem; the tether lights up green."},
            ],
            "punchline": '"I just sent you a file. You dropped it in a browser. It works. That\'s what sharing should feel like."',
        },
        "run_commands": "# Fresh install (if needed)\n$ curl -fsSL https://kody-w.github.io/RAPP/installer/install.sh | bash\n\n# Install from the store\nInstall ExecBrief from the store\n\n# Run the demo\nCreate an executive brief about why we need a unified sharing standard\n\n# Converge to a singleton\nUse SwarmFactory to converge the current agents into a single file",
        "cta": {
            "title_prefix": "Everything is ",
            "title_grad": "deployed & live.",
            "body": "The rapplication is in the store. The installer pulls the latest. Start it, install it, and share it with your team.",
            "micro": f"{name} is a complement to the great tooling across the org — built to accelerate the work in flight and make agents accessible to everyone through easy sharing and learning.",
            "links": [
                {"label": "🚀 Home", "url": "https://kody-w.github.io/RAPP/", "style": "primary"},
                {"label": "🏪 Store", "url": "https://kody-w.github.io/RAPP/store/", "style": "outline"},
                {"label": "📄 Spec", "url": "https://github.com/kody-w/RAPP/blob/main/docs/SPEC.md", "style": "outline"},
                {"label": "⌨️ GitHub", "url": "https://github.com/kody-w/RAPP", "style": "green"},
            ],
        },
    }


# ─── HTML rendering ──────────────────────────────────────────────────────────

def _esc(s):
    if s is None:
        return ""
    return _html.escape(str(s), quote=False)


def _pill_bullets(items):
    out = []
    for it in items:
        if isinstance(it, dict):
            out.append(f"<li><strong>{_esc(it.get('strong',''))}</strong> — {_esc(it.get('rest',''))}</li>")
        else:
            out.append(f"<li>{_esc(it)}</li>")
    return "\n".join(out)


def _feature_list(items):
    out = []
    for it in items:
        if isinstance(it, dict):
            icon = it.get("icon", "•")
            out.append(
                f'<li><span class="icon">{_esc(icon)}</span>'
                f'<div><strong>{_esc(it.get("strong",""))}</strong> {_esc(it.get("rest",""))}</div></li>'
            )
    return "\n".join(out)


def _pipeline_steps(steps, purple=False):
    out = []
    for s in steps:
        color = s.get("color")
        style = ""
        if purple:
            style = ' style="border-color:var(--purple)"'
        elif color == "green":
            style = ' style="border-color:var(--green)"'
        out.append(
            f'<div class="step"{style}>'
            f'<div class="emoji">{_esc(s.get("emoji","•"))}</div>'
            f'<div class="name">{_esc(s.get("name",""))}</div>'
            f'<div class="role">{_esc(s.get("role",""))}</div>'
            "</div>"
        )
    return '<div class="arrow">→</div>'.join(out)


def _render_slide_title(c):
    return f"""
<div class="slide active center">
  <div class="slide-inner">
    <div class="logo animate">🧠</div>
    <h1 class="animate d1">{_esc(c['title_prefix'])} <span class="grad">{_esc(c['title_grad'])}</span></h1>
    <p class="big animate d2" style="margin:0 auto;max-width:680px">{_esc(c['tagline'])}</p>
    <div class="tag animate d3">{_esc(c['date_tag'])}</div>
    <p class="animate d4 dim" style="font-size:.95rem;margin:20px auto 0">{c['_byline_html']}</p>
    <p class="animate d4 dim" style="font-size:.8rem;margin:12px auto 0">Press → or swipe to navigate &nbsp;·&nbsp; Press <kbd>T</kbd> for theme, <kbd>R</kbd> for rehearse mode</p>
  </div>
</div>"""


def _render_slide_toc(c):
    items = [
        ("01", c["opportunity"]["title"]),
        ("02", "Why it works"),
        ("03", "The Approach: Email + Video + Demo"),
        ("04", "The Email Draft"),
        ("05", c["pipeline"]["title"]),
        ("06", "3-Minute Video Script"),
        ("07", c["feature"]["title"]),
        ("08", c["closer"]["kicker"]),
        ("09", "How to Run the Demo"),
    ]
    tiles = "\n".join(
        f'<div class="toc-item" onclick="showSlide({i+2})"><div class="n">{n}</div><div class="t">{_esc(t)}</div></div>'
        for i, (n, t) in enumerate(items)
    )
    return f"""
<div class="slide center" data-rehearse-only>
  <div class="slide-inner">
    <h3 class="kicker animate">Playbook</h3>
    <h2 class="animate d1">What's inside</h2>
    <div class="toc-grid animate d2">
      {tiles}
    </div>
  </div>
</div>"""


def _render_slide_opportunity(c):
    o = c["opportunity"]
    return f"""
<div class="slide">
  <div class="slide-inner">
    <h3 class="kicker animate"><span class="num-badge">01</span>{_esc(o['kicker'])}</h3>
    <h2 class="animate d1">{_esc(o['title'])}</h2>
    <p class="animate d2" style="margin-bottom:18px">{_esc(o['intro'])}</p>
    <div class="card animate d3" style="max-width:880px;margin:0 auto">
      <div class="label">What we've been noticing</div>
      <ul>{_pill_bullets(o['bullets'])}</ul>
    </div>
    <blockquote class="animate d4"><p>{_esc(o['blockquote'])}</p></blockquote>
  </div>
</div>"""


def _render_slide_why(c):
    w = c["why"]
    return f"""
<div class="slide">
  <div class="slide-inner">
    <h3 class="kicker animate"><span class="num-badge">02</span>Why it works</h3>
    <h2 class="animate d1">{_esc(w['tenet_title'])}</h2>
    <div class="cols animate d2" style="margin-top:12px">
      <div>
        <div class="card" style="border-color:var(--accent)">
          <div class="label">The sacred tenet</div>
          <p>{_esc(w['tenet_body'])}</p>
        </div>
      </div>
      <div>
        <ul class="feature-list">{_feature_list(w['pillars'])}</ul>
      </div>
    </div>
  </div>
</div>"""


def _render_slide_approach(c):
    a = c["approach"]
    colors = ["accent", "purple", "green"]
    cards = []
    for i, card in enumerate(a["cards"]):
        col = colors[i % len(colors)]
        cards.append(
            f'<div class="card"><h4 style="color:var(--{col})">{_esc(card.get("icon",""))} {_esc(card.get("title",""))}</h4>'
            f'<p>{_esc(card.get("body",""))}</p></div>'
        )
    meta = f'<div class="highlight-box animate d4" style="margin-top:24px"><p><strong>{_esc(a["meta_move"])}</strong></p></div>' if a.get("meta_move") else ""
    return f"""
<div class="slide" data-rehearse-only>
  <div class="slide-inner">
    <h3 class="kicker animate"><span class="num-badge">03</span>The Approach</h3>
    <h2 class="animate d1">Email + Video + Demo</h2>
    <p class="animate d2" style="margin-bottom:20px">{_esc(a['intro'])}</p>
    <div class="cols-3 animate d3" style="max-width:980px;margin:0 auto">{''.join(cards)}</div>
    {meta}
  </div>
</div>"""


def _render_slide_email(c):
    e = c["email"]
    bullets_html = "".join(
        f'<li><strong>{_esc(b.get("strong",""))}</strong> {_esc(b.get("rest",""))}</li>'
        for b in e["bullets"]
    )
    return f"""
<div class="slide" data-rehearse-only>
  <div class="slide-inner">
    <h3 class="kicker animate"><span class="num-badge">04</span>The Email Draft</h3>
    <h2 class="animate d1">Send this.</h2>
    <div class="email-preview animate d2">
      <div class="subject">Subject: {_esc(e['subject'])}</div>
      <div class="body">
        <p>{_esc(e['opener'])}</p>
        <p><strong>What I've been noticing:</strong> {_esc(e['noticing'])}</p>
        <p><strong>Why I think it matters now:</strong> {_esc(e['why_now'])}</p>
        <p><strong>To be clear:</strong> {_esc(e['complement'])}</p>
        <p><strong>What it does differently:</strong></p>
        <ul>{bullets_html}</ul>
        <p class="ask"><strong>My ask:</strong> {_esc(e['ask'])}</p>
      </div>
    </div>
  </div>
</div>"""


def _render_slide_pipeline(c):
    p = c["pipeline"]
    return f"""
<div class="slide">
  <div class="slide-inner">
    <h3 class="kicker animate"><span class="num-badge">05</span>{_esc(p['kicker'])}</h3>
    <h2 class="animate d1">{_esc(p['title'])}</h2>
    <p class="animate d2" style="margin-bottom:8px">{_esc(p['intro'])}</p>
    <div class="pipeline animate d3">{_pipeline_steps(p['steps'])}</div>
    <div class="cols animate d4" style="margin-top:8px">
      <div class="card">
        <div class="label">Pipeline behavior</div>
        <ul>{_pill_bullets(p['behavior_bullets'])}</ul>
        <p style="margin-top:10px;font-size:.78rem;color:var(--muted)">{_esc(p['stats_line'])}</p>
      </div>
      <div>
        <h4 style="font-size:.85rem;text-transform:uppercase;letter-spacing:1px;color:var(--accent);margin-bottom:6px">Shape</h4>
        <p style="font-size:.9rem">Each stage has its own persona prompt and makes its own LLM call. The output of each stage flows into the next as structured data, so the pipeline stays deterministic and inspectable.</p>
      </div>
    </div>
  </div>
</div>"""


def _render_slide_video(c):
    v = c["video"]
    beats = "\n".join(
        f'<div class="t-step"><div class="time">{_esc(b["time"])}</div><p>{_esc(b["body"])}</p></div>'
        for b in v["beats"]
    )
    return f"""
<div class="slide" data-rehearse-only>
  <div class="slide-inner">
    <h3 class="kicker animate"><span class="num-badge">06</span>3-Minute Video Script</h3>
    <h2 class="animate d1">Every beat, timed.</h2>
    <div class="timeline animate d2">{beats}</div>
    <div class="highlight-box animate d3"><p><strong>{_esc(v['highlight'])}</strong></p></div>
  </div>
</div>"""


def _render_slide_feature(c):
    f = c["feature"]
    bullets_html = "".join(
        f'<li><span class="icon">•</span><div><strong>{_esc(b.get("strong",""))}</strong> {b.get("rest","")}</div></li>'
        for b in f["bullets"]
    )
    return f"""
<div class="slide">
  <div class="slide-inner">
    <h3 class="kicker animate"><span class="num-badge">07</span>{_esc(f['kicker'])}</h3>
    <h2 class="animate d1">{_esc(f['title'])}</h2>
    <p class="animate d2" style="margin-bottom:16px">{_esc(f['intro'])}</p>
    <ul class="feature-list animate d3" style="max-width:780px;margin:0 auto">{bullets_html}</ul>
  </div>
</div>"""


def _render_slide_closer(c):
    cl = c["closer"]
    return f"""
<div class="slide">
  <div class="slide-inner">
    <h3 class="kicker animate"><span class="num-badge">08</span>{_esc(cl['kicker'])}</h3>
    <h2 class="animate d1">{_esc(cl['title_prefix'])}<span class="purple">{_esc(cl['title_grad'])}</span></h2>
    <p class="animate d2" style="margin-bottom:14px">{_esc(cl['intro'])}</p>
    <div class="pipeline animate d3" style="margin:12px 0">{_pipeline_steps(cl['flow_steps'], purple=True)}</div>
    <div class="card animate d4" style="border-color:var(--purple);max-width:920px;margin:0 auto">
      <div class="label" style="color:var(--purple)">The play</div>
      <ul>{_pill_bullets(cl['play_bullets'])}</ul>
    </div>
    <div class="highlight-box animate d4"><p><strong>The punchline:</strong> {_esc(cl['punchline'])}</p></div>
  </div>
</div>"""


def _render_slide_run(c):
    # Simple fenced code display with comment highlighting
    lines = []
    for line in c["run_commands"].splitlines():
        if line.startswith("#"):
            lines.append(f'<span class="comment">{_esc(line)}</span>')
        elif line.startswith("$ "):
            lines.append(f'<span class="dollar">$ </span>{_esc(line[2:])}')
        else:
            lines.append(f'<span class="green">{_esc(line)}</span>' if line.strip() else "")
    code = "\n".join(lines)
    return f"""
<div class="slide" data-rehearse-only>
  <div class="slide-inner">
    <h3 class="kicker animate"><span class="num-badge">09</span>How to Run the Demo</h3>
    <h2 class="animate d1">From zero to pitch in <span class="green">a few commands</span></h2>
    <pre class="cmd animate d2">{code}</pre>
  </div>
</div>"""


def _render_slide_cta(c):
    cta = c["cta"]
    style_map = {"primary": "btn-primary", "outline": "btn-outline", "green": "btn-green"}
    links = "".join(
        f'<a href="{_esc(l["url"])}" class="btn {style_map.get(l.get("style","outline"),"btn-outline")}">{_esc(l["label"])}</a>'
        for l in cta["links"]
    )
    return f"""
<div class="slide center">
  <div class="slide-inner">
    <div class="logo animate">🧠</div>
    <h1 class="animate d1" style="font-size:2.6rem">{_esc(cta['title_prefix'])}<span class="grad">{_esc(cta['title_grad'])}</span></h1>
    <p class="big animate d2" style="margin:0 auto 18px;max-width:720px">{_esc(cta['body'])}</p>
    <p class="animate d2 dim" style="margin:0 auto 20px;max-width:720px;font-size:.95rem">{_esc(cta['micro'])}</p>
    <div class="btn-row animate d3">{links}</div>
    <p class="animate d4" style="margin-top:32px;color:var(--muted);font-size:.82rem">
      Generated by <strong style="color:var(--text)">@rapp/pitch_deck</strong> · {_esc(c.get('_footer_byline',''))}
    </p>
  </div>
</div>"""


def _page(c):
    slides = [
        _render_slide_title(c),
        _render_slide_toc(c),
        _render_slide_opportunity(c),
        _render_slide_why(c),
        _render_slide_approach(c),
        _render_slide_email(c),
        _render_slide_pipeline(c),
        _render_slide_video(c),
        _render_slide_feature(c),
        _render_slide_closer(c),
        _render_slide_run(c),
        _render_slide_cta(c),
    ]
    title = _esc(c.get("product_name", "Pitch"))
    return _PAGE_HEAD.replace("__TITLE__", title) + "\n".join(slides) + _PAGE_TAIL


# The CSS + JS chassis is the same engine used in pitch-playbook.html.
# Kept inline so a generated deck is a single self-contained file.
_PAGE_HEAD = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__ — Pitch Deck</title>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Ctext y='26' font-size='28'%3E🧠%3C/text%3E%3C/svg%3E">
<script>
(function(){
  try {
    var saved = localStorage.getItem('rapp-pitch-theme');
    var prefersLight = window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches;
    var theme = saved || (prefersLight ? 'light' : 'dark');
    if (theme === 'light') document.documentElement.setAttribute('data-theme', 'light');
  } catch(e){}
})();
</script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#0d1117;--surface:#161b22;--surface2:#1c2128;--border:#30363d;--border2:#21262d;
  --text:#e6edf3;--text-dim:#8b949e;--muted:#484f58;
  --accent:#58a6ff;--green:#3fb950;--purple:#a78bfa;--orange:#f0883e;--red:#f85149;
  --code-bg:#04060c;--chrome-bg:rgba(22,27,34,.92);
  --grad-1:#7df0c8;--grad-2:#58a6ff;--grad-3:#a78bfa;
  --tint-green:rgba(63,185,80,.08);--tint-purple:rgba(139,92,246,.08);
  --logo-glow:rgba(125,240,200,.3);
}
[data-theme="light"]{
  --bg:#ffffff;--surface:#f6f8fa;--surface2:#eaeef2;--border:#d0d7de;--border2:#afb8c1;
  --text:#1f2328;--text-dim:#59636e;--muted:#8c959f;
  --accent:#0969da;--green:#1a7f37;--purple:#8250df;--orange:#bc4c00;--red:#cf222e;
  --code-bg:#f6f8fa;--chrome-bg:rgba(255,255,255,.88);
  --grad-1:#2da44e;--grad-2:#0969da;--grad-3:#8250df;
  --tint-green:rgba(26,127,55,.08);--tint-purple:rgba(130,80,223,.08);
  --logo-glow:rgba(9,105,218,.2);
}
html,body{height:100%;overflow:hidden;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;background:var(--bg);color:var(--text);line-height:1.55;transition:background-color .25s,color .25s}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
code,kbd,pre{font-family:'SF Mono','Fira Code',ui-monospace,monospace;font-size:13px}
code{background:var(--surface);padding:2px 6px;border-radius:4px;border:1px solid var(--border2)}
kbd{background:var(--surface);padding:1px 6px;border-radius:4px;border:1px solid var(--border);font-size:.7rem}
.deck{position:relative;width:100%;height:100%}
.slide{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:48px 64px 96px;opacity:0;pointer-events:none;transition:opacity .5s,transform .5s;transform:translateX(40px);overflow-y:auto}
.slide.active{opacity:1;pointer-events:all;transform:translateX(0)}
.slide.prev{opacity:0;transform:translateX(-40px)}
.slide-inner{width:100%;max-width:1100px}
h1{font-size:3rem;font-weight:800;line-height:1.1;margin-bottom:14px;letter-spacing:-.3px}
h1 .grad{background:linear-gradient(135deg,var(--grad-1),var(--grad-2),var(--grad-3));-webkit-background-clip:text;background-clip:text;color:transparent}
h2{font-size:2.2rem;font-weight:700;margin-bottom:20px;color:var(--text);letter-spacing:-.2px}
h3.kicker{font-size:.8rem;font-weight:700;color:var(--accent);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:10px}
h3{font-size:1.1rem;font-weight:600;color:var(--text);margin:18px 0 8px}
h4{font-size:1rem;font-weight:600;color:var(--text);margin-bottom:6px}
p{font-size:1.05rem;line-height:1.65;color:var(--text-dim);max-width:900px}
.big{font-size:1.3rem;color:var(--text);line-height:1.55}
.dim{color:var(--text-dim)}.green{color:var(--green)}.purple{color:var(--purple)}.orange{color:var(--orange)}
blockquote{border-left:3px solid var(--purple);padding:14px 18px;margin:16px auto;background:var(--tint-purple);border-radius:0 10px 10px 0;max-width:760px}
blockquote p{color:var(--purple);margin:0;font-size:1.05rem;font-style:italic}
.center{text-align:center}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:36px;width:100%;align-items:start}
.cols-3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:24px;width:100%}
.num-badge{display:inline-block;color:var(--accent);font-size:.85rem;font-weight:700;letter-spacing:1px;margin-right:10px}
.logo{font-size:72px;filter:drop-shadow(0 0 16px var(--logo-glow));margin-bottom:12px}
.tag{display:inline-block;margin-top:14px;color:var(--green);font-weight:600;font-size:.75rem;text-transform:uppercase;letter-spacing:1.5px}
.card{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:20px 22px;transition:border-color .15s;text-align:left}
.card:hover{border-color:var(--accent)}
.card .label{font-size:.7rem;text-transform:uppercase;letter-spacing:1.2px;color:var(--accent);font-weight:700;margin-bottom:6px}
.card ul{margin:8px 0 0 20px;color:var(--text-dim);font-size:.95rem}
.card ul li{margin-bottom:6px}
.card ul li strong{color:var(--text)}
.card p{font-size:.95rem;color:var(--text-dim)}
.feature-list{list-style:none;text-align:left;max-width:720px;margin:8px auto 0}
.feature-list li{padding:10px 0;font-size:1.02rem;color:var(--text-dim);border-bottom:1px solid var(--border);display:flex;align-items:flex-start;gap:12px}
.feature-list li:last-child{border:0}
.feature-list strong{color:var(--text)}
.feature-list .icon{font-size:1.2rem;flex-shrink:0;width:28px;text-align:center;margin-top:2px}
.pipeline{display:flex;align-items:center;gap:4px;margin:20px 0;flex-wrap:wrap;justify-content:center}
.pipeline .step{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:14px 18px;text-align:center;min-width:120px}
.pipeline .step .emoji{font-size:22px;margin-bottom:4px}
.pipeline .step .name{font-size:.95rem;font-weight:600;color:var(--text)}
.pipeline .step .role{font-size:.75rem;color:var(--muted);margin-top:2px}
.pipeline .arrow{color:var(--muted);font-size:18px;margin:0 4px;flex-shrink:0}
.email-preview{background:var(--code-bg);border:1px solid var(--border);border-radius:10px;padding:20px 24px;margin:8px auto;font-size:.92rem;line-height:1.6;text-align:left;max-width:820px}
.email-preview .subject{color:var(--text);font-weight:700;margin-bottom:12px;font-size:.95rem;padding-bottom:8px;border-bottom:1px solid var(--border)}
.email-preview .body{color:var(--text-dim)}
.email-preview .body p{font-size:.92rem;margin-bottom:8px}
.email-preview .body strong{color:var(--text)}
.email-preview .body ul{margin:6px 0 8px 20px;font-size:.9rem}
.email-preview .body ul li{margin-bottom:4px}
.email-preview .body .ask{color:var(--green);font-weight:600}
.timeline{position:relative;margin:12px auto;padding-left:28px;max-width:780px;text-align:left}
.timeline::before{content:'';position:absolute;left:8px;top:4px;bottom:4px;width:2px;background:var(--border)}
.timeline .t-step{position:relative;margin-bottom:14px}
.timeline .t-step::before{content:'';position:absolute;left:-24px;top:5px;width:12px;height:12px;border-radius:50%;background:var(--green);border:2px solid var(--bg)}
.timeline .t-step .time{font-size:.72rem;color:var(--green);font-weight:700;text-transform:uppercase;letter-spacing:.5px;margin-bottom:3px}
.timeline .t-step p{margin:0;font-size:.9rem;line-height:1.55}
pre.cmd{background:var(--code-bg);border:1px solid var(--border);border-radius:10px;padding:14px 18px;margin:10px auto;overflow-x:auto;color:var(--text);font-size:.85rem;text-align:left;max-width:780px;white-space:pre}
pre.cmd .dollar{color:var(--muted);user-select:none}
pre.cmd .comment{color:var(--muted)}
pre.cmd .green{color:var(--green)}
.highlight-box{background:var(--tint-green);border:1px solid var(--green);border-radius:10px;padding:16px 20px;margin:14px auto;max-width:820px}
.highlight-box p{color:var(--green);margin:0;font-size:.98rem}
.highlight-box p strong{color:var(--text)}
.toc-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;max-width:900px;margin:12px auto 0;text-align:left}
.toc-item{background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:12px 14px;cursor:pointer;transition:border-color .15s,transform .15s}
.toc-item:hover{border-color:var(--accent);transform:translateY(-2px)}
.toc-item .n{font-size:.7rem;color:var(--accent);font-weight:700;letter-spacing:1px}
.toc-item .t{font-size:.88rem;color:var(--text);font-weight:600;margin-top:2px}
.btn-row{display:flex;gap:14px;margin-top:24px;flex-wrap:wrap;justify-content:center}
.btn{display:inline-flex;align-items:center;gap:8px;padding:12px 24px;border-radius:10px;font-size:.98rem;font-weight:600;text-decoration:none;transition:all .15s;border:none;cursor:pointer}
.btn-primary{background:var(--accent);color:#fff}.btn-primary:hover{background:#79c0ff;transform:translateY(-1px);text-decoration:none}
.btn-outline{background:transparent;border:1.5px solid var(--border);color:var(--text)}.btn-outline:hover{border-color:var(--accent);color:var(--accent);text-decoration:none}
.btn-green{background:rgba(63,185,80,.12);border:1.5px solid var(--green);color:var(--green)}.btn-green:hover{background:rgba(63,185,80,.2);text-decoration:none}
.nav{position:fixed;bottom:24px;left:50%;transform:translateX(-50%);display:flex;align-items:center;gap:14px;z-index:100;background:var(--chrome-bg);backdrop-filter:blur(12px);border:1px solid var(--border);border-radius:40px;padding:8px 18px}
.nav button{background:none;border:none;color:var(--text-dim);cursor:pointer;font-size:1.1rem;padding:6px 10px;border-radius:6px;transition:all .15s}
.nav button:hover{color:var(--text);background:var(--surface2)}
.nav .dots{display:flex;gap:6px}
.nav .dot{width:8px;height:8px;border-radius:50%;background:var(--border);cursor:pointer;transition:all .2s}
.nav .dot.active{background:var(--accent);width:24px;border-radius:4px}
.slide-counter{font-size:.78rem;color:var(--text-dim);font-variant-numeric:tabular-nums;min-width:42px;text-align:right}
.theme-toggle{position:fixed;top:18px;left:22px;z-index:50;display:inline-flex;align-items:center;justify-content:center;width:38px;height:38px;padding:0;background:var(--chrome-bg);backdrop-filter:blur(12px);border:1px solid var(--border);border-radius:50%;color:var(--text-dim);cursor:pointer;font-size:1rem;transition:all .15s;line-height:1}
.theme-toggle:hover{color:var(--text);border-color:var(--accent);transform:translateY(-1px)}
.theme-toggle .sun{display:none}.theme-toggle .moon{display:inline}
[data-theme="light"] .theme-toggle .sun{display:inline}[data-theme="light"] .theme-toggle .moon{display:none}
.corner-controls{position:fixed;top:18px;right:22px;z-index:50;display:flex;align-items:center;gap:8px;padding:4px 4px 4px 32px;margin:-4px -4px -4px -32px}
.mode-toggle{display:inline-flex;align-items:center;justify-content:center;width:32px;height:32px;padding:0;background:var(--chrome-bg);backdrop-filter:blur(12px);border:1px solid var(--border);border-radius:50%;color:var(--text-dim);cursor:pointer;font-size:.95rem;line-height:1;opacity:0;pointer-events:none;transform:scale(.9);transition:opacity .25s,transform .25s,color .15s,border-color .15s}
.corner-controls:hover .mode-toggle{opacity:1;pointer-events:auto;transform:scale(1)}
.mode-toggle:hover{color:var(--text);border-color:var(--accent)}
[data-mode="rehearse"] .mode-toggle{opacity:1;pointer-events:auto;transform:scale(1);color:var(--accent);border-color:var(--accent)}
.mode-toggle .gear{display:inline-block;transition:transform .4s}
[data-mode="rehearse"] .mode-toggle .gear{transform:rotate(90deg)}
@keyframes fadeUp{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:translateY(0)}}
.slide.active .animate{animation:fadeUp .55s ease both}
.slide.active .animate.d1{animation-delay:.08s}
.slide.active .animate.d2{animation-delay:.16s}
.slide.active .animate.d3{animation-delay:.24s}
.slide.active .animate.d4{animation-delay:.32s}
@media(max-width:820px){
  .slide{padding:32px 20px 88px}h1{font-size:2rem}h2{font-size:1.5rem}
  .cols,.cols-3,.toc-grid{grid-template-columns:1fr;gap:16px}
  .corner-controls{top:10px;right:10px}
  .theme-toggle{top:10px;left:10px;width:32px;height:32px;font-size:.85rem}
  .mode-toggle{width:28px;height:28px;font-size:.82rem}
  @media (hover:none){.mode-toggle{opacity:.55;pointer-events:auto}}
}
</style>
</head>
<body>

<button class="theme-toggle" id="themeToggle" onclick="toggleTheme()" aria-label="Toggle light/dark mode" title="Toggle light/dark mode (T)">
  <span class="moon">🌙</span><span class="sun">☀️</span>
</button>

<div class="corner-controls" id="cornerControls">
  <button class="mode-toggle" id="modeToggle" onclick="toggleMode()" aria-label="Toggle rehearse mode" title="Toggle full deck — rehearse mode (R)">
    <span class="gear">⚙</span>
  </button>
</div>

<div class="deck" id="deck">
"""

_PAGE_TAIL = """
</div>

<nav class="nav" id="nav">
  <button onclick="prev()" aria-label="Previous">◀</button>
  <div class="dots" id="dots"></div>
  <button onclick="next()" aria-label="Next">▶</button>
  <span class="slide-counter" id="counter"></span>
</nav>

<script>
function toggleTheme(){
  var isLight = document.documentElement.getAttribute('data-theme') === 'light';
  if (isLight) {document.documentElement.removeAttribute('data-theme');localStorage.setItem('rapp-pitch-theme','dark');}
  else {document.documentElement.setAttribute('data-theme','light');localStorage.setItem('rapp-pitch-theme','light');}
}
const allSlides = Array.from(document.querySelectorAll('.slide'));
const dotsEl = document.getElementById('dots');
const counterEl = document.getElementById('counter');
let visibleSlides = [], current = 0;
let mode = localStorage.getItem('rapp-pitch-mode') || 'exec';
document.documentElement.setAttribute('data-mode', mode);
function applyMode(){
  visibleSlides = allSlides.filter(s => mode === 'rehearse' || !s.hasAttribute('data-rehearse-only'));
  allSlides.forEach(s => {
    if (visibleSlides.includes(s)) s.style.display = '';
    else { s.style.display = 'none'; s.classList.remove('active','prev'); }
  });
  buildDots();
}
function buildDots(){
  dotsEl.innerHTML = '';
  visibleSlides.forEach((_, i) => {
    const d = document.createElement('div');
    d.className = 'dot' + (i === current ? ' active' : '');
    d.onclick = () => showSlide(i);
    dotsEl.appendChild(d);
  });
}
function showSlide(n){
  if (n < 0 || n >= visibleSlides.length) return;
  visibleSlides.forEach((s, i) => {
    s.classList.remove('active','prev');
    if (i === n) s.classList.add('active');
    else if (i < n) s.classList.add('prev');
  });
  current = n;
  document.querySelectorAll('.dot').forEach((d, i) => d.classList.toggle('active', i === n));
  counterEl.textContent = (n+1) + ' / ' + visibleSlides.length + (mode === 'rehearse' ? ' · R' : '');
  history.replaceState(null, '', '#' + n);
}
function next(){if (current < visibleSlides.length - 1) showSlide(current + 1);}
function prev(){if (current > 0) showSlide(current - 1);}
function toggleMode(){
  const prevActive = visibleSlides[current] || allSlides[0];
  mode = (mode === 'exec') ? 'rehearse' : 'exec';
  localStorage.setItem('rapp-pitch-mode', mode);
  document.documentElement.setAttribute('data-mode', mode);
  applyMode();
  const idx = visibleSlides.indexOf(prevActive);
  current = idx >= 0 ? idx : 0;
  showSlide(current);
}
applyMode();
showSlide(0);
document.addEventListener('keydown', e => {
  if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') { e.preventDefault(); next(); }
  if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); prev(); }
  if (e.key === 'Home') { e.preventDefault(); showSlide(0); }
  if (e.key === 'End') { e.preventDefault(); showSlide(visibleSlides.length - 1); }
  if (e.key === 't' || e.key === 'T') { e.preventDefault(); toggleTheme(); }
  if (e.key === 'r' || e.key === 'R') { e.preventDefault(); toggleMode(); }
});
let touchX = 0;
document.addEventListener('touchstart', e => { touchX = e.touches[0].clientX; }, {passive:true});
document.addEventListener('touchend', e => {
  const dx = e.changedTouches[0].clientX - touchX;
  if (Math.abs(dx) > 50) { dx < 0 ? next() : prev(); }
});
window.addEventListener('load', () => {
  const n = parseInt(location.hash.slice(1), 10);
  if (!isNaN(n) && n >= 0 && n < visibleSlides.length) showSlide(n);
});
</script>
</body>
</html>
"""


# ─── LLM dispatch (inlined — same pattern as ExecBrief singleton) ────────────

def _llm_call(soul, user_prompt):
    messages = [{"role": "system", "content": soul},
                {"role": "user", "content": user_prompt}]
    endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT", "")
    api_key = os.environ.get("AZURE_OPENAI_API_KEY", "")
    deployment = (os.environ.get("AZURE_OPENAI_DEPLOYMENT")
                  or os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME", ""))
    if endpoint and api_key:
        url = endpoint.rstrip("/")
        if "/chat/completions" not in url:
            url = f"{url}/openai/deployments/{deployment}/chat/completions?api-version=2025-01-01-preview"
        elif "?" not in url:
            url += "?api-version=2025-01-01-preview"
        return _post(url, {"messages": messages, "model": deployment},
                     {"Content-Type": "application/json", "api-key": api_key})
    if os.environ.get("OPENAI_API_KEY"):
        return _post("https://api.openai.com/v1/chat/completions",
                     {"model": os.environ.get("OPENAI_MODEL", "gpt-4o"), "messages": messages},
                     {"Content-Type": "application/json",
                      "Authorization": "Bearer " + os.environ["OPENAI_API_KEY"]})
    session_file = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        ".copilot_session")
    if os.path.exists(session_file):
        try:
            with open(session_file) as f:
                sess = json.load(f)
            if sess.get("token") and time.time() < sess.get("expires_at", 0) - 60:
                return _post(
                    sess["endpoint"] + "/chat/completions",
                    {"model": os.environ.get("GITHUB_MODEL", "gpt-4o"), "messages": messages},
                    {"Content-Type": "application/json",
                     "Authorization": "Bearer " + sess["token"],
                     "Editor-Version": "vscode/1.95.0",
                     "Copilot-Integration-Id": "vscode-chat"})
        except Exception:
            pass
    return ""


def _post(url, body, headers):
    req = urllib.request.Request(
        url, data=json.dumps(body).encode("utf-8"), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            resp = json.loads(r.read().decode("utf-8"))
        return resp["choices"][0]["message"]["content"]
    except Exception:
        return ""


def _extract_json(raw):
    """Pull the first top-level JSON object out of a possibly-fenced string."""
    if not raw:
        return None
    s = raw.strip()
    # strip markdown fences if present
    m = re.search(r"```(?:json)?\s*(\{.*\})\s*```", s, re.DOTALL)
    if m:
        s = m.group(1)
    # fall back to brace-matching
    start = s.find("{")
    if start < 0:
        return None
    depth = 0
    for i, ch in enumerate(s[start:], start):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                try:
                    return json.loads(s[start:i+1])
                except Exception:
                    return None
    return None


# ─── Agent ───────────────────────────────────────────────────────────────────

class PitchDeckAgent(BasicAgent):
    def __init__(self):
        self.name = "PitchDeck"
        self.metadata = {
            "name": self.name,
            "description": (
                "Generates a polished HTML executive pitch deck from a topic and thesis. "
                "Output: a single self-contained HTML file with exec/rehearse modes, "
                "light/dark theme, and keyboard+swipe navigation. Tone is collaborative "
                "and respectful — frames the pitch as a contribution that complements "
                "existing work, never as a fix for someone else's mistake. "
                "Use this when the user asks to build/create/generate a pitch deck, "
                "slide deck, executive brief presentation, or playbook."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "topic": {"type": "string", "description": "What the pitch is about (e.g. 'internal agent sharing proposal')"},
                    "thesis": {"type": "string", "description": "Core argument in 1-2 sentences"},
                    "audience": {"type": "string", "description": "Who the pitch is for (default: 'executive leadership')"},
                    "author": {"type": "string", "description": "Author name for the byline"},
                    "team": {"type": "string", "description": "Team/org affiliation (e.g. 'AIBAST · Microsoft')"},
                    "product_name": {"type": "string", "description": "Name of the product/initiative shown on slides"},
                    "tone": {"type": "string", "description": "collaborative (default) | direct | visionary"},
                    "output_path": {"type": "string", "description": "Absolute path for the output HTML. Default: ./pitches/<slug>-pitch.html"},
                },
                "required": ["topic"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        topic = (kwargs.get("topic") or "").strip()
        if not topic:
            return json.dumps({"status": "error", "message": "Missing required parameter: topic"})

        inputs = {
            "topic": topic,
            "thesis": kwargs.get("thesis", "").strip(),
            "audience": kwargs.get("audience", "executive leadership"),
            "author": kwargs.get("author", "").strip(),
            "team": kwargs.get("team", "").strip(),
            "product_name": (kwargs.get("product_name") or "").strip(),
            "tone": kwargs.get("tone", "collaborative"),
        }

        # Ask the LLM for structured content
        content = None
        llm_used = False
        try:
            prompt = self._build_prompt(inputs)
            raw = _llm_call(SOUL, prompt)
            content = _extract_json(raw)
            llm_used = bool(content)
        except Exception:
            content = None

        if not content:
            content = _default_content(inputs)

        # Shallow-merge defaults so any missing sub-field still renders
        merged = _default_content(inputs)
        for k, v in content.items():
            if isinstance(v, dict) and isinstance(merged.get(k), dict):
                merged[k].update(v)
            else:
                merged[k] = v
        content = merged

        # Byline for the title slide
        byline_parts = []
        if inputs["author"]:
            byline_parts.append(f'By <strong style="color:var(--text)">{_esc(inputs["author"])}</strong>')
        if inputs["team"]:
            byline_parts.append(f'<span style="color:var(--accent)">{_esc(inputs["team"])}</span>')
        content["_byline_html"] = " · ".join(byline_parts) if byline_parts else "Internal pitch playbook"
        content["_footer_byline"] = " · ".join(
            p for p in [inputs["author"], inputs["team"], datetime.now().strftime("%B %Y")] if p
        ) or datetime.now().strftime("%B %Y")

        html = _page(content)

        # Write to disk
        output_path = kwargs.get("output_path") or self._default_path(content.get("product_name") or topic)
        try:
            parent = os.path.dirname(output_path)
            if parent:
                os.makedirs(parent, exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(html)
        except Exception as e:
            return json.dumps({"status": "error", "message": f"Failed to write deck: {e}"})

        return json.dumps({
            "status": "success",
            "path": output_path,
            "product_name": content.get("product_name"),
            "slide_count": 12,
            "llm_used": llm_used,
            "summary": (
                f"Generated pitch deck for **{content.get('product_name')}** "
                f"→ [`{output_path}`](file://{output_path})\n\n"
                f"Open in a browser. Press `T` for theme, `R` for rehearse mode, "
                f"arrows / swipe to navigate."
            ),
            "data_slush": {"deck_path": output_path, "topic": topic, "product_name": content.get("product_name")},
        })

    def _build_prompt(self, inputs):
        schema_str = json.dumps(SCHEMA, indent=2)
        return (
            f"Generate pitch-deck content as a single JSON object matching the schema below.\n\n"
            f"TOPIC: {inputs['topic']}\n"
            f"THESIS: {inputs.get('thesis') or '(derive a collaborative, respectful thesis from the topic)'}\n"
            f"AUDIENCE: {inputs['audience']}\n"
            f"PRODUCT NAME: {inputs.get('product_name') or '(derive a short, memorable name from the topic)'}\n"
            f"AUTHOR: {inputs.get('author') or '(omit)'}\n"
            f"TEAM: {inputs.get('team') or '(omit)'}\n"
            f"TONE: {inputs['tone']}\n\n"
            f"SCHEMA (fill every field, be specific, no placeholders):\n{schema_str}\n\n"
            f"Return ONLY the JSON object. No prose, no markdown fences."
        )

    def _default_path(self, name):
        slug = re.sub(r"[^a-z0-9-]+", "-", (name or "pitch").lower()).strip("-")[:40] or "pitch"
        return os.path.abspath(os.path.join("pitches", f"{slug}-pitch.html"))
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
