---
name: "rar-cowork-cookbook-audit-evaluate-supplier-bids"
description: "Runs a read-only completeness and policy audit of supplier bid evaluation records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_evaluate_supplier_bids", "rar_sha256": "8ed995c3aeb5cf0e4eb265a55ab9bd770cafe66a79ca1d0a014936bba2ec2772", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_evaluate_supplier_bids`. The original RAPP
agent is preserved byte-for-byte in `audit_evaluate_supplier_bids_agent.py` and in the RCI capsule.

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

Evaluate supplier bids Completeness Audit — Runs a read-only completeness and policy audit of supplier bid evaluation records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-evaluate-supplier-bids
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
      "description": "Date range treated as current vs stale; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-evaluate-supplier-bids-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_evaluate_supplier_bids_agent.py` and embedded as the fenced Python below (sha256 8ed995c3aeb5cf0e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_evaluate_supplier_bids_agent.py` first:

```bash
python3 audit_evaluate_supplier_bids_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_evaluate_supplier_bids_agent.py   # or on stdin
python3 audit_evaluate_supplier_bids_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Evaluate supplier bids Completeness Audit — Runs a read-only completeness and policy audit of supplier bid evaluation records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-evaluate-supplier-bids
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_evaluate_supplier_bids',
    "version": '3.0.2',
    "display_name": 'Evaluate supplier bids Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of supplier bid evaluation records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.',
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
        "upstream_slug": 'audit-evaluate-supplier-bids',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-evaluate-supplier-bids',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bb0f920e333ff538',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/evaluate-supplier-bids'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/audit-evaluate-supplier-bids', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range treated as current vs stale; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-evaluate-supplier-bids-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit evaluate supplier bids records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to evaluate supplier bids. Output an Excel workbook 'audit-evaluate-supplier-bids-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no evaluate supplier bids data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads evaluate supplier bids records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of supplier bid evaluation records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.', 'example_request': 'Audit supplier bid evaluation records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range treated as current vs stale; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-evaluate-supplier-bids-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants supplier bid evaluation records checked for missing fields, stale dates, blank descriptions, inactive entity references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditEvaluateSupplierBids(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditEvaluateSupplierBids'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range treated as current vs stale; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-evaluate-supplier-bids-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditEvaluateSupplierBids().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
