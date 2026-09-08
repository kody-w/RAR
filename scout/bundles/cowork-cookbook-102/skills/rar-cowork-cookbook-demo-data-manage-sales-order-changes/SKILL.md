---
name: "rar-cowork-cookbook-demo-data-manage-sales-order-changes"
description: "Generates 25 realistic demo sales-order-change records via the Dynamics 365 ERP plugin in a sandbox legal entity, stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_sales_order_changes", "rar_sha256": "0ca9059991c33e6cb6111f20e9866b344c5391574ea8ebcd3dd800ae22dd562e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_sales_order_changes`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_sales_order_changes_agent.py` and in the RCI capsule.

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

Manage sales order changes Demo Data Generator — Generates 25 realistic demo sales-order-change records via the Dynamics 365 ERP plugin in a sandbox legal entity, stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-sales-order-changes
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
      "description": "Sandbox D365 legal entity to target (default USMF); must not be production.",
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
      "description": "Number of demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-manage-sales-order-changes-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_sales_order_changes_agent.py` and embedded as the fenced Python below (sha256 0ca9059991c33e6c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_sales_order_changes_agent.py` first:

```bash
python3 demo_data_manage_sales_order_changes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_sales_order_changes_agent.py   # or on stdin
python3 demo_data_manage_sales_order_changes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage sales order changes Demo Data Generator — Generates 25 realistic demo sales-order-change records via the Dynamics 365 ERP plugin in a sandbox legal entity, stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-sales-order-changes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_sales_order_changes',
    "version": '3.0.3',
    "display_name": 'Manage sales order changes Demo Data Generator',
    "description": "Generates 25 realistic demo sales-order-change records via the Dynamics 365 ERP plugin in a sandbox legal entity, stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-manage-sales-order-changes',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-sales-order-changes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '134bbf2daefc0849',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/manage-sales-order-changes'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/demo-data-manage-sales-order-changes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-manage-sales-order-changes-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic manage sales order changes data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for manage sales order changes. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-manage-sales-order-changes-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic manage sales order changes records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo sales-order-change records via the Dynamics 365 ERP plugin in a sandbox legal entity, stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo sales order change records in USMF sandbox, stage them in Excel, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-manage-sales-order-changes-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo/training data for manage sales order changes in a D365 sandbox tenant. Sandbox only — never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataManageSalesOrderChanges(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageSalesOrderChanges'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-manage-sales-order-changes-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataManageSalesOrderChanges().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
