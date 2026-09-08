---
name: "rar-cowork-cookbook-adaptive-card-cancel-sales-orders"
description: "Generates a read-only Adaptive Card JSON file visualizing cancel sales orders status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_cancel_sales_orders", "rar_sha256": "ce44515de8e7fe35522e9f001596dd1bed86372089566e8385e065aa790f77dc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
