---
name: "rar-cowork-cookbook-adaptive-card-plan-aggregate-supply"
description: "Generates a read-only Adaptive Card JSON file summarizing plan aggregate supply status for a Dynamics 365 F&SCM legal entity, with KPI tiles, RAG row, and action buttons; call to embed that snapshot in Teams, Outlook, or"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_plan_aggregate_supply", "rar_sha256": "555971fea6454be23262bdc6a5ca9de8677bd1f41c28c1b9d695edab23a7a5fa", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
