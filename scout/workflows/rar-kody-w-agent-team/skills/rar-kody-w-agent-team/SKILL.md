---
name: "rar-kody-w-agent-team"
description: "Plan a project the way the Agent Team Starter Kit would: frame the outcome, route the right personas, and emit a paste-ready GitHub issue body. Pass `goal` (required) and optionally `action`, `domain`, `constraints`. Returns a JSON envelope with outcome_frame, persona_route, issue_body, and needs_you_questions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/agent_team_agent", "rar_sha256": "60321dac590b9a80b2bcf85de9dea49e1617b00a6dbed28f4dcaf69d06ca40f4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "0.1.2", "author": "@kody-w", "tags": ["rapplication", "agent-team", "persona-routing", "outcome-first", "github-issues", "azure", "planning"]}
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
