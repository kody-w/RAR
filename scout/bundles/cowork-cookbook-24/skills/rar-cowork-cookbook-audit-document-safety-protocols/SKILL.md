---
name: "rar-cowork-cookbook-audit-document-safety-protocols"
description: "Read-only audit of document safety protocols records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_document_safety_protocols", "rar_sha256": "86031a57a192d0e6a3b03044467ad7d64768dcdff42b10cff4d5e858a9471691", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
