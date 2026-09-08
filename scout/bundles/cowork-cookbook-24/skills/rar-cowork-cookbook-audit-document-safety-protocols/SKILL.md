---
name: "rar-cowork-cookbook-audit-document-safety-protocols"
description: "Read-only audit of document safety protocols records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_document_safety_protocols", "rar_sha256": "86031a57a192d0e6a3b03044467ad7d64768dcdff42b10cff4d5e858a9471691", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_document_safety_protocols`. The original RAPP
agent is preserved byte-for-byte in `audit_document_safety_protocols_agent.py` and in the RCI capsule.

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

Document safety protocols Completeness Audit — Read-only audit of document safety protocols records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-document-safety-protocols
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
      "description": "Date range used to judge stale dates; adjust for demo data vintage (USMF is mostly FY2017).",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-document-safety-protocols-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_document_safety_protocols_agent.py` and embedded as the fenced Python below (sha256 86031a57a192d0e6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_document_safety_protocols_agent.py` first:

```bash
python3 audit_document_safety_protocols_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_document_safety_protocols_agent.py   # or on stdin
python3 audit_document_safety_protocols_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Document safety protocols Completeness Audit — Read-only audit of document safety protocols records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-document-safety-protocols
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_document_safety_protocols',
    "version": '3.0.2',
    "display_name": 'Document safety protocols Completeness Audit',
    "description": 'Read-only audit of document safety protocols records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.',
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
        "upstream_slug": 'audit-document-safety-protocols',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-document-safety-protocols',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7a9a14e7f554f77f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/document-safety-protocols'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-document-safety-protocols', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; adjust for demo data vintage (USMF is mostly FY2017).', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-document-safety-protocols-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit document safety protocols records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to document safety protocols. Output an Excel workbook 'audit-document-safety-protocols-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no document safety protocols data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads document safety protocols records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Read-only audit of document safety protocols records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit document safety protocols records in USMF for completeness and give me the Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; adjust for demo data vintage (USMF is mostly FY2017).', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-document-safety-protocols-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to check document safety protocols records for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditDocumentSafetyProtocols(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDocumentSafetyProtocols'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; adjust for demo data vintage (USMF is mostly FY2017).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-document-safety-protocols-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditDocumentSafetyProtocols().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
