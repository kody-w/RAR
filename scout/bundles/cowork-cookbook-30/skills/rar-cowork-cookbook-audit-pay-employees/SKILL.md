---
name: "rar-cowork-cookbook-audit-pay-employees"
description: "Runs a read-only completeness and policy audit of pay employees records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_pay_employees", "rar_sha256": "65255baaadd6e3093c37ce2e14c19b96bb21fc43405fb5526832fa0905766db9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
