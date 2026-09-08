---
name: "rar-cowork-cookbook-audit-design-warehouse-layout"
description: "Runs a read-only completeness and policy audit of design warehouse layout records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_design_warehouse_layout", "rar_sha256": "963615b4a16a65b6c12b5af8dd594092ba5937614145a1a7a76568b48205c06e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_design_warehouse_layout`. The original RAPP
agent is preserved byte-for-byte in `audit_design_warehouse_layout_agent.py` and in the RCI capsule.

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

Design warehouse layout Completeness Audit — Runs a read-only completeness and policy audit of design warehouse layout records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-design-warehouse-layout
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
    "date_window": {
      "description": "Date range used to judge stale dates; USMF demo data is mostly FY2017.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to audit; the recipe uses USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-design-warehouse-layout-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_design_warehouse_layout_agent.py` and embedded as the fenced Python below (sha256 963615b4a16a65b6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_design_warehouse_layout_agent.py` first:

```bash
python3 audit_design_warehouse_layout_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_design_warehouse_layout_agent.py   # or on stdin
python3 audit_design_warehouse_layout_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Design warehouse layout Completeness Audit — Runs a read-only completeness and policy audit of design warehouse layout records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-design-warehouse-layout
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_design_warehouse_layout',
    "version": '3.0.2',
    "display_name": 'Design warehouse layout Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of design warehouse layout records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-design-warehouse-layout',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-design-warehouse-layout',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '62f5bc724f9fc2ff',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-warehouse-operations/design-warehouse-layout'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/audit-design-warehouse-layout', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit; the recipe uses USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-design-warehouse-layout-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit design warehouse layout records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to design warehouse layout. Output an Excel workbook 'audit-design-warehouse-layout-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no design warehouse layout data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads design warehouse layout records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of design warehouse layout records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts', 'example_request': 'Audit design warehouse layout records in USMF for completeness and give me the Excel findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit; the recipe uses USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-design-warehouse-layout-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants design warehouse layout records in D365 checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditDesignWarehouseLayout(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDesignWarehouseLayout'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit; the recipe uses USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-design-warehouse-layout-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditDesignWarehouseLayout().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
