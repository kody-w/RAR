---
name: "rar-cowork-cookbook-adaptive-card-plan-aggregate-supply"
description: "Generates a read-only Adaptive Card JSON file summarizing plan aggregate supply status for a Dynamics 365 F&SCM legal entity, with KPI tiles, RAG row, and action buttons; call to embed that snapshot in Teams, Outlook, or"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_plan_aggregate_supply", "rar_sha256": "555971fea6454be23262bdc6a5ca9de8677bd1f41c28c1b9d695edab23a7a5fa", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_plan_aggregate_supply`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_plan_aggregate_supply_agent.py` and in the RCI capsule.

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

Plan aggregate supply Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing plan aggregate supply status for a Dynamics 365 F&SCM legal entity, with KPI tiles, RAG row, and action buttons; call to embed that snapshot in Teams, Outlook, or

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-plan-aggregate-supply
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
    "action_buttons": {
      "description": "Number or labels of action buttons to include on the card (2-3).",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_count": {
      "description": "How many KPI tiles to include (3-5), each with current value and trend arrow.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to report on, e.g. USMF.",
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
    "output_filename": {
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-plan-aggregate-supply-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_plan_aggregate_supply_agent.py` and embedded as the fenced Python below (sha256 555971fea6454be2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_plan_aggregate_supply_agent.py` first:

```bash
python3 adaptive_card_plan_aggregate_supply_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_plan_aggregate_supply_agent.py   # or on stdin
python3 adaptive_card_plan_aggregate_supply_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan aggregate supply Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing plan aggregate supply status for a Dynamics 365 F&SCM legal entity, with KPI tiles, RAG row, and action buttons; call to embed that snapshot in Teams, Outlook, or

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-plan-aggregate-supply
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_plan_aggregate_supply',
    "version": '3.0.2',
    "display_name": 'Plan aggregate supply Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing plan aggregate supply status for a Dynamics 365 F&SCM legal entity, with KPI tiles, RAG row, and action buttons; call to embed that snapshot in Teams, Outlook, or',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-plan-aggregate-supply',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-plan-aggregate-supply',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '08939b47d85950d3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-aggregate-supply'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/adaptive-card-plan-aggregate-supply', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'Number or labels of action buttons to include on the card (2-3).', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'legal_entity': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-plan-aggregate-supply-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical plan aggregate supply status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-plan-aggregate-supply-2026-05-24-card.json' that visualizes the current state of plan aggregate supply. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current plan aggregate supply KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing plan aggregate supply status for a Dynamics 365 F&SCM legal entity, with KPI tiles, RAG row, and action buttons; call to embed that snapshot in Teams, Outlook, or', 'example_request': 'Make an Adaptive Card JSON showing plan aggregate supply status for USMF with 4 KPI tiles and a RAG row.', 'inputs': [{'description': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-plan-aggregate-supply-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'name': 'kpi_count'}, {'description': 'Number or labels of action buttons to include on the card (2-3).', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'When a user wants a shareable Adaptive Card snapshot of current plan aggregate supply status from Dynamics 365 F&SCM, without changing any ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardPlanAggregateSupply(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardPlanAggregateSupply'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'Number or labels of action buttons to include on the card (2-3).', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-plan-aggregate-supply-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardPlanAggregateSupply().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
