---
name: "rar-cowork-cookbook-audit-evaluate-supplier-bids"
description: "Runs a read-only completeness and policy audit of supplier bid evaluation records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_evaluate_supplier_bids", "rar_sha256": "8ed995c3aeb5cf0e4eb265a55ab9bd770cafe66a79ca1d0a014936bba2ec2772", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
