---
name: "rar-howardh-tuftelove"
description: "UI design advisor for brainstem agents. Combines Edward Tufte's visual design principles, Microsoft's Agent Oversight Design Taxonomy (32+ patterns), and 8 academic papers on human-agent interaction. Use action=review to get structured feedback on UI output, action=guide for deep dives on specific design topics, action=patterns to see all 32+ oversight patterns, action=checklist for a tailored review checklist, action=principles for the 10 core design principles, action=tufte for Edward Tufte's principles applied to agent UI."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/tuftelove_agent", "rar_sha256": "f5bba7ff967f166255b5220496ae7e86cb5f636730cb01a43abbf32113ebd46d", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "Howard Hoy", "tags": ["ui", "design", "tufte", "oversight", "ux", "review", "accessibility", "data-visualization"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `tuftelove_agent.py` and embedded as the fenced Python below (sha256 f5bba7ff967f1662…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `tuftelove_agent.py` first:

```bash
python3 tuftelove_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 tuftelove_agent.py   # or on stdin
python3 tuftelove_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
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
