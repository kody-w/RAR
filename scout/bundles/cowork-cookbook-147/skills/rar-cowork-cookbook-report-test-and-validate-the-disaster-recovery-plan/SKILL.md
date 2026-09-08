---
name: "rar-cowork-cookbook-report-test-and-validate-the-disaster-recovery-plan"
description: "Builds a read-only summary report of disaster recovery plan testing and validation from Dynamics 365 F&SCM for a legal entity's most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sh"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_test_and_validate_the_disaster_recovery_plan", "rar_sha256": "cf636d7c79dbb51406bbe633eb3b406c0c9913153c09d8710440af8b8479c811", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
