---
name: "rar-cowork-cookbook-audit-rework-defective-inventory"
description: "Audits rework defective inventory records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel wor"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_rework_defective_inventory", "rar_sha256": "a7ce6167f777564be0e90023156cce20d1aefaf05a4144391ea87acad7c0e809", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_rework_defective_inventory`. The original RAPP
agent is preserved byte-for-byte in `audit_rework_defective_inventory_agent.py` and in the RCI capsule.

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

Rework defective inventory Completeness Audit — Audits rework defective inventory records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel wor

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-rework-defective-inventory
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
      "description": "D365 legal entity to audit, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-rework-defective-inventory-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_rework_defective_inventory_agent.py` and embedded as the fenced Python below (sha256 a7ce6167f777564b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_rework_defective_inventory_agent.py` first:

```bash
python3 audit_rework_defective_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_rework_defective_inventory_agent.py   # or on stdin
python3 audit_rework_defective_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Rework defective inventory Completeness Audit — Audits rework defective inventory records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel wor

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-rework-defective-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_rework_defective_inventory',
    "version": '3.0.3',
    "display_name": 'Rework defective inventory Completeness Audit',
    "description": 'Audits rework defective inventory records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel wor',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-rework-defective-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-rework-defective-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e9dd3ce04145aff4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/rework-defective-inventory'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/audit-rework-defective-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-rework-defective-inventory-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit rework defective inventory records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to rework defective inventory. Output an Excel workbook 'audit-rework-defective-inventory-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no rework defective inventory data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads rework defective inventory records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits rework defective inventory records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel wor', 'example_request': 'Audit rework defective inventory in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-rework-defective-inventory-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy-compliance audit of rework defective inventory records in D365 F&SCM, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditReworkDefectiveInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditReworkDefectiveInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-rework-defective-inventory-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditReworkDefectiveInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
