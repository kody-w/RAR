---
name: "rar-cowork-cookbook-adaptive-card-enter-sales-orders"
description: "Generates a read-only Adaptive Card JSON file visualizing enter sales orders status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons for Teams, Outlook, or the designer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_enter_sales_orders", "rar_sha256": "e872e2f0cd4607bc85a3d14380d4d0480e0c4d81839d1a80ecd22afff876823e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
