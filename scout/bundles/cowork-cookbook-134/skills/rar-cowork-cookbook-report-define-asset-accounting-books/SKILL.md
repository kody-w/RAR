---
name: "rar-cowork-cookbook-report-define-asset-accounting-books"
description: "Builds a read-only summary report of asset accounting books from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_asset_accounting_books", "rar_sha256": "99be8bafc68789867bfaa3f2f1ae0c41ddba44309180d8dc7896a2f0c8d4c899", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
