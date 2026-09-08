---
name: "rar-cowork-cookbook-audit-plan-projects-resources"
description: "Read-only audit of Dynamics 365 F&SCM plan projects resources records in a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references and policy violations as an Excel workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_projects_resources", "rar_sha256": "9350bbdef5a8a04a6d227068cea49316b1e13cc4a1f0b7ee1941aa841c94571a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_plan_projects_resources`. The original RAPP
agent is preserved byte-for-byte in `audit_plan_projects_resources_agent.py` and in the RCI capsule.

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

Plan projects resources Completeness Audit — Read-only audit of Dynamics 365 F&SCM plan projects resources records in a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references and policy violations as an Excel workbook.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-projects-resources
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
      "description": "Date range used to judge stale dates; adjust for demo data vintage (e.g. FY2017 for USMF).",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-plan-projects-resources-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_plan_projects_resources_agent.py` and embedded as the fenced Python below (sha256 9350bbdef5a8a04a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_plan_projects_resources_agent.py` first:

```bash
python3 audit_plan_projects_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_plan_projects_resources_agent.py   # or on stdin
python3 audit_plan_projects_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan projects resources Completeness Audit — Read-only audit of Dynamics 365 F&SCM plan projects resources records in a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references and policy violations as an Excel workbook.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-projects-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_plan_projects_resources',
    "version": '3.0.3',
    "display_name": 'Plan projects resources Completeness Audit',
    "description": 'Read-only audit of Dynamics 365 F&SCM plan projects resources records in a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references and policy violations as an Excel workbook.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-plan-projects-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-plan-projects-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c7a39bce70ade6d0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/plan-projects-resources'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/audit-plan-projects-resources', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; adjust for demo data vintage (e.g. FY2017 for USMF).', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-plan-projects-resources-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit plan projects resources records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to plan projects resources. Output an Excel workbook 'audit-plan-projects-resources-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no plan projects resources data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan projects resources records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Read-only audit of Dynamics 365 F&SCM plan projects resources records in a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references and policy violations as an Excel workbook.', 'example_request': 'Audit plan projects resources in USMF for completeness and export the findings to an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; adjust for demo data vintage (e.g. FY2017 for USMF).', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-plan-projects-resources-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a completeness and policy-compliance audit of plan projects resources data in D365 F&SCM, delivered as a multi-sheet Excel report with counts.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditPlanProjectsResources(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPlanProjectsResources'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; adjust for demo data vintage (e.g. FY2017 for USMF).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-plan-projects-resources-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditPlanProjectsResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
