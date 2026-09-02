---
name: "rar-howardh-tuftelove"
description: "UI design advisor for brainstem agents. Combines Edward Tufte's visual design principles, Microsoft's Agent Oversight Design Taxonomy (32+ patterns), and 8 academic papers on human-agent interaction. Use action=review to get structured feedback on UI output, action=guide for deep dives on specific design topics, action=patterns to see all 32+ oversight patterns, action=checklist for a tailored review checklist, action=principles for the 10 core design principles, action=tufte for Edward Tufte's principles applied to agent UI."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/tuftelove_agent", "rar_sha256": "f5bba7ff967f166255b5220496ae7e86cb5f636730cb01a43abbf32113ebd46d", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "tuftelove_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@howardh/tuftelove:53a27ba1944feb402e8d28652b77ba3624e2833c7411e805a05b6a9c2838fd23", "kind": "skill"}, "version": "1.0.1", "author": "Howard Hoy", "tags": ["ui", "design", "tufte", "oversight", "ux", "review", "accessibility", "data-visualization"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@howardh/tuftelove_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `tuftelove_agent.py` is
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
