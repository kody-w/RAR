---
name: "rar-cowork-cookbook-report-manage-project-quality"
description: "Builds a read-only manage project quality summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_project_quality", "rar_sha256": "90e4dff32fb78fe723bc8762debc983eb60805b8891ec79300e0c79d31052983", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_project_quality`. The original RAPP
agent is preserved byte-for-byte in `report_manage_project_quality_agent.py` and in the RCI capsule.

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

Manage project quality Summary Report — Builds a read-only manage project quality summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-project-quality
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
      "description": "D365 legal entity to query, e.g. USMF.",
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
      "description": "Excel workbook name, e.g. report-manage-project-quality-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_project_quality_agent.py` and embedded as the fenced Python below (sha256 90e4dff32fb78fe7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_project_quality_agent.py` first:

```bash
python3 report_manage_project_quality_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_project_quality_agent.py   # or on stdin
python3 report_manage_project_quality_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage project quality Summary Report — Builds a read-only manage project quality summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-project-quality
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_project_quality',
    "version": '3.0.3',
    "display_name": 'Manage project quality Summary Report',
    "description": 'Builds a read-only manage project quality summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-manage-project-quality',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-project-quality',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6af6814bc75afba9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/analyze-project-performance/manage-project-quality'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-manage-project-quality', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Excel workbook name, e.g. report-manage-project-quality-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where manage project quality stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of manage project quality for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-manage-project-quality-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage project quality records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only manage project quality summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a manage project quality summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Excel workbook name, e.g. report-manage-project-quality-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when a caller wants a no-write summary of manage project quality activity with totals, by-dimension breakdowns, and a Top 10 by value list from D365 ERP.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportManageProjectQuality(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageProjectQuality'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. report-manage-project-quality-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportManageProjectQuality().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6abOjSJblX9G8NpvMbCIeiJ0oa7NBYhMCIUASEhllkewgVrGj7Prv40iKyKWiqqvM5sso4j0EuF+/6znXH/z65nRtXNZvn97MwCkWopNlSRzUC6fwF+tyKOsUHMrUBT8LryzaOnG7tqybtw9vftB4dVK1SVmA6asuyfxm4SzqwPE/lkU2LXKncKJgUdXlNfDaxa1zsqSdFk2X5049gYFVWbeLsC7zBTcVTp54zQIjiYXwv821ughLoMUiSvqgWGRB5GSLoGjn+bNqVdm0ATgEdVL6H4CotquLpIjAzQU/ekG2mFV/aD0kbbwwn2t+WHBB6yTZh4eQQ1ktkUUTB0HbvAODgtHJqyxo3j79/NcPbwn4/vbp1zcvcxpw6c14qKs+bNo/TdKfFoGpmVNEYEw1AWcW4BwoBvTPwSU/CBevsx+bIAs/LP7zP9PBqaPmp0+fi8Xr8/lt/md0xaKNg0VbOg/zPKdy3GRe4n3BZoMzNS9LZz83IBZF9P6c+Zukslr813zvx+ci71HQ/vj5rQQqOHOkPr/9tACO/fxWd/P391lK9eNP71k5BPWPP/0mp+ncR9SAMKD1+5fX+UssGPjb0CRcfDH3/Pq1Vh14SRUA4b+zb/48VX+Je7nky3Pwj2X1YfF9ybM9/wX0fWabC+R+XyzwAZj59n4tk+LH1xp1CZLHKbzgx5/+kVgvDrw0S5r2X5L781NwDFIceOvlkp8+PML31wX0su2bzH+8bAUS5t+xBAz/utw3R/0j2Y/I/kl0lhRB8y2W3xX3vQnQfy1+/oe2/bMJHxbh5zcuyED11o6bBZ8Wvz5S5Ocf/N8u/vDXvwHR/6MYs+xq7yHhC0CUJAya9suXn39oHpd/+OvPP3QVyOLAyb90dfY9md/z62OdP3jwNerHP84F6x+LtCiHYvGthha/ltX/qv/2vjiB8vd/u958Wvy+EucPtJiN+Lro0wW/q8YG6Po7P/709jeAOwWwpvMetwF+/Md/LNTEq8umDNuF6ZVduwABbpM8mJU/xEmzAP9n1KgD4NcmAY59jXsB76xxGS5++T/eA88/ei88h58A/OUJ019eo7+8YPqX98UBCC3rJEoKAL4Gu99/ngcW7bxgVQdNUPcApNypDT6CWv44f1kkxeKXfyr3y0PEezX98sDg5Il4xnozo13TZcH7bJcVA9R/WuEBSA/GwOuA9Kz0gCphAkB6Bv2mzHqAlrMPmjTJsoWfADwB9PQkCeCnT7OwX375xXWa+HPxhGds8eStBgYDvqmz+PgR2BRmSRS3n4vAi8vFD7/+7YfFfy/+2ayH8HmNPSCJVxSAhrKp7RagqrocDAMBAiEFkPGIwq9/e3kWiCkA0YKYJWESPCeDrEwD/6ubTYn9iBLkwg2Ae4Fr89mtM8kl7ftiEy6+6fui0pkVYkCMCz+ogsIPCm8CUh1gzjdPFmW7aEDqNSHgwq4JHqv+4tbOQ8UclLfT/rJQ13vAQWUGfs1qPgaByWWRAPd/S4LndSCk/qFZrL6KeF/s5jxcVE7tVHHtvNYInWdcZlJ/TQfCnUURDJ+LmWqD2VWPoni6BwwCnvFeIf04xxw0IIDFC7/5uvZjjDMz5eHBmPXnonklvFPPofAAAYBFoy7xZxr4yyulmrjsMv/hP6DpLOkVBf8VlUcOqt9vX16txOLZDyw+dyiyxBf/v7c/s8GsKBq8yB54bsHvDsblGYi565sD9mwUZw1m1R5F91t/8hWDvkLx5yJLQFbV01+eIx/he415wltXAwMM1njIB7kDAjHLfaT2nKp1PReF87n4ivlA6cUD4EB0AQ6AOpnT8+uC892vmsag2Ofz3/j/kQq1P5sN0ndRdW4GUisMAt91vBRoNUftayhBngdzqQ5x4sV/sGoOAYgckL8ASiSg4AAvvH/D4efdr6r/YeKzzZmnPFrADlRn/RAA9AhmBeeAzKEC6rXPJhvY+ekhBJiRV+1suwvqA1j6vBjUwa1LmqSdsfDp16ACIPxxPj4tna8GYwWyDzgLJH7VAe8+SmXOlRw0MUAHgBagcvKkAKQOnPJywkOgk891D3D11XU+JT4uvwwKHvU1s9HXibMh85yZ4J/J7RTT7+Hh8L00AfLyecRj3T9n2rfVZtkzRDYA5sCKX+8+O4H3J5k/u4XFV7mf/m4X8+O/t9F50PPxjwnwaRG3bdV8guEnpX5l1HcAUPBT1+bFrh+fKPDxhQIfXyjwB6FPez8t/j3F/iDiVRifFst35B2ZbymvxHp9gB/WH1eXj/h893NhBL9hJ1i+zEFmzVGbAJ1/I7qvQwDbRTWAIDD4SXzNzJcDoOgH0oMQfC5+n+lzpQEiKaI5M5vydwjwYHyQ9c+IfSMkcKtowdr+3BlGwbwXe9RFE7x9Kros+/AG4DH4n/ZgM+Pkcy4387YNOBzAY5sEjzMX6Jb6oFq/+CBXi+bZXP36pz0s9+3eI7e+TWpmYwGhOFUF9Hr2s4BjnbqdSesDsKMNonLGV9CTVGD6owkDEwGTAMXaqZqVf27Y5hbvAVRj+/cKaI8vTvb+Aurm99n/Yq2ZtX9XpE9/Az97wN4PCx+o0swsC/w9u2IucKdJHwZ9V5cHt3x5cst3PDIT0h/oB2DurQtmW4P36H1xNFXhu3K/9bh/L9QCTcYsxy8/zXz74YVw4Aj2JcCbX7cYwJrXpu+xOy86sJ/+ed7ezMF+TJm/gDng8G3Stz9MuMHbX7+n1wMGv8zp+EyqP2v3J/6cB71s/acV/RFFUPIjQnxE8fcxa8bvOuVJ2H+/5v73fP7oup7NQVn8BfggdLoMFE1bPgKezx0eiPrMdH/oAxZOD1Jmzs7vrA0Wf/AFYN3Zib9F5zcflY/94EPNzGmff7749Q1UlAOSynnV1GtDAYYDeP3YzO0UDDAHLAjOn+gA7v17W43X5CZ2QLcLZjNIgPthiKGhS9FhQKGY69EUifqB6zE0FrgkQiOES9PMMvAoBkOQAAFHH1siBAoGAHlPgPkyN4zJrBDBUCHCMGiIL1HEBy5Fcd+nSZr0CApFHMZ1CJdgHPe3qWlS+C8rn1bNLvy265m98TIWgAuJg5ES3mzY52cNM0sXtih3Us7wGaHHbLC6SgAEp41SQFhugiwbebjqlFKhbXNeC4a5lfjMO45DF1Pm1RmvpQ7rMjQdMJ+m1OPaENAjiaJ+2/I8a2rnfX7fF3hxoe2AoM7B2KXD8bZVBA+ealbfE6cVH/uudxK6XSpCQuBNRyyN4V7Eerw72/bIW5GeZAiPnPJ8Euy+m/xKuzdYajs4iuemu6oafKltlZqizRqm7niftNa29JaCO7bHUdhk/mqTGw6yH6Lr0cz9tTRuwt3FMDV925T01VdP57I+cKSgjhtsW4/29nzJ3U6IqDgNE2Nlr4rNdJm47rQ/pGaQLLMyXAYUfa6XUFCAX7R2R4yKgSANhlcCBFvHUr8p7npYq1VSn2WnGKN6WfPWxWaFhLhisUALqyqwlZqDDyYkC/fCCtCLqHQ7vkv4y3HjRkI7hf09LuhU9KbqLo/lscdiPSq0YIy5FcWLIp0pJTtAskNcK4vfXLb1fU0dd6eJ2bljp1NIXhAcWa28dHMxkSg7Sa1oBVgcKNUGF3hAAchRP5d8cYyTWhWsShDLym3tsROpJkb0/fUioiy7G6ML5AprmTKo5k6N9/3Vyi6ah6cHm5O95LDdyRviMHhKmkXXnb1eB6lgEHsxURRutfVVFia6puSRPkoUUWiWXO514ZRdpdjXr1sEsq9G6KpnbBK6PIZlboUnbHoybHvtiNAR57uJw1H9eKATPrLUFuady13aBFCQ6EfX4cYNn7dGl3lMe+qMixjVg8ylpqfDV522EG7letWqG73G20YnTkR3a7DNZmsd2eHrs+tnVmtszYOmYOblhg550dUnO5f4enPGyy28Tv3ltsRP1gGBMk5ihovF76lBDIEaURJsKVNId8mIg71+7EhUuNzHx3rTJAizl2XNlEsbK2K0vKuX+y05S2lzlrDmfH78aCl6X5IFrinuTdgO+4N6PMB0BA9VA1upNsHTmsNhSZFoO8Tzc3/e4ul+3UQ6zZlOtOM2+akd9U0paPZ46hJZvG/2p1vjqZv9CtrUvnOH3SE+D2LZmaTULpvJkdatDzaBG2q5rXOC0n21EK9bIZbyW7V2lHG7ngaf9blJMA4leyIomiru9D7z9qsA2/s3vqLVpaKa7jqh901+Vyl+Gi4ok2KRWss+hfZ3YSseutbiMfVquvkp3t1veA4V1jIzWROKVibsqdDVEn25kRGKLOE1nN+mHbtdxhLcIt6qnZZRQwXXq7tzdwq+PY3dXQmrUZSdsdAY73axD/UVMeCjVbE946Q3Yx0y6j2SCkypLxwhmt105IxJDPectj7y6ZJXU8yCT9QqNe/dpFYjFxeabcOobZsFD8nnbUuZFVpNW9vpLoEhKNg1osOTlu/CNl6pZFY0PZL3F/SGDFE6cPiO1y+lFgY71GRSxIpwZo1nYiDBqeOdfEkWIKYl5UpSXUBbLI1FWZ9ZOtUxnSpLGm13k+XdV4obrWwpWt7K+zmAruNZvGDxMWDP5lEJ4s5klcqKLCIUJ3qLXRsPWgeBthkj/XZWubuPpZVBtZjdD/S1nCKxoS7YCBf7bZtpBnKd7lMchQHrYqiZ0ownQ9aWaFFlkpG7tKSGo3UNTbcRNfbuMkfRW4vRVbiEnhRAslFPaofpeqNDh9HHUMwC3XU3cPuG2W0li+CDewIJCQ3zQsQfJJ2cWMxbLXn2tNnFpe1I1w2CnAAKC6seo+73g2fn/IjYGz6d9C6rc5JU0Tjd2qblkK5hpsltRE+9FceavFozkSXuz/w5q/jB2ewUqd6X6qla8sldL9nLpvDr8SgUk3I55dQ1oFkOACToO5kDw97qbGithnXXtXlnDxfcXV1XtiyWY+kYGd142EiG4bkayEjdQJFphUZ1KgWVlzKn3knlUWPxab2pEpwOyb14jbETpXFyedP1M+IrCgwNhNoLkNT3w81KoDVcC5htnnBhOtzvOs1bq9Wac9XCHTy03uxEs+GMQOm04SByIYJh0cFZ59OVKnCxvPXpMb8eArdp2MveDDUH0qdAzNRhuulSpKXjcDBX3VAJzXhfHc8oICdcmvojqipwzTmant6xhs283a6AKJqQeZM1jLvHd4TKwdf22tvyeD+hEcnDdeMlkKJc7OAUtWfh3BXRWUBr4kaHKutv1mJcH5CTPaTt9uyGUSTcjmgY4fdSn1gFSwrJX6u8TNcKiuG61w3XBiSph5iGI5LmSt23sL2FRTyjTPXALxFY1u9GXu42WBWvppOMcfylNWkooq2Vq10KmIt1yawvm2NZd9valNm8jI+GMm29JarqRGLToRaalR6dpLV6VERCVKKSPVabvbBbbxK0kOM6gWmE3MrsKOg4fbpK9p69ViKkj1LNiFfQRyZrvUSwVUt60kbQ5aOQ+JtzAm3V8nbKleRoT5tOB76/qNYxqR2kP+V1vOflukwFZW2JCn3LfPLc6dFFkC+ewuYrq2WQu31OY2jnX0HeJQJJtIAJ0tEsTiiRiLf8vHIc5bp0VxvUI/ya8TjELPY717KnoK3FS77ZESPa3wxJgWL5QG9xnsWC2y1WCSW4BVuLbRyfuDZbYWtkArW21e2QbAlBUQkyqlJv5oqTwp/pdBfFhi1wHHa6kgayo8VSUos7hZ6pmyxqa+iS7cVAGHFUOsZGLp8pkltDgb01/H68X3Rhz4WcR+3aMzXou2TFbzQfsKCnQGZVcqHD2fa0Rvp7Qu0POHLdc72f3re7dHRvN5aIb5sKwzrZX5ftpWoyvTsYEqfJbGxqg0IyAn83c7sasNJI9Xoldmd8p56Wyu6awgZx14PTcU8nBsTlTdPwjtLUdslLu2ZZs0Vhn6RU2Khiv96twkY8DOoEsFqRNpf9Tqj5GnSL6QY5NPA+5nnVlVFvd1NGjEg9FiSJtpMOTqGh5Ek6QWlkr/kqsvT8dD0YcLkJdek65hXab4PD2duhZzjEoGQoZC7OKY7yjFSS9xizd6iTTKWldryH6ibL7mJGrfWQEC9HErMVxi0aKDgSG/K6r9atYvLZJqxuS95mo9owbXa3xQmNd/y1sLPZ63QRtWRiN3m4Oq+minUvUga6PHt/yyC6RstL5Liq5e8Gvq0dYd/ww2V7kYb0LG4Lc7nK8xHA23A0bRVW0YJks77Tthof0xZa34LSk24nEPPIWNVoxeb6RgJptFlfRt7Qco4VaV2Wx/MR8m6IEKrKBAuVu9559ZA1dSaG+nAhcHbkWzmEAoVKqKC/bgybkfYmL/L7g0Wepsihgp3DROeeZrRrtYS0a03b+x7WYXlfcuk9WGoCz9zGsBg3ZMsIZ/K6Yu+6cMtIVxjdDNU5NrFFxGLWWzzen7bCgZCc7iBXS+JQjinuGIebq59OyXnw5cltac7ouINXRlHKnT3d2ViRe7zopzDhe29yO424AHiRN76kVZ6grGqy30UiKjTU+hrhTnThWfE8rW09WW9cvMcNbafa7VHDxwtnqyB5TLo5rTDtmoWMNGJqnGUJvqPXk8bYN8l2YZlWChZnCZRKIaeu+53DQ6l1a05Vc66VK4P2Oqf2k1GHN85vPfl2JUGyhZixjPIJdPi7vGoEUWa3iLwTpyMer1WUNyR+AHugPbck6aIvKR5x5PzEl+7IOjrXtZ26LYNq2PEsgg28jiSQpO8TcoUIFM4dEdhZsswOqg7cQJTtnQ1YzeR4Ag8tnkMKEq73jFG3DOxKzK5Yx9tzkjsj3bQ7eimbwlR5DaYSveHLmXo+HJH2WqyFYs9CxEntboAEDUm+x4yJnSxLK6ybuW17XLROay4IEmK/ZqBA6Mvey6Fhya9jvYwUjyaXw7Rt10hh05V892+bfto4zTHaIayTosd0M+6K6zGPyroUh2pVM05DRn6/c7dwpznn1INMPbW2/dAo7JXfo46+EV3WO6nXZIXc+0PV3LjD3VeXLrc92cXKow5GDLrfK1WbLSNOw9I97q1VPRi8QJqE6m+n6VhCMJkFIDocVeXrTqxhJsR7USGFsVFTUzP9IUUuvTItu7206XE5ZzBSkPRCoLn7FdlXHUQGxjplymNrYuP+SkIdyQXTao1PImrA21AimDrZRX1p9fZdPjEd6ZFpjXdGiLoWPtq9vPSxFauwWpUhXWwuGzInrsikYwXUV0E2rLAJBdQXVMIwgAaUTqe9c4psTJNWxhbSnL66bgIM4j1DTAST5W3ftdQJU8US7G70Sq49bKcZlrts6Fbk6Au0x3fNaTqv76QauSfXtyukx06QMwrQoCcaXVok79jLC0tpd61wcl9yCvxuruqui3LkFMikNDn2qDrVNix6XZFsiSexHARISgiESU7lvmwJmFyBrr2lqaWs4e5ZbzBFSI2zewx3CHkmhzA84eiZphx17KSEROX2HLbBaeCQVITd+F6dNKhSj+ui3pRLssRQY7nutv1+XYiRX68NWD2v7oV+P0D56oytLDdYjjTVbe8R0Vr7sLzjmSfRTlkh/JlQGH3J1sLmEOSNrehUeuRPKzUnjUhCbb/h5dYpiMA+WMPoKxpxWtr0EiuM4bg6Bz2SRO59NywhgWPqAcev+9gs/dYmsV2/a1aHsogjUgp1bs0pR2QQe7tp4TQMYdqFy2554DaTFe7vJ1iE49ZDx10U0O1pl24ZhHM9+Xij0qyrd5EVSmXBTZoIpQrkgpqBYoeFmBPomsa9W/irU3vZXCmRw9nJFIkO8nahLxe7OEKr5qSomEZW6PbgEx3W+y5nJCvHY0KBatrpnGuaPpWj3eIDU1zhwqxGB663tR9RYLfDsbayJSWIZupKuSNYsuUmKkLCoVUaUh8vDAiKU2NbHobCxGsvWej37e62FN273SZ4BzpxutvGWGvilHVldmaYUUwuYnjCldNVB4jFJ8ZeuuLFwW8mmlRrPJcbZV21OhHLvlFulvloLx2yzW4BpfegTVNvzd4g2wC9pB7G5MIJitEjrfarq4r1t7t36EftbPLQxtLQTeYd92IqX5dcOsAlsj/e1CFbS6Z6OddjYTLd1haXvri71yp85A8IHozj5QitaIFh86LV0auMDcKBvSbHvYvqoXYF7QhpL411nsn7kKmD8wFhtkUPQRelDL3E6KmtPIk2SvTRanetN4K95AeayHdwcvEvqBA4MJWxnVU7h8Ohh5CiMZA+dc7IsBzv7BI7odvcjXa1fefysrNTn2hO13BLRpRxzrcg/de9XRFlDbsq06BLwH2ya+2CniAvfLdR66zhKA2x+lWHxruThWvqYcm4fHUO6A6tVRndH8xcA1tvfCAoK+fOF2m/s3i0yvYpZPmO5BZIilRqdD8dct6+JrgbZyRDcav7ClkBxF8JeJ61I8WydBrCxmgVEV5vvF1MDYKEGiHYkwS6ZE2mLVhEzN25FjOQxpXG3uoBEVGmc6rp2A9o2qeyU6vduf0OCtHO9Uq6FdSD1jMQefYmLcwzxRuDkKoCl2dWeeEgKHO6B/2oqudrt/TdlN+Zyu1yuFoKRrpSe+ixJtgcl2GzDtPgwuY9eyTP7T0IQfNhaDemkq7ryr+NS3bE9AAtJHS/rfyVxfjYlbwYVK4oKzokBETEy+1xoiMyyvSiVrxrHTd8eVdCMpOwxiiEfkmABU5NcrM5ukFkw64xtrdXmgIj3Oq8hljN1tPO309tfONkAJSO0dmZZo2WMkZwyuvhukCt0b9KSYoqh9DcUpbZ0dhFyNyMs6VSJQ+asyeSGlX6fSC1JaDwySk2pcQmwpIz15QFrzjXP2rXHbI3UOfYn7M17gVYSOtDaKxakZBCTNTuSG2jFbXdtwriVdrobmjFny6OgQMfYq59HOucbv1tfnUzhyCh6nSsuct2SVmau+mvA9rQTtQ1qRovEWUzhFiXTi7N6Eqfx1uiv7Fopt/cfq9gh7Rf3zTnwJJ5T529lihwIgpMLCVHa7cN5ZK9tYchXQVQttpAZt4cjmwqNw4ZWEp5LggZiSvMWZ+PXtBRyrL23TFUuoBK1zYPV4dtV8cHWKytmJhcAkYG+gJX9Oj10I2d2Gm0ki0j3IuIRy5ie9C2MRzAzJ5YE2OIyGiFCDAPOhHcrcaRQkm8Xx4quMMgogr99ZnJjqsS6m/d2amwK6bkuYatyBjlfORwH+XbStr6pSM4iCPeVkLI3ND6EGZSr6eYt6R4IvJyzC0lxWGIMDiNUQuZMncZOEPPj3eHXCbWxWAqL7tjq1oHNL5W16u6yPbR1rgoS25zi8KYoXuWi5ELvGoK9O67DaVGPh/hk5ruE/tGHyxPbCjHBb0iuQnMa3FTQK9nhKup3NccoO2upKYAYngCFfAlerJCJutYDsp7LzxfNxnMNBRiHFGXHnHNZRIPFzhIyYGWh0NMIg7VI9vbObmJlZMsuxN89DQsRAhTk0tmHKFlMy7J1mqEMO4aLnRrf+zOck+BesiFQD4j1BqF7Hg3ShSFUghyXxFXocLOWVd0aIoOy4Do3S4jhZgu6HWebxCeXW4J2rl5chVtkmB72244xthhBklrSVKXBHZ1TZ2n/Ri0hsUGje4bB83KGpNW0JEzLZ3RisDUCP1M+VLtNgPKW9S5h9qgXqvK3tMxBh9dLJC1vAy46YoeudbGi3NfYYY3SfhuaLCmOvEnVR22jneLYJRkain2Yfh+Hm7HsBsE0YPTiw3d5N3YZbRbncWQjIhO862BWWGsILa0P+FkzWEh2auaK2R6xLJvH95+ewD39q+9LzY/mvl/9oTo+TDn6+shj8eKgeN/eqz16V/U568f3movAdo8n381WRe9Hhj96enXx3/64HCeOj1fvvr6WPj5zLt1ovlV5Lek8LumracvTZk9XgsBM9yumV9gbGbtPHD8/RPR52rPKw/N23IeFibztaSYX/YI/MRpg9dp9HoS+OHNf72G9AUjiS9BXc0mvt4sAJZh78g78Nz/BT09hcYzLgAA -->
