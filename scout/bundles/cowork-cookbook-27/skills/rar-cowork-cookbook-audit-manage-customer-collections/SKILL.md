---
name: "rar-cowork-cookbook-audit-manage-customer-collections"
description: "Audits customer collections records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive references and policy violations, returning an Excel workbook with one"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_customer_collections", "rar_sha256": "c0a128a1fed43d986fcf37165af98191b68772d77f7f59e3a0cb82e3822c3d52", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
