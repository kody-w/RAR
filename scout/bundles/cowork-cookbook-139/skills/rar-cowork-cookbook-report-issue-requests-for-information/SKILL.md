---
name: "rar-cowork-cookbook-report-issue-requests-for-information"
description: "Builds a read-only summary report of issue requests for information from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_issue_requests_for_information", "rar_sha256": "041f7eba54651c13df0dea752422792c9b67f4acb6d2132d5417474c05209d23", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_issue_requests_for_information`. The original RAPP
agent is preserved byte-for-byte in `report_issue_requests_for_information_agent.py` and in the RCI capsule.

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

Issue requests for information Summary Report — Builds a read-only summary report of issue requests for information from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-issue-requests-for-information
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
      "description": "Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-issue-requests-for-information-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to cover; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_issue_requests_for_information_agent.py` and embedded as the fenced Python below (sha256 041f7eba54651c13…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_issue_requests_for_information_agent.py` first:

```bash
python3 report_issue_requests_for_information_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_issue_requests_for_information_agent.py   # or on stdin
python3 report_issue_requests_for_information_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue requests for information Summary Report — Builds a read-only summary report of issue requests for information from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-issue-requests-for-information
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_issue_requests_for_information',
    "version": '3.0.3',
    "display_name": 'Issue requests for information Summary Report',
    "description": 'Builds a read-only summary report of issue requests for information from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-issue-requests-for-information',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-issue-requests-for-information',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '36a15520df4b4b9b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/issue-requests-for-information'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/report-issue-requests-for-information', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-issue-requests-for-information-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where issue requests for information stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of issue requests for information for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-issue-requests-for-information-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads issue requests for information records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of issue requests for information from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build an issue requests for information summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available in the tenant.', 'name': 'period'}, {'description': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-issue-requests-for-information-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals, trends, and by-dimension breakdown report of issue requests for information from D365 ERP data, exported to Excel.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportIssueRequestsForInformation(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportIssueRequestsForInformation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-issue-requests-for-information-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportIssueRequestsForInformation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
