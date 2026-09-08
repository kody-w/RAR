---
name: "rar-cowork-cookbook-report-clean-up-and-view-log-storage"
description: "Builds a read-only summary report of clean up and view log storage activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_clean_up_and_view_log_storage", "rar_sha256": "ecc7f06af12e635d3f65456a30bad8e33d01a01bc84e4a8920fc1acf32da2e37", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_clean_up_and_view_log_storage`. The original RAPP
agent is preserved byte-for-byte in `report_clean_up_and_view_log_storage_agent.py` and in the RCI capsule.

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

Clean up and view log storage Summary Report — Builds a read-only summary report of clean up and view log storage activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-clean-up-and-view-log-storage
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
      "description": "D365 legal entity to report on (e.g. USMF).",
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
      "description": "Name of the Excel workbook to produce, e.g. report-clean-up-and-view-log-storage-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_clean_up_and_view_log_storage_agent.py` and embedded as the fenced Python below (sha256 ecc7f06af12e635d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_clean_up_and_view_log_storage_agent.py` first:

```bash
python3 report_clean_up_and_view_log_storage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_clean_up_and_view_log_storage_agent.py   # or on stdin
python3 report_clean_up_and_view_log_storage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Clean up and view log storage Summary Report — Builds a read-only summary report of clean up and view log storage activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-clean-up-and-view-log-storage
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_clean_up_and_view_log_storage',
    "version": '3.0.3',
    "display_name": 'Clean up and view log storage Summary Report',
    "description": 'Builds a read-only summary report of clean up and view log storage activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-clean-up-and-view-log-storage',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-clean-up-and-view-log-storage',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '42f79000b0d44f86',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/clean-up-and-view-log-storage'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-clean-up-and-view-log-storage', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-clean-up-and-view-log-storage-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where clean up and view log storage stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of clean up and view log storage for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-clean-up-and-view-log-storage-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads clean up and view log storage records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of clean up and view log storage activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a clean up and view log storage summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-clean-up-and-view-log-storage-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals/trends/breakdown report of clean up and view log storage from D365 ERP data, delivered as an Excel workbook. Read-only, no data changes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportCleanUpAndViewLogStorage(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportCleanUpAndViewLogStorage'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-clean-up-and-view-log-storage-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportCleanUpAndViewLogStorage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
