---
name: "rar-cowork-cookbook-report-sell-an-asset"
description: "Builds a read-only summary report of sell-an-asset activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_sell_an_asset", "rar_sha256": "639e536cc67f737fa1f33576a516afe83ac838d3179a70120aa95aadf4743955", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_sell_an_asset`. The original RAPP
agent is preserved byte-for-byte in `report_sell_an_asset_agent.py` and in the RCI capsule.

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

Sell an asset Summary Report — Builds a read-only summary report of sell-an-asset activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-sell-an-asset
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
      "description": "Name of the Excel workbook to produce, e.g. report-sell-an-asset-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_sell_an_asset_agent.py` and embedded as the fenced Python below (sha256 639e536cc67f737f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_sell_an_asset_agent.py` first:

```bash
python3 report_sell_an_asset_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_sell_an_asset_agent.py   # or on stdin
python3 report_sell_an_asset_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Sell an asset Summary Report — Builds a read-only summary report of sell-an-asset activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-sell-an-asset
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_sell_an_asset',
    "version": '3.0.3',
    "display_name": 'Sell an asset Summary Report',
    "description": "Builds a read-only summary report of sell-an-asset activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.",
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
        "upstream_slug": 'report-sell-an-asset',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-sell-an-asset',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b7f9c8f4269939ce',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/sell-an-asset'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/report-sell-an-asset', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-sell-an-asset-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where sell an asset stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of sell an asset for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-sell-an-asset-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads sell an asset records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Builds a read-only summary report of sell-an-asset activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.", 'example_request': 'Build a sell-an-asset summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-sell-an-asset-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary of asset sale activity with totals, dimension breakdowns, and a top 10 by value, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportSellAnAsset(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportSellAnAsset'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-sell-an-asset-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportSellAnAsset().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
