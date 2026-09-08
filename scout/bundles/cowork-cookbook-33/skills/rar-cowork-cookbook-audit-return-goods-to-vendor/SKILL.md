---
name: "rar-cowork-cookbook-audit-return-goods-to-vendor"
description: "Audits return-goods-to-vendor records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workboo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_return_goods_to_vendor", "rar_sha256": "df262eb2b8227502272d15fba427cae35ff1c2239eb44279473299ad171ba794", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
