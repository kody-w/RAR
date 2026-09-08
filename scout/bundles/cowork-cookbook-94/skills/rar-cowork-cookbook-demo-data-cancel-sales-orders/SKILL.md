---
name: "rar-cowork-cookbook-demo-data-cancel-sales-orders"
description: "Generates 25 realistic demo cancel-sales-order records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_cancel_sales_orders", "rar_sha256": "161ab32860da1149af299cfdc1623620a3338eb7d370d9339ea96f32d6e32ff0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
