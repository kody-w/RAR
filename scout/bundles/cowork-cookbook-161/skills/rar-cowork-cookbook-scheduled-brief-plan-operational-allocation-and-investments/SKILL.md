---
name: "rar-cowork-cookbook-scheduled-brief-plan-operational-allocation-and-investments"
description: "Builds a morning brief on plan operational allocation and investments from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and recommended next actions, then drafts an ema"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_operational_allocation_and_investments", "rar_sha256": "30caf084dac89485ffcba44b67131626d3a29b04cfdf7ea23af3c94a9a943f68", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_plan_operational_allocation_and_investments`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_plan_operational_allocation_and_investments_agent.py` and in the RCI capsule.

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

Plan operational allocation and investments Scheduled Email Brief — Builds a morning brief on plan operational allocation and investments from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and recommended next actions, then drafts an ema

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-operational-allocation-and-investments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to query; defaults to USMF.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "owner": {
      "description": "The responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "Optional cadence for the scheduled task, e.g. weekday mornings at 7am.",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_plan_operational_allocation_and_investments_agent.py` and embedded as the fenced Python below (sha256 30caf084dac89485…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_plan_operational_allocation_and_investments_agent.py` first:

```bash
python3 scheduled_brief_plan_operational_allocation_and_investments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_plan_operational_allocation_and_investments_agent.py   # or on stdin
python3 scheduled_brief_plan_operational_allocation_and_investments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan operational allocation and investments Scheduled Email Brief — Builds a morning brief on plan operational allocation and investments from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and recommended next actions, then drafts an ema

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-operational-allocation-and-investments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_plan_operational_allocation_and_investments',
    "version": '3.0.3',
    "display_name": 'Plan operational allocation and investments Scheduled Email Brief',
    "description": 'Builds a morning brief on plan operational allocation and investments from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and recommended next actions, then drafts an ema',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'scheduled-brief-plan-operational-allocation-and-investments',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-plan-operational-allocation-and-investments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '29b1f0d93bafc821',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/plan-operational-allocation-and-investments'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/scheduled-brief-plan-operational-allocation-and-investments', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; defaults to USMF.', 'owner': 'The responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where plan operational allocation and investments stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on plan operational allocation and investments for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan operational allocation and investments, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on plan operational allocation and investments from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and recommended next actions, then drafts an ema', 'example_request': 'Give me the morning brief on plan operational allocation and investments for USMF and draft it to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'The responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly allocation/investment brief for the responsible owner from D365 F&SCM, drafted as email and a Teams post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefPlanOperationalAllocationAndInvestments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPlanOperationalAllocationAndInvestments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'The responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(ScheduledBriefPlanOperationalAllocationAndInvestments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
