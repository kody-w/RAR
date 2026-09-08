---
name: "rar-cowork-cookbook-audit-plan-risks-and-opportunities"
description: "Runs a read-only completeness and policy audit of Dynamics 365 plan risks and opportunities records for a legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_risks_and_opportunities", "rar_sha256": "69e6430e460565fa1e4a0372e7f9e7f9c4927d297d6ee4d2bcfedbf51108f8fe", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
