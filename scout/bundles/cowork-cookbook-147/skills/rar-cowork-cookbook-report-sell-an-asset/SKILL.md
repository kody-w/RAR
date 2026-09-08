---
name: "rar-cowork-cookbook-report-sell-an-asset"
description: "Builds a read-only summary report of sell-an-asset activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_sell_an_asset", "rar_sha256": "639e536cc67f737fa1f33576a516afe83ac838d3179a70120aa95aadf4743955", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOjRrbmX9G8N2JsX1W9iB2q40YMIJAEYpFYhHA5yuwgsYlFLJ7+75NIqrLdXe65HTGfRrWIJfPkWZ/npOC3N7drk7J++/Smh26x2LhZliZhvXCLYMGVfVlfwVd59cC/hV8WbZ16XVvWzduHtyBs/Dqt2rQswHS2S7OgWbiLOnSDj2WRjYumy3O3HsGVqqzbRRktmjDLPrrFR7dpwnbh+m16T9txEdVlvliPhZunfrNACXwh/E+dkxdRCRRZZGHsZouwaMHQH5pFXjYtEOmDC4sKHIfBogrrtAw+gKttVxdpEQP1F/zgh9lituChfJ+2yUJ/avRhsQ5bN80+PMw0ygpeLZokDNvmHdgVDm5eZWHz9unnXz68peD47dNvb34GlAZ2Hh/G6MAQpmBmM8CMzC1icKsagSsLcA70Aarn4FIQRovX2Y/A+OjD4j//89q7ddz89OlzsXh9Pr/Nf45dsWiTcNGW7sMq361cL82A1e8LJuvdsXkZOHu5AZEo4vfnzN8lldXiv+Z7Pz4XeY/D9sfPbyVQwZ3j9PntpwXw6ee3upuP32cp1Y8/vWdlH9Y//vS7nKbzLqHfzsKA1u9fXucvsWDg70PTaPFF13jutRaITFqFQPgf7Js/T9Vf4l4u+fIc/GNZfVh8X/Jsz38BfZ+55gG53xcLfABmvr1fyrT48bVGXd7Dwi388Mef/kqsn4T+NUub9r8l9+en4AQkOPDWyyU/fXiE75fF8mXbN5l/vWwFEubfsQQM/7rcN0f9lexHZP9BdJYWYfMtlt8V970Jy/9a/PyXtv2rCR8W0ee3dZild5B3XhZ+Wvz2SJGffwh+v/jDL38Hov+vYvSyq/2HhC+5W6RR2LRfvvz8Q/O4/MMvP//QVSCLQzf/0tXZ92R+z6+Pdf7kwdeoH/88F6xvFtei7IvFtxpa/FZW/6P++/vCcrM0+P1682nxx0qcP8vFbMTXRZ8u+EM1NkDXP/jxp7e/A7gpgDWd/7gN8OM//mMhp35dNmXULnS/7AD0dQAJ83BW3kjSZgH+zqhRh8CvTQoc+xoH8n+O8KwxQN5f/5f/QPOP/gvNoScqf5kh+YtbfHlA8q/vCwPIKus0TgsAukdG0z4XbjxjLVinqsMmrO8Am7yxDT+CEv44HyzSYvHr98R9ecx8r8ZfH0CbPvHtyO1mbGu6LHyfrTglYfHS2Qe4HQ6h3wGhWekDDaIUIPGM7E2Z3QE2zhY31zTLFkEK0ANQ0fiQDbzyaRb266+/em6TfC6eYIwunhzVQGDAN3UWHz8CU6IsjZP2cxH6Sbn44be//7D434t/NeshfF5DA8a9fA40FHVVWYAa6nIwDIQDBBAAxMPnv/395VAgpgCkCiKURmn4nAxy8BoGX72rb5mPCE4svBB4FXg0n705M1navi920eKbvi82nTkgmZkwCKuwCMLCH4FUF5jzzZNF2S4akGhNBAiva8LHqr96tftQMQfF7La/LmROA4xTZuC/Wc3HIDC5LFLg/m+xf14HQmrAwOxXEe8LZc66ReXWbpXU7muNyH3GZWbv13Qg3F0UYf+5mPk0nF31KIGne8Ag4Bn/FdKPc8xBswGougiar2s/xrgzLxoPfqw/F80rvd16DoUP4B4sGndpMIP+314p1SRllwUP/wFNZ0mvKASvqDxycObzuWl4NiavNmHx5PrF5w5Zwdji/5MOZzaX2WyO/IYx+PWCV4zj+RmGub+b13y2hA+1y/pZcr/3Il/x5ivsfi6yFORUPf7tOfIRvNeYJ5R1NTDgyBwf8kHmgDDMch+JPSdqXc8l4X4uvuI7UHrxADMQW4ACoErm5Py64Hz3q6YJKPX5/HeufyRCHcxmg+RdVJ2XgcSKwjDwXP8KtJqD9zWiIMvDOWh9kvrJn6yagwHiCuQvgBIpKDfAAe/fMPd596vqf5r4bGnmKY92rwO1WT8EAD3CWcE5IHOogHrts50Gdn56CAFm5FU72+6B6gCWPi+GdXjr0iZtZyR8+jWsAPJ+nL+fls5Xw6ECBQGcBdK+6oB3H4Uy50oOGhagA8AKUDd5WgACB055OeEh0M3nqgc18OownxIfl18GhY/qmpnn68TZkHnOTObPBHeL8Y/gYHwvTYC8fB7xWPcfM+3barPsGSAbAHJgxa93n6z//iTuZ2ew+Cr30z/tV37897Y0Dyo2/5wAnxZJ21bNJwh60udX9nwH8AQ9dW1eTPrxT6X/J1lPMz8t/j19/iTiVQ+fFvD76n0139q/8un1AeZzH9nzR2y++7k4hr8DJli+zEFCzcEaAXV/Y7evQwDFxTXAIDD4yXbNTJI94OUHvAPPfy7+mOBzgQH2KOI5IZvyD4X/oHmQ7M9AfWMhcKtowdrB3PzF4bzLepRDE759Kros+/AGkDH8i93VzC75nLnNvA8DNQLAsE3Dx5kHVLoGoDa/BCAzi+bZNv32D3vT9bd7j0z6NqmZbQTk4VYVUOfZqQI+det2JqgPQP02jMsZTUH/UYHpj/YKTASsARRrx2rW+bkVm5u3BywN7T8roD4O3Oz9BcvNH3P9xVAzQ/+hJJ9uBu71gb0fFgFQpZkZFbh5dsVczm5zfRj0XV0enPLlySnf8chMQX+knQf9v1is+LAI3+P3hanLwndlf+tg/1nwCTQVs6yg/DTz64cXpoFvsOsAHv26gQAWvbZ0jy130YHd8s/z5mUO+GPKfADmgK9vk7796OCFb798T68H8H2ZM/GZT/+onTIDGgD82cH/wJ5AZ7Bu0Pnhy/rvVfVHZIUQH1f4RwR7H7Jm+K53nlz9z4trf6Tyeb1Hx/I34IjI7TJQNG35UOwv6X/h3kHuzGn6nXXBwg+aAGQ7e/L3EP3uqPKx5XuomLnt8xeK395Aabkgu9xXcb32DGA4QNWPzdxDQQBzwILg/IkO4N5/azfxmtMkLuhswSQCpUMcJXyfICMSJSMXjlAUJwkXhwk3CinU9SmUClCYpF1yBSMr16Vx1w0ijMRQGseBvCeufJmbw3TWA6fJaEXTSISB4QHwJIIFAUVQhI+TYD7tubiH0673+9RrWgQv457GzJ77trGZnfCyEYALgYGRW6zZMc8PB9EwuEh6o2gvayIsnTNnZXzSIKgiHjPsPuR4dOa4UA7GkN2p6kFQrnq4Ww2h1Ov7UDjGCp6uh6RIjUi1LIFyAdTnPp1jQ3JgRQf0CmZnT4XZnkIcQ1VHvEkyqyZwvTMd2uqEwSEp08tv6UXQIGi5hjZXvRXPKcyYcjkV0vWOHtr2mBzzDL5K6/EyyXjpSBvRFpeE4afoKQm6faXFLaq7hiDANCQ6JETTRSWRwok9pLmfqPkhP2dJScAIlwVxrvPsuN8GQ763WVdM8wA7ZY6Q5QcPuxtOskpzLNtZwthl++aYmTkWoJM2WKKTXBus3yfO3bJJqGhZTzLv7WXlajY5YNRyEjAy0oqyKlASpilCvqM5kaXC8bQqq8Q64VZvjuvOljyX3Qihl0hmcdvYo7mxyGu3O3uBxMMnNnBIl3G7K6wTu2NyOIbMCd3TOLTzxGR1zbkRVMwex05nsTf1gy4naNung6MD686REAqX6pibiRXstk7l3uySDNUJQcoWOpB7+kjmZ8sR+Sy/lUk1jjJVw07FlzmcafztwpEMv8wVxckrQ5TGfR2I7QZtE/zARGcJYRhFTM/Qfs2JpE42EzlMWn3KzirAM8NZV2Hq3vbiWTB6f3/N4ovicNwxFxyhyW9SvWXZQGYgsqMqHrn3lz0rNPD65KfRbXUoquAwSaulM8ERqdroKHR5AonrfcoMvHWywoOb3C032TclHWxYGdpVbrbfOmLWscOwb4tzx6ubmE4o301pKVm6tZ/2ARvG3Fa8Ygm0SZZdudkg+GXtpaMvWMxtEzQu32Vn9nRp3J5vEdIFJphpodtuMlhOokTB6UbcduLmcB/YDBLO5O1Q9bemqChpoxHXSRYjNGahateyPGV2K23nCZf+1rLGShuTOtoIiOhkdeIX4iBoF7WnNFgieUottYvQaTmEh6JqIqHIRWyPGof6RLNRei8g7Y75aER6yBmiE4KIJnGC1Dtl7FfHDr/aXHnVdK0KTJW+ygRSNlbJXW/XejJFBN/xGwxhbWYTQ7yV087yXvpbbG2exHOu5a0jR8mx7ZFhjd8CqyfhSkUM53ih+jQdjCpgscyxzuoVZ7xYpUN/bZpHBht6jKPMxL+cYqMoCURmhvvO69NJk/EGVbmt3UzUgPVSJCCQhB6HoK/6sYx3jMmfj27PNA5yTcxgihquv9857UwZhRslWsHyHrXHwxJbYRdtdVeoHXW5D5uLDDf3+HxAbV3yVWXopsl39oJgDvkWSS35JikOIlG3yzG2u4bpWS+54phzkZR74pymzc4/UhJyOLhXzqy2+rXC8o2/sS6sfL7dOzqOYBerecthWJat97thdd+bmDFsYLtxrVBRDVvTYD8Z3GVscMZ9q7h6zcpOB4VyW9pm7E/hiiZOrW5f+ZwLj2eWCjuc1keHbOIK5pMrRHXTAcUKO9CNcTAar6oZtBPW+LrG1vZYj0wzwec+pEh9S+4u055vO1ZIFWhH9CcWi7bcXcZRLiWYTV4iNOtfXUHHd7ehoyUUbVyV61yFHq7GTeaZiaYAjPUBWhXDwZTuQ7LStlq0VT3odpJJZpSqnRsyykHpfFw9GMTecFf7PqFZxPe1hlD6LbGTr5tuzYxKHwypAsosJnyWxrZTZxB8CTlnKl/WjdMpPGtdSp72VuMhEK5ara5X1nrCzRNzlIOt16y53VY+J9c43sRXdyMb1nCirEa70eH9bin73DE27DWFjM3IaPFZxGHY7yFJmQyD0A9e4Nf6iXY2611h7k+Hw3nlH48ny2DO8Qr0jctEhnNfrxXuygZpAN8F/2TL7WQb8b7ha6ssgVcOJOXVAtGeJMoN9+7gb50RaffkqFfWbVCk44pcQtp+hdhBMQ29f3Yo5nJdXvSLIVE7TYIlfHv21x1WM7JBDxg0+oq5bzuE5z2ZSmOroP1o0Gg3QrOYWELL0N0DIq1Iv1KpvGTw6hrp9Tk+sM5VJzHFq4jtzTnzhZwRhXm00gs3EZLScBfbopOckbAB91WIhSGFtKlVFPHmJchOYmPc4q1h7PD7Wkl2PumI2DoPQ35iPEQ67PjkLHLDcBj26kXTJwst93SzloydnwN+jBD/RtqDiaJ60DbZDVcaqViz5/1QsslENu1U4CDhcuFIhkfidEJLuNHK3sy5LsnWq6Mj5YN2sdTdbglvSJkHLXQTUhaJ+eu2zW9X+oLDTqqznNLwecfwLL8VE7+3FazB1M7pdgJ/KCa6UPDNub/elCTZbNf8einAzup0VuVo7x6NRKIqQc7MJAyKW+lz1Rrf4jvFN6ZKWWfaTkw2PrTszB1+8O31WjnZKbqpuQvHe+vdhVSE8ezuAiiju36QcDMs4nOlHgArHe6gW8HuQi2KZFqZl7VUdkiWkPIp5RnczCXgsaZWRT49qvaqGndNf2FYnRkch2rNcYlKucUDFksZsxOZc6PjvOZ0lZjoRhGnKWcrJxI1xMxnNRJGd/lm5C1vg+J1aG8lmrsl5akK/LQuw7XZmBdx0o435bA1WH+FBI6zh48NqJFkVRQmVK5OCiFXUr8HXZA0WPYtGtTMpyxTsxwTNARns9rwZ19Mh2p1rq+nw3lN8GxBDIJ+FxShOJdhfFyfYe08ZtFk8NUg7PBlfoFoURmYNSo4zTh0MtffALKy6nYXO9lI+rbUkqAK6HO/4x27StrlUhoajo/ZS2ZXoF/NlADsgXbaZXXd6M3WIZCwwAHOkukqOjS56jta09IBQFF4sjF241lWI8HuWZTFYX/dHE7x/VBhNGeuxb1Ku/tUMHk4TbfVmHdLislJbHnmiNtxyDfsIJNsxqAaJYChcU/dc4InZOsQHIVNIvm5vNWGwtfW1+3ATZLE9EeVVpJtLZpLcahltMZMdn0ag2Lt5lSw9G476sbjU3n0VjhCcSWBnq/c+ZA30mi6142r0YLhMlTo0wyMeweXrLoBImnydhNvR8zpmOUojoagou3WIycNbxmmLQbe3NeZKnFmsdQZr1wmyGlTy46P3KchTyIdD2BTkA51bdQFwrBC3o6sfhgSU8nwst700XrXjs5hL3GcBfHNWrwycBKeyP2lgsw7mvn0hWcN4TZUKpO13lmg45wVJ3nJp1hm6rp0jQ9H2L+wR6EZqUlnyzRc4hQDGyju6qABbw+2eCp9h0GlztNdlzkEO/tw2E28paY7mfFYpijgQBe4uylQVLv3A6FmBviensbudMiMkaIs+BrnlQcBaKGLGsc8ydMwht7p2IE6LndkzPH4dtoepTPMcUy3u10rTzU5LoLJQs0gYmttoTgwp8QIj5EytkOZpImSNiFf6JtRileaIYbR7UgIS4FMRWGFZZoZXHDFvbhwt96crYut0tnaXnXQulWl9l5yQ28k2YZXR2Q8bK0bvHbBXtTukwMq4mRBJSCNsWtMc20Uh2k4OAbVe/4Ry4ddX5Uoh/Os0F9Kk0tSU9/lK+lcodotLJg948lGUGCnK9dsmZt6hFbR1h83p9M+Hvr9jlRupSfcm6Lv/DbeX6luTdw6llqVBnF0b+gpZ4OuE22XjuVxWeUt0cgXzQ3XXoVgJAIaUH7XraQkMs+luD8YLSka8SgiZys5cigkR1t6JKFVWBK5eaosS+a9gSfjZU7fZTcXAZ3x/EFbMmqTYltNu7gHHAudK6wgY2lipH8ToOhumlXssTSJW4YtTGeVDtoYI+8YfU871NgPlrC56TVPnkCuoCYyYubNdJEdUnT0lHvF2T1VLcsF13gdVvlF1Nogv16zBq72J/oWV40pyj3iipFJk4BYLIkNls4WwrooD0bUYq++ZuqEfJvQa4JETgXKrc5A567EFX0o5h+kGzhuyiHzJOnWHHTT6Ch2tzzuMDpPmDhtgmA/bW3vciTy27mg7SV8I0+SQWk8y230FpEjxuI7d3VRTH59jHUi3/cs2F3j15XAifQpl6vEJOJbAgVlOap4CbYStT1e/DispS3EkDuwvcnEEFFbH3dOYTSdOhtXrMsVcWwtwAZymW1TivXJy94crofpml9azgdEUnrEZjwgG9Dy8Zxupsb9fL50/jL0rBRd3Xg4QwavO64cTKAdLzyIdjcgI0SEbOdt+nUEr3WUOFmy2iIruE2SC2ZreYQhfE+SPTCeOYyFcWiIZDJsmBJ39gqqDFXwcm9rSSEnHjR5JAJ5OkF7lkVdSl3vpFWWFPqIaxPYVqw8d+eml12jO0a7m4SR252XjuRveOPi7LwcUacK0ENxXfbHC3fVYu+4zYLaxrktA8cU7Npih95BX+KSAgW29qpcugTv6puzP+2IA9r5mu5ZxgFX2KCpqHWv+aspOmeODWmefGIHdXu50Tuc0tZM4PGAyY57jZZVbJAHLCBWR7+NSpMs9aG6OPV9Sfgbw9FkH/L2eBTkLmL0FMkP9b3TJJIipCRse/xG3CNzfeMuumwTFOLRvKMn4223wuHjlqCCaG3SPkTtVppyGdaplV+wu2bbO9VX1OpQ0MnEVudyg23XwhaSoNP+sGZP3FTa+RFWbXgNHfa37mhyBycp+arzpFuLFEoSbk7qZK1qWu3ZNq50AtXQziRHfKmFrExfYgxPtehUCUGNoPJ9jcUGZidXoogOF2Yt57CZl3jTQHkEQTEJlV1rbNXRjrRJW4oQQ9CtA7p8fHffN8qlZHPMaLNppwWngKeW6tElb34AMoCaRMam19MRxwvvPA1oFKviAZH9I70WlwwuGhR6V3Otu07FagDsJsGghstbALK589qbpvbCOUXQTTcsSclX8MtF528yaAnlQ0tCDl/5ueeM4vLQ1VTGMNJ1hLLlvVuSro/L2JIj7thhRZFeLV539vGM7ze3XjxCOI/ZPS6ik0sabnQ8jQSB3cTkMhDi6RrQY7AldMsTJ6KJmn4VYWaQUwddZ/RcZ/slRN+cAHGKYW3wx93ehZWUazKlqkXujkxCbVvNfX/P1ooq+ZyOQCaywxwkILRTaGon+XxhJgpuhig0wW68kCh65xL9Dj7rCnKW09AuR82wAyF2Lczk4zM/GNwSpxvTwt3lycv3KuVciUMcF5ejUnPVlDNtzUO+u2mO6hLOzat/6skoZPyRn05ofpe2HFId0WVNtjBJyWs0ilRhte2s3Qb0/PjaJ024R7tG4QHPpr7vTyrUN+rocnctCrjYluu7WCUwRF4QldimComnromnG7IhBTMbBKvBjz1ly/pmiXtslUXmqczo+MT7Y10YoImZgD/qXEUuEu42K0+ZFPNQTeKSwpgQXwkkcQ7OtmmFmi+3F2UgnVXoxejUB2kKt5ckZu5y6MDVldJw44IkfmgYzh0Qe6MOgdBJa15VDnC6KSH1VAb+naUmnzlylrI9FKGyPcv6yEDKFtJ126m481ic8c539OVNwPMmGuJ01Kc+sRvGdehuIwmXKMzbcNnvu6qanPagUPgEWn1hmEiZgkhz3/khqoNNxbYIurFWI3u4Hbe8USyXch5rRoKPXRtZoU2aektTQduGI2ubV+KM4YJOL7OBsEll4vXLziT1O7Y98VLNCFrmuXbONvblELa3kjoHXn1St7RKrJMVpiY4XF8s1Mu3kaFrfhactQu56/qJZ/Xcvh5W/M0UzuTK8ZU+2TgeBpdLPJCxCrqTE8O1iWk00fU0cFIrUQLNbzAV+Fvw99gOz7gjjkDSZlPKq+AWiht8dbLup0Af3C2+3xb8FRKupw3kp1p6RVBdH0cC5ZBeOc9pSoabokeMpSvRaT3WKN0ySqy6J5zf+3ycVtFh7dhnPiJuK/W86aGtmB3pDmyIjlAEXVAOy9yVZ1rLk8VijSIhwS0aL6ROMzejOY0a1xObzTXcW0GgIpZM4Pe9rbclgp+64J5bljQiXBvCl3zcY5RSa6dS8kRDCtbcKG9pzJFzSDNlEnf0ziFSujLFGyFRlDzs+9sluY5qVS8VdB8GS9bZXlucbayLXowuo9YmJcb2PT3o2rWo1zATcJ7a5VlKCPhSD3ZuMMQKzG/rbqRdVCXsES0SnMndaGXBW7PNoNgiVxSuYDSxC5VoRTid61m8wzvnEua7xMcxVtmwJTylwR29Q95SB9VLK0EesPbAZYZ6Gn3vflqh2fLmdwFCoUpF1hzdSKW2FSBrRB2V3OA+2BjAqKkO+y5JVIegz5nay9wUymuBv6hH2rPge39Bzmuvy6lUBm3rvoIvcBUu6b2EHnRIXBXNmS1Lg3WaQETqPRquOl0g46wJBoIhWWYYxwnjrieOPo9iuS3X0Z5hsGBz75vrEnGN8D4ZxVFUQ2M3Ab68M7B9vABvYSinXrbXEs9TYtuZdu/fFGLs02V921D5/e6G2w5ztm6t4qnNniDD7uJhyEcIGixCv+0V6EytW244rbmBFCavYapqRRGBgyCmtRmsbdCyji3dl3emrkkdj3Mq5HFIGgNi0uuTfu97hL2HVoojZIzAiDJN3F2IVtMa6ZwL2HeRUEiTrhPTQ9pvvRE1YM/e+xIUFBSkw4dyaXSsYfAhx0iJtzSOKr/qhaPGmsJKWN5SsqLVtXq0VgYJV9VOD9UVtTGnlXcIrntX54GCPSQd8f3OKQ6huPWb/bI+bhBSbpNtt9pTnp33MTehGwUKZZVG04NTb2OqVLIdaHN3CrkJVqbcLTlfbjwJbCKNdcPlhVje1clW7HB/h6hwuT6kwZIpjYJG11v0KFZyw0mTvlSpXoTQ/VrQAI+JyrLaDiu1KG3odgoO1+wQM8zbh7ffH869/ctXxuYnNv/PHhw9n/F8fUfk8aQxdINPj7U+/Ws1fvnwVvspUOL5EKzJuvj1+OgfHoF9/N4Dw3nG+Hzb6uuz4efz7taN5xeM31IA7E1bj1+aMnu8CQJmeF0zv5/YzK+w+uD7j49En4uAA9d/POz70pZfgrSpyiZ8m98enF/wCIPUbb+exq/HgB/egtfrR19QAv8S1tVs2uu1AmAR+r56R9/+/n8APLCgShEuAAA= -->
