---
name: "rar-cowork-cookbook-report-detect-synchronous-integrations-failures"
description: "Builds a read-only summary report of synchronous integration failures from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_detect_synchronous_integrations_failures", "rar_sha256": "bf47be1efd8307b91ec422f912d40680547793d244b09e79a230f992944a8dfb", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
