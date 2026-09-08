---
name: "rar-cowork-cookbook-demo-data-define-warehouse-management-kpis"
description: "Generates 25 realistic demo records for warehouse management KPIs in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_warehouse_management_kpis", "rar_sha256": "965f144c98d7e01cbd4f754345c3ebdbfc27cf4ccf48bbad299420bcc4535032", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_define_warehouse_management_kpis`. The original RAPP
agent is preserved byte-for-byte in `demo_data_define_warehouse_management_kpis_agent.py` and in the RCI capsule.

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

Define warehouse management KPIs Demo Data Generator — Generates 25 realistic demo records for warehouse management KPIs in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-warehouse-management-kpis
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
      "description": "Sandbox D365 legal entity to create records in; defaults to USMF.",
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
      "description": "Number of demo records to generate; defaults to 25.",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-define-warehouse-management-kpis-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_warehouse_management_kpis_agent.py` and embedded as the fenced Python below (sha256 965f144c98d7e01c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_warehouse_management_kpis_agent.py` first:

```bash
python3 demo_data_define_warehouse_management_kpis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_warehouse_management_kpis_agent.py   # or on stdin
python3 demo_data_define_warehouse_management_kpis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define warehouse management KPIs Demo Data Generator — Generates 25 realistic demo records for warehouse management KPIs in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-warehouse-management-kpis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_warehouse_management_kpis',
    "version": '3.0.3',
    "display_name": 'Define warehouse management KPIs Demo Data Generator',
    "description": "Generates 25 realistic demo records for warehouse management KPIs in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-define-warehouse-management-kpis',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-warehouse-management-kpis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5a0c38795fdcb9bf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/analyze-warehouse-operations/define-warehouse-management-kpis'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/demo-data-define-warehouse-management-kpis', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to create records in; defaults to USMF.', 'record_count': 'Number of demo records to generate; defaults to 25.', 'workbook_name': 'Excel staging file name, e.g. demo-data-define-warehouse-management-kpis-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic define warehouse management KPIs data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for define warehouse management KPIs. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-define-warehouse-management-kpis-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic define warehouse management KPIs records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for warehouse management KPIs in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 warehouse management KPI demo records in the USMF sandbox and list the new record IDs.', 'inputs': [{'description': 'Sandbox D365 legal entity to create records in; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate; defaults to 25.', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-define-warehouse-management-kpis-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need seeded warehouse management KPI demo data in a D365 sandbox for training or pilot scenarios. Never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDefineWarehouseManagementKpis(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefineWarehouseManagementKpis'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to create records in; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-define-warehouse-management-kpis-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataDefineWarehouseManagementKpis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
