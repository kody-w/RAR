---
name: "rar-cowork-cookbook-sales-order-validation"
description: "Reviews open sales orders in Dynamics 365 F&SCM and returns a read-only workbook of out-of-policy orders, one sheet per finding: price deviation >10%, credit hold, missing delivery terms, missing tax group."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/sales_order_validation", "rar_sha256": "2eb2b306eccbaaeecc156ce60abdff1bcc3e2d95fb8b9372208ff92488ea20cc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
