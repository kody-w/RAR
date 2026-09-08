---
name: "rar-cowork-cookbook-audit-rework-defective-inventory"
description: "Audits rework defective inventory records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel wor"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_rework_defective_inventory", "rar_sha256": "a7ce6167f777564be0e90023156cce20d1aefaf05a4144391ea87acad7c0e809", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
