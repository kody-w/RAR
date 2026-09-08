---
name: "rar-cowork-cookbook-audit-return-goods-to-vendor"
description: "Audits return-goods-to-vendor records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workboo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_return_goods_to_vendor", "rar_sha256": "df262eb2b8227502272d15fba427cae35ff1c2239eb44279473299ad171ba794", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_return_goods_to_vendor`. The original RAPP
agent is preserved byte-for-byte in `audit_return_goods_to_vendor_agent.py` and in the RCI capsule.

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

Return goods to vendor Completeness Audit — Audits return-goods-to-vendor records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workboo

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-return-goods-to-vendor
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
      "description": "Date range for stale-date checks; USMF demo data is mostly FY2017, so adjust accordingly.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to audit; the recipe uses USMF.",
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
      "description": "Excel workbook name, e.g. audit-return-goods-to-vendor-2026-05-24.xlsx, saved to Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_return_goods_to_vendor_agent.py` and embedded as the fenced Python below (sha256 df262eb2b8227502…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_return_goods_to_vendor_agent.py` first:

```bash
python3 audit_return_goods_to_vendor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_return_goods_to_vendor_agent.py   # or on stdin
python3 audit_return_goods_to_vendor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Return goods to vendor Completeness Audit — Audits return-goods-to-vendor records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workboo

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-return-goods-to-vendor
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_return_goods_to_vendor',
    "version": '3.0.3',
    "display_name": 'Return goods to vendor Completeness Audit',
    "description": 'Audits return-goods-to-vendor records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workboo',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-return-goods-to-vendor',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-return-goods-to-vendor',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '937e41ac0ab7f771',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/return-goods-to-vendor'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/audit-return-goods-to-vendor', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for stale-date checks; USMF demo data is mostly FY2017, so adjust accordingly.', 'legal_entity': 'D365 legal entity to audit; the recipe uses USMF.', 'output_filename': 'Excel workbook name, e.g. audit-return-goods-to-vendor-2026-05-24.xlsx, saved to Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit return goods to vendor records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to return goods to vendor. Output an Excel workbook 'audit-return-goods-to-vendor-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no return goods to vendor data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads return goods to vendor records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits return-goods-to-vendor records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workboo', 'example_request': 'Audit return goods to vendor records in USMF for completeness and export the findings to an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit; the recipe uses USMF.', 'name': 'legal_entity'}, {'description': 'Date range for stale-date checks; USMF demo data is mostly FY2017, so adjust accordingly.', 'name': 'date_window'}, {'description': 'Excel workbook name, e.g. audit-return-goods-to-vendor-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need a read-only completeness and policy-compliance audit of return-goods-to-vendor records in D365 F&SCM, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditReturnGoodsToVendor(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditReturnGoodsToVendor'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for stale-date checks; USMF demo data is mostly FY2017, so adjust accordingly.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit; the recipe uses USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. audit-return-goods-to-vendor-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'type': 'string'}},
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
    print(AuditReturnGoodsToVendor().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
