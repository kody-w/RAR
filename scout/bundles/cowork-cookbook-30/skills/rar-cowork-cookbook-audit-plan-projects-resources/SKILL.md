---
name: "rar-cowork-cookbook-audit-plan-projects-resources"
description: "Read-only audit of Dynamics 365 F&SCM plan projects resources records in a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references and policy violations as an Excel workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_projects_resources", "rar_sha256": "9350bbdef5a8a04a6d227068cea49316b1e13cc4a1f0b7ee1941aa841c94571a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
