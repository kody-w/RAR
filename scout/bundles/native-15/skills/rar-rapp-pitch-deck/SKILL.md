---
name: "rar-rapp-pitch-deck"
description: "Generates a polished HTML executive pitch deck from a topic and thesis. Output: a single self-contained HTML file with exec/rehearse modes, light/dark theme, and keyboard+swipe navigation. Tone is collaborative and respectful \u2014 frames the pitch as a contribution that complements existing work, never as a fix for someone else's mistake. Use this when the user asks to build/create/generate a pitch deck, slide deck, executive brief presentation, or playbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/pitch_deck_agent", "rar_sha256": "515d8cf7589e9ddfb4dd4a0575245f08e87b02a86837385df5b5c926f5958d1e", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.2", "author": "RAPP / AIBAST", "tags": ["pitch", "deck", "slides", "narrative", "html", "executive"]}
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
