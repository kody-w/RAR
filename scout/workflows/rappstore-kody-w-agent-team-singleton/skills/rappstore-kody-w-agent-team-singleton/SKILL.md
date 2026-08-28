---
name: "rappstore-kody-w-agent-team-singleton"
description: "Plan a project the way the Agent Team Starter Kit would: frame the outcome, route the right personas, and emit a paste-ready GitHub issue body. Pass `goal` (required) and optionally `action`, `domain`, `constraints`. Returns a JSON envelope with outcome_frame, persona_route, issue_body, and needs_you_questions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/agent-team-singleton", "rar_sha256": "c950b295557f7d25471aeff87b5caac9b51cf49633d9f71108c6e80d24db947f", "source_kind": "federated-rapplication", "source_commit": null, "version": "0.1.0", "author": "@kody-w", "tags": ["rapplication", "agent-team", "persona-routing", "outcome-first", "github-issues", "azure", "planning"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/agent-team-singleton`. The original RAPP
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
LLM tool call, or `/api/binder/agent`. UI mounts via the cartridge
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `agent_team_agent.py` and embedded as the fenced Python below (sha256 c950b295557f7d25…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `agent_team_agent.py` first:

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
LLM tool call, or `/api/binder/agent`. UI mounts via the cartridge
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
    "name": "@kody-w/agent_team",
    "display_name": "AgentTeam",
    "version": "0.1.0",
    "description": (
        "The persona-routing brain of the Agent Team Starter Kit as a "
        "single agent. Given a project goal, returns the outcome frame, "
        "persona route, paste-ready GitHub issue body, and the "
        "needs-you questions the team would surface."
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
