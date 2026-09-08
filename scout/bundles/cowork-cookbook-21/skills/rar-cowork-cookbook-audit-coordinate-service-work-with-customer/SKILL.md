---
name: "rar-cowork-cookbook-audit-coordinate-service-work-with-customer"
description: "Runs a read-only completeness and policy audit of coordinate service work with customer records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin, returning an Excel workbook of findings."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_coordinate_service_work_with_customer", "rar_sha256": "dddb4f1abb889c2ddb5d62b56ed341203ca0c61f4898cd5e70e2e1e7de530418", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_coordinate_service_work_with_customer`. The original RAPP
agent is preserved byte-for-byte in `audit_coordinate_service_work_with_customer_agent.py` and in the RCI capsule.

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

Coordinate service work with customer Completeness Audit — Runs a read-only completeness and policy audit of coordinate service work with customer records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin, returning an Excel workbook of findings.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-coordinate-service-work-with-customer
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
      "description": "Dynamics 365 legal entity to audit; the recipe uses USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-coordinate-service-work-with-customer-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_coordinate_service_work_with_customer_agent.py` and embedded as the fenced Python below (sha256 dddb4f1abb889c2d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_coordinate_service_work_with_customer_agent.py` first:

```bash
python3 audit_coordinate_service_work_with_customer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_coordinate_service_work_with_customer_agent.py   # or on stdin
python3 audit_coordinate_service_work_with_customer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Coordinate service work with customer Completeness Audit — Runs a read-only completeness and policy audit of coordinate service work with customer records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin, returning an Excel workbook of findings.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-coordinate-service-work-with-customer
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_coordinate_service_work_with_customer',
    "version": '3.0.2',
    "display_name": 'Coordinate service work with customer Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of coordinate service work with customer records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin, returning an Excel workbook of findings.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-coordinate-service-work-with-customer',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-coordinate-service-work-with-customer',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9963db722fc51439',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/coordinate-service-work-with-customer'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/audit-coordinate-service-work-with-customer', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'legal_entity': 'Dynamics 365 legal entity to audit; the recipe uses USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-coordinate-service-work-with-customer-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit coordinate service work with customer records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to coordinate service work with customer. Output an Excel workbook 'audit-coordinate-service-work-with-customer-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no coordinate service work with customer data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads coordinate service work with customer records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of coordinate service work with customer records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin, returning an Excel workbook of findings.', 'example_request': 'Audit coordinate service work with customer records in USMF for completeness and export the findings workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to audit; the recipe uses USMF.', 'name': 'legal_entity'}, {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-coordinate-service-work-with-customer-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to check coordinate service work with customer records in USMF for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditCoordinateServiceWorkWithCustomer(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditCoordinateServiceWorkWithCustomer'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to audit; the recipe uses USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-coordinate-service-work-with-customer-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditCoordinateServiceWorkWithCustomer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
