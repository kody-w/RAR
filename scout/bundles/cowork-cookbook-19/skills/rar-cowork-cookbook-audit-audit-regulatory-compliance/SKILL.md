---
name: "rar-cowork-cookbook-audit-audit-regulatory-compliance"
description: "Read-only audit of regulatory compliance records in Dynamics 365 F&SCM (via the Cowork ERP plugin) that flags missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, returning a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_audit_regulatory_compliance", "rar_sha256": "f6101b14ba180d7d31cc2cf76d6a035d041c0df65c7993eed1aa79b0b6d1add3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
