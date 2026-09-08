---
name: "rar-cowork-cookbook-sales-order-validation"
description: "Reviews open sales orders in Dynamics 365 F&SCM and returns a read-only workbook of out-of-policy orders, one sheet per finding: price deviation >10%, credit hold, missing delivery terms, missing tax group."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/sales_order_validation", "rar_sha256": "2eb2b306eccbaaeecc156ce60abdff1bcc3e2d95fb8b9372208ff92488ea20cc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/sales_order_validation`. The original RAPP
agent is preserved byte-for-byte in `sales_order_validation_agent.py` and in the RCI capsule.

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

Sales Order Compliance Check — Reviews open sales orders in Dynamics 365 F&SCM and returns a read-only workbook of out-of-policy orders, one sheet per finding: price deviation >10%, credit hold, missing delivery terms, missing tax group.

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
  Upstream entry : https://coworkcookbook.com/recipes/sales-order-validation
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `sales_order_validation_agent.py` and embedded as the fenced Python below (sha256 2eb2b306eccbaaee…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `sales_order_validation_agent.py` first:

```bash
python3 sales_order_validation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 sales_order_validation_agent.py   # or on stdin
python3 sales_order_validation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Sales Order Compliance Check — Reviews open sales orders in Dynamics 365 F&SCM and returns a read-only workbook of out-of-policy orders, one sheet per finding: price deviation >10%, credit hold, missing delivery terms, missing tax group.

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
  Upstream entry : https://coworkcookbook.com/recipes/sales-order-validation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/sales_order_validation',
    "version": '3.0.3',
    "display_name": 'Sales Order Compliance Check',
    "description": 'Reviews open sales orders in Dynamics 365 F&SCM and returns a read-only workbook of out-of-policy orders, one sheet per finding: price deviation >10%, credit hold, missing delivery terms, missing tax group.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'sales-order-validation',
        "upstream_url": 'https://coworkcookbook.com/recipes/sales-order-validation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '019ff11eb2b1c48c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/sales-order-validation', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the Sales role', 'Output matches: Workbook of out-of-policy sales orders by category.'], 'confidence': 1.0, 'deliverable': 'Workbook of out-of-policy sales orders by category.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Prevents shipped-but-uninvoiceable orders by catching pricing, credit, and tax issues at order entry instead of at invoicing.', 'expected_output': 'Workbook of out-of-policy sales orders by category.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the Sales role'], 'prompt': 'Review all open sales orders. Flag: orders with item prices that deviate >10% from the active price list, customers on credit hold, missing delivery terms, and missing tax group. Output a workbook with one sheet per finding. Do not modify orders.', 'steps': ['Paste the prompt.', 'Resolve flagged orders in D365 before shipping.'], 'tenant_caveat': "Validated against a live Cowork tenant on 2026-05-23 with USMF. Cowork engaged the D365 ERP plugin, queried open sales orders, and identified 3 customers on credit hold (US-017, US-041, US-103). Honesty note: on this run Cowork advanced 1/5 plan steps (find open orders, identify credit-hold customers) and queued the workbook build but did not produce the final file before the screenshot. The data findings are real (the 3 credit-hold customers cross-match the customer-credit-limit-review recipe's 'inactive 12mo' set). Re-running with smaller scope (one finding category at a time) typically produces the full workbook.", 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'Pre-shipment policy check on the sales-order book.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reviews open sales orders in Dynamics 365 F&SCM and returns a read-only workbook of out-of-policy orders, one sheet per finding: price deviation >10%, credit hold, missing delivery terms, missing tax group.', 'example_request': 'Check our open sales orders for policy violations and give me a workbook by finding.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call before shipping or during order review to find open sales orders that violate pricing, credit, delivery terms, or tax group policy. Read-only; no orders are modified.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt.', 'Resolve flagged orders in D365 before shipping.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class SalesOrderValidation(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'SalesOrderValidation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(SalesOrderValidation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
