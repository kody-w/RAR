---
name: "rar-howardh-tuftelove"
description: "UI design advisor for brainstem agents. Combines Edward Tufte's visual design principles, Microsoft's Agent Oversight Design Taxonomy (32+ patterns), and 8 academic papers on human-agent interaction. Use action=review to get structured feedback on UI output, action=guide for deep dives on specific design topics, action=patterns to see all 32+ oversight patterns, action=checklist for a tailored review checklist, action=principles for the 10 core design principles, action=tufte for Edward Tufte's principles applied to agent UI."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/tuftelove_agent", "rar_sha256": "fe047c604edf53eac949ec02837dac4c6b32cba0db69d3d99119dbc3e50caf14", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Howard Hoy", "tags": ["ui", "design", "tufte", "oversight", "ux", "review", "accessibility", "data-visualization"]}
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
