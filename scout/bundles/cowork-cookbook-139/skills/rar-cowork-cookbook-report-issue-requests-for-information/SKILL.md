---
name: "rar-cowork-cookbook-report-issue-requests-for-information"
description: "Builds a read-only summary report of issue requests for information from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_issue_requests_for_information", "rar_sha256": "041f7eba54651c13df0dea752422792c9b67f4acb6d2132d5417474c05209d23", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
