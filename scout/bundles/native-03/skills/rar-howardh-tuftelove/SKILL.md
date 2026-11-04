---
name: "rar-howardh-tuftelove"
description: "UI design advisor for brainstem agents. Combines Edward Tufte's visual design principles, Microsoft's Agent Oversight Design Taxonomy (32+ patterns), and 8 academic papers on human-agent interaction. Use action=review to get structured feedback on UI output, action=guide for deep dives on specific design topics, action=patterns to see all 32+ oversight patterns, action=checklist for a tailored review checklist, action=principles for the 10 core design principles, action=tufte for Edward Tufte's principles applied to agent UI."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/tuftelove_agent", "rar_sha256": "fe047c604edf53eac949ec02837dac4c6b32cba0db69d3d99119dbc3e50caf14", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "Howard Hoy", "tags": ["ui", "design", "tufte", "oversight", "ux", "review", "accessibility", "data-visualization"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@howardh/tuftelove_agent`. The original RAPP
agent is preserved byte-for-byte in `tuftelove_agent.py` and in the RCI capsule.

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

TufteLove — "Every pixel should earn its place." — Made by HOLO

UI design advisor for brainstem agents. Combines Edward Tufte's visual design
principles, Microsoft Aether Central Team's Agent Oversight Design Taxonomy
(32+ patterns), and 8 academic papers on human-agent interaction into a single
agent that shapes how all other agents create UI.

Provides always-on design awareness via system_context() plus on-demand
deep dives into patterns, checklists, and reviews.

## 5 Usage Examples

1. "Review my dashboard HTML for design issues"
   → TufteLove action=review, source="./deliverables/my-dashboard.html"
   → Structured feedback: data-ink violations, missing oversight patterns, Tufte improvements

2. "How should I design approval flows for a financial agent?"
   → TufteLove action=guide, topic="approval flows"
   → Deep dive: Before 3.2 plan review, During 2.1 approval requests, risk patterns

3. "What does Tufte say about designing data-heavy agent dashboards?"
   → TufteLove action=tufte
   → Small multiples, sparklines, micro/macro readings, layering for agent UIs

4. "Give me a UI checklist for a high-risk medical agent"
   → TufteLove action=checklist, topic="high-risk medical agent"
   → Tailored checklist: mandatory approval gates, audit trails, undo/reversal

5. "Show me all the oversight patterns I should consider"
   → TufteLove action=patterns
   → 32+ patterns organized by Before/During/After with descriptions

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "review = analyze UI against all frameworks; guide = deep dive on a topic (set topic); patterns = list all 32+ oversight patterns; checklist = tailored UI review checklist (set topic for context); principles = 10 core design principles with sources; tufte = Tufte's visual design principles for agent UI",
      "enum": [
        "review",
        "guide",
        "patterns",
        "checklist",
        "principles",
        "tufte"
      ],
      "type": "string"
    },
    "source": {
      "description": "For review: file path to the UI file to analyze.",
      "type": "string"
    },
    "topic": {
      "description": "For guide: design topic (e.g. 'approval flows', 'monitoring', 'error recovery'). For checklist: use case description (e.g. 'high-risk financial agent'). For review: file path to HTML/code to review, or description of the UI.",
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `tuftelove_agent.py` and embedded as the fenced Python below (sha256 fe047c604edf53ea…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `tuftelove_agent.py` first:

```bash
python3 tuftelove_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 tuftelove_agent.py   # or on stdin
python3 tuftelove_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@howardh/tuftelove_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/tuftelove_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@howardh/tuftelove_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
TufteLove — "Every pixel should earn its place." — Made by HOLO

UI design advisor for brainstem agents. Combines Edward Tufte's visual design
principles, Microsoft Aether Central Team's Agent Oversight Design Taxonomy
(32+ patterns), and 8 academic papers on human-agent interaction into a single
agent that shapes how all other agents create UI.

Provides always-on design awareness via system_context() plus on-demand
deep dives into patterns, checklists, and reviews.

## 5 Usage Examples

1. "Review my dashboard HTML for design issues"
   → TufteLove action=review, source="./deliverables/my-dashboard.html"
   → Structured feedback: data-ink violations, missing oversight patterns, Tufte improvements

2. "How should I design approval flows for a financial agent?"
   → TufteLove action=guide, topic="approval flows"
   → Deep dive: Before 3.2 plan review, During 2.1 approval requests, risk patterns

3. "What does Tufte say about designing data-heavy agent dashboards?"
   → TufteLove action=tufte
   → Small multiples, sparklines, micro/macro readings, layering for agent UIs

4. "Give me a UI checklist for a high-risk medical agent"
   → TufteLove action=checklist, topic="high-risk medical agent"
   → Tailored checklist: mandatory approval gates, audit trails, undo/reversal

5. "Show me all the oversight patterns I should consider"
   → TufteLove action=patterns
   → 32+ patterns organized by Before/During/After with descriptions
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@howardh/tuftelove_agent",
    "version": "1.0.1",
    "display_name": "TufteLove",
    "description": "Advises on and reviews agent UI design using Tufte principles and Microsoft's Agent Oversight pattern taxonomy.",
    "author": "Howard Hoy",
    "tags": ["ui", "design", "tufte", "oversight", "ux", "review", "accessibility", "data-visualization"],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

import os
import re

try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    from basic_agent import BasicAgent


# ═══════════════════════════════════════════════════════════════
# EMBEDDED KNOWLEDGE — Tufte + Aether Taxonomy + Paper Insights
# ═══════════════════════════════════════════════════════════════

_TUFTE_PRINCIPLES = """## Edward Tufte's Principles for Agent UI — Made by HOLO

### 1. Data-Ink Ratio
Maximize the share of "ink" (pixels) dedicated to actual data/content. Remove every
border, shadow, gradient, background, and decoration that doesn't directly convey
information. In agent UIs: status indicators should be data, not decoration.

### 2. Chartjunk Elimination
No ornamental icons, 3D effects, or visual noise. Every element must earn its pixels.
In agent UIs: avoid decorative loading animations, gratuitous emoji walls, or styled
containers that add visual weight without meaning.

### 3. Small Multiples
Show series of similar charts/panels with consistent scale and layout for instant
comparison. In agent UIs: use card grids for multi-agent status, consistent layouts
for step-by-step plan views, or repeated panels for A/B comparisons.

### 4. Sparklines
"Data-intense, design-simple, word-sized graphics." Inline trend indicators that
convey history without taking space. In agent UIs: embed tiny progress bars, trend
arrows, or mini-charts next to KPIs and status fields.

### 5. Micro/Macro Readings
Users should see both fine details AND the big picture simultaneously. Don't force
a choice between overview and detail. In agent UIs: show summary + expandable detail
in the same view; use progressive disclosure but keep context visible.

### 6. Layering & Separation
Use color, spacing, opacity, and whitespace to organize visual hierarchy without
physical borders. In agent UIs: distinguish active/completed/pending states through
color intensity, not heavy outlines. Push secondary info to lighter visual weight.

### 7. Escape from Flatland
Encode multiple dimensions without literal 3D: use position, color, size, shape.
In agent UIs: a single status card can show state (color), progress (bar width),
risk (icon), and timing (position) simultaneously.

### 8. Graphical Integrity
Represent data honestly and proportionally. No misleading scales, truncated axes,
or cherry-picked ranges. In agent UIs: progress bars must reflect actual progress,
confidence scores must be calibrated, time estimates must be honest.

### 9. Narrative Evidence
UI should tell a coherent story guiding the user through data exploration or task
completion. Sequence matters. In agent UIs: structure output as a narrative flow —
what was done → what was found → what needs attention → what's next.

### 10. Data Density
Don't fear dense information if well-organized. Users can process more than assumed.
In agent UIs: don't over-simplify dashboards to 3 metrics when users need 20 —
organize them well instead. Use small multiples and layering to pack information
without clutter.
"""

_OVERSIGHT_PATTERNS = {
    "before": [
        ("1.1", "Communicate capabilities", "Show what the agent can do: function controls, example demos, capability maps"),
        ("1.2", "Communicate limitations", "Show what it cannot do: action boundaries, ethical limits, dependency limitations"),
        ("2.1", "User configures general settings", "Risk tolerance, notification preferences, privacy/data controls, output format preferences"),
        ("2.2", "User configures task-specific settings", "Autonomy level (in-loop/on-loop/out-of-loop), allowed/forbidden actions, time/scope limits, monitoring detail"),
        ("3.1", "Clarify user goals", "Intent disambiguation, deliverable specification, constraint identification, priority setting"),
        ("3.2", "Create a plan", "Step-by-step plan review, alternative approaches, trade-off analysis, dependency mapping"),
        ("3.3", "Test the plan", "Dry run/sandbox mode, result preview, what-if scenarios, edge case exploration"),
        ("3.4", "Understand risk level", "Reversibility status, action type classification, impact scope, external dependencies"),
    ],
    "during": [
        ("1.1", "Show actions and reasoning", "Live execution steps, resource usage, decision explanations, timing/progress, co-created artifacts, kanban/mind-map views"),
        ("1.2", "Alert user", "Risk warnings, state change notifications, milestone updates, error alerts"),
        ("2.1", "Agent asks for help", "Approval at critical points, missing info requests, verification prompts, handoff to user, low-confidence situations"),
        ("2.2", "User takes control", "Pause/resume, stop/cancel, step back, manual override, adjust parameters mid-flight, add constraints"),
    ],
    "after": [
        ("1.1", "Provide action summary", "What was done and why, time/cost breakdown, resource consumption, efficiency stats"),
        ("1.2", "Evaluate outcome", "Goal achievement check, completeness assessment, quality validation, side effect detection, environment changes"),
        ("2.1", "Failure analysis", "Root cause identification, contributing factors, error pattern detection"),
        ("2.2", "Undo/reverse actions", "Low-risk (simple undo), medium-risk (time-limited), high-risk (irreversible with traces)"),
        ("2.3", "Recovery actions", "Compensating tasks, dispute/correction processes, escalation paths"),
        ("3.1", "Request user feedback", "Satisfaction rating, outcome evaluation, preference capture, improvement suggestions"),
        ("3.2", "Update preferences", "User-editable learnings, rule management, reset options, graduated permissions, trust building"),
        ("3.3", "Agent learns", "Saved task templates, work style patterns, new rules from feedback"),
    ],
}

_PAPER_INSIGHTS = """## Academic Foundations — Made by HOLO

### Bansal et al. 2024 — Communication Challenges
12 challenges (A1-A5 agent→user, U1-U3 user→agent, X1-X4 cross-cutting).
Key: Make plans, permissions, progress, and outcomes legible — not just chatty.

### Mozannar et al. 2025 — Magentic-UI
6 mechanisms: co-planning, co-tasking, action guards, verification, memory, multi-tasking.
Key: Build for low-cost interruption and recovery; make control continuous, not one-shot.

### Dibia et al. 2024 — AutoGen Studio
Composable primitives, trace views, reusable templates, session comparison.
Key: Recommend composable UI patterns and inspection/debugging views.

### Methnani et al. 2021 — Variable Autonomy
Meaningful human control via accountability, responsibility, transparency.
Key: Let users DIAL autonomy up/down by task/risk — not binary approve/deny.

### Sterz et al. 2024 — Effective Oversight
Effectiveness = causal power + epistemic access + self-control + fitting intentions.
Key: If the user can't meaningfully intervene, the oversight UI is performative.

### Verhagen et al. 2024 — Traceability
Traceability is the key measurable construct for meaningful human control.
Key: Pair live telemetry with post-hoc explainability and reason capture.

### Reinmund et al. 2024 — Autonomy State Machine
Variable autonomy needs governed transitions, not ad-hoc switching.
Key: Treat autonomy as a state machine with explicit modes and transition rules.

### Nyholm 2024 — Meaningful Control
Control is multi-dimensional and context-dependent.
Key: Recommend control only where it affects safety, accountability, or user values.
"""


class TufteLoveAgent(BasicAgent):
    """TufteLove — 'Every pixel should earn its place.' — Made by HOLO"""

    def __init__(self):
        self.name = "TufteLove"
        self.metadata = {
            "name": self.name,
            "description": (
                "UI design advisor for brainstem agents. Combines Edward Tufte's "
                "visual design principles, Microsoft's Agent Oversight Design Taxonomy "
                "(32+ patterns), and 8 academic papers on human-agent interaction. "
                "Use action=review to get structured feedback on UI output, "
                "action=guide for deep dives on specific design topics, "
                "action=patterns to see all 32+ oversight patterns, "
                "action=checklist for a tailored review checklist, "
                "action=principles for the 10 core design principles, "
                "action=tufte for Edward Tufte's principles applied to agent UI."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["review", "guide", "patterns", "checklist", "principles", "tufte"],
                        "description": (
                            "review = analyze UI against all frameworks; "
                            "guide = deep dive on a topic (set topic); "
                            "patterns = list all 32+ oversight patterns; "
                            "checklist = tailored UI review checklist (set topic for context); "
                            "principles = 10 core design principles with sources; "
                            "tufte = Tufte's visual design principles for agent UI"
                        ),
                    },
                    "topic": {
                        "type": "string",
                        "description": (
                            "For guide: design topic (e.g. 'approval flows', 'monitoring', 'error recovery'). "
                            "For checklist: use case description (e.g. 'high-risk financial agent'). "
                            "For review: file path to HTML/code to review, or description of the UI."
                        ),
                    },
                    "source": {
                        "type": "string",
                        "description": "For review: file path to the UI file to analyze.",
                    },
                },
                "required": ["action"],
            },
        }
        super().__init__()

    # ------------------------------------------------------------------
    # system_context — injected into EVERY conversation turn
    # ------------------------------------------------------------------
    def system_context(self):
        return (
            "<TufteLove — Every pixel should earn its place. — Made by HOLO>\n"
            "When generating ANY UI (HTML, dashboards, reports, interactive pages), apply these principles:\n"
            "1. DATA-INK RATIO (Tufte): Maximize meaningful content, remove decorative noise\n"
            "2. PROGRESSIVE DISCLOSURE (Aether): Start simple, reveal complexity as needed\n"
            "3. MICRO/MACRO READINGS (Tufte): Show detail AND big picture simultaneously\n"
            "4. TRANSPARENT BOUNDARIES (Aether): Always clear what agent can/cannot do\n"
            "5. VARIABLE AUTONOMY (Methnani): Let users dial control up/down by risk\n"
            "6. EFFECTIVE OVERSIGHT (Sterz): If user can't meaningfully intervene, the UI is performative\n"
            "7. LAYERING & SEPARATION (Tufte): Organize with color, spacing, opacity — not borders\n"
            "8. USER EMPOWERMENT (Aether): Observable, interruptible, reversible\n"
            "9. SMALL MULTIPLES (Tufte): Consistent layouts for comparison\n"
            "10. TRACEABILITY (Verhagen): Pair live telemetry with post-hoc explainability\n"
            "Call TufteLove action=review to get detailed feedback on any UI output.\n"
            "</TufteLove>"
        )

    # ------------------------------------------------------------------
    # perform — action dispatcher
    # ------------------------------------------------------------------
    def perform(self, action="principles", topic="", source="", **kwargs):
        dispatch = {
            "review": self._action_review,
            "guide": self._action_guide,
            "patterns": self._action_patterns,
            "checklist": self._action_checklist,
            "principles": self._action_principles,
            "tufte": self._action_tufte,
        }
        handler = dispatch.get(action, self._action_principles)
        return handler(topic=topic, source=source)

    # ------------------------------------------------------------------
    # Action: review
    # ------------------------------------------------------------------
    def _action_review(self, topic="", source="", **kwargs):
        source_path = source or topic
        if not source_path:
            return (
                "## TufteLove — UI Review\n\n"
                "Please provide a file path or description of the UI to review.\n\n"
                "**Examples:**\n"
                "- `source=./deliverables/my-dashboard.html`\n"
                "- `topic=a monitoring dashboard with 3 charts and a progress bar`\n\n"
                "I'll analyze it against Tufte's principles, the Aether oversight taxonomy, "
                "and academic best practices. — Made by HOLO"
            )

        # Try to read the file
        content = ""
        if len(source_path) < 500 and not source_path.startswith("<"):
            for candidate in [source_path, os.path.join(os.getcwd(), source_path)]:
                if os.path.isfile(candidate):
                    try:
                        with open(candidate, "r", encoding="utf-8", errors="replace") as f:
                            content = f.read(15000)
                    except OSError:
                        pass
                    break

        if not content:
            content = source_path  # treat as description

        return (
            "## TufteLove — UI Review — Made by HOLO\n\n"
            "I've read the UI content. Here is my structured review framework.\n"
            "Apply each section to the content below and provide specific feedback.\n\n"
            "### Tufte Lens\n"
            "- **Data-Ink Ratio**: What decorative elements can be removed? Are there borders, shadows, or backgrounds that add no meaning?\n"
            "- **Chartjunk**: Any ornamental icons, 3D effects, or visual noise?\n"
            "- **Small Multiples**: Could any repeated data be shown as consistent side-by-side panels?\n"
            "- **Micro/Macro**: Can users see both detail and big picture? Or is it one or the other?\n"
            "- **Layering**: Is visual hierarchy achieved through color/opacity/spacing, or through heavy borders/containers?\n"
            "- **Graphical Integrity**: Are progress bars, scores, and metrics honestly proportional?\n"
            "- **Data Density**: Is the UI over-simplified or appropriately dense?\n\n"
            "### Oversight Lens (Aether Taxonomy)\n"
            "- **Before**: Does the UI communicate capabilities and limitations? Can users set preferences?\n"
            "- **During**: Is there real-time monitoring? Can users pause/stop/intervene? Are alerts clear?\n"
            "- **After**: Is there an action summary? Can users undo? Is there a feedback mechanism?\n\n"
            "### Academic Lens\n"
            "- **Variable Autonomy** (Methnani): Can users dial control up/down, or is it binary?\n"
            "- **Effective Oversight** (Sterz): Can the user actually intervene meaningfully?\n"
            "- **Communication Legibility** (Bansal): Are plans, permissions, progress, outcomes readable?\n"
            "- **Traceability** (Verhagen): Can users trace what happened and why?\n\n"
            "### UI Content to Review\n"
            f"```\n{content[:8000]}\n```\n\n"
            "Provide specific, actionable feedback for each lens above. "
            "Cite the principle being violated and suggest a concrete fix."
        )

    # ------------------------------------------------------------------
    # Action: guide
    # ------------------------------------------------------------------
    def _action_guide(self, topic="", **kwargs):
        if not topic:
            return (
                "## TufteLove — Design Guide — Made by HOLO\n\n"
                "What topic do you need guidance on? Examples:\n\n"
                "- `topic=approval flows` — how to design approval/confirmation UI\n"
                "- `topic=monitoring dashboards` — real-time agent monitoring\n"
                "- `topic=error recovery` — failure analysis and undo patterns\n"
                "- `topic=onboarding` — first-run experience and capability communication\n"
                "- `topic=autonomy levels` — variable autonomy controls\n"
                "- `topic=progress indicators` — showing agent activity\n"
                "- `topic=data dense displays` — Tufte-style information-rich layouts\n"
            )

        topic_lower = topic.lower()

        # Find matching patterns
        matches = []
        for phase, patterns in _OVERSIGHT_PATTERNS.items():
            for num, name, desc in patterns:
                if any(word in name.lower() or word in desc.lower() for word in topic_lower.split()):
                    matches.append((phase.upper(), num, name, desc))

        # Find matching Tufte principles
        tufte_lines = _TUFTE_PRINCIPLES.split("### ")
        tufte_matches = []
        for section in tufte_lines:
            if any(word in section.lower() for word in topic_lower.split()):
                tufte_matches.append(section.strip())

        result = f"## TufteLove — Guide: {topic} — Made by HOLO\n\n"

        if matches:
            result += "### Relevant Oversight Patterns\n\n"
            for phase, num, name, desc in matches:
                result += f"**{phase} {num} — {name}**\n{desc}\n\n"

        if tufte_matches:
            result += "### Relevant Tufte Principles\n\n"
            for t in tufte_matches[:3]:
                result += f"{t}\n\n"

        # Always include paper insights
        result += "### Academic Foundations\n\n"
        paper_lines = _PAPER_INSIGHTS.split("### ")
        for section in paper_lines:
            if any(word in section.lower() for word in topic_lower.split()):
                result += f"### {section.strip()}\n\n"

        if not matches and not tufte_matches:
            result += (
                f"No exact pattern match for '{topic}', but here's how to approach it:\n\n"
                "1. **Tufte**: What data does the user need? Show that first. Remove everything else.\n"
                "2. **Aether**: Which execution phase? Before (setup), During (monitoring), After (review)?\n"
                "3. **Papers**: What's the risk level? Higher risk → more oversight, more user control.\n\n"
                "Try a more specific topic like 'approval flows', 'error handling', or 'progress display'."
            )

        return result

    # ------------------------------------------------------------------
    # Action: patterns
    # ------------------------------------------------------------------
    def _action_patterns(self, **kwargs):
        lines = ["## TufteLove — All Oversight Patterns — Made by HOLO\n"]

        phase_labels = {
            "before": "🔵 BEFORE EXECUTION — Planning Phase",
            "during": "🟡 DURING EXECUTION — Real-Time Oversight",
            "after": "🟢 AFTER EXECUTION — Retrospective",
        }

        for phase_key in ["before", "during", "after"]:
            lines.append(f"\n### {phase_labels[phase_key]}\n")
            for num, name, desc in _OVERSIGHT_PATTERNS[phase_key]:
                lines.append(f"**{num} — {name}**\n{desc}\n")

        lines.append(
            "\n---\n"
            "*Source: Microsoft Aether Central Team Agent Oversight Design Taxonomy (Oct 2025)*\n"
            "*32+ patterns from 73 slides + 8 academic papers. — Made by HOLO*"
        )
        return "\n".join(lines)

    # ------------------------------------------------------------------
    # Action: checklist
    # ------------------------------------------------------------------
    def _action_checklist(self, topic="", **kwargs):
        context = topic or "general agent UI"

        return (
            f"## TufteLove — UI Review Checklist: {context} — Made by HOLO\n\n"
            "### 🎨 Tufte Visual Design\n"
            "- [ ] **Data-Ink Ratio**: Every visual element serves a purpose (no decorative borders/shadows)\n"
            "- [ ] **No Chartjunk**: No ornamental icons, 3D effects, or visual noise\n"
            "- [ ] **Small Multiples**: Repeated data shown in consistent side-by-side panels\n"
            "- [ ] **Sparklines**: Inline trends/progress where applicable\n"
            "- [ ] **Micro/Macro**: Users see detail AND big picture in the same view\n"
            "- [ ] **Layering**: Visual hierarchy via color/opacity/spacing, not heavy borders\n"
            "- [ ] **Graphical Integrity**: Progress bars, scores, metrics are honestly proportional\n"
            "- [ ] **Narrative Flow**: UI tells a coherent story (what → found → attention → next)\n\n"
            "### 🔵 Before Execution\n"
            "- [ ] Agent communicates what it CAN do (capabilities visible)\n"
            "- [ ] Agent communicates what it CANNOT do (limitations stated)\n"
            "- [ ] User can configure preferences and risk tolerance\n"
            "- [ ] User can set autonomy level (in-loop / on-loop / out-of-loop)\n"
            "- [ ] Goals are clarified collaboratively (not assumed)\n"
            "- [ ] Plan is shown before execution (reviewable, editable)\n"
            "- [ ] Risk level is communicated (reversibility, impact scope)\n"
            "- [ ] Sandbox/dry-run option available for high-risk actions\n\n"
            "### 🟡 During Execution\n"
            "- [ ] Real-time progress visible (what's happening and why)\n"
            "- [ ] Alerts for critical events (risk warnings, errors, milestones)\n"
            "- [ ] Approval gates at critical points (especially for high-risk actions)\n"
            "- [ ] User can PAUSE execution without losing state\n"
            "- [ ] User can STOP/CANCEL with graceful shutdown\n"
            "- [ ] User can take manual control (override + hand-back)\n"
            "- [ ] Parameters adjustable mid-flight (scope, speed, accuracy)\n\n"
            "### 🟢 After Execution\n"
            "- [ ] Action summary provided (what was done, time, cost)\n"
            "- [ ] Outcome evaluated against original goal\n"
            "- [ ] Side effects and environment changes listed\n"
            "- [ ] Full audit trail available (chronological log)\n"
            "- [ ] Undo/reversal options clear (with risk level indicators)\n"
            "- [ ] Recovery actions available for failures\n"
            "- [ ] Feedback mechanism present (satisfaction, improvements)\n"
            "- [ ] Preferences can be updated based on experience\n\n"
            "### 📚 Academic Requirements\n"
            "- [ ] **Variable Autonomy** (Methnani): Users can dial control up/down, not just binary\n"
            "- [ ] **Effective Oversight** (Sterz): User has causal power to change outcomes\n"
            "- [ ] **Legibility** (Bansal): Plans, permissions, progress, outcomes are readable\n"
            "- [ ] **Traceability** (Verhagen): Every decision can be traced and explained\n"
            "- [ ] **Composable** (Dibia): UI components are reusable across agents\n"
            "- [ ] **Continuous Control** (Mozannar): Control is always available, not one-shot\n\n"
            "---\n"
            f"*Checklist tailored for: {context}*\n"
            "*Higher-risk use cases should implement ALL items. Lower-risk can prioritize.*\n"
            "*— Made by HOLO*"
        )

    # ------------------------------------------------------------------
    # Action: principles
    # ------------------------------------------------------------------
    def _action_principles(self, **kwargs):
        return (
            "## TufteLove — 10 Core Design Principles — Made by HOLO\n\n"
            "These principles are injected into every conversation via system_context().\n"
            "They combine Tufte's visual design, Aether's oversight taxonomy, and academic research.\n\n"
            "### 1. Data-Ink Ratio *(Tufte)*\n"
            "Maximize meaningful content, minimize decoration. Every pixel must earn its place.\n\n"
            "### 2. Progressive Disclosure *(Aether Taxonomy)*\n"
            "Start simple, reveal complexity as needed. Don't overwhelm — layer information.\n\n"
            "### 3. Micro/Macro Readings *(Tufte)*\n"
            "Show detail AND big picture simultaneously. Don't force a choice between overview and detail.\n\n"
            "### 4. Transparent Boundaries *(Aether Taxonomy)*\n"
            "Always clear what the agent can and cannot do. 🟢 Can do 🟡 Needs approval 🔴 Cannot do.\n\n"
            "### 5. Variable Autonomy *(Methnani et al. 2021)*\n"
            "Let users dial control up/down by task and risk — not binary approve/deny.\n"
            "Three levels: human-in-the-loop, human-on-the-loop, human-out-of-the-loop.\n\n"
            "### 6. Effective Oversight *(Sterz et al. 2024)*\n"
            "If the user can't meaningfully intervene, the oversight UI is performative.\n"
            "Real oversight = causal power + epistemic access + self-control.\n\n"
            "### 7. Layering & Separation *(Tufte)*\n"
            "Organize visual hierarchy with color, spacing, opacity, whitespace — not borders.\n"
            "Push secondary info to lighter visual weight. No heavy containers.\n\n"
            "### 8. User Empowerment *(Aether Taxonomy)*\n"
            "Observable: user can see what's happening. Interruptible: user can pause/stop.\n"
            "Reversible: user can undo where possible.\n\n"
            "### 9. Small Multiples *(Tufte)*\n"
            "Consistent layouts for comparison. Card grids, step views, dashboard panels.\n"
            "Same scale, same axes, side by side.\n\n"
            "### 10. Traceability *(Verhagen et al. 2024)*\n"
            "Pair live telemetry with post-hoc explainability. Every decision traceable.\n"
            "Users must be able to answer: what happened, when, why, and can I reverse it?\n\n"
            "---\n"
            "*\"Every pixel should earn its place.\" — Made by HOLO*"
        )

    # ------------------------------------------------------------------
    # Action: tufte
    # ------------------------------------------------------------------
    def _action_tufte(self, **kwargs):
        return _TUFTE_PRINCIPLES + "\n---\n*\"Every pixel should earn its place.\" — Made by HOLO*"
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
