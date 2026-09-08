---
name: "rar-cowork-cookbook-report-transfer-assets"
description: "Builds a read-only Excel summary report of transfer assets from Dynamics 365 F&SCM for a given legal entity and posted period, with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_transfer_assets", "rar_sha256": "2b8e92a82ab00afec15d55dd08aa9595bef0fe3fd28e185d6704d462f33dafbf", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_transfer_assets`. The original RAPP
agent is preserved byte-for-byte in `report_transfer_assets_agent.py` and in the RCI capsule.

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

Transfer assets Summary Report — Builds a read-only Excel summary report of transfer assets from Dynamics 365 F&SCM for a given legal entity and posted period, with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-transfer-assets
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
      "description": "Excel workbook name, e.g. report-transfer-assets-2026-05-24.xlsx, saved to Documents/Cowork/output/.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to summarize; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_transfer_assets_agent.py` and embedded as the fenced Python below (sha256 2b8e92a82ab00afe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_transfer_assets_agent.py` first:

```bash
python3 report_transfer_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_transfer_assets_agent.py   # or on stdin
python3 report_transfer_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Transfer assets Summary Report — Builds a read-only Excel summary report of transfer assets from Dynamics 365 F&SCM for a given legal entity and posted period, with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-transfer-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_transfer_assets',
    "version": '3.0.3',
    "display_name": 'Transfer assets Summary Report',
    "description": 'Builds a read-only Excel summary report of transfer assets from Dynamics 365 F&SCM for a given legal entity and posted period, with Summary, Detail, and Top 10 by value sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'report-transfer-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-transfer-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b6e0010da00c0b3f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/transfer-assets'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/report-transfer-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Excel workbook name, e.g. report-transfer-assets-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where transfer assets stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of transfer assets for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-transfer-assets-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads transfer assets records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only Excel summary report of transfer assets from Dynamics 365 F&SCM for a given legal entity and posted period, with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a transfer assets summary report for USMF for the latest posted period as an Excel file with a Top 10 sheet.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Excel workbook name, e.g. report-transfer-assets-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write transfer assets summary report with totals, by-dimension breakdowns, and a Top 10 by value list exported to Excel.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportTransferAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportTransferAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. report-transfer-assets-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportTransferAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
