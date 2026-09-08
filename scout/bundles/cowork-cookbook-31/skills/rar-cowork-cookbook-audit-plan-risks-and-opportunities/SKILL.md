---
name: "rar-cowork-cookbook-audit-plan-risks-and-opportunities"
description: "Runs a read-only completeness and policy audit of Dynamics 365 plan risks and opportunities records for a legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_risks_and_opportunities", "rar_sha256": "69e6430e460565fa1e4a0372e7f9e7f9c4927d297d6ee4d2bcfedbf51108f8fe", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_plan_risks_and_opportunities`. The original RAPP
agent is preserved byte-for-byte in `audit_plan_risks_and_opportunities_agent.py` and in the RCI capsule.

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

Plan risks and opportunities Completeness Audit — Runs a read-only completeness and policy audit of Dynamics 365 plan risks and opportunities records for a legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-risks-and-opportunities
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
      "description": "Date range used to judge stale dates; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-plan-risks-and-opportunities-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_plan_risks_and_opportunities_agent.py` and embedded as the fenced Python below (sha256 69e6430e460565fa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_plan_risks_and_opportunities_agent.py` first:

```bash
python3 audit_plan_risks_and_opportunities_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_plan_risks_and_opportunities_agent.py   # or on stdin
python3 audit_plan_risks_and_opportunities_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan risks and opportunities Completeness Audit — Runs a read-only completeness and policy audit of Dynamics 365 plan risks and opportunities records for a legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-risks-and-opportunities
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_plan_risks_and_opportunities',
    "version": '3.0.3',
    "display_name": 'Plan risks and opportunities Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of Dynamics 365 plan risks and opportunities records for a legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-plan-risks-and-opportunities',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-plan-risks-and-opportunities',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bf149b3d8257eff7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-risks-and-opportunities'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/audit-plan-risks-and-opportunities', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-plan-risks-and-opportunities-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit plan risks and opportunities records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to plan risks and opportunities. Output an Excel workbook 'audit-plan-risks-and-opportunities-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no plan risks and opportunities data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan risks and opportunities records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of Dynamics 365 plan risks and opportunities records for a legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit plan risks and opportunities in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-plan-risks-and-opportunities-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants plan risks and opportunities records in Dynamics 365 F&SCM checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditPlanRisksAndOpportunities(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPlanRisksAndOpportunities'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-plan-risks-and-opportunities-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditPlanRisksAndOpportunities().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
