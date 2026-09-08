---
name: "rar-cowork-cookbook-report-report-production-output"
description: "Builds a read-only summary report of production output from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_report_production_output", "rar_sha256": "034aeabf1076afa239773a1cf79bbcfbdb24f106cb3eb18280ec33517b35031b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_report_production_output`. The original RAPP
agent is preserved byte-for-byte in `report_report_production_output_agent.py` and in the RCI capsule.

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

Report production output Summary Report — Builds a read-only summary report of production output from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-report-production-output
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query; defaults to USMF.",
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
      "description": "Excel workbook name, e.g. report-report-production-output-2026-05-24.xlsx, saved to Documents/Cowork/output/.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to report on; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_report_production_output_agent.py` and embedded as the fenced Python below (sha256 034aeabf1076afa2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_report_production_output_agent.py` first:

```bash
python3 report_report_production_output_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_report_production_output_agent.py   # or on stdin
python3 report_report_production_output_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report production output Summary Report — Builds a read-only summary report of production output from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-report-production-output
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_report_production_output',
    "version": '3.0.3',
    "display_name": 'Report production output Summary Report',
    "description": 'Builds a read-only summary report of production output from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-report-production-output',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-report-production-output',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f60e3979ca66cd7b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/report-production-output'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/report-report-production-output', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'output_filename': 'Excel workbook name, e.g. report-report-production-output-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where report production output stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of report production output for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-report-production-output-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads report production output records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of production output from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a production output summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Excel workbook name, e.g. report-report-production-output-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write D365 ERP production output summary with totals, dimension breakdowns, and a Top 10 by value list as an Excel file.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportReportProductionOutput(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportReportProductionOutput'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. report-report-production-output-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportReportProductionOutput().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916+7OiSLbuv+LdJ+J296FqIy+BOjERF5WniAioYNdENW+Q9xvs0//7TdSq6p7pmTkTcX+6Vu2tQubK9crvW2snv77ZXRsV9dunN9238wVvp2kc+fXCzr3FphiKOgFvReKAn4Vb5G0dO11b1M3bhzfPb9w6Ltu4yMH0dRenXrOwF7Vvex+LPJ0WTZdldj2BK2VRt4siWJR14XXuPGNRdG3ZtYugLrLFdsrtLHabBbYiFtz/1jf7xY+pH9rpws/buJ0WJ33P/bQIinrRRv4iK5oWCHXBzUUJPvveovTruPA+LPxxXirOQ2DAgh1dP13MNjzUH+I2WuhPnT4stn5rx+mHh6FGUSLLRRP5ftu8A8v80c7K1G/ePv381w9vMfj89unXNze1G3DpTXuY8/ytfjPo8LAHTE7tPASjygn4NQffgWpA8Qxc8vxg8fr2Y+OnwYfFf/5nMth12Pz06XO+eL0+v83/tC5/2NoW9sNA1y5tJ06BM94XTDrYUwM80HZ1Pru8AWHJw/fnzO+SinLxl/nej89F3kO//fHzWwFUsGeNP7/9tAAe/fxWd/Pn91lK+eNP72kx+PWPP32X03TOzXfbWRjQ+v3L6/tLLBj4fWgcLL7oKrt5rQWCFJc+EP47++bXU/WXuJdLvjwH/1iUHxZ/Lnm25y9A32fiOUDun4sFPgAz395vRZz/+FqjLno/t3PX//GnfyTWjXw3SeOm/R/J/fkpOALZDrz1cslPHx7h++sCetn2TeY/XrYECfPvWAKGf13um6P+kexHZP9GdBrnfvMtln8q7s8mQH9Z/PwPbftnEz4sgs9vWz+Ne5B3Tup/Wvz6SJGff/C+X/zhr78B0f9SjF50tfuQ8CWz8zjwm/bLl59/aB6Xf/jrzz90Jchi386+dHX6ZzL/zK+Pdf7gwdeoH/84F6x/ypO8GAB4fd1Di1+L8n/Vv70vznYae9+vN58Wv9+J8wtazEZ8XfTpgt/txgbo+js//vT2G0CeHFjzhJcZeP7jPxb72K2Lpgjahe4CBF2AALdx5s/KG1HcLMD/GTVqH/i1iYFjX+NA/s8RfgBvsPjl/7gPaP/ovqAdfkL0l9fbd5j+8oTpX94XBhBb1HEY5wCWNUZVP+d2OCMwWLKs/cavewBTztT6H8Fu/jh/WMT54pd/IfnLQ8h7Of3yQOL4iXraRpwRr+lS/3227RL5+csSFwC7P/puB+SnhQuUCWIA1R+AzU2R9gAxZz80SZymCy8GmALYanrIBr76NAv75ZdfHLuJPudPiMYWTxprYDDgmzqLjx+BVUEah1H7OffdqFj88OtvPyz+e/HPZj2Ez2uogCpekQAaSvpBWYCd1WVgGAgSCCuAjUckfv3t5VsgJge8C+IWB7H/nAwyM/G9r47WBeYjSqwWjg8cDJybfaW6uH1fiDO5vvR9Ee7MDNFMlZ5f+rnn5+4EpNrAnG+ezIt20YD0awLAiF3jP1b9xanth4oZ2OJ2+8tiv1EBDxUp+DWr+RgEJhd5DNz/LQ2e14GQ+odmsf4q4n2hzLm4KO3aLqPafq0R2M+4AP75Oh0Itxe5P3zOZ8L1Z1c9NsbTPWAQ8Iz7CunHOeagHgFcnnvN17UfY+yZLY0Ha9af8+aV9HY9h8IFJAAWDbvYm6ngv14p1URFl3oP//nPCuMVBe8VlUcOPgn/T0qYV0mxeA343KFLBF/8f1MPzbYzPK+xPGOw2wWrGJr1jMlcD85rPkvIWa+nRmD/fS9XvkLSV2T+nKcxSLB6+q/nyEckX2OeaNfVwACN0R7yQRqBmMxyH1k+Z21dz/vD/px/pQCg9OKBd8CNABLAlpkz9euC892vmkZg38/fv5cDj6yovdlskMmLsnNSkGWB73uO7SZAqzl8X2MKUt6fwzZEsRv9wao5MCCyQP4CKBGDvQdo4v0bLD/vflX9DxOfVc885VERdmCj1g8BQA9/VnAOyBwqoF77LL+BnZ8eQoAZWdnOtjtgqwBLnxf92q+6uInbGRaffvVLgMgf5/enpfNVkBtgdwBnPVPv/blr5lzJQE0DdADAATZRFueA44FTXk54CLSzGQIAxL6K0KfEx+WXQf5jq83k9HXibMg8Z+b7Z57b+fR7pDD+LE2AvGwe8Vj3bzPt22qz7BktG4B4YMWvd5+FwfuT25/Fw+Kr3E9/19/8+O+1QA+2Pv0xAT4torYtm08w/GTYrwT7DrAKfuravMj24+vtOwZ8fAbiD2KfFn9a/Huq/UHEa2t8WiDvy/flfEt+pdbrBTyx+bi2PuLz3RnovgMpWL7IQG7NcZsAu39jva9DAPWFNYAmMPjJgs1MngPg6wfsgyB8zn+f6/NeA6ySh3NuNsXvMOBB/yDvnzH7xk7gVt6Ctb25VAz9uT177IzGf/uUd2n64Q1gpf+v27KZgLI5n5u5lwNOBxDZxv7j2wMexnb++Mem9vD4YKfvL3hsfp9zL9qYafN3W+NpI7DNBSt8WHjAM81Mc8DGefF5W9kNyFOQorMt7VTOyj87uLnme+D8lyfO/71C25kR/kAFAOmqzp/hFLSXdpcCD4JLM0H8qfhv9ebfy74Asp/nesWnmfc+vOAFvIMe4cPiW7kPjHo1YI9eOe9Ab/vz3GrMXn5MmT+AOeDt26Rvfy9w/Le//plez2pwzoRnPP9Wu78hr3kQoLf38H3xL7bTR3SJrj4uiY8o/j6mzQhCY/dPitgW7rMkg5+bCX7OgP/Uc09K/XvF1N8z7qNEetF7/seQ/FOmXtg9SK8ZGf9kbbD4A9EBL86e/h7C744sHg3cQ83Ubp9/b/j1DeS7DRLQfmX8qwMAwwEAfmzm2gcGmAAWBN+fuxfc+3d7g9f0JrJBcQrmLzHc9m0nQJbkyg5sFKNJErMRNyBpx3EDx3NQHNxcuQ7mOwiFUkvfxTACIR2MWGKIA+Q9IeDLXN/Fs0oETQZLmkYDHEGXHnAqinsetaJWLkGiS5t2bMIhaPt3U5M49152Pu2anfitTZn98TL31zdnhYORAt6IzPO1gWnEgXHSGWsTMpfUmA6nqrpeitbb4xU3BiO36rdHZWx6ZiVbu1bk1ESXikYzRNdtg41VsJAmQYOB7WAXtXkxTqvWvHbLm71mQQt5l5I7QXlY0EwNgWW0d5dkaiklvladLVvQtZ2WJtcL121CLJu2webWhyYM4yUWadXtpovRhtjupDFrNKfw0QITx106oqc0z1asDmG6s9YK7Rqoaqr3ak2PfursrVu6K2LOYMqzszcxDqWDrXua7qfLmGY7YxVK7JEcTrxDyjp/nM5osmR78SbbFz09hrobWGMq87geHGrtWvqx1p7rNZaLMKdzBb/TxtCMA6+ku4hdyZdTFFzJ3vd7k6RIH8Yo2EtlEPwWwlwYOoj0OcSMcsecQ1Kyyns6XoNIuxTamovHk7GHhxgJmz2CMKwEUHNtEUjeVuuYOMvK8rgVmWKK7m6P9dCtSYRdyRIJcuFkGj+J0j3Xk13Vn9BjtTNPay28IHfZlPYivrWpoVvGNeHHLY7tvdXWpKNm6q+amBS6fi3NlL1AZOQ7mXjW48spsWVRHjbG6kgg2UWXSvnkOcoFd6pRQERRYWqbCaeCiShsczLQPL/m2C3zefowNE2RGNft6MbGTpJEwhhcOUnDm3LdbPyE0wi+1JIC2WdHB8fQI+eYhcYxpaMwdCrnVJWebQ7Z7GuDyBSObsYgEC8rXWiO1jUR945b7JPlkh+CbGLiIDkmGyLtzzt5OBwMb09yIYMvBfd4PxS2wtKrKvfiRt/yS46XRAq0Njnlshs+s2/bctf6ErctL+vCWk6Fo13C1mbXPW84dVWdY0EHvXTTInF6cVEauXR2FB0mrjts+iHlvbg9nOo1HlSGQA/WhVXJgQ/QQhk0laMjZuLHK5V1ABwEMkDU6FSLTbykVUk6gB1zxfIISjMrup1ZSC0suBtd2B4Tc+VVbd6ehcG2sNMOAY0zXnJgA8Dh3Qgu6WGEk71cQvuTit/hSLquG8nnHOaabNIERHZz1hHEakJOiepa2hj0dPSdtU1YTLDdX02Sg0lUcw6h4lmpaATV2KDdWce3pXi+2NLBJogDOrE3ZVVtAl2TLmGsnJfZugSk6sZdsWTUC91d7wSk3jszzJy8W25OkGDTsaiMZ1/IjGumZFdrH/iTPAguW1GkSbfIVkL9ml9lSqfmOplpkUcfaHqXnCKKMVIIvxKCnnljIy1JKKT2a++8tC2t0gM6CwvVye9cgLZVzjsbxxyO9c3LzOB6ZqXTWB5or7zvtqaA51DR6uKaqww0kajlbb8N4WPbEjLf3CORSM5Vq/dlcirEe6Ynlox19FDyjp4K5zK6b4R9R60GuBkmjpfpHTUhbWXYudXH+b7a4koMnQge25KGl4ax1zF7ZZT7swu26bJB0nRzTVgUdEdWKNI0iWdHAm+YCtkA5PaFoCDd84rbpTTVCFwjxAl+7tm1EJ7Uidy72GEpcPAtPMHXIyQ1aRuy7TZEkU7qe4th6tveG+qe2ZU7rjliyjpKqkh263PTb9otKZNhnt8SymJ2xY0BgEPsTj7poQ5lsmf+xKAweYBUdyIvTdkdksvJX1JrMpFDaHLTvO6USQsOh0FQc+ygyGq0pQ6r3FyKntZvV+J+UFrpcGD6w55entcyYl+EWEat+rBCyaW1DflTYKv1YeRsU96zqJHAAMoolovYbX8kppAm1txmi1nCppD065aFSCMWsYq8AhRL8sg5WDcG1RQtHmknOJgno00LQ+P2BHK5pVJ6yHsZ7cI4CVhuy98bNRZ752itE/eKYrY/EBt9V56T9WUzjRB23jV2KLalWUNrfBishK860jzL2GbVXTZne1q7eiO7V9WIwnTP5SAnOeayh/Ps7ufXdvTybbUbDGgrEQib8ok57E+YftdW3DY67MN4Z3WqAN3G0vIQ/x5Otp6wbJsTd1GGSQq5wlt8nxl7tawsH9sZvVidDvZVGDoUkOz1yjb+FiX8tcNfop1XdWct4o97oYT7kF8qSmpih8E7nwKxP/EZhV4tdvSTlYtQUUpxGjdMVSiEh2IcjJMUakdFuuU7zbiWULRmLmu35Pcmw9vISdPiLrwq1oZSaGpKxqCWjh7kNSdSag5Wd1L1nD5FiTk6zk2eaq4aqjMFbawG7dF2cMMBOy6lzalPpdFYdyvS8o5GXZcuwWjBMboNQZ/EPMHiew33vUbN1pXMyTtfxEvWJfY4z5N9CteerozbY8QFKmUK9n5kygu8F3lNukM8q9kp4a3xZoP6bQ/tK0YTq2SPNB4XpOejIfISKB84t0KoEx6JyVWAoVLbIhvEdUXi2smh1eiheHSVDXta5lJVxAKE2dP22OiTu9+Mpwx4f6f1yf6Mw+u6rPLwhlfr/VBf0vWgqKzNTJx+UHv9ttN35xiPdn7shCLIPSauEse5ImSzJG5jbOOSZg/pOl7tdpiPOEuZ1/STOOFiwOWe10AntDBDE4c8W4zcTnai7iqaEqL13BFR0sHMY5wwhwnkMubTZkiz5f1ucnyRjTadSoDoD5uUPlqQvyQOfiSwEVtPnO86E0pqeHqUgjssuspxNPZFbRnX6EKtVam83tTThYnrEbKo0o3hJGpYiRQL0Sab4BhsA65ciwUDtRG80q9xqHY7Q8tvrs1FCCFa8RkrQ1TOV6tmiRZEL8X3sNMyP0MxEq+zYdCZzeEcFEKFVRXOICgDnXYhn0KuSaB+ll7xK9msvGOTqS7HqIqirWWIHq2CE2pF3hHqadBDIzNENqY3/s3Q4KRwvKvqR5zGFyIy9esyztqg2eek6tubXdVCyUYdXSRKmfvZTWVlHRJ53l4YmtTLdViuGaTQQCWO3/11rIOsuBLbNV60bmLVWCJ5LO5jbrflpXAF6UvWwuB7o8HIzgk1FqrvXnLQORMXkWW4E7l0PGvrZT+thUQiKSn2QMeRI+Y2iFQMHqhmKW+9ZLV1TkY4QcaNPKIQpUOGKMhXOGKnFXGW9CnBpmOK8C46YWdiJecI5O8LGd+d7SFZy1J2PeljeZaSLXu7JYUnL62TcktY3+GH097hvbbfe9yqXJNKD7g6cORl7Ojtkd2w0tmjwpPA3oRjzizZiOfckL1avDJICdKWp3VgX0WZorC0Kpardk06x92BX9vDFG6ptGPio4FGK8DgLWpE8pVdbcRlGPIVtkJOmx3N+dBhLWkjTqvCjQLF20AE/ZDD6KFRUdEZnHMpjqS+VpWwyiIbqkf/3O6pM7XPjcDpZdfjXAaREtzEOf7i8YSUGQLXegpooJCMO5scBYqwNIZEhGRUVBL34pBC9VbdTNtddN7U+PFEhqm3wpLbJS2H2PUA83rrwcik3Y7fGpa+q0qFldghdDrAx1dWLpiJrZO9gstMRq2KkhJaxh0vpFw0MhFcOtyRe4puTZFJuA5XbtC4b/WKU4LNFQeVCJlZ5Lg8IXS9zO6bq37zzhWFi2cPkTmz8/Ir36PF7nDzuK2iES13gJoEMJqiWah0DMfC0KMqGYrDYIWtxhxHUjmptyXlB8dL25/yTScOBbf2xBUlBF40lLZYknTYWhNyYdGdwzEKa2mny5FbaXzJUl3rOqZ5KPZt5YvMcbp0xtnV14WW9aGddcRJVOt+uRyoQyVYzm3Y6EepRyIXLQ4j1sFVEK8FOoIdgdkAAk5F6tw0LU2tJYMbc7cxZak/e1K0N7fLZXqzNtv6gEPMat3sU7S1mrzlz3KoxMid5C6GqeSH+5SZthFapekGd4aGWWw5QJcmZLP1mrGM7OJTiTUoCgqn9irWBBnUlKcLZdWM31jkbn/lj3FpsDuENcxhnU41tjqvTLXPeOyi2n7iF3izZ+trQzKDC8qN27UIGbhdR1YfuAKS49yRpgSem4LR9M9lRq3plt6wGCLsOo8niwM+cuRR5rlo4hJZ3hicAKdmTV0demW4jqUM5x5x1RYmr6uOMQ6DbsvEdRqMqDj3DjMsI/aUtU0iRwknyM04BhTNKAIpqFUmDp2NRnouaxzspmSYFBwfNixi4/0EY71Yx0jH4ofuasKItDdHhF1ZZBM5zKmYyFqjVtFoiCMiCfUSLq09TMaWkKruOhAPrE7vE8GDk1ickEZwjpdkXLZbPtwNDM7wcNSutmx7YaGW6W8DV7XJzrFJyTXKLKdNcUNnuFAqOFAgvVPxnkGjgbPla8H2+dm1Iw4fjrHMAJQOzgc3G/cVBcN3PVtmWkigqdO04x1TB8wwhHV0vjonGtUuJJ1D9dFX75czkWNnqKagBgl6Cur7ij4SJuzY+x7f4+sdtbsRXX9xzyRdq/wEmfIlbxN8urRKLSP1HVJ2MUVePF8NS6FUCcP17JXdnC/QUsWlSS8Tk2inwqxgUFUMvelAxLkQStlhgJhqlQ9wKlzaE3EhTSaHbkEYitohA5i75jtsz5+ZSOTTQbodsCsDiuK+MtyAJ0dsb8ZmJqxInFoLl/HS+l3PRjdnq4wIL7u0XGC4Lmu6p3SyfVN7L4mOVh+Fq23AjEZEs9OFV722gT0XhnEOtmLsdtvfHVideojzt6eih9vivPI0Ndkh6PYsFpszJsmEVzMNqmieGbtOy5rLe547q2h1XMFn73YZ6TH1prGw8NuK3y7Xk65sQ/90CGgpUaICKe0sBVWJd3I2+CFzfBppFP7GRXeckrsJk3wLJ2+CwWXYbX3wTVo65VyNVlU7bGNSHJR1qsc3GDbt1YTTCp5uicNwEBrBILtif7GPtASKxininRzP5cs1WDqOanpKRaHOsZWjGiWlDLDQsT+cy0CyTeoanG9tx9+K8iop4jo5inUyuGrf85zjZVfKOA1sxqKtdwzrMsXPk1XQDb1DkEBqzFWU5dxhXXp+7bj+3jmQQq1Kgnw4aOEVstGz0ks9Xsil77NyYLF6J0Fjxo+7EbPUgsj1NX/ViXXB7/dLRMH6OgaUr+pn/8pmq+Q2CutKITfZsE+Kgl1SVba0DpAgn1hLj0j7viUGL3Nl/bAKqHspreg+mIiDMVo0jN01b0Pi543bJAJzzZ0M2jbIoQnPtXnb3jILg6QIuVlnooa702aVtL3CHGBS9wHnUZoULG96zm5Nz7Sqa8egbb4/2DGRaVg2XhSqrjYNKP7LTNjv6IzJvL5t7ugdwHm6T1sLWcH5jdXxcOoug9qMxxXFkzaLnJ1wuKs7pNFTj6xIr2mEI63sAJBshds2b21L8TrXQSzDTk6+QVyRwmv8ydCTaaucDqKWHeSo480aa/bCXjhyWrvcmbZ9wYSG2U4aDAvnzWUbN9GAbvt4p3axDyiUqg6tSQ27lmSETHW6TSSi/c1v/WO6vCRobQ7QyiNWJBGnNp3xPrmkWxcitV6rufuhozvacTe2i24rfxOA+AjrECJMva2CoFqWLB70+QXLmgsiY7JxWlWwYdFyNRGwvddTxZKhNRJtqmFtIErrDILpdCUKtjxkpUZ56TDq7HGjtQ+01SpCZadEkiANhc7sXHNcJYJ7jZlWl2O13nA7r1FWh47Hj7d9SVVLQLOodYKxlAi1y1DZw2Ey3JzjEz+GoK0rkCWvVyx1dKfoaq0CxNmc+MsBEUG1sdrXy9uut1oB19fEKKrjlct6jLnhtdIu86Zskbh2yQY0v7u2MzQxkGCFc8czmWBeuz0MGxvCJcPVj8dT4a6buuFU+qiS7taCzXWitZnMjRoUCF0UYMXJ0TrNhKyTUE3L2kNTVA9sMyR0ulqCBoo4DuxtpCuiu6A53zkTsqxspTvXOYmnZ71RwtpsLaKJIXVr38dqs5qOk2Aem9sa9leG1N8RpoOsZZ75YGVblzqK6r2jnuwKotxvKxtuvQnLglu2JmTfqDlrWVJ5uKkQdXPkSPzE3ghx1SnH/JiNdUlYXeQHSa7zuRdqrjauyKa/tEifoh1BdkcpM2ne4xDODvDUR9SD4atxJdwCSN/nilIf9/Ge0qo40HxCXKv8Oj/dQ/RAYnAJW+iBO9zU1g8rLAZd0/Z6EHobNc9Q5V0kBAYYS5IZ1IBOUEjp80SCAsInvGU5ntTTZnSgeOetR2NJGO2W6c0bM2pHBENru1Wgk09vDO9uNka2nhyvC90WtAVbguc3GCEmyo1RuM3VUOr6ol5FAU0nU3X5dpupR2YQ+c4/QUzJhf1pH1cSlWITxRwE7UbxU+AoSHdvkPIeb2/UuIQGNB+V62Df27JDhryIiN3BL7polXIUX4X+xRfys2dgLEKvZMzFPPN6vsKojoGaTdHxg6CqaU8X8vpsos4w4X6QhS7Fbzs1OQ6ybqxBJyvX6a7axlXWOrHSAMTCgw6OanbXFnREUIhLICvl0nB91Dd306rbsTeJvCyiPOOgHV1elJYCdW4cwLetGZWZMcbyPe1IT81rqY0qGvZzT4ak26jiocJrIrOuzvcVshw0g9FY6gxqVWEFdBfqAd/tulvuK63EGCPK5VPm3uztPqrtS9xbrkAcFem6XQIcEcl0HbRLv+3uW0tzWh9eIatGHBp63AbYjes9PFnZEa7u1OvxgOSx50O5x93FIMw3d39KT9ppuDNlOVVb2KnRxudyGN7Dm1KDSOZ0vUOXKFgVCVpdtytM7w7waby7PnQG3N6JFXclruWIoGoD115YszmxZhjmL28f3r6fr739Tx/Mmg9V/p+d7TyPYb4+fPE4N/Rt79NjrU//Y43++uGtdmOgz/P0qkm78HXY8zdnVx//xdngPHl6Pun09Qj4eabc2uH89O9bnHtd09bTl6ZIHw9egBlO18xPDDazhi54//2x53Oh1/nnl7Z4WeG/zQ/zzQ9T+F5st1+/hq9zvA9v3uuJny/Yivji1+Vs4uvcHliGvS/fsbff/i+50JRarS0AAA== -->
