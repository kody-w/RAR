---
name: "rar-cowork-cookbook-report-define-asset-accounting-books"
description: "Builds a read-only summary report of asset accounting books from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_asset_accounting_books", "rar_sha256": "99be8bafc68789867bfaa3f2f1ae0c41ddba44309180d8dc7896a2f0c8d4c899", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_asset_accounting_books`. The original RAPP
agent is preserved byte-for-byte in `report_define_asset_accounting_books_agent.py` and in the RCI capsule.

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

Define asset accounting books Summary Report — Builds a read-only summary report of asset accounting books from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-asset-accounting-books
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
      "description": "Excel workbook name, e.g. report-define-asset-accounting-books-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_asset_accounting_books_agent.py` and embedded as the fenced Python below (sha256 99be8bafc6878986…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_asset_accounting_books_agent.py` first:

```bash
python3 report_define_asset_accounting_books_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_asset_accounting_books_agent.py   # or on stdin
python3 report_define_asset_accounting_books_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define asset accounting books Summary Report — Builds a read-only summary report of asset accounting books from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-asset-accounting-books
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_asset_accounting_books',
    "version": '3.0.3',
    "display_name": 'Define asset accounting books Summary Report',
    "description": 'Builds a read-only summary report of asset accounting books from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
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
        "upstream_slug": 'report-define-asset-accounting-books',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-asset-accounting-books',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '01faafd451124038',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/define-asset-accounting-books'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/report-define-asset-accounting-books', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Excel workbook name, e.g. report-define-asset-accounting-books-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where define asset accounting books stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of define asset accounting books for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-define-asset-accounting-books-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads define asset accounting books records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of asset accounting books from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': "Build an asset accounting books summary report for USMF's latest posted period as an Excel workbook.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Excel workbook name, e.g. report-define-asset-accounting-books-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary of define asset accounting books activity with totals, dimension breakdowns, and a top-10 list as an Excel file.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDefineAssetAccountingBooks(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineAssetAccountingBooks'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. report-define-asset-accounting-books-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportDefineAssetAccountingBooks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
