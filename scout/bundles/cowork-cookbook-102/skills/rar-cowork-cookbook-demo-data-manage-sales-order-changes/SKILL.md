---
name: "rar-cowork-cookbook-demo-data-manage-sales-order-changes"
description: "Generates 25 realistic demo sales-order-change records via the Dynamics 365 ERP plugin in a sandbox legal entity, stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_sales_order_changes", "rar_sha256": "0ca9059991c33e6cb6111f20e9866b344c5391574ea8ebcd3dd800ae22dd562e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
