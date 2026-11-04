---
name: "rar-rapp-pitch-deck"
description: "Generates a polished HTML executive pitch deck from a topic and thesis. Output: a single self-contained HTML file with exec/rehearse modes, light/dark theme, and keyboard+swipe navigation. Tone is collaborative and respectful \u2014 frames the pitch as a contribution that complements existing work, never as a fix for someone else's mistake. Use this when the user asks to build/create/generate a pitch deck, slide deck, executive brief presentation, or playbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/pitch_deck_agent", "rar_sha256": "515d8cf7589e9ddfb4dd4a0575245f08e87b02a86837385df5b5c926f5958d1e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.2", "author": "RAPP / AIBAST", "tags": ["pitch", "deck", "slides", "narrative", "html", "executive"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pitch_deck_agent.py` and embedded as the fenced Python below (sha256 515d8cf7589e9ddf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pitch_deck_agent.py` first:

```bash
python3 pitch_deck_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 pitch_deck_agent.py   # or on stdin
python3 pitch_deck_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@rapp/pitch_deck_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/pitch_deck_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@rapp/pitch_deck_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
