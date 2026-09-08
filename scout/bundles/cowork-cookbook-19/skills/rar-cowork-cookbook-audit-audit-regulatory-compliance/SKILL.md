---
name: "rar-cowork-cookbook-audit-audit-regulatory-compliance"
description: "Read-only audit of regulatory compliance records in Dynamics 365 F&SCM (via the Cowork ERP plugin) that flags missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, returning a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_audit_regulatory_compliance", "rar_sha256": "f6101b14ba180d7d31cc2cf76d6a035d041c0df65c7993eed1aa79b0b6d1add3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_audit_regulatory_compliance`. The original RAPP
agent is preserved byte-for-byte in `audit_audit_regulatory_compliance_agent.py` and in the RCI capsule.

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

Audit regulatory compliance Completeness Audit — Read-only audit of regulatory compliance records in Dynamics 365 F&SCM (via the Cowork ERP plugin) that flags missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, returning a

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-audit-regulatory-compliance
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
      "description": "Date range for staleness checks; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-audit-regulatory-compliance-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_audit_regulatory_compliance_agent.py` and embedded as the fenced Python below (sha256 f6101b14ba180d7d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_audit_regulatory_compliance_agent.py` first:

```bash
python3 audit_audit_regulatory_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_audit_regulatory_compliance_agent.py   # or on stdin
python3 audit_audit_regulatory_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Audit regulatory compliance Completeness Audit — Read-only audit of regulatory compliance records in Dynamics 365 F&SCM (via the Cowork ERP plugin) that flags missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, returning a

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-audit-regulatory-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_audit_regulatory_compliance',
    "version": '3.0.2',
    "display_name": 'Audit regulatory compliance Completeness Audit',
    "description": 'Read-only audit of regulatory compliance records in Dynamics 365 F&SCM (via the Cowork ERP plugin) that flags missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, returning a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-audit-regulatory-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-audit-regulatory-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '84409bd331627bd0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/audit-regulatory-compliance'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/audit-audit-regulatory-compliance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-audit-regulatory-compliance-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit audit regulatory compliance records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to audit regulatory compliance. Output an Excel workbook 'audit-audit-regulatory-compliance-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no audit regulatory compliance data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads audit regulatory compliance records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Read-only audit of regulatory compliance records in Dynamics 365 F&SCM (via the Cowork ERP plugin) that flags missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, returning a', 'example_request': 'Audit regulatory compliance records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-audit-regulatory-compliance-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a completeness and policy-compliance audit of D365 regulatory compliance records for a legal entity, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditAuditRegulatoryCompliance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAuditRegulatoryCompliance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-audit-regulatory-compliance-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditAuditRegulatoryCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
