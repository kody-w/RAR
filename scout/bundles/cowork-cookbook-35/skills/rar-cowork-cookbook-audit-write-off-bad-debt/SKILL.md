---
name: "rar-cowork-cookbook-audit-write-off-bad-debt"
description: "Read-only audit of write-off bad debt records in Dynamics 365 F&SCM for a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, output as an Exce"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_write_off_bad_debt", "rar_sha256": "133938e73d658743659d778dbf1c44b531f2e157c4fcf2ee8ffeb0d7ee079d6d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_write_off_bad_debt`. The original RAPP
agent is preserved byte-for-byte in `audit_write_off_bad_debt_agent.py` and in the RCI capsule.

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

Write off bad debt Completeness Audit — Read-only audit of write-off bad debt records in Dynamics 365 F&SCM for a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, output as an Exce

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-write-off-bad-debt
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
      "description": "Date range used to judge stale records; adjust for demo data that may be older (e.g. FY2017).",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-write-off-bad-debt-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_write_off_bad_debt_agent.py` and embedded as the fenced Python below (sha256 133938e73d658743…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_write_off_bad_debt_agent.py` first:

```bash
python3 audit_write_off_bad_debt_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_write_off_bad_debt_agent.py   # or on stdin
python3 audit_write_off_bad_debt_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Write off bad debt Completeness Audit — Read-only audit of write-off bad debt records in Dynamics 365 F&SCM for a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, output as an Exce

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-write-off-bad-debt
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_write_off_bad_debt',
    "version": '3.0.3',
    "display_name": 'Write off bad debt Completeness Audit',
    "description": 'Read-only audit of write-off bad debt records in Dynamics 365 F&SCM for a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, output as an Exce',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-write-off-bad-debt',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-write-off-bad-debt',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2bda81674d6eec7d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/write-off-bad-debt'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/audit-write-off-bad-debt', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale records; adjust for demo data that may be older (e.g. FY2017).', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-write-off-bad-debt-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit write off bad debt records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to write off bad debt. Output an Excel workbook 'audit-write-off-bad-debt-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no write off bad debt data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads write off bad debt records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Read-only audit of write-off bad debt records in Dynamics 365 F&SCM for a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, output as an Exce', 'example_request': 'Audit write-off bad debt records in USMF for completeness and give me the Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale records; adjust for demo data that may be older (e.g. FY2017).', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-write-off-bad-debt-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a completeness and policy-compliance check of write-off bad debt records in D365 ERP, delivered as a multi-sheet Excel workbook without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditWriteOffBadDebt(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditWriteOffBadDebt'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale records; adjust for demo data that may be older (e.g. FY2017).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-write-off-bad-debt-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditWriteOffBadDebt().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
