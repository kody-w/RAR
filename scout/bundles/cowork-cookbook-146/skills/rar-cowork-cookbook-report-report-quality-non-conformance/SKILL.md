---
name: "rar-cowork-cookbook-report-report-quality-non-conformance"
description: "Builds a read-only summary report of quality non-conformance activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top 10 by valu"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_report_quality_non_conformance", "rar_sha256": "e3fed605ee3eec314e8183d812162582804b7493118c84831b1fa1d9acab513b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
