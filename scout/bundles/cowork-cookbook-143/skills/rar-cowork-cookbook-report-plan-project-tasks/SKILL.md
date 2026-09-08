---
name: "rar-cowork-cookbook-report-plan-project-tasks"
description: "Builds a read-only summary report of plan project tasks from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_plan_project_tasks", "rar_sha256": "f395f63d30389ee6aa69c489b58e639cc004b12417cf7496cbad8c301c517ee7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_plan_project_tasks`. The original RAPP
agent is preserved byte-for-byte in `report_plan_project_tasks_agent.py` and in the RCI capsule.

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

Plan project tasks Summary Report — Builds a read-only summary report of plan project tasks from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-plan-project-tasks
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
      "description": "Excel workbook filename, e.g. report-plan-project-tasks-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_plan_project_tasks_agent.py` and embedded as the fenced Python below (sha256 f395f63d30389ee6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_plan_project_tasks_agent.py` first:

```bash
python3 report_plan_project_tasks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_plan_project_tasks_agent.py   # or on stdin
python3 report_plan_project_tasks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan project tasks Summary Report — Builds a read-only summary report of plan project tasks from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-plan-project-tasks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_plan_project_tasks',
    "version": '3.0.3',
    "display_name": 'Plan project tasks Summary Report',
    "description": 'Builds a read-only summary report of plan project tasks from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-plan-project-tasks',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-plan-project-tasks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7fb2981d004ea401',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/plan-project-tasks'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-plan-project-tasks', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Excel workbook filename, e.g. report-plan-project-tasks-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where plan project tasks stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of plan project tasks for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-plan-project-tasks-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan project tasks records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of plan project tasks from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a plan project tasks summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'name': 'breakdown_dimensions'}, {'description': 'Excel workbook filename, e.g. report-plan-project-tasks-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary of plan project tasks activity from D365 ERP with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportPlanProjectTasks(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportPlanProjectTasks'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook filename, e.g. report-plan-project-tasks-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportPlanProjectTasks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6adOjRrbmX9G8N2JsX6peECAJqqMjhk0IgVgEWsDVUWbfF7EJ8PV/n0RSlZe2+/aNmC+jKlsCMk+e9XlOVvLzm921UVm/fXrTfbtY8HaWxZFfL+zCWzDlvaxT8FWmDvhv4ZZFW8dO15Z18/bhzfMbt46rNi4LMJ3u4sxrFvai9m3vY1lk46Lp8tyuR3CnKut2UQaLKgNrVHWZ+G67aO0mbRZBXeYLdizsPHabBbZeLbb/W2cOi6AESizCuPeLReaHdrbwizZux4dmVdm0Pvjy67j0PoAF2q4u4iIEDxfc4PrZYtb8ofQ9bqOF/tTkw4L1WzvOPjyEGGW1RBZN5Ptt8w7s8Qc7rzK/efv04z8+vMXg99unn9/czG7ArbfjwwgVGKA+9Tdm9cE0cCcEz6sR+LEA10ApoHsObnl+sHhdfd/4WfBh8Z//md7tOmx++PS5WLw+n9/mP8euWLSRv2hL+2Gaa1e2E2fA4PcFld3tsXlZObu4AWEowvfnzF8lldXi7/Oz75+LvId++/3ntxKoYM9B+vz2wwI49fNb3c2/32cp1fc/vGfl3a+//+FXOU3nPAIEhAGt37+8rl9iwcBfh8bB4ouucsxrrdp348oHwn9j3/x5qv4S93LJl+fg78vqw+LPJc/2/B3o+0w0B8j9c7HAB2Dm23tSxsX3rzXqEiSOXbj+9z/8lVg38t00i5v235L741NwBLIbeOvlkh8+PML3jwX0su2bzL9edq6B/4klYPjX5b456q9kPyL7B9FZXPjNt1j+qbg/mwD9ffHjX9r2ryZ8WASf31g/A5Vb207mf1r8/EiRH7/zfr353T9+AaL/WzF62dXuQ8KX3C7iwG/aL19+/K553P7uHz9+11Ugi307/9LV2Z/J/DO/Ptb5nQdfo77//Vyw/qlIi/JeLL7V0OLnsvpf9S/vi7Odxd6v95tPi99W4vyBFrMRXxd9uuA31dgAXX/jxx/efgGYUwBrOvfxGODHf/zH4hC7ddmUQbvQ3bJrFyDAbZz7s/JGFDcL8HdGjdoHfm1i4NjXuBfGzhoD2P3p/7gPKP/ovqAcfkLyIxu+vMZ+eeDxT+8LAwgs6ziMCwC6R0pVPxd2CMB3Xqyq/cavewBQztj6H0Edf5x/LOJi8dNfyvzymP5ejT89cDd+It2REWaUa7rMf5/tuUQA6Z/auwDG/cF3OyA5K12gRhADYJ6BvimzHqDkbHuTxlm28GKAI4CRnsQA/PNpFvbTTz85dhN9Lp6wjC2eVNXAYMA3dRYfPwJ7giwOo/Zz4btRufju51++W/zX4l/Negif11ABMby8DzTc64q8ANXU5WAYCAwIJYCKh/d//uXlVSCmANwKYhUHsf+cDLIx9b2vLtZ31Ed0tV44PnAtcGs+u3Qmtrh9XwjB4pu+L1Kd2SACZLjw/MovPL9wRyDVBuZ882RRtosGpFwTAP7rGv+x6k9ObT9UzEFZ2+1PiwOjAu4pM/C/Wc3HIDC5LGLg/m8J8LwPhNTfNQv6q4j3hTzn36Kya7uKavu1RmA/4zIT+Ws6EG4vCv/+uZjp1Z9d9SiGp3vAIOAZ9xXSj3PMQc8BmLvwmq9rP8bYM0MaD6asPxfNK9Hteg6FC4AfLBp2sTfD/99eKdVEZZd5D/8BTWdJryh4r6g8clD95/7k1Tosnvy/+NyhyBJf/H/e7cy2Ujx/5HjK4NgFJxtH8xmDucebY/VsC2cNZtUe9fZrS/IVdr6i7+cii0FC1ePfniMfkXuNeSJaVwMDjtTxIR+kDYjBLPeR1XOW1vVcD/bn4ivMA6UXD0wDgQUQAEpkzsyvC85Pv2oagTqfr3+l/EcW1N5sNsjcRdU5GciqwPc9x3ZToNUctK+RBCnuz8G6R7Eb/c6qOQQgnkD+AigRg1oDVPD+DXqfT7+q/ruJz85mnvLo+jpQmPVDANDDnxWcAzKHCqjXPltqYOenhxBgRl61s+0OKA1g6fOmX/u3Lm7idobBp1/9CmDvx/n7ael81x8qkGzAWSDnqw5491Elc67koG8BOgCgAEWTxwXgceCUlxMeAu18LnkAqa9G8ynxcftlkP8orZmAvk6cDZnnzJz+TG67GH+LDMafpQmQl88jHuv+MdO+rTbLntGxAQgHVvz69En+70/+fjYIi69yP/3TnuX7/9m25sHIp98nwKdF1LZV8wmGnyz6lUTfATbBT12bF6F+nEv+46vkPz5K/ncCn7Z+WvzPlPqdiFdRfFos35F3ZH4kvZLq9QE+YD7S5kd8fvq5OPq/QiZYvsxBVs0RGwGDf+O3r0MAyYU1gB8w+Ml3zUyTd8DMD4AH7v9c/DbL5yoD/FGEc1Y25W+q/0H0IOOf0frGQ+BR0YK1vbkRDP152/WoicZ/+1R0WfbhDUCj/6+2WzPJ5HMON/PuDLgawGIb+48rB+iVeqBKv3ggR4vm2Uf9/IedKvvt2SOnvk0CJvjv4ftMpXbdztz0Aejd+mE5YyloPSow5dFjgcF+/WH2C6Acu6qACXMBzNa0YzWr/9yhzT3dA6aG9p/VUB4/7Oz9BdPNb3P/RVczXf+mRJ8eB552gdUfFh5QrpnpFXh8dshc3k+WKes/1eXBLF+ezPInfpnp6HfkM/cCTzazw0dFvzx00g/bP13gW3f7z9IvoM2YBXrlp5lxP7yA7sODJYGjv24ugFmv7d5jT150YCf947yxmWP/mDL/AHPA17dJ3/41wvHf/vFnej3Q8Mucmc/8+qN2f6DRrwNf9v5lcX9EEXT9EVl9RPH3IWuGP3XKk7f/eU31t7T+G1+Xxd+ADwK7y0D9tOUj8vnc44Hwz4T3u3ZgYfcgd/4i+8DiD9oA5Ds78dfo/Oqj8rETfKiZ2e3zHy5+fgMFZoPssl8l9tpKgOEAZT82c0MFA/gBC4LrJ1CAZ//+JuM1sYls0OuCmQFGroI15mEIRpC+v7btNeniBOmsCH+Nka6LILizRPHlxg02OLl2HdsjXAxZuqvlxvc3QN4TZ77M7WI8K7MiNwFCkmiAL1HEA+5Ecc8j1sTaXW1QxCYde+WsSNv5dWoaF97LwqdFs/u+7XdmT7wMBTizxsHIHd4I1PPDwOTSgdGNM0pX6IoQQ3Y/3W7WqdxveoeMa3nQbZS7G+aGvg0tcWW2R13ccZl7Gu5dtNESnnLW3A5j1DSHXdTmhbgQvVaSsXzNUntJyA25mEq4h/fxsMJyshmPwtGy6x16NmNG0s7Lm5utWjnl4a2yyqueZmFYbeDh0IxGLLRUtZME+lbLcio6pyCzqqMd52OwZPdXHuNHw5TlHV8PwxGCuBsJ+diGOMfDmc3FGtrecqHia4HmRsnfxyIuIFxV6JGr7yb+cE4cmjr5VlWIm/upGiCGPwGUPELtmb3p7cQNXj0og1A0YRJbhyMnZQa64pKytfQtWXTkdk0G/dSSsC/FJKe7QdEPm9ALruKYMduzbfLcMTucQcA0CHw15ogxAtVc3JOkEmJP4axk0I4Nr/XrIDTeeiImyrIGQb5r7Bixbti3mETiA6TTiuWuUpwQrs691KZeNrXKJg2L5fV1Kh2YsbPsVUJf+JKgbhOzPLVHlPAKqKVqKMUiatrTl7QUrKW2Om7bzgyKlS7utQ1/OmQlhx/PuFCgA50pZz2T9MkolSWOkakSR0eSupgM1RE73tBy7dqy/TT1OzcX7DOOTDq9T5vjen8QVsXkSVQYG2edGvNyOxy3uxgWqahzDyF274lURHstFvl9gxjjqQvGKtmdXZ1FR6IyLF/iPGT0+vS4EdkhPbDcXrcs/swpty1THGmy5vZCt98dJVGDdEsxp7viB95BkiMKR3j9IvR6798qzCw5bdnQUXxUhX5VBRJDRW2uh5hWXztLE4+JzdPy7XI/l84lpCQyR29omQkVxonGkNYOY/vr9pybrt5EQVxIhHjETrckOluqsT4dAozuTA3uKQsmjjdmj9etcNFQaRef1+O2DFr4BG31Jh4lAyHSdCXkUeH7Ozs5DIly27s+MUCBY0K9bQZOq0zQMInJWqmMcmvDpEG4GkyU8H0VtfVRNQOyIIigL1iI64iNhBriPe+ZJhQaybDvQiSczt1AMeutb93Pfifyk6CexTDgTJaBzC6wp411pzYTX8YGem3RdLQKxrOYbqTs5a1PcccMDugY7rOKz28RZdekwOiISzXYfbu6ZtTSWxGbetioUaAOF1SVu13lUlhNiA4z4oeGnw4bDppMflVgdy7ftzDaJyeJN2L5wmCqfm+Hm+mu7LXcWecCRyCtFQiqx1ShXO5zrEh6kXW3pJxxtpZ1ca9SDH49ZmylLclCzNfQ6XJHqohETdi4CcbRUTx7rw0NbO1KCSnlVvbtM23E6Qq3bqLcd9apV6eDfWaPIx+orMJctTTjDjp2gc8THepTNx6qgY0KxbJg1LL0goP2V7Hd6BVajeLKgsVQlMxeCDNnmJRezwx1x7H87jjdfHfsbZuc9FIaGe2uaigNq4YLrW4HrxYEj77bBiw1iAwJzViGkC+SydmZRME0tj4cqQGTq4eexq64EDoEaaIQ5yyzmCfZmNoyUt0XysrZMT417JgbSfFdicq0l5a0QZXJ4G/rzVLGrPOBh4lpFVG05uFBxV/d+rixCEfFiVC4dTwLB8thumV21h6GprkbfBGqWGsWSlAcvLPY2fKK5pS1SwZ0zOL7zZ5E7CGhxeXdGybZ4/lwXSokbiTX0PKIFDJbItM3fduRHHWR092lxqeTp2Saw+xwVB2I0KeP7pGqcdUtdweNdsMbT+9vohto9E44NzpPBlc1yiHjsEq0UWNXKS1LVzk5WC0AVj2lEATNst3ypDQbv0mOuN6dJ8o9mJ0AS/oqNDX7Il0DzakNW+by6EJ1g7i5jp0og/yovWlL4hRrJEfNraF8RZ8v0uA3V2qZXpZZmA93LGNJa8+XQxkMKdGgDk7K/YQQ3oHng/ueVkukROKOYXVQ+gki7ojTmeZOk+ur5I69jpsbmdHchAmlusav7ERiE0HG5lrpK4POEE+tt5iln/HtYEyTRnAXWmUY51BIdxetBZnXD+zRlzrlbgg0iWAYZdhMPiabAudLUIZXPWF9p2koU9UDxYa00ee9w32s7rtQcYe7odCdVtHNMNGnKyperNPu5vDb3iraK3e61Led4dfQTXc9LKkSyRKq6Yzgaw6uOdeHJMm0oPOhFbdXpdCuW7Re3eorruo8A0XZhJytezqoQ6vi2m0pOqp5MpAmOG03eJ60bd5xZJ05BiEozu1IMTtL8feczHpVqOyQICqCxNXIPS/F63WQCsdyOimpU5muK0PevbOlk8qWalZepskj721IRFsu8uT6Vodxyax2pCA3eq3IwVYRjjRvwtDtdPS085Vj+IsZY6LE9Qyb7IVpH6PFvt1EMIGsxT1lbDU8PydbS74nFY9qt11N8kRc+DGjlQhGt2uXd7envbaNA0FvIOlQ3s65FKdWLCnanbpQB+MUbCy/P+d1tOcEowy3EnPixfSme/C11kJza10JKcyqS0si0+rKRZDsJfuhjLfrVUuJm3Q4FaApiPlbfqVjm02WDi1ALugcSJdF9EKVtctV96JaMX1BXg1dfzvuJCjaG4SIh2rbn89aTmTtud/uKYQ8EEfkymTCPfYiJd96EefGRe4OujjKwq4qxyxncZ2/a8kBMJITT2Q5clByogF1wRuJXHLsjg4aPUtUBtc221ISNlxtbZl1sEOzssNwqxGYouqjzstRaYkLDIwcRylnSHd366lKDWH0zot+KLMErEwoRB6GuwObB72wD/mkw51mxtaKcGj2eKv1vdM1QsqZ5sSY0snEKSg46myaFXazXXEVJ96PWUoY123LsNaqJzz3tMdOLCamXrgunG3Mg/hCFswONW3b1RJdHo+UXu5v1LQ943RIslCYDvFw5w1Yt4/ieC1oRkYwr7jHFN+mK4Und/gGGZHj+rQ3eh1Bq6m1ttpW3QtsGO3NcyothQMSrBkeoXHYWlu38RJimOEVMLaCykYetdLrKSXhV4OvkX2AdJkOCEtNDwXG7q3TsFdcgHnHaNt6Sz3QV01QFAqjlNNaK9VTJOkF7yw1iE9OucboCmiayv4QGfpRcGM2MdOYWSX3s6bV2mBTK+eUoRNUBT0P3fKdgIg6TNQcxjG5gFvbe2ixt+NqGenp0O6o8aLYfDjJ6R3fHlLGWzPTkSxLH8IJCtGxlX3q2jWhXaoLaEqptdiu9bWtaW551UI84c78WjhQ0UCl12Wrnw7d5T4WaSUVWVsripz6p+U6B82djjbhcMIK5X7pJxKGiFIoWGA4fjpuaf58zrHm2uYWDak4pBRHZIIOyQa3VRjT4RVbssjkb2WSI+3BT7wAP3XpRLUUBVl6PhDO1TvtGEGku7PKxZ1gmomd9LdS57ILaP7zA5rYN7e2xdvNhthKOXp96ezvp2PGcfy4nkLWjBE2DWFcq5LYaZdLiScP7UpFMJm/anvQ50F1ZlJt5HCjaEYdxtHcIUPC5rQ7xaIv+Jzv1AlozTAOpjb7aAiZayaW4gpxE7i8Q2ubaxoAFzVqyDWtbSQ4UkDbu2sKZalRwtUlVyVD7be3ems71hol19qQkozs4KGvOuxg5QbMCGmuXMXoSK8PGrUsZbEty7vFuYJ5EwRahyDQNyHWAdYyskcSqhLwuqQvJe1KpndG6LM2ngZtywYmSPID5YmQdNvpRQfqUJdrjkWkpZYX0XCMc4agpJQHm0Go2W2rftpdgo2+IQfYOdKHIu73V6ZLBrfpZZcWtGx9dgXpYAVWsF9S59MJCxMz5tqeg6tMWN+W+u2IHbhoeVme84tyzWNDbIslP55ZsAkK4YAnIWjfl/0pp6jVjiHQPFCVDrSQemgbPXxKV/mS3eGcdpHCCxLKjCPpnJkv6WrSuO2SPWtRBlXXShOxtM0U7KqKY+cJwqhusVLfhsez5+VpTF/ufGUweCgeNu7aYUKEaAyZv4/ZBXS2HYKYhntSoBVSq8e6kfWMXYa2y0e0nHbGTmmaTFR7sE5NpBS0Nsc6um3gAOKHGAc+ZvdckhbqXub3OtGed1oUYDI2MMQGVP4h4iVslzllcLRIZH3ZcvWpspadDpu6uQn3K2HCQqX2thDqq6Nz3Tq+0V96Z1plkBK6m6bGO6+Y1MA1OwxZl5swFMIiva8Ls1kvSQN0jnthg8OVv+c3qLbLIoJFBOXKKOdrkg9j1CYi7Nyg2GvMZTH4oz/lpkztTLrqOl05xEe91RjuhrCnpPSFM7GMnaLYDfIacY2EoQ4+DHYc4kaiLQi7y3bLp2iOTbdzG8SQqQ48fJJaRj5sDpyXeDsLtdrjUvNKG/CD2KZw6B/xPL9ttjexxjYeP6B7hGjZaqdGhOUBALNDVPB7JcKI5bHH/JK/7hx7e8FDwhZXYrLqivPtwsKHnh+hQjoXconLl0GuN2Q9dWqcmFjvKSJaYZm8Cw8reXvpdR5C1fIwnFblaVWzlan1GyZVTJu3nelurvHbJGG+Wrjni7uT10uGVEApRWh9PqB0HV8hvUWSk4CdMm61Awkx8dsQixTcpts4dI6+edtDlxwhW/mqD93WUwLSuiPElj5fd7DQ8tDk0l6E9FYK8YKBEfXOsch2ciandOG9aapRgbMTNZ1kaVuhkuytMBjCIRiXSHMc3QidQPc8BITtya0A7NufJ4/uW2HJMD7XWXtHTMJdEaHSuikSaS9COXPg4NIW1eBowxfXWO5hQ3UUWvBXCURRaQQZYDMUILoFW6Ycm9sYlicl9+MU4Z12g15CwjlcCnlztDcS0a4SI1fqg276YHcNoHB19qULufcc4Rqhx7vJVHvjCGNF61m+nxMG7e/MXQLRlYddeEm4+2ly9FduyBRlL12sAHE8sBulRxJ1tFaKahSW8tKTtF45l7CR9is/OCdtxyW3JkT4lBoF7jriyhbDagpsYhVoH9tMuXYuSqmfT4IvW4eLf/EL2y7mPkObpltBIV1/bnOZl3svOfcpmfU74S7A8kZMMW5DXDOkVeNt38T7K7cDe0CzNTcHFT0kKZocKjdEWJ5fu2esr+MskB09cZe0CnKKVKjUzWk59GRf27f4qW3uXrPHeuGesvmy2E3hhqiUzENsq2KuS5iHQcu+M6rNps9HiMPKxrT1MYj5Y+fg0mSKEHuRz6KqHMOg7HYXrz3lKrTWNlmJuvhmE0TSBjkLK3Qg1qTmDuQR8UBrhic24oarWsot3q9lC9PjGkX2G+WC+/d6tG1bIQdWdWTS80+jjSXXgvSrlRizCu6E6J1cFnenDfVz1tEJQSaXQbli/a7bJXyQckid+Eulaxh3uSpRlMaQMy3frAnsnUHLi1pLVV5fhcNW2ySXE97ld9PvL+OduHvUdrvUNj5XbU7e/S4JOxgJQM+viLHEmj5BH0nQH1gNkkZk01+Ol044kXfpiLVr9E44S7CX6FrQWNmwsTn1gepuztdjE8JTsCNvOaaodaRuJ2nyu2lSrtfhZmCcVIyQlleqYa3GTg7OPuacdJYk8jbyl7R9DT2lc/Uohg2TlHxldRv0XISoK5Ek1HZZMoXetvXkXOphtby0JmGeneqi4LGyPo8Ifh/WZ6kvMOdmBQajupVnqclG6O4TR+v5Nb2euNtpZTqI58r3iLeczbmEVskBr+FemiimDU+GGaT5oIiyQuw2gnwPutQSS2OgJ3GbJTVcm3o0RmM1Itf8mPiwdQZo2XOs7+o0wXtWvUU1SDRMbw8LTmuKDuaF+bE9tZ0fsJW6Kje52DsXosU9FOxMr3sxiMMTLWw0VdhEDnHa+ksKVbH7irOsCxSe1GTYnInSoEkORZw0m/ItPbatjbk3CEmcEdmJfXKKMXo58EzhY+251dGLOy6b2vFu5g27Qll2y2RqunSllyXdJJmTXLPizZl2oJQMenRFWGrZTFV9v64ueseuI7nyBbQn7x5xE+63pkhNtXJGDHXiCwkJStFuhSaDLylz20qStpTu17S+i2J2NRgkHCQLtUG37HMbn7/ubwPpLVcSV19I8la4KLaGUiVj86hfKTHb46d+XWdCEKAHg2zgnSpO6qVmy+TAiU2GFN2RmlaRtaU2ZRHhMNL3NXZca1cSPhau7iC7rCl2QuMELZQB2tokm2zZriVYPxuX6x0SK7suUN+DIH0Vsh1nVqQ2BWyKa+syH4qLFOWWENrE5Rp07e0UkLrjsmpxvAyQCbo1n2THvPcuuzjApVMWU6RMmcYeFHzvBUWeTterxZHT7UCZpJAz2gUC/TVVXJRRZ6CqwGFNpLTJ5SfY2S87LJ/2d4c1BEj3JaOMrAB0A2ATuEQLk4ZEJS/bIb7tmusu9EtWhIfNNriSwz4A5L++IPbmVsvEJeBoONEajYWL8QpN25ipN/LdcXvOOHY+TWO7+8GU632IWW22XGdnegC+aIcbaGFHm9/09+N+p6D+nYDs7rQm8/rEYHcMterujOLL2kUI9L4ZGJgv7WViBg1emBtsjWW4Y3EEGhNwOV7P44ZxHBs+cS3mYjF+1yBkp6WMwNrZCW7lw/akUUf1fNyle+jGGyHhXz3jTNjr47aQYkUZDtDlzjm6nbZnHSHhOAwYZl9zQWEU4g7kHem3qIzqDrMJKgwz26Ul8jtIsX3Xbh2MKyZ3y6wiUqL5GzlJG2yjdVbC8StUwi+3mM94bXtQSNAFey6W4B0J08lmOdIIHreHQDjJQXtI8cKFWqSP1EPo7qTEPQSaq2wDrBhSdNdfCTqmOm7LZgxFUX9/+/D264Hb23//dth8FPP/7EToeXjz9Y2QxxGib3ufHmt9+jd0+ceHt9qNgSbPc64m68LX4dAfTrk+/uXh4DxtfL5i9fUM+HnE3drh/JLxW1x4XdPW45emzB5vgIAZTtfMryc2s14u+P7tqedzpeedp87lPCyI53txMb/X4Xux3fqvy/B12vfhzXu9cfQFW6++ANSazXu9SACswt6Rd+ztl/8LotmwygwuAAA= -->
