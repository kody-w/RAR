---
name: "rar-cowork-cookbook-audit-write-off-bad-debt"
description: "Read-only audit of write-off bad debt records in Dynamics 365 F&SCM for a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, output as an Exce"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_write_off_bad_debt", "rar_sha256": "133938e73d658743659d778dbf1c44b531f2e157c4fcf2ee8ffeb0d7ee079d6d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
