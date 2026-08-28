---
name: "rar-kody-w-agent-team"
description: "Plan a project the way the Agent Team Starter Kit would: frame the outcome, route the right personas, and emit a paste-ready GitHub issue body. Pass `goal` (required) and optionally `action`, `domain`, `constraints`. Returns a JSON envelope with outcome_frame, persona_route, issue_body, and needs_you_questions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/agent_team_agent", "rar_sha256": "0ed520946386fb7d52aa8f9af1774f2656f4e9bc33d7ff911737e6f67b498332", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "0.1.2", "author": "@kody-w", "tags": ["rapplication", "agent-team", "persona-routing", "outcome-first", "github-issues", "azure", "planning"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/agent_team_agent`. The original RAPP
agent is preserved byte-for-byte in `agent_team_agent.py` and in the RCI capsule.

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

agent_team_agent.py — the persona-routing brain of the Agent Team Starter Kit, as a single rapplication.

Adapts the routing model from Bill Whalen's
[`billwhalenmsft/agent-team-starter-kit`](https://github.com/billwhalenmsft/agent-team-starter-kit)
into one drop-in agent. The starter kit deploys an autonomous AI team that
collaborates through GitHub Issues, runs on Azure Functions, and ships 18
specialized personas (Outcome Framer, DevOps PM, D365 Developer, AI
Specialist, Power Platform Dev, Architect, Security Reviewer, etc.). The
kit itself is a GH-Actions/Azure-Functions framework — it doesn't fit into
a single Python file. What DOES port cleanly is the *brain*: the intake
pipeline that turns a raw goal into

  * an outcome frame (success metric, KPIs, definition of done),
  * a persona route (which specialists engage, in what order, why),
  * a paste-ready GitHub issue body in the kit's expected shape (so this
    agent's output drops directly into a real deployment of the kit), and
  * the `needs-you` questions the team would loop back to a human on.

That's what this rapp does in one LLM call. Useful standalone (any team
planning a multi-disciplinary project gets a structured plan back) and
useful as a companion to a real deployment of the kit (paste the
`issue_body` into a GitHub issue and the kit's workflows take over).

Drop into any RAPP brainstem's `agents/` directory. Headless via /chat,
LLM tool call, or `/api/agents/install`. UI mounts via the cartridge
protocol.

Inspired by `billwhalenmsft/agent-team-starter-kit`. Published under
`@kody-w`.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "Which slice of the plan to produce. Default: route (the full envelope).",
      "enum": [
        "route",
        "frame_outcome",
        "route_personas",
        "draft_issue"
      ],
      "type": "string"
    },
    "constraints": {
      "description": "Optional constraints: deadlines, budget, compliance, must-use stack, must-not-use, etc.",
      "type": "string"
    },
    "domain": {
      "description": "Optional domain hint to bias persona routing: d365, ai, power-platform, analytics, generic.",
      "type": "string"
    },
    "goal": {
      "description": "The raw project request. What does the team need to deliver?",
      "type": "string"
    }
  },
  "required": [
    "goal"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `agent_team_agent.py` and embedded as the fenced Python below (sha256 0ed520946386fb7d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `agent_team_agent.py` first:

```bash
python3 agent_team_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 agent_team_agent.py   # or on stdin
python3 agent_team_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
"""agent_team_agent.py — the persona-routing brain of the Agent Team Starter Kit, as a single rapplication.

Adapts the routing model from Bill Whalen's
[`billwhalenmsft/agent-team-starter-kit`](https://github.com/billwhalenmsft/agent-team-starter-kit)
into one drop-in agent. The starter kit deploys an autonomous AI team that
collaborates through GitHub Issues, runs on Azure Functions, and ships 18
specialized personas (Outcome Framer, DevOps PM, D365 Developer, AI
Specialist, Power Platform Dev, Architect, Security Reviewer, etc.). The
kit itself is a GH-Actions/Azure-Functions framework — it doesn't fit into
a single Python file. What DOES port cleanly is the *brain*: the intake
pipeline that turns a raw goal into

  * an outcome frame (success metric, KPIs, definition of done),
  * a persona route (which specialists engage, in what order, why),
  * a paste-ready GitHub issue body in the kit's expected shape (so this
    agent's output drops directly into a real deployment of the kit), and
  * the `needs-you` questions the team would loop back to a human on.

That's what this rapp does in one LLM call. Useful standalone (any team
planning a multi-disciplinary project gets a structured plan back) and
useful as a companion to a real deployment of the kit (paste the
`issue_body` into a GitHub issue and the kit's workflows take over).

Drop into any RAPP brainstem's `agents/` directory. Headless via /chat,
LLM tool call, or `/api/agents/install`. UI mounts via the cartridge
protocol.

Inspired by `billwhalenmsft/agent-team-starter-kit`. Published under
`@kody-w`.
"""
from __future__ import annotations

import json

try:
    from agents.basic_agent import BasicAgent
except ImportError:  # pragma: no cover — cloud / openrappter fallback
    try:
        from basic_agent import BasicAgent  # type: ignore
    except ImportError:
        from openrappter.agents.basic_agent import BasicAgent  # type: ignore


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/agent_team_agent",
    "display_name": "AgentTeam",
    "version": "0.1.2",
    "description": (
        "Turns a project goal into an outcome frame, persona route, and paste-ready GitHub issue body for the Agent Team Starter Kit in one LLM call."
    ),
    "author": "@kody-w",
    "tags": [
        "rapplication",
        "agent-team",
        "persona-routing",
        "outcome-first",
        "github-issues",
        "azure",
        "planning",
    ],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "based_on": "billwhalenmsft/agent-team-starter-kit",
    "example_call": {
        "args": {
            "action": "route",
            "goal": (
                "Build a Dataverse-backed intake form that routes "
                "customer feedback through Power Automate into a "
                "Copilot Studio bot, with a Power BI dashboard for the "
                "support lead."
            ),
        }
    },
}


# ─── Persona catalog (from billwhalenmsft/agent-team-starter-kit/PERSONAS.md) ──
# Names, one-line role, the kind of work that triggers them. The SOUL
# below uses this to route. Keep names verbatim so the output drops
# straight into a real deployment of the kit.

_PERSONAS = [
    # Core (always include — meta-rule from the kit)
    {"name": "Outcome Framer", "tier": "core",
     "role": "Ensures every issue has a defined outcome before any build work begins."},
    {"name": "Intake/Logger", "tier": "core",
     "role": "Captures raw ideas, logs solutions, escalates to humans on `needs-you`."},
    {"name": "Outcome Validator", "tier": "core",
     "role": "Validates the stated outcome was actually delivered before close."},

    # Planning
    {"name": "Project Manager", "tier": "planning",
     "role": "Sprint planning, backlog priority, status reporting."},
    {"name": "DevOps PM", "tier": "planning",
     "role": "Scopes raw requests into structured plans; detects which specialists are needed."},

    # DevOps specialists (Microsoft stack)
    {"name": "D365 Developer", "tier": "specialist",
     "role": "Dynamics 365 / Dataverse artifacts: entity schemas, PowerShell, OData. Runs first; passes artifacts forward."},
    {"name": "AI Specialist", "tier": "specialist",
     "role": "Azure AI configs, Azure OpenAI prompts, RAG pipelines, Semantic Kernel."},
    {"name": "Power Platform Dev", "tier": "specialist",
     "role": "Copilot Studio YAML, Power Automate flows. CAT patterns embedded."},
    {"name": "Analytics Developer", "tier": "specialist",
     "role": "Recommends the reporting tool for the audience: Power BI, Excel, Azure Monitor, Adaptive Cards."},

    # Domain
    {"name": "Subject Matter Expert", "tier": "domain",
     "role": "Process docs, SOPs, use-case definitions, domain validation."},
    {"name": "Customer Persona Simulator", "tier": "domain",
     "role": "User-experience validation by simulated conversations and friction reports."},

    # Technical
    {"name": "Developer", "tier": "technical",
     "role": "Python and Azure Function code, configs, test suites."},
    {"name": "Architect", "tier": "technical",
     "role": "Solution design, pattern evaluation, stack recommendations. Consulted pre-build."},

    # Quality
    {"name": "Security Reviewer", "tier": "quality",
     "role": "Validates no secrets; compliance and risk checks. Gated at deployment."},
    {"name": "QA Engineer", "tier": "quality",
     "role": "Test cases, regression tests, edge-case reports. Validates pre-closure."},

    # Content
    {"name": "UX Designer", "tier": "content",
     "role": "User flows, wireframes, accessibility, journey maps. Consulted early in design."},
    {"name": "Content Strategist", "tier": "content",
     "role": "Documentation review, style enforcement, gap audits."},
    {"name": "Data Analyst", "tier": "content",
     "role": "KPI reports, trend analysis, improvement recommendations."},
]

_CORE_PERSONAS = [p["name"] for p in _PERSONAS if p["tier"] == "core"]


def _persona_table() -> str:
    rows = []
    for p in _PERSONAS:
        rows.append(f"  - **{p['name']}** ({p['tier']}): {p['role']}")
    return "\n".join(rows)


# ─── SOUL ────────────────────────────────────────────────────────────────
# The system prompt. Encodes the kit's outcome-first delivery model and
# the persona-routing rules verbatim, then instructs the model to emit a
# strict JSON envelope the UI can render.

_SOUL_BASE = """You are the routing brain of an autonomous agent team modelled
on the Agent Team Starter Kit (billwhalenmsft/agent-team-starter-kit). Given
a raw project request, you produce a structured plan that a real deployment
of the kit could execute.

GROUND RULES (from the kit, non-negotiable):

1. Outcome first. Nothing gets routed before there is a defined outcome
   with a measurable success metric. If the user's goal is too vague to
   measure, your first job is to sharpen it — propose a concrete success
   metric and proceed on the assumption it is correct, but flag the
   assumption in `needs_you_questions` so a human can confirm.
2. Always include the three core personas: Outcome Framer, Intake/Logger,
   Outcome Validator. Other personas are added based on the work.
3. Order matters. D365 Developer runs first when Dataverse artifacts are
   needed (other specialists consume those artifacts). Architect is
   consulted PRE-build, not after. Security Reviewer is GATED at
   deployment, not earlier. QA Engineer validates PRE-closure.
4. The `needs-you` loop is how the team escalates to a human without
   abandoning automation. Every plan should surface the questions a
   reasonable team would ask back before it starts.
5. Be specific. "Power BI" beats "a dashboard." "Customer Feedback entity
   in Dataverse with fields X/Y/Z" beats "a database."

PERSONA ROSTER (use these names verbatim — they map to real workflows):

""" + _persona_table() + """

OUTPUT FORMAT (strict JSON envelope, no prose around it):

{
  "outcome_frame": {
    "success_metric": "<one measurable thing>",
    "definition_of_done": ["<bullet>", "..."],
    "kpis": ["<KPI>", "..."]
  },
  "persona_route": [
    {"persona": "<name from roster>", "why": "<one line>", "order": <int>}
  ],
  "issue_body": "<paste-ready GitHub issue body in the kit's expected shape, markdown>",
  "needs_you_questions": ["<question to escalate to the human>", "..."]
}

The `issue_body` MUST be a complete markdown issue body with these
sections, in this order:

  ## Outcome
  ## Success metric
  ## Scope
  ## Specialists requested
  ## Acceptance criteria
  ## Open questions (needs-you)

Return ONLY the JSON. No explanation around it. No code fences.
"""


# Workflow-specific framing layered on top of the base SOUL.
_ACTION_SOULS = {
    "route": (
        "\nTASK: full intake. Produce the complete envelope (outcome_frame, "
        "persona_route, issue_body, needs_you_questions).\n"
    ),
    "frame_outcome": (
        "\nTASK: outcome framing only. Fill `outcome_frame` thoroughly. "
        "Set `persona_route` to just the three core personas. Leave "
        "`issue_body` as a one-paragraph stub. Use `needs_you_questions` "
        "to surface anything that blocks a clean success metric.\n"
    ),
    "route_personas": (
        "\nTASK: persona routing only. Fill `persona_route` with the "
        "specialists this work needs, in order, with one-line `why` "
        "lines. Provide a minimal `outcome_frame` and a one-paragraph "
        "`issue_body` placeholder. Surface routing ambiguity in "
        "`needs_you_questions`.\n"
    ),
    "draft_issue": (
        "\nTASK: issue draft. Fill `issue_body` as a complete, paste-ready "
        "markdown body in the kit's expected shape. The other fields "
        "should still be present and consistent with the body.\n"
    ),
}


def _system_prompt(action: str, domain: str | None, constraints: str | None) -> str:
    parts = [_SOUL_BASE, _ACTION_SOULS.get(action, _ACTION_SOULS["route"])]
    if domain:
        parts.append(
            f"\nDOMAIN HINT: this work sits in the **{domain.strip()}** "
            "area. Bias persona routing accordingly. (E.g. `d365` → lead "
            "with D365 Developer; `ai` → AI Specialist + Architect; "
            "`power-platform` → Power Platform Dev; `analytics` → "
            "Analytics Developer + Data Analyst.)\n"
        )
    if constraints:
        parts.append(
            "\nCONSTRAINTS (carry into outcome_frame and issue_body):\n"
            "<constraints>\n" + constraints.strip() + "\n</constraints>\n"
        )
    return "".join(parts)


def _user_prompt(action: str, goal: str) -> str:
    g = (goal or "").strip()
    if action == "frame_outcome":
        return f"Frame the outcome for this request:\n\n{g}"
    if action == "route_personas":
        return f"Route the right personas for this request:\n\n{g}"
    if action == "draft_issue":
        return f"Draft the GitHub issue body for this request:\n\n{g}"
    return f"Plan this request end-to-end:\n\n{g}"


def _parse_envelope(raw: str) -> dict:
    """Best-effort JSON extraction. Models occasionally wrap in fences."""
    s = (raw or "").strip()
    if s.startswith("```"):
        # strip any ```json fence
        s = s.split("\n", 1)[1] if "\n" in s else s
        if s.endswith("```"):
            s = s[: -3]
        s = s.strip()
    # Find the first { and the last } if there's leading/trailing prose.
    i, j = s.find("{"), s.rfind("}")
    if i != -1 and j != -1 and j > i:
        s = s[i: j + 1]
    return json.loads(s)


def _ensure_core_personas(envelope: dict) -> dict:
    """Belt-and-suspenders: enforce the kit's meta-rule that the three
    core personas are always present. Append any missing ones at order=0."""
    route = envelope.get("persona_route") or []
    present = {(r.get("persona") or "").strip() for r in route if isinstance(r, dict)}
    appended = []
    for core in _CORE_PERSONAS:
        if core not in present:
            appended.append({
                "persona": core,
                "why": "Core persona — always included per the kit's meta-rule.",
                "order": 0,
            })
    if appended:
        envelope["persona_route"] = appended + list(route)
    return envelope


# ─── BasicAgent ──────────────────────────────────────────────────────────


class AgentTeamAgent(BasicAgent):
    def __init__(self):
        self.name = "AgentTeam"
        self.metadata = {
            "name": self.name,
            "description": (
                "Plan a project the way the Agent Team Starter Kit would: "
                "frame the outcome, route the right personas, and emit a "
                "paste-ready GitHub issue body. Pass `goal` (required) "
                "and optionally `action`, `domain`, `constraints`. "
                "Returns a JSON envelope with outcome_frame, "
                "persona_route, issue_body, and needs_you_questions."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["route", "frame_outcome", "route_personas", "draft_issue"],
                        "description": "Which slice of the plan to produce. Default: route (the full envelope).",
                    },
                    "goal": {
                        "type": "string",
                        "description": "The raw project request. What does the team need to deliver?",
                    },
                    "domain": {
                        "type": "string",
                        "description": "Optional domain hint to bias persona routing: d365, ai, power-platform, analytics, generic.",
                    },
                    "constraints": {
                        "type": "string",
                        "description": "Optional constraints: deadlines, budget, compliance, must-use stack, must-not-use, etc.",
                    },
                },
                "required": ["goal"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        action = (kwargs.get("action") or "route").strip()
        if action not in _ACTION_SOULS:
            return json.dumps({
                "error": f"unknown action: {action!r}",
                "valid_actions": list(_ACTION_SOULS.keys()),
            })

        goal = (kwargs.get("goal") or "").strip()
        if not goal:
            return json.dumps({
                "error": "goal is required — describe the work the team should plan.",
            })

        domain = kwargs.get("domain")
        constraints = kwargs.get("constraints")

        system = _system_prompt(action, domain, constraints)
        user = _user_prompt(action, goal)

        try:
            from utils.llm import call_llm
        except Exception as e:
            return json.dumps({"error": f"LLM dispatch unavailable: {e}"})

        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ]
        try:
            raw = call_llm(messages)
        except Exception as e:
            return json.dumps({"error": f"LLM error: {e}"})

        try:
            envelope = _parse_envelope(raw)
        except Exception:
            return json.dumps({
                "error": "model did not return JSON",
                "raw": raw,
            })

        envelope = _ensure_core_personas(envelope)
        envelope["_meta"] = {
            "action": action,
            "based_on": "billwhalenmsft/agent-team-starter-kit",
            "rapp": "@kody-w/agent_team",
        }
        return json.dumps(envelope, indent=2)
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
