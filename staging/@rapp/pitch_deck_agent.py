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
    "description": "Generates a polished HTML executive pitch deck from a topic and thesis. Output: a single self-contained HTML file with exec/rehearse modes, light/dark theme, keyboard/swipe nav.",
    "author": "RAPP / AIBAST",
    "version": "1.0.0",
    "tags": ["pitch", "deck", "slides", "narrative", "html", "executive"],
    "category": "productivity",
    "quality_tier": "community",
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