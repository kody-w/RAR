---
name: "rar-kody-w-agent-team"
description: "Plan a project the way the Agent Team Starter Kit would: frame the outcome, route the right personas, and emit a paste-ready GitHub issue body. Pass `goal` (required) and optionally `action`, `domain`, `constraints`. Returns a JSON envelope with outcome_frame, persona_route, issue_body, and needs_you_questions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/agent_team_agent", "rar_sha256": "0ed520946386fb7d52aa8f9af1774f2656f4e9bc33d7ff911737e6f67b498332", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "agent_team_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/agent-team:50d0767d5d2ef83f34d1c314a75c2f1e25726a97c9211bcfd546e721e096357f", "kind": "skill"}, "version": "0.1.2", "author": "@kody-w", "tags": ["rapplication", "agent-team", "persona-routing", "outcome-first", "github-issues", "azure", "planning"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/agent_team_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `agent_team_agent.py` is
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
