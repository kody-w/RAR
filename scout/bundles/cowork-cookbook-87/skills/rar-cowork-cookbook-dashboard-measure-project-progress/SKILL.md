---
name: "rar-cowork-cookbook-dashboard-measure-project-progress"
description: "Pulls measure project progress data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard file to the Cowork output folder; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_measure_project_progress", "rar_sha256": "66344a6241de9af15648ff6edf274602e88529376c9791aed3a90749a40ff427", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_measure_project_progress`. The original RAPP
agent is preserved byte-for-byte in `dashboard_measure_project_progress_agent.py` and in the RCI capsule.

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

Measure project progress Interactive HTML Dashboard — Pulls measure project progress data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard file to the Cowork output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-measure-project-progress
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
    "fiscal_period": {
      "description": "Fiscal period to report on; defaults to the most recent available.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-measure-project-progress-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the file, typically Documents/Cowork/output/ in OneDrive.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_measure_project_progress_agent.py` and embedded as the fenced Python below (sha256 66344a6241de9af1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_measure_project_progress_agent.py` first:

```bash
python3 dashboard_measure_project_progress_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_measure_project_progress_agent.py   # or on stdin
python3 dashboard_measure_project_progress_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure project progress Interactive HTML Dashboard — Pulls measure project progress data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard file to the Cowork output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-measure-project-progress
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_measure_project_progress',
    "version": '3.0.3',
    "display_name": 'Measure project progress Interactive HTML Dashboard',
    "description": 'Pulls measure project progress data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard file to the Cowork output folder; read-only.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-measure-project-progress',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-measure-project-progress',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cb84a36069dbf41c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/analyze-project-performance/measure-project-progress'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/dashboard-measure-project-progress', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-measure-project-progress-2026-05-24.html.', 'output_folder': 'Destination folder for the file, typically Documents/Cowork/output/ in OneDrive.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of measure project progress with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull measure project progress data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-measure-project-progress-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing measure project progress.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls measure project progress data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard file to the Cowork output folder; read-only.', 'example_request': 'Build me an interactive HTML dashboard of measure project progress in USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-measure-project-progress-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the file, typically Documents/Cowork/output/ in OneDrive.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of measure project progress from D365 that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardMeasureProjectProgress(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMeasureProjectProgress'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-measure-project-progress-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the file, typically Documents/Cowork/output/ in OneDrive.', 'type': 'string'}},
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
    print(DashboardMeasureProjectProgress().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adPaSLbmX2HeGzFVdbGtBS3gjo4YoV1CCwItqNzh0i6B9g1ETf33SQGvq6rbffv2xHwabAdIyjxbnvM8J5369c0b+rRq3z6/HSKvXPBenmdp1C68MlzQ1bVqL+Cruvjg3yKoyr7N/KGv2u7tw1sYdUGb1X1WlWC6PuR5tygirxvaaFG31TkK+vk7aaOuW4Re7y3itioWzFR6RRZ0ixWBL7j/eaCVxY95lHj5Iir7rJ8W5kHhflrEVbvo02hRVF2/aKMAPFzEWReAcXXUZlX4MLHzxqhbeIuuB1deXpXRIiv7qPWCPhujhXBUdkB1l/qV14Zgfh4t+uoh9+VcNfT1ACRXeRi1fwGKvPBjVebTJ+BgdPOKOo+6t88//+3DWwZ+v33+9S3IvQ7cemPexSpPn/Wny/rLYzA/98oEDKwnEOESXAO7gVcFuBVG8eJ19WMX5fGHxX/+5+XqtUn30+cv5eL1+fI2/zGG8mFwX3ldH4WLwKs9P8tBpD4tqPzqTR2wuh/a8hmHNiuTT8+Zv0uq6sVf52c/PpV8SqL+xy9vFTDBm5fvy9tPCxDuL2/tMP/+NEupf/zpU15do/bHn36X0w3+Y1mBMGD1p6+v65dYMPD3oVm8+HrQWfqlC6xgVkdA+B/8mz9P01/iXiH5+hz8Y1V/WHxf8uzPX4G9zxT0gdzviwUxADPfPp2rrPzxpaOtxqj0yiD68ad/JjZIo+CSZ13/35L781NwClIHROsVkp8+PJbvb4vly7dvMv+52hokzL/jCRj+ru5boP6Z7MfK/p3oPCtB8byv5XfFfW/C8q+Ln/+pb//VhA+L+MsbE+WgMlvPz6PPi18fKfLzD+HvN3/4229A9L8Uc6iGNnhI+Fp4ZRZHXf/1688/dI/bP/zt5x+GGmRx5BVfhzb/nszvxfWh508RfI368c9zgX6zvJTVtVx8q6HFr1X9P9rfPi0sL8/C3+93nxd/rMT5s1zMTrwrfYbgD9XYAVv/EMef3n4D4FMCb4bg8Rjgx3/8x0LJgrbqqrhfHAIAYguwwH1WRLPxxzTrFuDvjBptBOLaZSCwr3EvZJ4truLFL/8reODgx+AF8tA3tPz6wvKvrxlf37H8l0+LI5BctVmSlQCODUrXv5ReMiM00FqDMVE7AqTypz76CAr64/wD4PLil38t/OtDzqd6+uWB79kT+wxanHGvG/Lo0+yhnUbly58AsFZ0i4IBqMirmR5mlO8+AM+7Kgcc0M/R6C5Zni/CDCALYK/pIRtE7PMs7JdffvGBXV/KJ1CvFk9a6yAw4Js5i48fgWNxniVp/6WMgrRa/PDrbz8s/vfiv5r1ED7r0AFnvNYDWCgdNHUB6msowDCwVGBxAXg81uPX317hBWJKwMNg9bI4i56TQX5eovA91geB+ojixMKPQIxBfIu6anuA/ous/7QQ48U3e4HS+dHMD+nMpmFUR2UYlcEEpHrAnW+RLKseUGqfdfH0YTF00UPrL37rPUwsQKF7/S8LhdYBG1X5TKXti53A5KrMQPi/ZcLzPhDS/tAttu8iPi3UOSMXtdd6ddp6Lx2x91wXwELv04Fwb1FG1y/lzLzRHKpHeTzDAwaByASvJf34YPagKgAWhN277scYb+bM44M72y9l90p9r52XIgBUAJQmQxbOhPCXV0p1aTXk4SN+0bMJea1C+FqVRw4q/6zVEf++AfnWKSy+DCiMYIv/33qlORwUzxssTx1ZZsGqR+P0XKa5ZZyteXaZs8VPW0FJ/t7HvGPVO2R/KfMM5Fw7/eU58mHKa8wTBkHYQoA7xkM+yCywTLPcR+LPidy2c8l4X8p3bvgA/H4AIVh7gBKgimbf3hXOT98tTUEE5uvf+4RHorSPGILkXtSDn4PEi6Mo9L3gAqyaA/G+tOUcVlDI1zQL0j95NS8ZSDYgfwGMyEA5Av749A2vn0/fTf/TxGc7NE95tIoDqN32IQDYEc0Gzqt7zXoAYV7/7NCBn58fQoAbRd3PvvugeoCnz5tRGzVD1mX9jJTPuEY1wOmP8/fT0/ludKtBZoJgPZf+07OQZowpQLMDbABYAjKoyEpA/iAoryA8BHrFjAoAdV/d6VPi4/bLoehRfTNrvU+cHZnnzI3AswK8cvojeBy/lyZAXjGPeOj9+0z7pm2WPQNoB0AQaHx/+uwYPj1J/9lVLN7lfv6HLdCP/94u6UHj5p8T4PMi7fu6+wxBT+p9Z95PAL6gp63d7yz88YUSH18o8fEdJf4k+en058W/Z92fRLyq4/MC+QR/gudHu1d2vT4gGPTH7ekjNj/9UhrR7/AK1FcFSK956SZA+9+48H0IIERgdDIPfnJjN1PqFbD4gwzAOnwp/5juc7kBrimTOT276g8w8GgKQOo/l+0bZ4FHZQ90h3MbmUTz7u1RHF309rkEaPvhDQBp9N/atc3MVMxZ3c27PRBuAKF9Fj2uHiBx6+eff979ao8fXv5pwUQAkPLuj5n34pOZT/9QIE83gXsB0PBhBn1Q9yApgZuz8rm4vA5kK0jU2Z1+qmf7nxu8uSV8AvzXJ8D/o0Xcn/B/ZupHEwCw5y+gaGNvyEEUX/j+R97wRmD+XH/fVfogn69P8vlHncxMU3/iJ6CgGUCVf1hEn5JPD7r6rtxvze8/CrVBzzHLCavPM/1+eEEa+AYblg+Lb3sPEMLXbvCxdy8HsNH+ed73zGv6mDL/AHPA17dJ3/4bw4/e/vY9ux6493VOvWcC/b116oxnAO/nMD4Y9J03rwCDopfb/7qaP6IwSnyE8Y8o9inti/z7QXoZ8+Df70Q/mqH5uRl5jvkGcrNRAOen+lWiTBU8e0/oiQ/QUzQ0d05aGTEtKKPvmABsePAGYN85tr8v2u+hqx77x9laEOr++d8dv76BevLmruZVUa8NCBgOYPZjNzddEIAdoBBcPwECPPu/2Jq8JHSpBxpjIIIgVhjmESiGhNHGixGcwNZxTERhjJIYAaPReo2jmxVJBBtyg3hRuPI2MIltPAyOYwwlgbwn0Hyde8tstmo2CQTjI8Cq6PfH4Fb4cudp/hyrbzuh2e2XV7+++QQGRgpYJ1LPDw1tEB/CSP/WOksHXt/yqz3UnJcJTCf5g0OIozeQRiOWJ8c5GFy3dXL2nBmFvCcZ0Yn6HYjKHtpLy+m40tCI59jcaEjriJOnG5JnUsnkd3y8r+917t4hlWhxEzY8ly2GIrYk5kgidnHe8uMlv+VKl53lyVlCGon0S8ksRouepqsJQXdSXxsuG4S8T5EqU5jD7bg78iueOEb7gq5u2Ea3HKyzoBJfrrlKPbX2vrMkSVha7jqGSOJmUV14AJtBQ/R9RzaaPTXejuJEgaSUqx6W+f2BzrQx33KHYnuPXfl6lDwRLVGBw++ynAcJAt9XBnJvSG7XivBVNkNjakiGtS8Dd5IgwSYhOxrLO74Zy129XEYl1pb+hthAIeuQd2qEZUp3ioPRriwe4mpNnBS6CGqOU5V7LKtc1h8v4q6sbyGbXTYl2hkrMd4lKc9RrGbv7awN9dVdwvmD2ZxIySCr3tH2aWmbR5LkkQubodZkxqc17shHeX9kozFhW+3WrkQ8ysdpCPyBOHZw4JmHYn+Qa/lyz/O1fsd6TqCsrLEO2EVh84gW3Y6tjmwTRtnQI5x89ZcTZ7nWkO2CLZVruhPuZWP09BB1gvyOIbXN5DJnIvu1I16yxKDxZZ7sDa6tVb2VOWjlSngJezuxC9gavjJQcT+Ux8PmIhT8btMIMqJsOFeWgsLljzXcCtkSPcWjYhOeQFwU0RMPh9Yv0sMBV4UJNA4ue15nHLP1zq7BDtztuuvLUyky56DDtkO8N22JQCxtxe1tvk9ERXZxFlJVbDjRPBre8i51dKVJTIZHO9q3e6rdo6pIO77aW70hG+dGv8BVhtyKNrcJbbfj6P1oMCXE8aYlR/nZ3VSxX1LxncWsu2js1lzci36S2RJJSxeVRvDSTTJvdQ8QPXVaHWgPGVGK+F2Cj8V2dbl2FeoetPB+Sk/ajb7GZyW9m3TYqce1I6wtr8S2t1RuyasAJfpac30XXg3C1bgpJYliULobtWljHTpug0sXxko9H92q9Y7vbX7iaF+s7gF6ERjZkSGarDoBo7fsSd+saAGivAzfraOV40vNWkbOkns5sp7jqCiakO4QmvaRNqSQxhQnM/E8wYx2J1q9lqTUGBfrzU7FV/rNUO+wt9UiOjxdWXTdjOxUEO7ZLWxGWHXZ0kAMK1JH6FbUhSPXRY0RuLmOg8ZWo6bRxwOTbtnaEkByn9fl5VQcDza6KvAbHV8ysTG7s4RO0N3uLh5+tEezVzRdWfZTnOHOtlXGZc4euDN9JcN7VchqGk9HIluLiWGkDJ3cTjEhjdikbugymPB11BH5/YjxDiuusjt/s3hFu0/La4uSXSYce/c+Cc3QtXsoQK4cv4MOqOujltsfgxi5i4eSvMequA4xg2NcLsninKJIG9ZugWRF8GjlOefl9O6S0C51I8gSYdQz7h62CoeM7FqFjBXW3GR3h2MkuQt08Z4EUE4SVKvlhOkOaq/rDqPfltM6YC3Bp1SvZNLGPpa+sc86ZUsyJCbtLpJr+PxlyLJEk2Oes/2jAraDEanmyapt2v4kNtHA4ANx21eAT7QVFqWWu2fcuCexdet4m1zfwudsmorEiVkibi7mGb+zt6AtymAdCaGmk2QD+SqDX2UEVYx0PBMiDHJ0nV3OcRCSVcr21YT3oo4eo0u+gRwRFttjI26mZR8XKwCh14ukHNfRTUhMh73Kt9ztNJKhnSt9Yh1zr4z7ayeFSlZs4tbSNhCti5GWU4epq3c1j4U3o0BOe4ThFQm2z025h1Vi2o3IfkXt9pVlCMfsMF0bVskYAyXuBK8fwrTVrnKmYPKAbNpD7uEr7qThwiAyslVVGrI8hl3bclhnKx2P2WRe9atLzbPcBbY77qbSWq2ODg6v45W+LEVJrXNZjQ9yE29rq6qFHXNvjeIOy4LlirxtHc5jCClVivV3k/SUExC/Akh3rYXVaoNpHZRWY54jaxZQRiDJS/kOPvs1ZqcCxaPuLk7wzlHOnlwVDeyw7pY9KN5xDJmAuiJWfMK3SHhc712ctteoccJu7oUIkHWWr9VITHMnjarbVffcqx8oS+nk4nUjiHpmH+Aun3THk07cyTegoog2KSuddxHUrIr6UDN5j+wpCQs2GuV6uK94CFacYwLO3TZYrib/Uo8Wm5/zNVEqyBK3MqIkt1t2r9S0P5wmSgE5k1/pBq67pXQjjRRN7FGL7vAttHnZEncoSWwpG+YO0EW/hBEdBbZnZTy5AextnoP9QczaktDOG/6UmG1cXI5U5Jy0dH3dXQnlPgS33QTBoQVI22Mu9a00LK+9sCNlENxhmd2145nS3AKKVyU1mjuAgedc6HMrv5o0i1EtlXOSrBXqGcrwVdUHN74dqWvWYClAwaOiBrR6I5ZbPzBbNugyOvQ0obqFImrn5v6+j3DMOXlHrlaMLbtiI1G6pqOaEPDG4RC0CwN8ojNU3BpYyfC8cHVcdG0yYqnsomSv3OWw7IrdNgPcoAyGqV+S1tqhkr3m+WhzLrLKGU6KwvbR7jSwMYqTo0GIx7IYdtGt0y2GkemdVzPt7nZUiY10iDbqQdjTbDuqbsp63UorlylrD7F7u8hC4144n/cVGaFNL7NPZ1zYn6rsxDM7NxApEWNyR5K2jBOeCWOtru0LKyc+0cfLqRSTLW6G3ZTWenFw0d1pMlDVkhpxWg7hMQ3L6+a0F3QyZhS/75wjZu0YWhDzk3ODDziV+1d+CV/uh8u2jgEnQdqR7tbaBrWVarAPAey4LRMdLf0cZJ6690ygnbpvJUnLzeTAIEqz1QXSLoLCpAnTZrVk2yIUkci2TSbwKiLvrGOJPuICh2zx1ObkMa2qq+7H+3UzOYNnAUBOFLm/u2FA2vG1Uyhr4opLICSZRRwzXTuYxO4GaajbbVnGnqISP56JMjBpmT9uMze3i5USXojaoLSUqvYHm7M0/BArgpuc+6utokN2Mn2NXtLxCC0RJeS23RRKISrdXPyokkd0uT6EbrPNQbmzE4GfqTN7WU0UfDiXpOs3wbSCiZXKJ0fccj2OPiSi6KWuklGGVAfJSTyhO5HGTW5dF9u6lED/kqoddAxb8qzkPj+eM2S9E6I24Vk5p3KRsqzVwfCThPa20bYyFLPfJIp74tUraDt6GXADExTc0vc4YnO12/aYZPApz/BUxqjL1pgiXbZwMaH6o9W0CJ2nUXIcQDOo511/yRViJ9e9XdUmT6/XkigLUB6geb8NLoeyVjJZOe5xJjCDaOv09NG52zYSS6ttvEW32CYnIJ3ZXglIAGTl6dD94Cwjf9ixgbUplcaTC8EbD0hIWEzIT42moY09FsJO1upSCKwzzYb20IZFl5/9Jjx7dDM0m4ujM8VIWEojCuppcrZnLhcah+KSw3YndBFVGobdZhJytEQC1c5JIlPLRqYTpgIdiuH1F17Y2xBACn5drnY2LPeKuBVPuRWeuIAcdwBqYplUms7ZlsfC1FvJxHe6oZ+lVDgNRocv4QonsZXEshliZb16WQ4DB7ebsd41CuAcLReHZY3RRA0KqC5SykHGaNg0EhxvjlAUQBWK2455XJfiZdv0rYU42XVPcHtNonK7Q50pPAu2RleKehHYVqbR272um2l310ubuA6XXDi1DOVI4qETGbG9m3Y2sAk2TkK+2XP3iPIpjJq2TBNyctocDiSLpNsjhbS2KLi3anOzV2tpaQeUmMTdTd7eJ830ugy9KdzxEF52d1bOhPQUGGJwIEaEJqdBYRxCgVOV7+i+PtbV0rYHiIdlAi8GD/yDusEyC9ez0c053/OjkDm5sdUQr7faXWKB1j9Oco7amXP/5fEKLEnMYX3B9HMUj+wKc4bdGXAFu8Wnm0BEG8u9DfK21rAQHkjQzNXrPW9f7X2wo1wKIOx2Ckw06Iw1gmyN4sBAXstXko/y9xPuaDSx0pMJoe9LyI5Na7lbErvrhctUdG/4d4tGLy6aSUv+bPahc/EEdLWBMEuzqRQHuxTS3KNcfl0mLLu7iAhS5Okth5BmE5j+2KCFjBG3cRW7SnS6noNABlvZrPJlogqRxEZRwc8QOIfx7dGVbeKG8ls98viV1i+RuOPdbhUOh82I3vb7i8gPGU0sKXty1mpGF46Hypd2NJcSLNaDDVJ2wpbQ4CS1rW4y3BhkQ0wwucBgcllRMFlSJ7rY6AR7Pke4PGFSexDVSdzvvMtpUjMDMEM93tKD4yv0Mr9ynjrtd1htsN10yc2TSplrqj/tYb1zymibJMd2T7eCVZcR44eVYzr68RxA+9N5oC92zFOMuYqJ7moJxP18ujlWc9KduGroFKqMXsoNAewoTbKbGjy41a6/bdU20ZIhxCueIXlPa9glpbVrZ2Bk3TKhHd7u5Ltlce0xPPrsCJ9b3SKBMEvFkMEoS9MO2Ui1lqtzNrY34uLc3ei+6e48YRvtaUDC6EY66erAXJm9lsjtCmEOyQUZ1WG0+OWkiIhcdf0yjDeH+r7D8DXZNHdfYE7n5EyeyG4PmdfbaOu51awIGpKOW4hvdpsttzysze5CdQinEGpa9kwR7rkTwiKHgTI4tLzK/lSr6dqrozRb25ts7AH2bVYB2GDi/kYui/EehGMKmodOi453DG4Q34r6u38PU7ejr9eQGW8C6/NGnTZSeofsFIIKfVwqQmppwSWB3BZaGzpp70lLBt0uHjtd37l2kxakgTa+dzmLQnlrpG6dJgOchGSj0LGpdoLTdOe7DR+2/LrybVpa3pIlpVzSmwHpPNRc7qv91WenXV76RchC3CYh7DjsW92+X8R81IcSxu/FqAR2ld+Gq89UflTexN4v7sLg2oxLhiBxC4UeamiMPeJALIObmmNhMugYX6zCkxtozPri+XeZorQoE3s3h4xQ2FxR0V+5PQ0P/OhfMi+Fe3qN2+eNTI8WvrHB7iQYzF2pAEAu9mJZXtdcP6KSFwrW+shijlj3JwI0O7m0HmTd1w99qE8+t6zCfKqpSzRam0ETwjI4I6ucQc68eFWgztfK1eW+3lvXTj9wQ0erNpvb9Lk7dCHKELyB3tMkI0WVuqVDzvUkgYkm0xKsj2LSshaJyzVLr5iJMkG2oYqxSXueGdMDatlsFaHdbY1pS0aEz91ZBtivx3m7jgDvYdGS3HR6zl1t1qG6EucveIixFMqPCXK2QuZ+OQnELkVK35LO0HDRrIN/UNXNCqOXm3pPh2OsQpbQM2YoBKk7iEUgiBrYrBfGqrnbIVw1UA+6yASl0W10dI9VmwjqpkMRBD9KR7CvHq/4To5Epc0rZqXDzrgd0FS1bExHUg8dM/g8uiubKRRSrWtfCFEjOq2R9rhth3OJ1jR5PFRTLGnqrjsSxMnU9nfrXgS4wMEws0MI1BYKd09nTeUPErxpNezEXRiI0JeXircMNu30iDVjl9vYrcTtY0dCLhaZbfWAhkMoQjqd33jBiuxVFVA/nCHu6j4Nw1QVZrwZyyXC+KWQw1BWpzgAzr6Mxw0i1pmlnFbWgLhEofM+jG6sVXS/6Rx51wh5kBlU3CCreq1gI4zq3uo8WKwpNWPGjYN8AitImegqSKMWlG+oNZtG57dW0NwQ1VgZB7RkG30+luGhkD4uxWrd7HbpMsbZjjUzr2ZrDpHkUutUUhs0M+ElZ2MpS2IDmya0IrArVZ6QXBZwqTc4vox4NdGvfcG5RL4/M0uK49oGYm2qMmUtFCP6LoI9JG5Zg52ut2wQHISldgsbKzMh+ehEEik0/do5OTvQduchbHhGcVxa4Z1zYiSy1zq5N6oWsbSby7EHHlYmDeMhDvRjB50nm+Csrdvw4AkwRg7Q2U2is++pd34zDue81sjxSJix5yTugWxgC4vw9RVub3jrDva9znfasuv5/Ox6qzuy3te1zV/vZzgIUCMW6t49IUzoij7TVvb26sMDjHpB1OGOGeTBmUjUW7xRw5YlmYubWpIu7ePUv5K4ikldSO3Q8FTyFx2GKc7fryXKGYu9rGd1yyHbnPaLnpluO1pZncsLp5CEjAtCG01rYmXLDkGWAyEqTQizrL1ZTsXSCnqGHOAd5TO3+1TcuwpB9vzBtilEJFFTW4oHax8hV2w8L/MNHhPqREOjrPpZGSVKzWGr9OxvRqS2mtIvg7GHDlFx6QQ3ZrAub4bYcVc4vkNrDY6yEuHUdXkuGMAnfHgaePcybVvDCJc4Wh8gROqv3UbeofqdcnflsA/61ilQvFzSK0m8qEdK4yb3oLaltcVrDEVQSw/kkVGiJKJPehCc14Bx6c1+kisB8+PdnsJCXr/60qZb2aRGKoIhavZZYrDBG1mk5FoNLUiHDyk9OeFERgiN6dwCk0Gna7ZsG21djKOhgZozwtwqoZhM2BhG/DMWrJdmvBJRkR4Rn0LJqBzSYM0zwchCVCgpAhlWw2BOlSY3HjJIfA0trb0TQBOTyOEaSl0Y7UxiU5TBdpWQK9cfLBTbtFHJwrfdLYaUPdKm6yBg9XFDQmFSMKN0Z7pRVRWrRwdcjex4PUo9cwbtnqgrl2TPVYKfm/de7bbmPvWihtalc2yi5RYKBmJob23C7vhjomkTH0/EVt1zDVO1K1Jagp03QLzyOEpCIHERdCB4UlfpXdyuVuaIVBzNQIKqR6rdk9kRH/hLkER5crciHMGJkHCUJXzAUBc2m0wuij3Xa+EhJsMA2awHCLqRt8aMhytXBNBQuctGUo0uX5P1kY83e1wTPPIUZY7pSR4hlgiCCiN0pXTbT70VPB+z/PWvb/OB6fsh3tu/8R7afMbz/+w46Xkq9P5iyeN8MvLCzw9dn/8do/724a0NMmDS89isy4fkdfz0d4dmH//12eM8f3q+3vV+vP08Mu+9ZH73+S0rw6Hr2+lrV+WPV0vADH/o5pclu9m24HVw/n7I+k3l8+bDhb6aR8bZ/Pzx1lERhZnXR6/L5HWQCCa/Xnn6uiLwr1Fbz66+3k0AHq4+wZ9Wb7/9H6wuetm3LgAA -->
