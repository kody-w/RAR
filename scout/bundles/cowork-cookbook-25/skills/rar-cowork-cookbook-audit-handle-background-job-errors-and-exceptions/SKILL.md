---
name: "rar-cowork-cookbook-audit-handle-background-job-errors-and-exceptions"
description: "Runs a read-only completeness and policy audit of background job error/exception records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary shee"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_handle_background_job_errors_and_exceptions", "rar_sha256": "d6788591b348a13fda7245040cbe82c27fa59c02715d2b453badeec97ce056ce", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_handle_background_job_errors_and_exceptions`. The original RAPP
agent is preserved byte-for-byte in `audit_handle_background_job_errors_and_exceptions_agent.py` and in the RCI capsule.

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

Handle background job errors and exceptions Completeness Audit — Runs a read-only completeness and policy audit of background job error/exception records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary shee

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-handle-background-job-errors-and-exceptions
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
      "description": "Date range to treat as current vs stale; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-handle-background-job-errors-and-exceptions-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_handle_background_job_errors_and_exceptions_agent.py` and embedded as the fenced Python below (sha256 d6788591b348a13f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_handle_background_job_errors_and_exceptions_agent.py` first:

```bash
python3 audit_handle_background_job_errors_and_exceptions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_handle_background_job_errors_and_exceptions_agent.py   # or on stdin
python3 audit_handle_background_job_errors_and_exceptions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Handle background job errors and exceptions Completeness Audit — Runs a read-only completeness and policy audit of background job error/exception records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary shee

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-handle-background-job-errors-and-exceptions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_handle_background_job_errors_and_exceptions',
    "version": '3.0.2',
    "display_name": 'Handle background job errors and exceptions Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of background job error/exception records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary shee',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'audit-handle-background-job-errors-and-exceptions',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-handle-background-job-errors-and-exceptions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f9a5db7055447163',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-03', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/handle-background-job-errors-and-exceptions'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-handle-background-job-errors-and-exceptions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range to treat as current vs stale; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-handle-background-job-errors-and-exceptions-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit handle background job errors and exceptions records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to handle background job errors and exceptions. Output an Excel workbook 'audit-handle-background-job-errors-and-exceptions-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no handle background job errors and exceptions data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-03', 'what_it_does': 'Reads handle background job errors and exceptions records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of background job error/exception records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary shee', 'example_request': 'Audit background job error and exception records in USMF for completeness and give me the Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range to treat as current vs stale; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-handle-background-job-errors-and-exceptions-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-modify audit of D365 background job error/exception records for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditHandleBackgroundJobErrorsAndExceptions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditHandleBackgroundJobErrorsAndExceptions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range to treat as current vs stale; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-handle-background-job-errors-and-exceptions-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditHandleBackgroundJobErrorsAndExceptions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
