---
name: "rar-cowork-cookbook-audit-manage-customer-collections"
description: "Audits customer collections records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive references and policy violations, returning an Excel workbook with one"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_customer_collections", "rar_sha256": "c0a128a1fed43d986fcf37165af98191b68772d77f7f59e3a0cb82e3822c3d52", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_manage_customer_collections`. The original RAPP
agent is preserved byte-for-byte in `audit_manage_customer_collections_agent.py` and in the RCI capsule.

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

Manage customer collections Completeness Audit — Audits customer collections records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive references and policy violations, returning an Excel workbook with one

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-customer-collections
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
      "description": "Date range for stale-date checks; USMF demo data is mostly FY2017.",
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
      "description": "Excel workbook name, e.g. audit-manage-customer-collections-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_customer_collections_agent.py` and embedded as the fenced Python below (sha256 c0a128a1fed43d98…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_customer_collections_agent.py` first:

```bash
python3 audit_manage_customer_collections_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_manage_customer_collections_agent.py   # or on stdin
python3 audit_manage_customer_collections_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage customer collections Completeness Audit — Audits customer collections records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive references and policy violations, returning an Excel workbook with one

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-customer-collections
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_manage_customer_collections',
    "version": '3.0.3',
    "display_name": 'Manage customer collections Completeness Audit',
    "description": 'Audits customer collections records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive references and policy violations, returning an Excel workbook with one',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-manage-customer-collections',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-manage-customer-collections',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a9ee946af220e458',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/manage-customer-collections'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/audit-manage-customer-collections', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for stale-date checks; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit; the recipe uses USMF.', 'output_filename': 'Excel workbook name, e.g. audit-manage-customer-collections-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit manage customer collections records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to manage customer collections. Output an Excel workbook 'audit-manage-customer-collections-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no manage customer collections data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage customer collections records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits customer collections records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive references and policy violations, returning an Excel workbook with one', 'example_request': 'Audit USMF customer collections records for completeness and give me the findings as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit; the recipe uses USMF.', 'name': 'legal_entity'}, {'description': 'Date range for stale-date checks; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Excel workbook name, e.g. audit-manage-customer-collections-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy compliance audit of D365 customer collections data delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditManageCustomerCollections(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditManageCustomerCollections'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for stale-date checks; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit; the recipe uses USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. audit-manage-customer-collections-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditManageCustomerCollections().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
