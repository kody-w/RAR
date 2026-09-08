---
name: "rar-cowork-cookbook-report-clean-up-and-view-log-storage"
description: "Builds a read-only summary report of clean up and view log storage activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_clean_up_and_view_log_storage", "rar_sha256": "ecc7f06af12e635d3f65456a30bad8e33d01a01bc84e4a8920fc1acf32da2e37", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
