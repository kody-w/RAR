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
    "name": "@borg/tuftelove_agent",
    "version": "1.0.0",
    "display_name": "TufteLove",
    "description": "UI design advisor combining Edward Tufte's visual principles, Microsoft Aether Agent Oversight Taxonomy (32+ patterns), and 8 academic papers — shapes how agents create UI and reviews existing UI for design quality.",
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