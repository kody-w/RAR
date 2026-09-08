---
name: "rar-cowork-cookbook-adaptive-card-enter-sales-orders"
description: "Generates a read-only Adaptive Card JSON file visualizing enter sales orders status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons for Teams, Outlook, or the designer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_enter_sales_orders", "rar_sha256": "e872e2f0cd4607bc85a3d14380d4d0480e0c4d81839d1a80ecd22afff876823e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_enter_sales_orders`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_enter_sales_orders_agent.py` and in the RCI capsule.

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

Enter sales orders Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing enter sales orders status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons for Teams, Outlook, or the designer.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-enter-sales-orders
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-enter-sales-orders-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_enter_sales_orders_agent.py` and embedded as the fenced Python below (sha256 e872e2f0cd4607bc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_enter_sales_orders_agent.py` first:

```bash
python3 adaptive_card_enter_sales_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_enter_sales_orders_agent.py   # or on stdin
python3 adaptive_card_enter_sales_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Enter sales orders Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing enter sales orders status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons for Teams, Outlook, or the designer.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-enter-sales-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_enter_sales_orders',
    "version": '3.0.2',
    "display_name": 'Enter sales orders Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing enter sales orders status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons for Teams, Outlook, or the designer.',
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
        "upstream_slug": 'adaptive-card-enter-sales-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-enter-sales-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '563783fe14249cbd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/enter-sales-orders'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/adaptive-card-enter-sales-orders', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the card timestamp and file naming.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-enter-sales-orders-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical enter sales orders status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-enter-sales-orders-2026-05-24-card.json' that visualizes the current state of enter sales orders. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current enter sales orders KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing enter sales orders status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons for Teams, Outlook, or the designer.', 'example_request': 'Make an Adaptive Card JSON of enter sales orders status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-enter-sales-orders-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and file naming.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of enter sales orders status from D365 ERP for dashboards, email, or Teams, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardEnterSalesOrders(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardEnterSalesOrders'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the card timestamp and file naming.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-enter-sales-orders-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardEnterSalesOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
