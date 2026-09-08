---
name: "rar-cowork-cookbook-report-define-service-workflows"
description: "Builds a read-only summary report of define service workflows activity from Dynamics 365 F&SCM for a legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_service_workflows", "rar_sha256": "5740e1029c6163b70704e29c057d34bdc5d77a66baab557d1320f81604151634", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_service_workflows`. The original RAPP
agent is preserved byte-for-byte in `report_define_service_workflows_agent.py` and in the RCI capsule.

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

Define service workflows Summary Report — Builds a read-only summary report of define service workflows activity from Dynamics 365 F&SCM for a legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-service-workflows
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
      "description": "Name of the Excel workbook to produce, e.g. report-define-service-workflows-2026-05-24.xlsx.",
      "type": "string"
    },
    "posted_period": {
      "description": "The posted period to cover; defaults to the most recent available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_service_workflows_agent.py` and embedded as the fenced Python below (sha256 5740e1029c6163b7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_service_workflows_agent.py` first:

```bash
python3 report_define_service_workflows_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_service_workflows_agent.py   # or on stdin
python3 report_define_service_workflows_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define service workflows Summary Report — Builds a read-only summary report of define service workflows activity from Dynamics 365 F&SCM for a legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-service-workflows
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_service_workflows',
    "version": '3.0.3',
    "display_name": 'Define service workflows Summary Report',
    "description": 'Builds a read-only summary report of define service workflows activity from Dynamics 365 F&SCM for a legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-define-service-workflows',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-service-workflows',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dbb4a4cc4cd76f4f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/define-service-workflows'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/report-define-service-workflows', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-define-service-workflows-2026-05-24.xlsx.', 'posted_period': 'The posted period to cover; defaults to the most recent available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where define service workflows stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of define service workflows for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-define-service-workflows-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define service workflows records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of define service workflows activity from Dynamics 365 F&SCM for a legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a define service workflows summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'The posted period to cover; defaults to the most recent available in the tenant.', 'name': 'posted_period'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-define-service-workflows-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write D365 ERP summary of define service workflows activity with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDefineServiceWorkflows(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineServiceWorkflows'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-define-service-workflows-2026-05-24.xlsx.', 'type': 'string'}, 'posted_period': {'description': 'The posted period to cover; defaults to the most recent available in the tenant.', 'type': 'string'}},
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
    print(ReportDefineServiceWorkflows().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOjRrbmX9G8N2JsX1W9gMQiquNGDGJHCBBCLHJ1lNn3RWwS8vV/n0RSle3u6tvdEfNpZFdJkJknz/o8Jwt+fXOHPqnbt09vx9CtFrxbFGkStgu3ChZ0fa3bHHzVuQf+LPy66tvUG/q67d4+vAVh57dp06d1BZZvh7QIuoW7aEM3+FhXxbTohrJ02wncaeq2X9TRIgijtAoXXdiOqR8uZvFRUV/BMr9Px7SfFlFblwtmqtwy9bvFGscW3P8+0vtFVAOdFkUYu8UirPp56qxiU3d9CL7CNq2DD4umrYPBT6sYDC7Ymx8Wjz0e2l/TPlkcnyp9WDBh76bFh4cQo24QeNElYdh378Cw8OaWTRF2b59+/uuHtxT8fvv065tfuB249aY/rGEelhyfhlhf7QCLC7eKwaxmAm6twDVQDeheglvA+MXr6scuLKIPi//8z/zqtnH306fP1eL1+fw2/6cP1aJPwkVfuw8DfbdxvbQAZr8vqOLqTh3waj+01ezxDkSlit+fK3+XVDeL/5rHfnxu8h6H/Y+f32qggjvH7PPbTwvg1M9v7TD/fp+lND/+9A7sCNsff/pdTjd4Wej3szCg9fuX1/VLLJj4+9Q0Wnw5aiz92qsN/bQJgfA/2Dd/nqq/xL1c8uU5+ce6+bD4vuTZnv8C+j7zzgNyvy8W+ACsfHvP6rT68bVHW49h5VZ++ONP/0isn4R+XqRd/y/J/fkpOAHJDrz1cslPHx7h++ti+bLtm8x/vG0DEubfsQRM/7rdN0f9I9mPyP6N6AKkbfctlt8V970Fy/9a/PwPbfufFnxYRJ/fmLBIR5B3XhF+Wvz6SJGffwh+v/nDX38Dov+pmGM9tP5DwpfSrdIo7PovX37+oXvc/uGvP/8wNCCLQ7f8MrTF92R+z6+Pff7kwdesH/+8Fux/qvKqvlaLbzW0+LVu/lf72/vCdIs0+P1+92nxx0qcP8vFbMTXTZ8u+EM1dkDXP/jxp7ffAPJUwJrBfwwD/PiP/1jsU7+tuzrqF0e/HvoFCHCfluGsvJGk3QL8P6NGGwK/dilw7GseyP85wrPGAIV/+T/+A9k/+i9kh54I/eUJz19e8PzlGzz/8r4wgNi6TeO0AgCsU5r2uXJjAMTzlk0bzksATHlTH34E1fxx/rFIq8Uv/0Tyl4eQ92b65YHE6RP1dFqcEa8bivB9ts1KwupliQ+APbyF/gDkF7UPlIlSANUfgM1dXYwAMWc/dHlaFIsgBZgCyOpJFcBXn2Zhv/zyi+d2yefqCdHrxZPFOghM+KbO4uNHYFVUpHHSf65CP6kXP/z62w+L/178T6sewuc9NEAVr0gADaWjqixAZQ0lmAaCBMIKYOMRiV9/e/kWiKkA7YK4pVEaPheDzMzD4KujjwL1cYXhCy8EDgbOLWfHzlSX9u8LMVp80/fFtzMzJIAeAek2YRWElT8BqS4w55snq7pfdCD9uggw4tCFj11/8Vr3oWIJStztf1nsaQ3wUF2Av2Y1H5PA4rpKgfu/pcHzPhDS/tAttl9FvC+UORcXjdu6TdK6rz0i9xmXmdRfy4Fwd1GF18/VTLjh7KpHYTzdAyYBz/ivkH6cYw7aEcDlVdB93fsxx53Z0niwZvu56l5J77ZzKHxAAmDTeEiDmQr+8kqpLqmHInj4D2g6S3pFIXhF5ZGDzD9qXV4txeLZFyw+DysYQRf/v7RDs+kUz+ssTxkss2AVQ3eeIZm7wTl0zwbyoWzdPsvv927lKyJ9BebPVZGC/GqnvzxnPgL5mvMEu6EFBuiU/pAPsgiEZJb7SPI5adt2Lg/3c/WVAYDSiwfcgTgDRAAVMyfq1w3n0a+aJqDs5+vfu4FHUrTBbDZI5EUzeAVIsigMA8/1c6DVHL2vIQUZH85Ruyapn/zJqjkEILBA/gIokYLSAyzx/g2Vn6NfVf/TwmfTMy95NIQDqNP2IQDoEc4KzgGZQwXU65/NN7Dz00MIMKNs+tl2D1QKsPR5M2zDy5B2aT+j4tOvYQMA+eP8/bR0vhveGlAcwFmgBJoBePdRNHOulKClATqA7AQ1VKYVoHjglJcTHgLdckYAgLCvHvQp8XH7ZVD4qLSZm74unA2Z18x0/0xrt5r+CBTG99IEyCvnGY99/zbTvu02y57BsgOAB3b8OvrsC96f1P7sHRZf5X76u9PNj//eAehB1qc/J8CnRdL3TfcJgp4E+5Vf3wFUQU9duxfXfnzW/sdX7X/8Vvt/Evu0+NPi31PtTyJepfFpgbzD7/A8JL9S6/UBnqA/bp2P6Dz6udLD33EUbF+XILfmuE2A3L+R3tcpgPniFoAQmPwkwW7mziug6wfqgyB8rv6Y63OtAVKp4jk3u/oPGPBgf5D3z5h9IycwVPVg72DuFONwPp09KqML3z5VQ1F8eAPQGP7zU9nMP+Wcz918lAOVAyCyT8PHlQe0ywNQsV8CkK9V92y3fv2b8y3zbeyRX98WdbO5gF7cpgGaPTtcwLhu288U9gFY0odxPWMs6FAasPzRloGFgFeAYv3UzOo/j3Bz0/cAq1v/9wqojx9u8f4C6+6PFfDisJnD/1CoT48DT/vA3g+LAKjSzZwLPD67Yi5yt8sfBn1Xlwe/fHnyy3c8MtPRnyhobhBe5FZ9WITv8fvidNxz35X9rfP9e8EWaDtmWUH9aWbgDy+kA9/gtAI8+vXgASx6HQUfp/ZqAKfsn+dDzxzwx5L5B1gDvr4t+vYPF1749tfv6fWAwy9zUj5T62+1U2aYAzQwO/hvOBXo/KTc8GX9P6n1jyt4hX+EsY8r9P1WdLfvOurJ6V+enP736syw+Sfan7V4dDp/mfsLdyhAVfX1Q91ybgdBUjxoewQ59ADjV/vUz5TYf0cFoMODUgAxz/79PXC/u69+HCAf2hZu//z3jl/fQMG5IOfcV8m9TiBgOkDgj93ce0EAlMCG4PoJH2Ds3z2bvJZ3iQuaY7AeI1A4ROAV6eMIvvYImIDREFzBGBGsUS/wsYAgXBz3XNfDwD1kvYKjDYLDKIKBBSiQ98SgL3N/mc4qzXsBT3wEMBb+PgxuBS9bnrrPjvp2FJptfpkEEAZHwUwB7UTq+aEhEvEglPCU1luuYWh7uVoDYSKe0e9g+h6vORgp85ShpBiecN3j2p0gsuXqLsLDZbdfg25sujIEpw3sclrf8/x8Kq3z5DVeSA7xlV5JkXzdaHf0HpOTtt941f5iHi/2oWuTU67rtmXzt2MrtrKPXwjD6YJhR95lNeU0aLO8Q+wGrotOd5Mdf3AMYg+vDkWv38zSlJ3jxuBpB0g7IvZw27ViP0hwgZ49zqpuiBFEKRZBke1N+mWaqPZgDAfUEAP1mNTnRtakfXETo67YnrUth+W+aTaKiNh1bVfT7rzZtrIsdwcTb31171RocbTqU10aqs4UGbkRNZ2fCpmIN/zdxKFwXGcIsVflEySkhBOtNahNr7C727G9LNN3+tLf8q233xXdRYFTcbdZ0w1bXXh7OvEmkQ+iE/UiJ8jU0JH7g2LvGm6gqfPpZOYmqhFkBwV7rdY7OnXbY7HcyDmP7qQjG1Cet+dO7eXUXWUaK2rTstL0KMsZTdzVtsB368y/aRcmWvFHMM5fnEMw8VkrJs103W9azJXSTt9NVXzWkyhOdUO45Nc7TmWAdC+1q2gug+YhHZs9dTifUmfZcrRMHOTuTtzuWmsVjhVaR6lLckXnTL4b6Abdc0d30vk82cYE1dGE1R3L2/WeGRR0d0Y30OSOM5y6ymsaKu6Nd7g0Z8wJ/WYz9DcFP6vrIwUVDXLjz/T2bIaOmWh1Qq9NiWxZxVmKAldUO+fSHxPf1wkMlxKzrzX2evQpNGjs5qARppdb21ra0AeMrVgNhbWCpK6rNe0QnXGn0po7IH12KFYttYMBYVPFsD6bLXzMWcwMXVmQOqkhLoR6SWk9lzeHc3SzVLyY/DNvIMt9uscdSJW0e8JFicFf03AnuEKulFdUVugMFu5LwuOxlWQUbRneV45uoPdOY6Bdn2nMRULPGrZxJYwEfyDL6PHcrRyCwyDBklSadHZYqMbQZgvFd3PZ7YICyveyRGqlBm8CVLXjEbntltxZbBy16GhknwbhmmUzyuSO9Uj6V4X2ZWSImYPD0EtnhNz7Orhu2ztfp8bmEKjXybVS45wOky4hyLiFVzF6HkzWJGhF6RCpHtlGlrdwm3M9k+h4HCQUe+9C5sBcTeSqgaIMM8a6s+V1GGlN2UzDfd/xyuj0KCNNdsi0G8Rtcnw0k2DLOnYcmNxJ7VNXDbydvpPaiRFa8n631HxD2+G2XkPakdtqBezWxWiMkuGihF61zRkhq3GFLy0LRZqE1Aq9sff8MagFle3cDXo67AvM4kX5oF4FnjXWTXmS6CVnegdnSE9WeT74sAzOjqR5rKnSudpE4EFARC9rspfSE708bD3M5zkszbbLSj8Rq8LMjG59vyOmyB7RugiPwRXi1ybIWi+mGD/lEFFR5FU/pX1t+tQAGTTHb6tqjAAga8WFs/KIHe9XgozXib2d+iiSj7osxqa9Gze0tKSzm4lRIaper8NmQ1XEjrmrbD/QXBwK+nDoyZymOPdsDFwAU4F86HEekzi1QLeO7RY2jsTjOfb5zebUZNTdFFGtFOpmZ0BGd9cK+saahrxHQwHFJiM4TdV5pZsSY1y59DYYlTzRtn5srSoUDkygQtEghRsJItYnHsoYVUH9m1xulUa6nRTiXpUp8EFrHDaTanDntWYfM8rnJpq5kR6+a49YEPOTX6FjqVH1IOYBzia+MO4pXI8MaqlwO6M7VKjl33gy9JAtucl9w1vnR2GSUtWqPed83x29nqPTuilUCR4aH1sxZwsBEzPs0DmrICF1k3GFmI2NYYkaliC6ErnrKOZorTS4rFfJKWkBvNhXrVS3LIWcNB5vQgcyLxOwNJZLRPeq89Hv2HPX5dYGrTOsIrHIllIiqOTbbeecISqfltkxM3YbTrXOfceAYi55MShUQcug8wbuVLwEKNpLNM+kTSTflkK2E2r/ZkPL82ii53C9A9l7sVX3XMGXFSDb85kFhbPCQnAutJJdcOlNSS8OlIChUVzCW6W3YR7l62Gd7rBb0/emtdszdXbfgsNbdWlqi1qfTlcGKUTG1Sl2R7O8fjhzDJ0y6rRpOryUqTrjD1S30n1v76xO0xHzrMxpNyeqcu/1Fd84e+sYHE6DFd+ru5PkNuYSFTd1rKdfog3E+Lk6hmOKsXeM0nMlXeZiQYfrS5gk22NQrKY9xzM0f5KspRUTgx7ftGoZWQe4zvbp1pkYYrsTpKS7GtvNAOmjNIgWW7foMiuxdOPQpujxAr1T25j3O/cKZxNBm2HZkTHpyxPF7DDB8wQzYkyXn7YrPUdT+9IzhSLuGt6EoOEkFYfKFrei5aeoLdMdzXrMoVAUafIuYgoVZH9Nds1pmVPn3Vokck60Jz7ZRDHCFgC9Uz0pTo53vC75KuUO2LHZ6lVvma2wu+3vhZYpNy4WdhS9KuP2YBLkqTze0gyVMOfKSSm927MhstnKK9M5tS4qbbdlEHTkCRft2N6QgSsmfi/wyVC4dnPzRpOFFW4wKzrH7XglF5rtM5TDsNL6bnPqVFpHKD/nYh/aMMnkZJiDViSR+cTJrtuuAANkifndXtWGdMcxyp62slRbseEBYTr+qm/pGMlDXgPAs8/tTdrHiQFSIoPMDNdhZcPX3BQzgCqIi8SrgAMKjQ+5SVwxfiWVUgSi1S0jJ03XkXG55bLKMAxNgFS8Xw0lzVhRDUD3MLbLe3PNDijT5M12ZyQEuZTzNaMxo38ydkp+87oLTSYX8XJShn1A14bueWjil+mBDo43OpdjG8Zd9VDs78diPKVoeqVdzOjgmwHCQxvkNdpvA9O5EluKGrJ4is+gi0iq5OCg67tFk+00LqkYcHVtXNpSvS+55MiJybkQKFQswhLNkLxQ000ok+qKPVBIVzWAKSDBLxmYNumcgEcF9wnHPskHOmcOh+Kai/Vdh5q9dxAysmrLSoqYKFBWoBCq8qz3R5PpJ259bnfq6hTgSwS+GNfxsEnyJXoWW93NiekQYbxvERBA1bYil+EGFfFKa6ZEObLJLg4alpXYpNWPLqXQGAlsCo7J/nxNZeCcdEookJQyNWFU4NjFMF1JDeeWy1bI3Xh3GC2Q1myfeYKW81dJdaprZ/N0cKMxLB0udMmmnhRjJaIeTv3mNplTqaUrrDeUWwwd+8MFoUUpXJ/9KTkQxysVH0sxdU5xvF2nW1HdLcukcGsZSyK7blonGYuQ7XNwWKF5gxmOIGkLUoqWS5no7v6YnXWAjFyTRrRAy9dCFWWDNdSATy4nQ8x7+QwT1NjCsKMIa/gaRQxCkkoGFWqijbtjszooRkeqtECFXmJMPYvz0w5DD7XoiSNzIPctPh5vot6v8lE8EcOt41Yqb5VDK8O7M0UYU1SUiByWHN+WvA/63fE23enGoujREcWrpVd8rgU8dqKv5ikhrfBqOU5vj5wxTaOuTadJJbPTYUmqzpDvHTYtMndr3AbGkli5oIea33F6bgTYmio3eBP7oInb36yMQjulCLZb9lxA6DLELRGEYdtu+TPk6Trbiux4U3yCFazb7eqcop5s6bhnL63pOgiOYu25XyGCuJvclaZvl8YIvOFhTWWtZK3ctU6ut/FIrdjbvWA9XKT3cj7dNpFmZ+h5lfWBXhfm6a6P+YGjImwF31q2rGPk0DGRcztMChUcl8KFOsURqmQu2W2ZoVTtFD0oOwG9CY689FlopG+XO7Pu2+t+DboLhRwqJlN2e7XId6SlrnA0x1K0AevKfH0ZkKmUh6NbJ/CNcarMO5wp2hpWdhoeVZjPrxxicUHaSm05Vd4yC3ZV4Uj6NsoOEGiRNrBriPUp3W6PJlVaIVmgV0Xh16OLlYYgnLwolyRnCRQXCWnfuDfa94Dzt5h9kKpJXvGBIWwz67KyotDfjA6VWq7fWUHihAzv6x3iH+xVvBLdcc8glcMZsS9VIu6i1jY4F74C9QovrDkJGkgXgz2Dsbi6ZRrHDyXKvMJTZZlEgwcRs8xOZ5RkTkhlM6GWEm4SG0odeZrEbg9nGOarZjiFOuryoDjGpJCFrZMXTKyhlB75ae0hLQXv8pVpbwVYWtqsHHe1ZFo+b/ti1ENCe/JAX2EkMmFG+Jq928KhvDOrfSS1Z3hQawtPg1xBKTM9HV1oPJ0H34hXByuQCfbeVphyxo77vEQZcj9EmNotCzMO0g2D31V5gIroeM5XG+bEYaZvqjnLnVhpuLJ6G3hiVq6Od7jyRiE/XuOMQbWYuAl9INsk7VPrmEFcrSmJuqIgbydv84L1A52HFRjdX/W1XGIqsb+oudDgNsg9LhmueIiteBx3uD0+4FvNry1QS6qRQDtso8nr8czX2Fr3+NPeWyqtymQWKidDb0D+1QqUUJGWa6OEvC0+VG0QyW19t+DQrpxSCUgEsznmeD7IgZqGlzUCTjc+dtuT7kW55yDcZS+zzd0QXFjW1gq8xxH9dI2SALnZRB76GteahEiuheNuhWyc1bq2LnK3jwIdqhnnRO+9c0VhsTT2mVDoSr4jWo3fjv1AgoDx8KrCmju+027O/ggZvnbIED9wR3Q9HSBck27wUklJ0EBhlVZbLRLYK2I/KlV2cuykJoQozmJGs1YdH5PdGRoiCIoJqB4UQwBVr2l3bSlBFLntOVkm8XpoOy5rty1loMVdFNwiw5TydpE3GyOrmvRelii/rKFJHeHlfkVFm2btOB4fisukJik/v9WoUGQVdDxnG7d3raY4d6hm8vcB1Nc63hCMeTFcnxoFouundUmr9YTezj0oQqGC8pWXrsbjVV1ymH/a89SFNjcRia9t066akY1B40KhUOwagZKkEyo0e9hObJGV8N0GtiKSR6q1d0BG39rsJtQlx2NzEUx4x4CeB7dMSLARh/ASccokZYttQWPIbQYmUUgc3d27+5iyZdyVK6S6sIXJ2FlpcFVRtauywfxjctoD7L0qoqfI50xvvbWDeBiLebdpv9Xu6oT1ty3EDn5roElLiKl5E5LiSF95HXeh+q55A13ntHbcO3Z7uQFqK9TeHbrGB03PhaYn3xHxbmdvdwwfG8yt8245ARqbi36ThV6gpMog8GnTY3pRFpIWIR4ZMtsaDpcE1o2JgsmJfrQNBJn6e7RVPdk+4OAstcXuexlirrjU7robBOOcL6pIWa+9zRD5Xd3uN2PSt1l1dYess+k1G1hGITC6fxeJNVeX5Yn0VkW8mdYpvw0JwzjaaeAKUtvW9MrASXfjGMoo+YezbTv8SungkIkGeje0V22s+vNK2i3JPCKHs7EUyt73Vg0Qdx/6Pb+EtXxZS1mkFkrXE3B4165Kfzxvk0ulxZMgrdaMjCxXllYyNV1jF564axqflewWE6GlgRU7/W7pGzu5JvjeT4cG4bte6+t62iF3RigZd7nuo5WWbXvNC1brnGztvMLJM0ZUbo8rqRDaKNr7A6ZjIWhP1ZHBcXSD5VTgGehBpMZBao3VMfRzz0bsHoLZKopCz7Ong43sw2LQpBMcNX5YQJFPFfuGHq8FJKLXbeBSDVauCnzjcbhOtGF92IcN3NqC04ZZ14ehH5I7NAtwTFujcLaW1+cMhSaADTfq1BSYgGx3RWipJG8zvqiX1lJxtSEy1F1ELDdXqnUQThMwrjukrTGK24n2BWHgjxd2cwJ9lYPiESLQJz5UEYrNfFz1cG9XO6QAZ9k9PWrpXWacwbFvuic3ypkLPYaH1g6XO6Z8ri4xbixdlUxbhIo8WvBiCi7uRoXWGHVkYW5SURfiKK+Pg4zZqDpvmeNgMugmXEcn/z7qSm9hks8lB7/1rH5tRfi5L0KqEJBWl2NIyLjjKGMgFVzLn7Cx9fTewQlrafaXIhAnS+3CIisnGYWUlrFq15AzP4Doac+TWq+VmmbtZcI9DgGe9OnVRDY2BnWxk5gcI+WRsYa9YQVjm3RSJA8nHVnNRxamAyvBjXgM/DgPpMgyLkzKrwJTkYuNdN90+AG+x3tv2ml2UOHmEOYj0mskzux3EYxwhL3GoMSUr0ssmDbKdX+GjHOJmb2j53qRZicDFwWZktDrnh98O1iSEBYhlH4bYXMtwQTEuuYe86SJElYrdECMcjOsV1gRBXubTE7bejPig4XrKA1YrlDxJZ6slACW74h0YaFdULscD7v8ZSeoCemZ2DhlK0f3VJpMN1fV8PpVVvThkl7voWtIimwxONv4Yqh6H4BmQwE8MNwxIjY7/4Zv0W1M3idW5MROQW+soWuItbGp7YQrdnI7yudGWUL7MhBrDNmXWl5dNowV8hsc93pfxvfhMStduQ4xPdri9boFrTc+1N4ULjc5sQ4wb2Va0V0fxGBZ9kHtZXIBkZcW8U4rb3NDNQfJFJTLlnIZHRjDSDDEJUZYvNjphcfcdNl1EL6hh7Fvy12CQrfbEukwpOytjouSZSdHTkveelsaiIGpyiIUoabk+s2d91JtfcuuQVMy60oWhvGo7JFh118bchVBgaTId0xFeUXVUZG6cCOmsKhhUCa74Q72wcaPdiA0V28lD6kX9oFEG8ldGI9llLlMn8hHPY2JQcCOmiQJCq7cZKJIwoClx/EueHqbkBAOUvGMduQ2i8BZdAjEnnB1VNu1wUEt2owMscLnRnGkIFq28OK09W/EIamni5CgLT0MJrSBoohqrjxGwcFtmSoNLnarSyDGHdtm2hUN1nZ7c8Irke4SO7QufmDcUW4lTyUGwYeYot4+vP3+dO7tX33BbH5w8//sGdHzUc/Xt0geTx1DN/j02OvTv6zRXz+8tX4K9Hk+BeuKIX49UPqbZ2Af/8lzxHnx9Hxj6+vT4+fD8d6N57eY39IqGLq+nb50dfF4gwSs8IZufvOxm1+O9cH3Hx+aPvebxb607+svr9c13+b3EucXQ8IgdfvwdRm/Hgl+eAteLyt9WePYl7BtZitf7yAA49bv8Pv67bf/C0aU/TJ3LgAA -->
