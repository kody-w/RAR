---
name: "rar-cowork-cookbook-audit-plan-asset-leases"
description: "Runs a read-only completeness and policy audit of plan asset leases records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_asset_leases", "rar_sha256": "68283c175fe59be38aaf29e6fd3182e661204b3eb8cf3192984c6f6ee2677b63", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_plan_asset_leases`. The original RAPP
agent is preserved byte-for-byte in `audit_plan_asset_leases_agent.py` and in the RCI capsule.

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

Plan asset leases Completeness Audit — Runs a read-only completeness and policy audit of plan asset leases records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-asset-leases
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
      "description": "Date range used to judge stale dates; adjust for demo tenants where data is mostly FY2017.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to audit, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-plan-asset-leases-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_plan_asset_leases_agent.py` and embedded as the fenced Python below (sha256 68283c175fe59be3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_plan_asset_leases_agent.py` first:

```bash
python3 audit_plan_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_plan_asset_leases_agent.py   # or on stdin
python3 audit_plan_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan asset leases Completeness Audit — Runs a read-only completeness and policy audit of plan asset leases records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_plan_asset_leases',
    "version": '3.0.3',
    "display_name": 'Plan asset leases Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of plan asset leases records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-plan-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-plan-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e8d55f68b95e7453',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/plan-asset-leases'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/audit-plan-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; adjust for demo tenants where data is mostly FY2017.', 'legal_entity': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-plan-asset-leases-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit plan asset leases records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to plan asset leases. Output an Excel workbook 'audit-plan-asset-leases-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no plan asset leases data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan asset leases records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of plan asset leases records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit plan asset leases in USMF for completeness and export the findings to an Excel workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; adjust for demo tenants where data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-plan-asset-leases-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants plan asset leases records checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditPlanAssetLeases(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPlanAssetLeases'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; adjust for demo tenants where data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-plan-asset-leases-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditPlanAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
