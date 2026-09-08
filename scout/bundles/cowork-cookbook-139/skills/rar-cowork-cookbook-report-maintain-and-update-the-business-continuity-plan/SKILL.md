---
name: "rar-cowork-cookbook-report-maintain-and-update-the-business-continuity-plan"
description: "Builds a read-only business continuity plan summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_maintain_and_update_the_business_continuity_plan", "rar_sha256": "006e0367513446457c15e539285fdceceb96642f0a0aef5eb1515d058f89c99b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_maintain_and_update_the_business_continuity_plan`. The original RAPP
agent is preserved byte-for-byte in `report_maintain_and_update_the_business_continuity_plan_agent.py` and in the RCI capsule.

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

Maintain and update the business continuity plan Summary Report — Builds a read-only business continuity plan summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-maintain-and-update-the-business-continuity-plan
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
    "breakdown_dimensions": {
      "description": "Dimensions to break out by, such as department, category, or responsible owner, where applicable.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report against, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-maintain-and-update-the-business-continuity-plan-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to cover; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_maintain_and_update_the_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 006e036751344645…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_maintain_and_update_the_business_continuity_plan_agent.py` first:

```bash
python3 report_maintain_and_update_the_business_continuity_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_maintain_and_update_the_business_continuity_plan_agent.py   # or on stdin
python3 report_maintain_and_update_the_business_continuity_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain and update the business continuity plan Summary Report — Builds a read-only business continuity plan summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-maintain-and-update-the-business-continuity-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_maintain_and_update_the_business_continuity_plan',
    "version": '3.0.3',
    "display_name": 'Maintain and update the business continuity plan Summary Report',
    "description": 'Builds a read-only business continuity plan summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-maintain-and-update-the-business-continuity-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-maintain-and-update-the-business-continuity-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '90a054307805c8b0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/maintain-and-update-the-business-continuity-plan'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-maintain-and-update-the-business-continuity-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions to break out by, such as department, category, or responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-maintain-and-update-the-business-continuity-plan-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where maintain and update the business continuity plan stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of maintain and update the business continuity plan for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-maintain-and-update-the-business-continuity-plan-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads maintain and update the business continuity plan records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only business continuity plan summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a business continuity plan summary report for USMF from D365 for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-maintain-and-update-the-business-continuity-plan-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions to break out by, such as department, category, or responsible owner, where applicable.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals/trends/breakdown summary report of business continuity plan activity from Dynamics 365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportMaintainAndUpdateTheBusinessContinuityPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportMaintainAndUpdateTheBusinessContinuityPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions to break out by, such as department, category, or responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-maintain-and-update-the-business-continuity-plan-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportMaintainAndUpdateTheBusinessContinuityPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
