---
name: "rar-cowork-cookbook-audit-handle-background-job-errors-and-exceptions"
description: "Runs a read-only completeness and policy audit of background job error/exception records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary shee"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_handle_background_job_errors_and_exceptions", "rar_sha256": "d6788591b348a13fda7245040cbe82c27fa59c02715d2b453badeec97ce056ce", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
