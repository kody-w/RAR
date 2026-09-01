---
name: "rar-rapp-pitch-deck"
description: "Generates a polished HTML executive pitch deck from a topic and thesis. Output: a single self-contained HTML file with exec/rehearse modes, light/dark theme, and keyboard+swipe navigation. Tone is collaborative and respectful \u2014 frames the pitch as a contribution that complements existing work, never as a fix for someone else's mistake. Use this when the user asks to build/create/generate a pitch deck, slide deck, executive brief presentation, or playbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/pitch_deck_agent", "rar_sha256": "ca3c2f325342769f9d799ccb0fc0cd41a23f90d2e6ddfb1dcb7c79d7bdd78145", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.2", "author": "RAPP / AIBAST", "tags": ["pitch", "deck", "slides", "narrative", "html", "executive"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/pitch_deck_agent`. The original RAPP
agent is preserved byte-for-byte in `pitch_deck_agent.py` and in the RCI capsule.

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
