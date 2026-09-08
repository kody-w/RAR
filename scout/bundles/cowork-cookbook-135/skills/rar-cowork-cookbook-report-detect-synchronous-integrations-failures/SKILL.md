---
name: "rar-cowork-cookbook-report-detect-synchronous-integrations-failures"
description: "Builds a read-only summary report of synchronous integration failures from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_detect_synchronous_integrations_failures", "rar_sha256": "bf47be1efd8307b91ec422f912d40680547793d244b09e79a230f992944a8dfb", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_detect_synchronous_integrations_failures`. The original RAPP
agent is preserved byte-for-byte in `report_detect_synchronous_integrations_failures_agent.py` and in the RCI capsule.

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

Detect synchronous integrations failures Summary Report — Builds a read-only summary report of synchronous integration failures from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-detect-synchronous-integrations-failures
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
      "description": "Dimensions to break down by where applicable: department, category, responsible owner.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-detect-synchronous-integrations-failures-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_detect_synchronous_integrations_failures_agent.py` and embedded as the fenced Python below (sha256 bf47be1efd8307b9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_detect_synchronous_integrations_failures_agent.py` first:

```bash
python3 report_detect_synchronous_integrations_failures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_detect_synchronous_integrations_failures_agent.py   # or on stdin
python3 report_detect_synchronous_integrations_failures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Detect synchronous integrations failures Summary Report — Builds a read-only summary report of synchronous integration failures from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-detect-synchronous-integrations-failures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_detect_synchronous_integrations_failures',
    "version": '3.0.3',
    "display_name": 'Detect synchronous integrations failures Summary Report',
    "description": 'Builds a read-only summary report of synchronous integration failures from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-detect-synchronous-integrations-failures',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-detect-synchronous-integrations-failures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3bd18eebb36c6c54',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/detect-synchronous-integrations-failures'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-detect-synchronous-integrations-failures', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-detect-synchronous-integrations-failures-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where detect synchronous integrations failures stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of detect synchronous integrations failures for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-detect-synchronous-integrations-failures-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads detect synchronous integrations failures records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of synchronous integration failures from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a summary report of synchronous integration failures for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-detect-synchronous-integrations-failures-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-change summary of synchronous integration failures in D365 ERP with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDetectSynchronousIntegrationsFailures(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDetectSynchronousIntegrationsFailures'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-detect-synchronous-integrations-failures-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportDetectSynchronousIntegrationsFailures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
