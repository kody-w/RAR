---
name: "rar-cowork-cookbook-report-report-quality-non-conformance"
description: "Builds a read-only summary report of quality non-conformance activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top 10 by valu"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_report_quality_non_conformance", "rar_sha256": "e3fed605ee3eec314e8183d812162582804b7493118c84831b1fa1d9acab513b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_report_quality_non_conformance`. The original RAPP
agent is preserved byte-for-byte in `report_report_quality_non_conformance_agent.py` and in the RCI capsule.

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

Report quality non-conformance Summary Report — Builds a read-only summary report of quality non-conformance activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top 10 by valu

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
  Upstream entry : https://coworkcookbook.com/recipes/report-report-quality-non-conformance
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
      "description": "Dimensions for breakdowns, such as department, category, or responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-report-quality-non-conformance-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to report on; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_report_quality_non_conformance_agent.py` and embedded as the fenced Python below (sha256 e3fed605ee3eec31…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_report_quality_non_conformance_agent.py` first:

```bash
python3 report_report_quality_non_conformance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_report_quality_non_conformance_agent.py   # or on stdin
python3 report_report_quality_non_conformance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report quality non-conformance Summary Report — Builds a read-only summary report of quality non-conformance activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top 10 by valu

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
  Upstream entry : https://coworkcookbook.com/recipes/report-report-quality-non-conformance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_report_quality_non_conformance',
    "version": '3.0.3',
    "display_name": 'Report quality non-conformance Summary Report',
    "description": 'Builds a read-only summary report of quality non-conformance activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top 10 by valu',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-report-quality-non-conformance',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-report-quality-non-conformance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'df1d602b33e2ffcc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/report-quality-non-conformance'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/report-report-quality-non-conformance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-report-quality-non-conformance-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where report quality non-conformance stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of report quality non-conformance for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-report-quality-non-conformance-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads report quality non-conformance records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of quality non-conformance activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top 10 by valu', 'example_request': 'Build a quality non-conformance summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-report-quality-non-conformance-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a non-conformance summary from D365 ERP with totals, by-dimension breakdowns, and a top-10-by-value list, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportReportQualityNonConformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportReportQualityNonConformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-report-quality-non-conformance-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportReportQualityNonConformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
