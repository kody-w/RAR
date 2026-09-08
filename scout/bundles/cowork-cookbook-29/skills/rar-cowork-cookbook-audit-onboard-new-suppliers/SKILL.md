---
name: "rar-cowork-cookbook-audit-onboard-new-suppliers"
description: "Audits new-supplier onboarding records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workbo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_onboard_new_suppliers", "rar_sha256": "3ebbf67a3bcd1357e2c585a70d1799fee4e3ec4423152d6435a209740f157ea2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_onboard_new_suppliers`. The original RAPP
agent is preserved byte-for-byte in `audit_onboard_new_suppliers_agent.py` and in the RCI capsule.

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

Onboard new suppliers Completeness Audit — Audits new-supplier onboarding records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workbo

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-onboard-new-suppliers
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
      "description": "Name of the Excel workbook to produce, e.g. audit-onboard-new-suppliers-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_onboard_new_suppliers_agent.py` and embedded as the fenced Python below (sha256 3ebbf67a3bcd1357…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_onboard_new_suppliers_agent.py` first:

```bash
python3 audit_onboard_new_suppliers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_onboard_new_suppliers_agent.py   # or on stdin
python3 audit_onboard_new_suppliers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard new suppliers Completeness Audit — Audits new-supplier onboarding records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workbo

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-onboard-new-suppliers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_onboard_new_suppliers',
    "version": '3.0.3',
    "display_name": 'Onboard new suppliers Completeness Audit',
    "description": 'Audits new-supplier onboarding records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workbo',
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
        "upstream_slug": 'audit-onboard-new-suppliers',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-onboard-new-suppliers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'df5998672b9f08fe',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/onboard-new-suppliers'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/audit-onboard-new-suppliers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-onboard-new-suppliers-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit onboard new suppliers records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to onboard new suppliers. Output an Excel workbook 'audit-onboard-new-suppliers-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no onboard new suppliers data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads onboard new suppliers records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits new-supplier onboarding records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workbo', 'example_request': 'Audit our new supplier onboarding records in USMF for completeness and give me the findings as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-onboard-new-suppliers-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy compliance audit of supplier onboarding records in D365 ERP, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditOnboardNewSuppliers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditOnboardNewSuppliers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-onboard-new-suppliers-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditOnboardNewSuppliers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
