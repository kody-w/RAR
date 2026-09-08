---
name: "rar-cowork-cookbook-adaptive-card-cancel-sales-orders"
description: "Generates a read-only Adaptive Card JSON file visualizing cancel sales orders status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_cancel_sales_orders", "rar_sha256": "ce44515de8e7fe35522e9f001596dd1bed86372089566e8385e065aa790f77dc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_cancel_sales_orders`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_cancel_sales_orders_agent.py` and in the RCI capsule.

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

Cancel sales orders Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing cancel sales orders status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-cancel-sales-orders
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
    "as_of_date": {
      "description": "Date used for the card timestamp and file naming.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-cancel-sales-orders-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_cancel_sales_orders_agent.py` and embedded as the fenced Python below (sha256 ce44515de8e7fe35…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_cancel_sales_orders_agent.py` first:

```bash
python3 adaptive_card_cancel_sales_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_cancel_sales_orders_agent.py   # or on stdin
python3 adaptive_card_cancel_sales_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Cancel sales orders Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing cancel sales orders status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-cancel-sales-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_cancel_sales_orders',
    "version": '3.0.2',
    "display_name": 'Cancel sales orders Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing cancel sales orders status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-cancel-sales-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-cancel-sales-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '792a0dad2566c00a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/cancel-sales-orders'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/adaptive-card-cancel-sales-orders', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the card timestamp and file naming.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-cancel-sales-orders-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical cancel sales orders status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-cancel-sales-orders-2026-05-24-card.json' that visualizes the current state of cancel sales orders. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current cancel sales orders KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing cancel sales orders status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON showing cancel sales orders status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-cancel-sales-orders-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and file naming.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of cancel sales orders status for Teams, Outlook, or a dashboard, without changing any D365 data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardCancelSalesOrders(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardCancelSalesOrders'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the card timestamp and file naming.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-cancel-sales-orders-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardCancelSalesOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
