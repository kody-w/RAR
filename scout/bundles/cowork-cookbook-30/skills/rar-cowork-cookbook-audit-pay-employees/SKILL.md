---
name: "rar-cowork-cookbook-audit-pay-employees"
description: "Runs a read-only completeness and policy audit of pay employees records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_pay_employees", "rar_sha256": "65255baaadd6e3093c37ce2e14c19b96bb21fc43405fb5526832fa0905766db9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_pay_employees`. The original RAPP
agent is preserved byte-for-byte in `audit_pay_employees_agent.py` and in the RCI capsule.

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

Pay employees Completeness Audit — Runs a read-only completeness and policy audit of pay employees records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-pay-employees
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
      "description": "Dynamics 365 legal entity to audit, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-pay-employees-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_pay_employees_agent.py` and embedded as the fenced Python below (sha256 65255baaadd6e309…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_pay_employees_agent.py` first:

```bash
python3 audit_pay_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_pay_employees_agent.py   # or on stdin
python3 audit_pay_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pay employees Completeness Audit — Runs a read-only completeness and policy audit of pay employees records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-pay-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_pay_employees',
    "version": '3.0.3',
    "display_name": 'Pay employees Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of pay employees records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-pay-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-pay-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fd3ab15f21b7af1e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/pay-employees'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-pay-employees', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-pay-employees-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit pay employees records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to pay employees. Output an Excel workbook 'audit-pay-employees-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no pay employees data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads pay employees records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of pay employees records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.', 'example_request': 'Audit pay employees records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-pay-employees-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants pay employees records in Dynamics 365 checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditPayEmployees(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPayEmployees'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-pay-employees-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditPayEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
