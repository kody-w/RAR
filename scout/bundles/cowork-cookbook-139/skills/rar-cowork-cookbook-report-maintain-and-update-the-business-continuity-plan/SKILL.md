---
name: "rar-cowork-cookbook-report-maintain-and-update-the-business-continuity-plan"
description: "Builds a read-only business continuity plan summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_maintain_and_update_the_business_continuity_plan", "rar_sha256": "006e0367513446457c15e539285fdceceb96642f0a0aef5eb1515d058f89c99b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
