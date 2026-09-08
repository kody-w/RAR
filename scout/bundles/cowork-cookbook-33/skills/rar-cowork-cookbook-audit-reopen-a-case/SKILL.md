---
name: "rar-cowork-cookbook-audit-reopen-a-case"
description: "Audits reopen-a-case records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workboo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_reopen_a_case", "rar_sha256": "05cbe9eee0c22d43fc7df014a1cccaec8354466eb1d0ecc1f4bf2ae149d854fe", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_reopen_a_case`. The original RAPP
agent is preserved byte-for-byte in `audit_reopen_a_case_agent.py` and in the RCI capsule.

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

Reopen a case Completeness Audit — Audits reopen-a-case records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workboo

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-reopen-a-case
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
      "description": "Date range for stale-date checks; USMF demo data is mostly FY2017.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to audit; defaults to USMF.",
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
      "description": "Excel workbook name, e.g. 'audit-reopen-a-case-2026-05-24.xlsx'.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_reopen_a_case_agent.py` and embedded as the fenced Python below (sha256 05cbe9eee0c22d43…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_reopen_a_case_agent.py` first:

```bash
python3 audit_reopen_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_reopen_a_case_agent.py   # or on stdin
python3 audit_reopen_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reopen a case Completeness Audit — Audits reopen-a-case records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workboo

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-reopen-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_reopen_a_case',
    "version": '3.0.3',
    "display_name": 'Reopen a case Completeness Audit',
    "description": 'Audits reopen-a-case records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workboo',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-reopen-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-reopen-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'eb059468fee75744',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/reopen-a-case'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/audit-reopen-a-case', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for stale-date checks; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit; defaults to USMF.', 'output_filename': "Excel workbook name, e.g. 'audit-reopen-a-case-2026-05-24.xlsx'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit reopen a case records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to reopen a case. Output an Excel workbook 'audit-reopen-a-case-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no reopen a case data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads reopen a case records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits reopen-a-case records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workboo', 'example_request': 'Audit reopen-a-case records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Date range for stale-date checks; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': "Excel workbook name, e.g. 'audit-reopen-a-case-2026-05-24.xlsx'.", 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a completeness and policy-compliance audit of reopen-a-case records in D365 ERP, delivered as a multi-sheet Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditReopenACase(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditReopenACase'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for stale-date checks; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': "Excel workbook name, e.g. 'audit-reopen-a-case-2026-05-24.xlsx'.", 'type': 'string'}},
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
    print(AuditReopenACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
