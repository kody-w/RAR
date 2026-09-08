---
name: "rar-cowork-cookbook-audit-coordinate-service-work-with-customer"
description: "Runs a read-only completeness and policy audit of coordinate service work with customer records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin, returning an Excel workbook of findings."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_coordinate_service_work_with_customer", "rar_sha256": "dddb4f1abb889c2ddb5d62b56ed341203ca0c61f4898cd5e70e2e1e7de530418", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
