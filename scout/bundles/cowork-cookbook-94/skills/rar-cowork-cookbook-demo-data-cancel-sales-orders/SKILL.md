---
name: "rar-cowork-cookbook-demo-data-cancel-sales-orders"
description: "Generates 25 realistic demo cancel-sales-order records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_cancel_sales_orders", "rar_sha256": "161ab32860da1149af299cfdc1623620a3338eb7d370d9339ea96f32d6e32ff0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_cancel_sales_orders`. The original RAPP
agent is preserved byte-for-byte in `demo_data_cancel_sales_orders_agent.py` and in the RCI capsule.

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

Cancel sales orders Demo Data Generator — Generates 25 realistic demo cancel-sales-order records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-cancel-sales-orders
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
    "legal_entity": {
      "description": "Sandbox D365 legal entity to target; defaults to USMF. Must not be production.",
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
    "record_count": {
      "description": "Number of demo cancel sales order records to generate; defaults to 25.",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-cancel-sales-orders-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_cancel_sales_orders_agent.py` and embedded as the fenced Python below (sha256 161ab32860da1149…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_cancel_sales_orders_agent.py` first:

```bash
python3 demo_data_cancel_sales_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_cancel_sales_orders_agent.py   # or on stdin
python3 demo_data_cancel_sales_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Cancel sales orders Demo Data Generator — Generates 25 realistic demo cancel-sales-order records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-cancel-sales-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_cancel_sales_orders',
    "version": '3.0.3',
    "display_name": 'Cancel sales orders Demo Data Generator',
    "description": "Generates 25 realistic demo cancel-sales-order records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-cancel-sales-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-cancel-sales-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '83aa56c9a9801743',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/cancel-sales-orders'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/demo-data-cancel-sales-orders', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'record_count': 'Number of demo cancel sales order records to generate; defaults to 25.', 'workbook_name': 'Excel staging file name, e.g. demo-data-cancel-sales-orders-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic cancel sales orders data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for cancel sales orders. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-cancel-sales-orders-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic cancel sales orders records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo cancel-sales-order records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo cancel sales order records in the USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo cancel sales order records to generate; defaults to 25.', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-cancel-sales-orders-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training cancel sales order data created in a sandbox D365 legal entity — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataCancelSalesOrders(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataCancelSalesOrders'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo cancel sales order records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-cancel-sales-orders-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataCancelSalesOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
