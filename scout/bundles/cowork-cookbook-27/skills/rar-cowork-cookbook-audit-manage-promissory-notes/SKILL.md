---
name: "rar-cowork-cookbook-audit-manage-promissory-notes"
description: "Audits Dynamics 365 promissory note records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_promissory_notes", "rar_sha256": "96668b8362cbf53578498528f24b8a12b7dff5ea849317c4198c07389da739bc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
