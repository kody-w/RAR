---
name: "rar-cowork-cookbook-audit-manage-promissory-notes"
description: "Audits Dynamics 365 promissory note records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_promissory_notes", "rar_sha256": "96668b8362cbf53578498528f24b8a12b7dff5ea849317c4198c07389da739bc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_manage_promissory_notes`. The original RAPP
agent is preserved byte-for-byte in `audit_manage_promissory_notes_agent.py` and in the RCI capsule.

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

Manage promissory notes Completeness Audit — Audits Dynamics 365 promissory note records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-promissory-notes
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
      "description": "Name of the Excel workbook to produce, e.g. audit-manage-promissory-notes-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_promissory_notes_agent.py` and embedded as the fenced Python below (sha256 96668b8362cbf535…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_promissory_notes_agent.py` first:

```bash
python3 audit_manage_promissory_notes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_manage_promissory_notes_agent.py   # or on stdin
python3 audit_manage_promissory_notes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage promissory notes Completeness Audit — Audits Dynamics 365 promissory note records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-promissory-notes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_manage_promissory_notes',
    "version": '3.0.3',
    "display_name": 'Manage promissory notes Completeness Audit',
    "description": 'Audits Dynamics 365 promissory note records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of counts.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-manage-promissory-notes',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-manage-promissory-notes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd407eefb2621e5a9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/manage-promissory-notes'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/audit-manage-promissory-notes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-manage-promissory-notes-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit manage promissory notes records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to manage promissory notes. Output an Excel workbook 'audit-manage-promissory-notes-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no manage promissory notes data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads manage promissory notes records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits Dynamics 365 promissory note records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit promissory notes in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-manage-promissory-notes-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy audit of promissory notes data in Dynamics 365 F&SCM via the Cowork ERP plugin.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditManagePromissoryNotes(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditManagePromissoryNotes'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-manage-promissory-notes-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditManagePromissoryNotes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
