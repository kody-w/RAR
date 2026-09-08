---
name: "rar-cowork-cookbook-audit-reopen-a-case"
description: "Audits reopen-a-case records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workboo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_reopen_a_case", "rar_sha256": "05cbe9eee0c22d43fc7df014a1cccaec8354466eb1d0ecc1f4bf2ae149d854fe", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
