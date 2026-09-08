---
name: "rar-cowork-cookbook-report-define-project-stakeholders"
description: "Builds a read-only summary report of define project stakeholders activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_project_stakeholders", "rar_sha256": "a3e22d961139f4e8cf983a32fac117afd5550d1685a782e2031f00ccbf696c98", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_project_stakeholders`. The original RAPP
agent is preserved byte-for-byte in `report_define_project_stakeholders_agent.py` and in the RCI capsule.

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

Define project stakeholders Summary Report — Builds a read-only summary report of define project stakeholders activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-project-stakeholders
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
      "description": "Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report against, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-define-project-stakeholders-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_project_stakeholders_agent.py` and embedded as the fenced Python below (sha256 a3e22d961139f4e8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_project_stakeholders_agent.py` first:

```bash
python3 report_define_project_stakeholders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_project_stakeholders_agent.py   # or on stdin
python3 report_define_project_stakeholders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define project stakeholders Summary Report — Builds a read-only summary report of define project stakeholders activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-project-stakeholders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_project_stakeholders',
    "version": '3.0.3',
    "display_name": 'Define project stakeholders Summary Report',
    "description": 'Builds a read-only summary report of define project stakeholders activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-define-project-stakeholders',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-project-stakeholders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '93bb1960c479c4f6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/define-project-stakeholders'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-define-project-stakeholders', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-define-project-stakeholders-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where define project stakeholders stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of define project stakeholders for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-define-project-stakeholders-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define project stakeholders records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of define project stakeholders activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a define project stakeholders summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-define-project-stakeholders-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals, breakdown, and top-10 summary report of define project stakeholders activity from D365 ERP data, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDefineProjectStakeholders(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineProjectStakeholders'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-define-project-stakeholders-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportDefineProjectStakeholders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916aZOjSLblX9HEM5uqemQGq0DKZ202gAAhgcQiJERlWxb7voMQ1NR/H0dSZmV1V3e/HptPo8wIBLhfv+s51wN+fbP7Liqbt09vum8XC8HOsjjym4VdeAu2HMomBYcydcDPwi2Lromdviub9u3Dm+e3bhNXXVwWYDrTx5nXLuxF49vex7LIxkXb57ndjOBKVTbdogwWnh/Ehb+omjLx3W7RdnbqR2Xm+Q2Y6XbxLe7GRdCU+WIzFnYeu+0CJ5cL/n/qrLwISqDWIoxvfrHI/NDOFn7RzRNmXauy7Xxw8Ju49D6AJbu+KeIiBDcX3N31s8Vsy8OMIe6ihf7U7cNi43d2nH14CDmVFYos2sj3u/YdWOjf7bzK/Pbt089//fAWg+9vn359czO7BZfetIdZm4dJytMi/TuDwPzMLkIwsBqBiwtwDrQDRuTgEnDE4nX2Y+tnwYfFf/5nOthN2P706XOxeH0+v83/tL5YdJG/6Er7YaNrV7YTZ8Dy9wWdDfbYvsydvd+CCBXh+3Pm75LKavGX+d6Pz0XeQ7/78fNbCVSw5/h9fvtpAbz7+a3p5+/vs5Tqx5/es3Lwmx9/+l1O2zuPyAFhQOv3L6/zl1gw8PehcbD4oisc+1qr8d248oHw7+ybP0/VX+JeLvnyHPxjWX1Y/Lnk2Z6/AH2fOegAuX8uFvgAzHx7T8q4+PG1RlOCDLIL1//xp38k1o18N83itvtvyf35KTgCiQ+89XLJTx8e4fvrAnrZ9k3mP162Agnz71gChn9d7puj/pHsR2T/RnQGMrf9Fss/FfdnE6C/LH7+h7b9swkfFsHnt42fgRJubCfzPy1+faTIzz94v1/84a+/AdH/Uoxe9o37kPAlt4s48Nvuy5eff2gfl3/4688/9BXIYt/Ov/RN9mcy/8yvj3X+4MHXqB//OBesbxRpUQ7F4lsNLX4tq//R/Pa+ONtZ7P1+vf20+L4S5w+0mI34uujTBd9VYwt0/c6PP739BsCnANb07uM2wI//+I+FHLtN2ZZBt9Ddsu8WIMBdnPuz8qcobhfg/4wajQ/82sbAsa9xL/CdNQaI/Mv/ch8o/9F9oTz8ROsvT6j+8hr95Xuo/uV9cQKSyyYO4wLAsEYryufCDgEcz6tWjd/6zQ0glTN2/kdQ0B/nL4u4WPzyr4V/ech5r8ZfHpAcP7FPY8UZ99o+899nCy8RIIGnPS5AeP/uuz1YIitdoE8QA8yeOaAtsxvAzdkbbRpn2cKLAbIA+npyBvDYp1nYL7/84tht9Ll4AjW+ePJaC4MB39RZfPwIDAuyOIy6z4XvRuXih19/+2Hxvxf/bNZD+LyGAjjjFQ+g4U4/HhagvvocDAOhAsEF4PGIx6+/vdwLxBSAiEH04iD2n5NBfqa+99XX+pb+iC3JheMDHwP/5rNvZ86Lu/eFGCy+6fti4JkfIsCTgIYrv/D8wh2BVBuY882TRQlYGSRhGwBq7Fv/seovTmM/VMxBodvdLwuZVQAblRn4Nav5GAQml0UM3P8tE57XgZDmh3bBfBXxvjjMGbmo7MauosZ+rRHYz7jMHP+aDoTbi8IfPhcz8/qzqx7l8XQPGAQ8475C+nGOOWhQAKkXXvt17ccYe+bM04M7m89F+0p9u5lD4QIqAIuGfezNhPBfr5Rqo7LPvIf/gKazpFcUvFdUHjm4+SfNzKu9WDx7hMXnHkNQYvH/XY80u4EWBI0T6BO3WXCHk3Z9hmfuFecwPtvLh8pl8yzF3/uXrxj1Fao/F1kMcq0Z/+s58hHU15gn/PUNMECjtYd8kFEgPLPcR8LPCdw0c6nYn4uvnACUXjwAEMQcoAOonjlpvy443/2qaQQgYD7/vT94JEjjzWaDpF5UvZOBhAt833NsNwVazWH8GluQ/f4cviGK3egPVs0hABEG8hdAiRiUIeCN9284/bz7VfU/THy2QfOUR4vYg5ptHgKAHv6s4ByQOVRAve7ZmgM7Pz2EADPyqpttd0DVAEufF/3Gr/u4jbsZIZ9+9SuAzx/n49PS+ap/r0DyAWeBcqh64N1HAc25koMmB+gA0hTUUx4XgPSBU15OeAi08xkNANq+utKnxMfll0H+o+pmtvo6cTZknjM3AM/ktovxe9A4/VmaAHn5POKx7t9m2rfVZtkzcLYA/MCKX+8+O4X3J9k/u4nFV7mf/m7v8+O/tz160LfxxwT4tIi6rmo/wfCTcr8y7juALfipa/ti349PEPj4AoGP34PAHyQ/jf60+Pe0+4OIV3V8WqDvyDsy35Je2fX6AGewH5nrR2K++7nQ/N9hFSxf5iC95tCNgO6/ceDXIYAIwwbgEBj85MR2ptIBsPeDBEAcPhffp/tcboBjinBOz7b8DgYezQBI/WfYvnEVuFV0YG1vbh9Df961PYqj9d8+FX2WfXgDGOn/t3ZrMyPlc1a38y4PuB4AZRf7jzMHKJh6oG6/eCBri/bZhv36N3vgzbd7jyz7NgnY4r+H7zPv2k03E9kHYEDnh+WMrqBPqcCUR4sGBvvNh9lBgJ/sqgK2zCUxm9WN1WzHc4M3t4QP4Lp3f6/G8fHFzt5fwN1+Xw0vbpu5/buifboeuNwFVn9YeEC5duZi4PrZIXPB2236MOtPdXlwzZcn1/yJX2aC+gMdzY3Dk/Hs8FHjLw8Zusz/6QLfmuO/l34BPcks0Cs/zfT84QV94Ag2NMDRX/cmwKzXbvGxty96sBH/ed4XzbF/TJm/gDng8G3St79zOP7bX/9Mrwc+fplT9Jlof6vdYcY9wAuzl/+GZIHOYF2vd/2X9f+6+D9iCEZ+RJYfMeL9nrX3P/XVk+D/XhXle/7/LgRl8V9z12H3Gaivrnyoms99IsiKmRn/0Dcs7BtIqX+QlGDxB78Alp59+3vQfndd+dhfPtTM7O7555Bf30Dd2SDp7FflvTYoYDiA44/t3JTBAJ7AguD8CSTg3v/F1uUloY1s0DgDETbuY5i3JlEUXweEv3KD9Qq3cQy0oyhK2YG3XC4RDyVXS5taYT6G4GiAIK7rBOSadNcrIO8JSF/m3jOetZpVAs74CDDN//02uOS9zHmqP/vq205pNvtlFcAakgAjt0Qr0s8PC69RB75QziiZsIms7tlw6St+bn/uWxDgw123MW7QwG7Q9hyHH5irEWvrfbu3JEn0ETEqOUjbQcNpLQXH02GTamp2XBd91yFhyGrjsh2tFcxR20nBlP0a30duneqShNzX2YWOPObgjZlra5N0IaRD0IgHSGSXeebrW2jl+HC8BNv3WO7oaiuJTF3ozqBhJbWf7AgRbXFzEI+DsfFrTIz4oqZ4Ur/u0LgxiLK/3e77G3wLxuUevVabQpTWl8OJU9sM4VqLl9SIZXfazqnVfrdZxvVBy+Jxrxy4ndGveMEN1HsuYZMOF3VQdU50vrtNd2W1o6UJpS9rHF4HVoodozMqXrAeRs3mDgXmFoNak2rRw33dU+u7CkG+BOliOp7osJdK9n6xXUIOKT6uHFUMx/FaL2OfOPvMcLnk7BCl+PV2VmSPnFYTHV3rTCBExlKjfghwPh7afIsw4tE6nCMd9nmWdZdIxWoNiqb7mEdp48onrpojZZRs9NW9H+LGspOOoJSzzZhrpmMjSGd3O109VUnOXbBlBAWZwtvRhQut6aoMQjJqTJYXulpl6gXD9/dLL9zaCDGOU8nidMg2g2t1tHVcVx5kewSV3jd635wOIifoa6FMx9CviCMf63ctL0MmuLBlm5xv7DgManGiFbhp9sxhIg7s9XrLS3fKTqSp1xVDWkfQPcD8SiYtBY/FdcasJoEZuWxn8ed0X1LrA81jakCOdBzkrB25k7nPeGKrSH1+joeotTdH6XqpzNvZoNozWACjw/uuSE8rBI7CTYhNOzXYac0kl2dx6DbXHJWue4RvTjRPjs45OOupSp7bHOXr1qipHD/G+GRwEqZm03iGhPLUajs9s5VkrV/hntGHaO2HE4SGPbu7Fq2Yq4iktDjKbXTYwaqVmFl86hc75LwVOUSmpgE+rS0+OjMrK7qvHOe+Bj+weXPQIybcCTEhD91U8uQQnlauCq9L+L5M4UveDzB73KWwst+uLI/AnF7VhwJn29ButzoZJRftnljxpg337tI4Q214yFVTslSyHS7MKlJjpMDwcIPHB80ooJtTdSnq8/XIWGmyrbuj03YMNrqk3OVcrFc0Q9+4ci8xCIMGYtYdQ8Y3+yk3lQkzhhWPu2us1Ivhbsr3XStKAzQ68tRuhe0Wb+MVgzH72xGF7UmdvLq+k1Voee7YHnML9QK1Y/VOLG8iryk579+JqnBNxurti7+9tzUbiSJaSfDJNSVvgJLT9sQn8KE44MCfUT1JVF2Pan09x05uLBOt3UK6ciqqq8V17DWLbnFqDVeTPHf9zqWUi+zxeiybcQTVEcMctbC5UFvidvX1i5dr2VGUZWuSFChTJKNM7uN0CpC9VbtjfQnGcsMW+aSmhX/cMaGpWwQRXge19/QJ00YV751zYmu6qtM7Tr+Wx8DvsNNVgw90vWaIHPO3cEq65/VW4u/r1t51PFsuL4HIbgdfGSXaw3uYE5RbLiuaA1lE3qnXPtF0xFii3XWgm0S2hu5GW1V9uKnFTtkZjS65jVEGx/5EycsQv8WlfOX28m2zCs7UHglsTzitT6nGGwMCUz10dG+U0VbYIc1dF1nRNIGO7hJy74jJLiu8PYr4qVgTZyPY3kWSJ0OGyw9UoLHF5tCI9xVP3fE+LjW71u+t5k+KhWd4kKjXdpyIYd2KnGl5/GDsjqf2JG0H9cKpxzVb7DekwRkim0XpPsok7nhiSFXLQcofoPU6Xd+sjAsFfe/LltLYu8ROvHi5ga5dfqzxtDJqxqtsVDbcmFeHK3GIdxpP2SgtxomPkRO2UXRNk9phD+BTwuulGp8Zvt2Hwajo7IYbALHa68onivM4Zc1FVZoscuokJexzQSPJWllytoFrOCBdXMKomySrmomx59NS2VdcOYRQleYkXm/V6/WsGbS2dZoJLgcnxr2gLcW0sPhNEGyEQIGLnISUYZzWEAf6UujQ2JmFp2d/I8vT6uJwAi2v4gvMUO6NrmJJzc7oZR8NiSgI6RITT7GQxw1ViEITm/G2YLobml8Y2ayE4hCIVsCYmivXPUNsmtbl0MHB9nojryJ9T/HAQ9flpRJkh93bqKtpbV96zFXN5QrfGZvsIvZg95vSnnJxDqmZyOZBqU9+No4S0R20ZHlhUew8YB7TOvvbJRrWTMrTOncooazhZR9vm2jNnqCcnFB+u2YF83iBriE1apGllOgZC9KyMXTGiwtMiGzBHplWGa+q6SYrleHKhoDiDIrlq3FWGkFMxWO71AveNnPEzIf9borgkmjYi5Yxp73X+WQ9lSW9188jB/P7pVaSkWRYHgxVmoyyvFuKO4uQ4pusY6KaHnSeRopdPMQKhJMkS8eZQZyYtHYTRDWSQGy2d2hjjpeAF+6cYEVsJ20o2xfzXbZP7dhHcyM1Gj51eyZptYzdqJu+Smykc9huTafDXV3xdHfVy3ucbb2bDR2XG7rabyGfG8h732PeHkKkoVl5xwOn9uYhI0w3l1xyxOPSzmNCmjTQkV2trV7AYOMz+DG3XDZxkp3otabz++2l2ENQxbk3ksuUoQlV/kDmhlZIHlbc96FpFL2xjKMxtxj9XpzYKqUTQbpcJ37PizDt59r+alzZ0yXmtdSQle6iVFsVH+xQrxmlsIK+TK+EtIyNlUWYu9O1i1HhmrVOqTXkOqkPh15xxLszTPSkTI61XhnStWdYpmB7YQu6kXodopiIWftQyDDfXGJufrYIi0IwT21zxUXp4nDQmAu0vq9KXmgO0i6TjUGXT/VJ5JI1C1Bcw5Eqtw2URM6crSaX/TEv9jbFD7pzWy9Dad/gpHpdyggtXBIvGwyDUDYmCA8kYdW+NVhjx17ux653JYUQtuI55vPUVcL4TJ5i5aIb5O7uFVy/EXYhCekId8XhqVbZPU8xsbU0curgpXW5DOWRKWn9wp+POz2Qt36YdMPliPX1Nb3IhzUHO/CG9KrLntohAm4op/3uvua2/q3zxHQ9IYpoKb2gswCiFTnd7rWaB1ynBza5CQr8yB7LifRLw4h2YynYd4bVxH1qCiFolEIn2hdGexKu4uqya0u5dHcm4g9yrYoXfum0N/xERsGtvtfCGgCJfl9T9FJgBYbY8Xehwg+qVcVRzV0EEKuUt1xSoK1VrAf0xdnuGBbHt5kpqxB1ZdHAFDhlj3G1sVMz+NxNO3QDSwy3Fa/xNRpZlTuKLsmOuXeOOSaQ1/6K5wPx0Dn3e5uMQm5Mw+F+WbaCnqMZFq/Xwa1AM0Ym7Xy3ZVmxFsekY3e3MHA9ta4R7tiXyd7gS3JDBPjKU5IKhZSEWtkKjOvwPWkSaqz3Pl+1wYE8ndfJAcF8ziaEUeYQ5XRVS7rXOZ/Hy7sbhlEnolgS3tIKNHKWbF2gtj5vnZbijSzIQLPuryDPHzQ+7jdigmduSVtiT99pGwItG6GacQL6/6rdSeQGNqgVaKDqLcYZNjfuUv+erHsTdG2S3hKctKV4R8+HalLqxmQoupHPxKBL0844yeTxHpBHpc8jWWJG+e6Py86vxSxgLV1p6S4l8b3I1attd6CvO/FwtpvJUXxkq17cstYoLeSKdWK57Q6ORExXpcItV0tRVG1EEuKbseKiLSXIMcvkt1sTkYFwUpDd3VmKgxTLe1g1arZhCeHsi+dSvsnGBsEJ0USSy9a8xSSNrihyYyAbZ0evD1CRm9F4knJupbbpzgIkthKF9oAJFxg+pfYGxljSO3JIRZCGobIIhu/KQjeF8wgbmLC28Ny4u+zGQhVBdLk221gpvXOkyr1XO0fbnzanc5NjeyJHnD1aoAqJbulpjEM4Z2DoeKtCo7foHc3y9G0jtyORhoN2wPDKJUttu7mGgeGL1xJg1pXayxYoo5biJFQQcZq5j22xPJtbGs5H3FRsdxWUDicjjXWj6AE5HsPKKkN67NhYRbGQ3h6ROsuJq2wY2KpdUSeZ4BK75vS+1g6+7VElBnGdpAWHZTTyKZtsQC9Ynfvmfobx+mBlKY6e3PP5uITXXbuPDjYDtW2WyKyC5cjak+Kx5QnEGwjZpUriQGdVeQ8ZNEGkGoJs7by5rUtj1LEoQOycOOw3WicxqHmU1s1qVR3cS0dkG5Taww7vFMIxkffO7Qppl3Eve6cj4VO7u8pc5JpA7lhVI8tiI4crMkB2hXUYqwkLLUa7i0ZM6DUUJ14/toERT66VUht4q90RmSNGBdtDA4PLgoVOipiMSYxa0vLAYuJxIzuZCCuXbXn1N6uNe2VNl1rqdOxfpXNVl7fL3gGUtT0e6X1s1fQ5hiIzV2TIhXeIM52nC79RrqBK23QlTQpPD5J10NDLOFjQLvaRRrez2zKgTzamYpV3guviCkM06BJ8uLPFwj9EZUqpNlomy/p2If1wfVbsGnIk2+xyAtang7PFmgRTdJQl8z3taMh09qFKQkR+GJsG1Zo22SvQ2b/wR0y5XtpmNTJShcV9DrdC19trxDMLqsIaf5Oj1yW8X4l+hDVnFtuDRgpSE6Q1RFxnNTxMJGersTEibk9m19KC4ylsRXe7PqDcKHXNeOp42FklytYYzp25vgH7EMEJb61yotgMv7OBlV0aR8owx3cgvtKkDYMcYdq8CqFVqwd/srJbCMM3AocZtxEuXor0ThGsTFhoTk4qqA7u+bjqUMbhGhaElF+EsRqZJeHFiHQgMN24Vcm0CciLFTfIpUXvTRIyq2xjD8wGl82BTtMjS69WDlSfFGfDtCdelmT8OJbY/oRYPX7znI3W3m3XU7ZU241mfjyqE323OmI4FAWcAaqcEh2+UDzppysBbOjPSLCmKNMwi+rGGWYHsBsO7cBDo3gkqUpGzP4s8ktSqrHcXAuohN+0zc3PU0kn7PVtXNZbHdlPmQ06rAwWTPRKOZG4TsQdU9FyzPCrfhOt1+QgndrpFl/zsI1zNKk5wL9Bgp34IisqLK+WfdwZ8oqshoPUoI6VaImDX1FnSS+d+ygzynQcdwdQuRzvSicipCgxPt95JFQxycYmZV3Qy1U57U3xQN+jPq98FHYNf9eQejUxV6ESyWjoEoDx7WYp28xB2WedsLlFRwwVuFuPtUPvgk5MGpK+yA5H3b9R5uqWEORZCdYrxFR7aFmGezbJ27GbAoZ1FFO1p/oKLSdZgvmB0rp9e4dxm3c5AS8q01llgRtX3IG+5ctmKqu6b1rdwDnzkuTbg+ZOIoVXnUAaqIsVhTYQG4z3p8ukm2lsU1XVNGN+6lf2KkjQ9c5VLVxSBWzXEv7Ga1m77wbZLzoS27HQOvUJwU6gVZ65NnbHmXDKu4OA3ZXSLnfd9Vjt2s5BLoMyLTvdYuJ6qxnTlkfQjYSS2GWbb0q2hOptg1iKneQcsxRhKCGzPRNdNMLZ4OFeaeO+OnCg4esqYtyvJwbMsrFlByo4OXZHC8XTFG1MMiMheuWhndkdp41ygDysd9yS6NS4KswjFeSQGjNYhq6CljatFrtTyeGILiuywchdfPVvhtc6ZCmOLlX1p+XlgJPOtjsR+B3VWbtYHW/jQQ5PZmjbTRf4lF343bFeV3zCVl69xPT9VCPUKQy3a6PvJb+vjvChXI/nHFkpq5jYuMZ2b11UT7XLE9q1GjpgrAGqd20nFCZOsTKubi0tYp03/xHP5sQWl1iqDQt+vYzCKoJ3S7m0zWOxBFixS5OtK6i9xx+8ZWa2l3nXQ9538N3i8x4/TERziBAd85H67rXd5XgVMh+pGvmQwnncX/N1SEFjtFU3B8aFdj5Lq0bmMm3TbpS17lLu5oqbTKp1RSNrGhQofSFY8hZxrhp0OR8Jl99j68rLCyymfCO0vJXNXQjFuA4GBVFNV53zQu6cPYbb+b5D4aq6VidVRpt6a12pdsTkyR7GOl/dB0wyBrdgbyOlLk8UnuoUnzYhVEpz0pokqlx44XrWT6NHId3SoQ6REgQcrGNjetHhZmJ4NstufUpImEHwvG4sU1Iloo7yTnoVsO5to6SoTB3JVZScKRtCnfKK7MniiG7yTFnSyaaBOHisszJwMdyVr8cjXMl3V8B6ZaTH+yXer7mpCDnkKnT68RDBPrxSlmx1x5EI95BrIB7Pe8KORpHCSOKGnhrrSE3uUPRRgyF1uApM1JS61UrY6MtqunFuuQ5xzwYsZ1f6WFy2UV5xkV3Hza24oGwAlQdIyKfydoVlNr3g/m15Ot+m6X5cMb1+Z+o8dHfpkDpmXyqTvrs1bewTqEnIfnqiRSlwNZ3WG8lTGMVM1iuZDTkZZ9I1PnpOt+wGV6aRUSmk+EoaF3N13BH21HkVRt9iuKol91pHFF8R25oeb6ub2JCyIvAeVa+JRu+OfWcKGqya0LG/G0cIFjyKIZU9XCLMAVo3HksS/OQG9DLCVjXjYaNpstp5e/YONr43LRg6qbgFbS6c6SxhdrLq5anB7G6QfIDxGbY0nQTLpng6sTdOWaGbS+8k64yjFB/GkWJDiVkB9vB4DjZXuHp1qIDUc5YUVibHbvGQ5EKNpty68Koq3McsW4GiXvUKkqWEss1wAw2EPtWskUiS9qRkLSMgeSWdjU4JiFIaiti+b5fIcoTgfbw1Gy/x0nzIccpbY5J30SMITvKiEJrL+r5z8bV6NJjKIXCztwK/tDZLQdSdba2p/Gl7YIVkXwZLpCOXS1OZ1tOKLbZNutHwLVlitzKe7CrtCnlf4vBtexoQ0EKV/lots6bsg6159aGAYGqo460NTdN/efvw9vsDurd/4x20+fnN/7NHRc8nPl9fLnk8ewSd76fHWp/+HaX++uGtcWOg0vORWJv14evR0t88EPv4rx8ozvPH56tdXx8nPx+bd3Y4v/f8Fhde33bN+KUts8frJWCG07fzi5LtrKcLjt8/QH0u+bzysKEr52FBPF+Li/mlEd+L7c5/nYavJ4Qf3rzX60xfcHL5xW+q2c7XywnAPPwdecfffvs/Jm5jXLEuAAA= -->
