---
name: "rar-cowork-cookbook-report-test-and-validate-the-disaster-recovery-plan"
description: "Builds a read-only summary report of disaster recovery plan testing and validation from Dynamics 365 F&SCM for a legal entity's most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sh"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_test_and_validate_the_disaster_recovery_plan", "rar_sha256": "cf636d7c79dbb51406bbe633eb3b406c0c9913153c09d8710440af8b8479c811", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_test_and_validate_the_disaster_recovery_plan`. The original RAPP
agent is preserved byte-for-byte in `report_test_and_validate_the_disaster_recovery_plan_agent.py` and in the RCI capsule.

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

Test and validate the disaster recovery plan Summary Report — Builds a read-only summary report of disaster recovery plan testing and validation from Dynamics 365 F&SCM for a legal entity's most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sh

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
  Upstream entry : https://coworkcookbook.com/recipes/report-test-and-validate-the-disaster-recovery-plan
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
      "description": "Dimensions to break totals down by, such as department, category, or responsible owner, where applicable.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-test-and-validate-the-disaster-recovery-plan-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to summarize; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_test_and_validate_the_disaster_recovery_plan_agent.py` and embedded as the fenced Python below (sha256 cf636d7c79dbb514…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_test_and_validate_the_disaster_recovery_plan_agent.py` first:

```bash
python3 report_test_and_validate_the_disaster_recovery_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_test_and_validate_the_disaster_recovery_plan_agent.py   # or on stdin
python3 report_test_and_validate_the_disaster_recovery_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Test and validate the disaster recovery plan Summary Report — Builds a read-only summary report of disaster recovery plan testing and validation from Dynamics 365 F&SCM for a legal entity's most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sh

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
  Upstream entry : https://coworkcookbook.com/recipes/report-test-and-validate-the-disaster-recovery-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_test_and_validate_the_disaster_recovery_plan',
    "version": '3.0.3',
    "display_name": 'Test and validate the disaster recovery plan Summary Report',
    "description": "Builds a read-only summary report of disaster recovery plan testing and validation from Dynamics 365 F&SCM for a legal entity's most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sh",
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
        "upstream_slug": 'report-test-and-validate-the-disaster-recovery-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-test-and-validate-the-disaster-recovery-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3a121ad78cbde827',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/test-and-validate-the-disaster-recovery-plan'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-test-and-validate-the-disaster-recovery-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions to break totals down by, such as department, category, or responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-test-and-validate-the-disaster-recovery-plan-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where test and validate the disaster recovery plan stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of test and validate the disaster recovery plan for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-test-and-validate-the-disaster-recovery-plan-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads test and validate the disaster recovery plan records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Builds a read-only summary report of disaster recovery plan testing and validation from Dynamics 365 F&SCM for a legal entity's most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sh", 'example_request': "Build a disaster recovery plan test summary report from D365 for USMF's latest posted period as an Excel workbook.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available in the tenant.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-test-and-validate-the-disaster-recovery-plan-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions to break totals down by, such as department, category, or responsible owner, where applicable.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals, breakdown, and Top 10 by value summary report of disaster recovery plan test/validation activity from D365 ERP data, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportTestAndValidateTheDisasterRecoveryPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportTestAndValidateTheDisasterRecoveryPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions to break totals down by, such as department, category, or responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-test-and-validate-the-disaster-recovery-plan-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportTestAndValidateTheDisasterRecoveryPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
