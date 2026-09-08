---
name: "rar-cowork-cookbook-adaptive-card-build-a-quality-plan-for-a-product"
description: "Generates a read-only Adaptive Card JSON file visualizing quality-plan-for-a-product status from Dynamics 365 F&SCM, with a header, KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_build_a_quality_plan_for_a_product", "rar_sha256": "90d95d3a3860a6ebbef9236f74cce7241f657edee4b658b704a835aaaf6af66a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_build_a_quality_plan_for_a_product`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_build_a_quality_plan_for_a_product_agent.py` and in the RCI capsule.

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

Build a quality plan for a product Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing quality-plan-for-a-product status from Dynamics 365 F&SCM, with a header, KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-build-a-quality-plan-for-a-product
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
      "description": "Date used for the card timestamp and file name.",
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
      "description": "D365 legal entity to query, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-build-a-quality-plan-for-a-product-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_build_a_quality_plan_for_a_product_agent.py` and embedded as the fenced Python below (sha256 90d95d3a3860a6eb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_build_a_quality_plan_for_a_product_agent.py` first:

```bash
python3 adaptive_card_build_a_quality_plan_for_a_product_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_build_a_quality_plan_for_a_product_agent.py   # or on stdin
python3 adaptive_card_build_a_quality_plan_for_a_product_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Build a quality plan for a product Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing quality-plan-for-a-product status from Dynamics 365 F&SCM, with a header, KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-build-a-quality-plan-for-a-product
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_build_a_quality_plan_for_a_product',
    "version": '3.0.2',
    "display_name": 'Build a quality plan for a product Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing quality-plan-for-a-product status from Dynamics 365 F&SCM, with a header, KPI tiles, a RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-build-a-quality-plan-for-a-product',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-build-a-quality-plan-for-a-product',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '27bf85e9d0738c99',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/build-a-quality-plan-for-a-product'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/adaptive-card-build-a-quality-plan-for-a-product', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'as_of_date': 'Date used for the card timestamp and file name.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-build-a-quality-plan-for-a-product-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical build a quality plan for a product status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-build-a-quality-plan-for-a-product-2026-05-24-card.json' that visualizes the current state of build a quality plan for a product. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current build a quality plan for a product KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing quality-plan-for-a-product status from Dynamics 365 F&SCM, with a header, KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing quality plan status for USMF as of 2026-05-24, with 4 KPI tiles.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-build-a-quality-plan-for-a-product-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and file name.', 'name': 'as_of_date'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an Adaptive Card snapshot of product quality plan status from D365 ERP for Teams, Outlook, or a dashboard, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardBuildAQualityPlanForAProduct(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardBuildAQualityPlanForAProduct'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date used for the card timestamp and file name.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-build-a-quality-plan-for-a-product-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardBuildAQualityPlanForAProduct().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
