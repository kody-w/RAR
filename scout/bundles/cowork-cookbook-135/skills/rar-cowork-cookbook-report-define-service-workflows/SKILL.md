---
name: "rar-cowork-cookbook-report-define-service-workflows"
description: "Builds a read-only summary report of define service workflows activity from Dynamics 365 F&SCM for a legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_service_workflows", "rar_sha256": "5740e1029c6163b70704e29c057d34bdc5d77a66baab557d1320f81604151634", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_service_workflows`. The original RAPP
agent is preserved byte-for-byte in `report_define_service_workflows_agent.py` and in the RCI capsule.

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

Define service workflows Summary Report — Builds a read-only summary report of define service workflows activity from Dynamics 365 F&SCM for a legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-service-workflows
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
      "description": "Dimensions for breakdowns where applicable: department, category, responsible owner.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-define-service-workflows-2026-05-24.xlsx.",
      "type": "string"
    },
    "posted_period": {
      "description": "The posted period to cover; defaults to the most recent available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_service_workflows_agent.py` and embedded as the fenced Python below (sha256 5740e1029c6163b7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_service_workflows_agent.py` first:

```bash
python3 report_define_service_workflows_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_service_workflows_agent.py   # or on stdin
python3 report_define_service_workflows_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define service workflows Summary Report — Builds a read-only summary report of define service workflows activity from Dynamics 365 F&SCM for a legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-service-workflows
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_service_workflows',
    "version": '3.0.3',
    "display_name": 'Define service workflows Summary Report',
    "description": 'Builds a read-only summary report of define service workflows activity from Dynamics 365 F&SCM for a legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-define-service-workflows',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-service-workflows',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dbb4a4cc4cd76f4f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/define-service-workflows'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/report-define-service-workflows', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-define-service-workflows-2026-05-24.xlsx.', 'posted_period': 'The posted period to cover; defaults to the most recent available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where define service workflows stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of define service workflows for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-define-service-workflows-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define service workflows records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of define service workflows activity from Dynamics 365 F&SCM for a legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a define service workflows summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'The posted period to cover; defaults to the most recent available in the tenant.', 'name': 'posted_period'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-define-service-workflows-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write D365 ERP summary of define service workflows activity with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDefineServiceWorkflows(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineServiceWorkflows'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-define-service-workflows-2026-05-24.xlsx.', 'type': 'string'}, 'posted_period': {'description': 'The posted period to cover; defaults to the most recent available in the tenant.', 'type': 'string'}},
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
    print(ReportDefineServiceWorkflows().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
