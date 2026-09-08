---
name: "rar-cowork-cookbook-audit-plan-asset-leases"
description: "Runs a read-only completeness and policy audit of plan asset leases records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_asset_leases", "rar_sha256": "68283c175fe59be38aaf29e6fd3182e661204b3eb8cf3192984c6f6ee2677b63", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
