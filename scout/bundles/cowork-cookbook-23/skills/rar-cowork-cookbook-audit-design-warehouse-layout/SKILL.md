---
name: "rar-cowork-cookbook-audit-design-warehouse-layout"
description: "Runs a read-only completeness and policy audit of design warehouse layout records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_design_warehouse_layout", "rar_sha256": "963615b4a16a65b6c12b5af8dd594092ba5937614145a1a7a76568b48205c06e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
