---
name: "rar-cowork-cookbook-report-transfer-assets"
description: "Builds a read-only Excel summary report of transfer assets from Dynamics 365 F&SCM for a given legal entity and posted period, with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_transfer_assets", "rar_sha256": "2b8e92a82ab00afec15d55dd08aa9595bef0fe3fd28e185d6704d462f33dafbf", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
