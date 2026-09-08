---
name: "rar-cowork-cookbook-demo-data-define-warehouse-management-kpis"
description: "Generates 25 realistic demo records for warehouse management KPIs in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_warehouse_management_kpis", "rar_sha256": "965f144c98d7e01cbd4f754345c3ebdbfc27cf4ccf48bbad299420bcc4535032", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
