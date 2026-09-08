---
name: "rar-cowork-cookbook-adaptive-card-plan-production"
description: "Generates a read-only Adaptive Card JSON file summarizing current plan production status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_plan_production", "rar_sha256": "626759fefe2206be38f46f9de75ea5f6b78f211dc1359e2e17488b901942f417", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_plan_production`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_plan_production_agent.py` and in the RCI capsule.

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

Plan production Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing current plan production status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-plan-production
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
      "description": "The 2-3 action buttons to place on the card.",
      "type": "string"
    },
    "as_of_date": {
      "description": "Date the snapshot represents, used in the card timestamp and filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_count": {
      "description": "How many KPI tiles to include (3-5).",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to query, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-plan-production-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_plan_production_agent.py` and embedded as the fenced Python below (sha256 626759fefe2206be…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_plan_production_agent.py` first:

```bash
python3 adaptive_card_plan_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_plan_production_agent.py   # or on stdin
python3 adaptive_card_plan_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan production Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing current plan production status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-plan-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_plan_production',
    "version": '3.0.2',
    "display_name": 'Plan production Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing current plan production status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-plan-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-plan-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7ecd839853f4c020',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-production'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/adaptive-card-plan-production', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'as_of_date': 'Date the snapshot represents, used in the card timestamp and filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 F&SCM legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-plan-production-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical plan production status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-plan-production-2026-05-24-card.json' that visualizes the current state of plan production. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current plan production KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing current plan production status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing plan production status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date the snapshot represents, used in the card timestamp and filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-plan-production-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a plan production status snapshot as an Adaptive Card to embed in Teams, Outlook, or a dashboard, without changing any ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardPlanProduction(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardPlanProduction'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date the snapshot represents, used in the card timestamp and filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-plan-production-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardPlanProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
