---
name: "rappstore-kody-w-agent-team-singleton"
description: "Plan a project the way the Agent Team Starter Kit would: frame the outcome, route the right personas, and emit a paste-ready GitHub issue body. Pass `goal` (required) and optionally `action`, `domain`, `constraints`. Returns a JSON envelope with outcome_frame, persona_route, issue_body, and needs_you_questions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/agent-team-singleton", "rar_sha256": "c950b295557f7d25471aeff87b5caac9b51cf49633d9f71108c6e80d24db947f", "source_kind": "federated-rapplication", "source_commit": null, "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "agent_team_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/agent-team-singleton:b215252eb4005eabe533e9476b6e088802845945be7e386972d1ba0f7c04c490", "kind": "skill"}, "version": "0.1.0", "author": "@kody-w", "tags": ["rapplication", "agent-team", "persona-routing", "outcome-first", "github-issues", "azure", "planning"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/agent-team-singleton`. The
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
