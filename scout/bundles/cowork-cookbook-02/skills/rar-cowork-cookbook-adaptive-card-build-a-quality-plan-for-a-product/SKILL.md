---
name: "rar-cowork-cookbook-adaptive-card-build-a-quality-plan-for-a-product"
description: "Generates a read-only Adaptive Card JSON file visualizing quality-plan-for-a-product status from Dynamics 365 F&SCM, with a header, KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_build_a_quality_plan_for_a_product", "rar_sha256": "90d95d3a3860a6ebbef9236f74cce7241f657edee4b658b704a835aaaf6af66a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
