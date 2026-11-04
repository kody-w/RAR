---
name: "rar-kody-w-agent-team"
description: "Plan a project the way the Agent Team Starter Kit would: frame the outcome, route the right personas, and emit a paste-ready GitHub issue body. Pass `goal` (required) and optionally `action`, `domain`, `constraints`. Returns a JSON envelope with outcome_frame, persona_route, issue_body, and needs_you_questions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/agent_team_agent", "rar_sha256": "60321dac590b9a80b2bcf85de9dea49e1617b00a6dbed28f4dcaf69d06ca40f4", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "0.1.2", "author": "@kody-w", "tags": ["rapplication", "agent-team", "persona-routing", "outcome-first", "github-issues", "azure", "planning"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `agent_team_agent.py` and embedded as the fenced Python below (sha256 60321dac590b9a80…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `agent_team_agent.py` first:

```bash
python3 agent_team_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 agent_team_agent.py   # or on stdin
python3 agent_team_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/agent_team_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/agent_team_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/agent_team_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
