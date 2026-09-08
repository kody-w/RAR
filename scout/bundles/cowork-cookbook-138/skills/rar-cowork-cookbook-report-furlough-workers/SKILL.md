---
name: "rar-cowork-cookbook-report-furlough-workers"
description: "Builds a read-only furlough workers summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_furlough_workers", "rar_sha256": "f0369a257c04ef1ad4789b36fb12fcadf3d54c8dbab1ef281824339b07016407", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_furlough_workers`. The original RAPP
agent is preserved byte-for-byte in `report_furlough_workers_agent.py` and in the RCI capsule.

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

Furlough workers Summary Report — Builds a read-only furlough workers summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-furlough-workers
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
      "description": "Dimensions to break down by where applicable: department, category, responsible owner.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-furlough-workers-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_furlough_workers_agent.py` and embedded as the fenced Python below (sha256 f0369a257c04ef1a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_furlough_workers_agent.py` first:

```bash
python3 report_furlough_workers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_furlough_workers_agent.py   # or on stdin
python3 report_furlough_workers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Furlough workers Summary Report — Builds a read-only furlough workers summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-furlough-workers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_furlough_workers',
    "version": '3.0.3',
    "display_name": 'Furlough workers Summary Report',
    "description": 'Builds a read-only furlough workers summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-furlough-workers',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-furlough-workers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '336653a6fcb49c5f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/offboard-talent/furlough-workers'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-furlough-workers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-furlough-workers-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where furlough workers stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of furlough workers for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-furlough-workers-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads furlough workers records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only furlough workers summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a furlough workers summary report for USMF from the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-furlough-workers-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a furlough workers summary report from Dynamics 365 ERP data with totals, dimension breakdowns, and a top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportFurloughWorkers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportFurloughWorkers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-furlough-workers-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportFurloughWorkers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6adObyJbmX9G8HTFV1bJfEJvAHTdiBBKrQGKRBCrfcLGD2HdQ9f3vk0iya7mu290R82VkVwlB5smzPs9JJ7++2V0bFfXbpzfdt/MFZ6dpHPn1ws69BVMMRZ2AryJxwH8Lt8jbOna6tqibtw9vnt+4dVy2cZGD6XQXp16zsBe1b3sfizydFkFXp0UXRotZjF83i6bLMruewJCyqNtFUBfZYjvldha7zQIl8AX7v3VGXgQFWH8Rxr2fL1I/tNOFn7dxOz2UKoum9cGXX8eF9wGIars6j/MQPFzsRtdPH6s99B3iNlrozzU/LLZ+a8fph4cQoyhX8KKJfL9t3oEp/mhnZeo3b59+/vuHtxhcv3369c1N7QbcetMe6rIvay5PY8Cs1M5D8LicgAdz8BvoBFTPwC3PDxavXz82fhp8WPz7vyeDXYfNT58+54vX5/Pb/Efr8kUb+Yu2sB+WuXZpO3EK7H1fbNLBnpqXkbNzGxCAPHx/zvxNUlEu/jY/+/G5yHvotz9+fiuACvYcns9vPy2ATz+/1d18/T5LKX/86T0tBr/+8aff5DSdc/PddhYGtH7/8vr9EgsG/jY0DhZf9OOOea1V+25c+kD47+ybP0/VX+JeLvnyHPxjUX5YfF/ybM/fgL7PFHOA3O+LBT4AM9/eb0Wc//haoy5A3ti56//401+JdSPfTdK4af9bcn9+Co5AXgNvvVzy04dH+P6+WL5s+ybzr5ctQcL8TywBw78u981RfyX7Edk/iU7j3G++xfK74r43Yfm3xc9/adu/mvBhEXx+2/opKNzadlL/0+LXR4r8/IP3280f/v4PIPq/FKMXXe0+JHzJ7DwO/Kb98uXnH5rH7R/+/vMPXQmy2LezL6Asvyfze359rPMHD75G/fjHuWD9U57kxZAvvtXQ4tei/F/1P94XZzuNvd/uN58Wv6/E+bNczEZ8XfTpgt9VYwN0/Z0ff3r7B4CcHFjTuY/HAD/+7d8WcuzWRVME7UJ3i65dgAC3cebPyhtR3CzA3xk1ah/4tYmBY1/jQP7PEZ41LoLFL//HfYD4R/cF4tATe798xeYvL2z+5X1hAHFFHYdxDhBX2xyPn3M7BMg7L1XWfuPXPYAnZ2r9j6CKP84Xizhf/PIXEr88Jr+X0y8PyI2fKKcxwoxwTZf677MtlwiA/FNzFyC4P/puB+SmhQuUCGKAyTPGN0XaA4Sc7W6SOE0XXgwwBPDQkxOAbz7Nwn755RfHbqLP+ROS0cWToBoIDPimzuLjR2BNkMZh1H7OfTcqFj/8+o8fFv+5+FezHsLnNY6AE16eBxqK+kFZgErqMjAMBAWEEcDEw/O//uPlUyAmB4wK4hQHsf+cDDIx8b2vDtb5zUcEJxaODxwLnJrNDp05LW7fF0Kw+KbvizlnJogADy48v/Rzz8/dCUi1gTnfPJkX7aIB6dYEgPq6xn+s+otT2w8VM1DSdvvLQmaOgHeKFPxvVvMxCEwu8hi4/1v4n/eBkPqHZkF/FfG+UObcW5R2bZdRbb/WCOxnXGYOf00Hwu1F7g+f85lZ/dlVj0J4ugcMAp5xXyH9OMccdBqAtHOv+br2Y4w9s6PxYMn6c968ktyu51C4APTBomEXezP0/8crpZqo6FLv4T+g6SzpFQXvFZVHDrJ/7lNePcPiSfyLzx0Cr7DF/78dzmzkhuO0HbcxdtvFTjE06+n8uaWbg/TsAmcNZtUehfZbH/IVa75C7uc8jUEm1dN/PEc+QvYa84SxrgYGaBvtIR/kC3D+LPeRznN61vVcCPbn/Cu2A6UXDyADEQW1D2pjTsmvC85Pv2oagQKff//G84/w195sNkjZRdk5KUinwPc9x3YToNUcr69BBLntz+U5RLEb/cGqOQQgckD+AigRgyID+P/+DW+fT7+q/oeJz3ZmnvJo9TpQkfVDANDDnxWcAzKHCqjXPjtoYOenhxBgRla2s+0OqAlg6fOmX/tVFzdxO+Pf069+CSD34/z9tHS+648lKAPgLJDsZQe8+yiPOVcy0KwAHQBCgGrJ4hyQN3DKywkPgXY21zrA0ld3+ZT4uP0yyH/U1Mw6XyfOhsxzZiJ/JredT7+HBON7aQLkZfOIx7p/zrRvq82yZ1hsALSBFb8+fTL++5O0n13B4qvcT/+0Rfnxf7aLedDw6Y8J8GkRtW3ZfIKgJ3V+Zc53AErQU9fmxaIfv9b/x1f9/0Hc09JPi/+ZSn8Q8SqJT4vVO/wOz4/2r5R6fYAHmI+09RGbn37ONf83pATLFxnIqTleE6Dtb7T2dQjgtrAG4AMGP2mumdlxAIT8wHXg/M/573N8rjFAG3k452RT/K72H/wO8v0Zq2/0Ax7lLVjbm3u/0J83Wo+KaPy3T3mXph/eADD6/2KDNVNLNidwM2/HQKkATGxj//HLAWolHijRLx5I0Lx5dk6//mlXuv32bMaTx5zFPGn2B7AUcIddlkCpZ7sK6NSu25mfPgAjWj8sZlgF7UcJBDx6LDAVkAZQrZ3KWfPnfmzu4B74NLb/rMLhcWGn7y98bn6f9C+Cmgn6d7X5dDZwsgss/rDwgCrNTKjA2bMz5rq2G1AooEa+q8uDUr48KeU7Ppl56A+sM7P/k7CK/MPCfw/fFyddZr8r+1sb+8+CL6CnmGV5xaeZXj+8wA18g60H8OjXXQSw6LWve+y98w5smX+edzBzyB9T5gswB3x9m/TtHxwc/+3v39PrgYBf5nx8ZtWftVNmZAPIPzv4TzQKdAbrep3rv6z/i/L+iMAI8RHGPyLY+5g243cd9OTtf17/+Hta/4PL/wP4I7C7tH0k6axfNjd3IAtmwvtDO7Cwe5BCc7Z+Z22w+IM2APnODv0tUr/5q3hs/x5qpnb7/NeKX99AjdkgyexXlb32D2A4QNmPzdxJQQCAwILg9xMqwLP/7s7iNa2JbNDignkBjBIUuF67MOYHK9vD1iTloETgrJDAtb0A9XDMJQF5Oys/QMgViWAoSjnwGl4RGLwG8p4482XuEuNZFZxaBzBFIQG2QmAPOBPBPI8kSMLF1whsU46NOzhlO79NTeLce9n3tGd23rdNzuyHl5kAaAgMjOSxRtg8PwxErcDNtXMQneWaCEK7YFbHy3HfmfrEcf6dkNSKUUUZTnbV0VpxN58XdhlS66NzLkpdOulRyGeS74p40qOKMNUVXpWSvy5RXxDoNjYG8igGvSnfpiMHDU0zGOcLgWDpPmXvexOr7u7aEsk9td4bhwu7PAQBNHF+iu50W+MEc+NoZ8kUzeoOvKZ7admWxOrejodkuTWvYyWb2xGDdhNEkgc0ua3igs9PKKnbVpxcm3BnCC2WCX14U/XMk9hRCGRrPCuqVBTkXTsoaFia+XC4ulJdX3ViJ3pjY14ao9HLvSBgmcFo26kCMYEK8JylQn97JSi/N6GRaDOeJYJ49JrjGoXg0fJbVmIlZhqasN5bVXm/iKQtOfbIcpxBS8m64EzszLFj1jXbg4fJidmdrTWWXDsBMwjrGqp0xlzQLQS16VqMoF3lTleHvWNYfqIHsM/SsWhsNr3uM6vVxnJYcQj7c8RwTEwO3Wp7dnvjQjqJQonX5XWdMbggwKlIH6qjJLS3+4ZEpfMosZY+Zm3Yb5ijyFUXPiv16qzaKIffXKW17mTiZ6Hcbk5WvGlJU7JURA3s3ATbDA6XB7IcxSxjDMUyTrat3fmEuIjbHVdlNLtVhTiWjmfkQm9d4kr3t+Cqnls/Op1k51rwTelC6Z07xESSpxE+ZROBJFCZrD1huzRzQ7gmglQ0TSQykL1hzCtNrQVJWNKctuf0ZUzJ1g0++kdN3nstjSWMcSl6PfSzChUaXjWLTTRdD0IwFkEt0VHbqSFq9fnhrEpR7nCRUl4252LNNfS+7ZDqUqSCiLJE4Z4vlmGi56qZttM52ZPqNRgvByKdXGkvEgET3ZaVfGdMCqODdbxXtSOrtNuJGy2SqU2L2pJ9lY+dF14028mbVS7sYHl9H6Czk1nWyjjeJvaYE+yxJvhzdS29O3k5ySs9tQh8uV9CGAWNax+SL3ZyRHj0Ssk5RGKQavX0Ekq1Rso3N4HeSytEZlgd4EdDJRLvX4ez39ncXjgqYhhsrC2ztFrIvkPXYVPfuSI2YNVDwulqMs6V7qaNtKryBHMsX0aIUPBKLquijV1TAqPD/qbJh+3KTDYwyU6EOa47TTuO3mWjdHzpbnqHPDjMhMlNdhfW8vJuZfgNVXeZ2JJKfzOqzIioCw13eUiY58HbHhpKulUqGfVY0PmaUe83OaLDAcoWU18myU3b9ROF9YSTHLljlvQmYkdOjmnOVsvyAbopTBlJUJeew+yGmJs4qlp9s5RWZrg/qfldlzGlpxgELSJz61zv+6vNXRA6XsJXGROvsX5S77W3J1GZLfeHvcCYO2mj42k+YGYqkgZ2c2u0lY52LtRBTnYbrLWnmDF7riNIaSWTripb1/xQpvc9pdGtcxbro8huyK3Fryjlvk7DcdWGJczTdU/6d/WIRehZvU3jyXVy/KptZbc8NuIN27F4WhzWTstsbvdVtMVU6HIR1jCIXE2aBnTYZhduR0TBYcdOG8XUOlu6izKTphpfkXsUKqxu8i3ljucUS9EbEYemXYMfnOGO4d543Rhnct9GHj7ey6tzpYRpF1PbDTcyyLHJxSuRGW5yvN8aulvjdyddF+yd78pVyrAnJ1nGzIFUSnEYlPs9z247Yh0d19FuvT/n15XHKHS1lQRvO/ZWpu27jN5fJzc+uBATD7GWFw6+sZVwijbbhrVOu2YY42tTYbFCyGi9XePieBk4YVCSI2y5KoLek12ypmwaVu8H71zh2lWfvOsFgRP55m4aa/QiX0vvlhHuQqNbYsaFw2zRk5qNNJ2R4+pyugxlmKOpVGP8lmfi0JU4RTv3DV/hVnuuVKXmhLZuSoknEL3UqjFNhfUB6rc4TgZOE53kZE0fMdI8n+KTpQWsXSL5qaDEyGdpg74LKBpQ+03bdTZv6FoIH62B9I/8HZb5CtquDA/aRsu2PqNX/Uywg3G/u+TuQh8YxpHz7eCie0HhdHKr+PXyMBgCvSYnwHQpbVyv1N7dnkwH38UYiXT7Lc3tsfzO1YmcR7nRbCqrHLaZpHJ31RwYCLl0hRxGtNozSySLysjp2fWZZlmaGJv7ya9XuqrhSoxt9TjNeWP0m+Ndiku1YQY0oSYlNkeQ6gZRs4VbtQ2xtZqmsvWRYunkft4J9jIWD7tsj9lRCZYLYdwpwoiq+7g3GVlpWzi5VRAXWlF0P+hco+Maxwhg61pw07Vnu/tKU8aNENvLIMG7Yr3bpDaveXJMu2ECSXCtFJASmka8hTZyTu3iKxOr1YFamSJ9opPblLCdmOaHNuYaSbrRPWRKIlzsxChM6n3knM+MO9JIGeowF+LKsDtA0xJVrZ1c8cAWIRfLHSuYk9CTQbiSk/t4iTU6s66OPpBITdP35hbRRJ5eUpZrRnlK5a0ysqGUhnSVjXs5JfzzRVQHiNwOjcUk4yHdZQDztfNdKCR55ewcYuo6xJcuzX5wlv6h3amdSdfC3MnAhIY2KnyW4L3Rgz4Zu7J6xnQ0JtOxjON1lZUGe/X1u7jrDzJM3hLKT65HOtpztENDBSFMyYU6k2eBVlMoObjFoczUk3sNh3rcZEnWjaYkXDSmWMrlqaIDTkSYHZOcOGWLHEt+QEdbNSavr4s+Vw3ZpanRtmXSAEyJqkexE9Xa3iyXwZXRgr7ErYHtt8bWXSuteR8MtgMa8fKKsGHWpy+G1q4sTvLDdjuuqeU+QbfHbe+eDElJRqff43hUCCl87DYeU9RW2XhqZWiHuyJuIp0beIJi+VG/XMsRLbRErWmuMxtFPq+49pZAKntXXVOV5Vib7pnQ1Dtr3xRi3vCstz5jx8OyFgVJDRVtZ+kELKOhRSaIcPHVwZf2pshJFC5qRc/fICO67QbFEW1dtiEcFkk9zAcr8894d79bVaUlHqeyG2aCq4KQjrhwRziq24z0amVwVR/1cb6GSA+ExlrLueoYFzcrrhFV7oOgDASYnkAXrsldZ2ElMwW4cLzEJ/5q2U0EOhjoyJ1YSkyRVD2VjNMeGs/a7GzbFGhxy53V0UymxtkIMomISdEUgmjC+iAX2nIvkS3isyVldba1HSV4S098pCoHv7GdRHIy5JALbKIux2MkxPvz7VZsw+uNUMqwchEnEMMJnnjPRVVbdLCWN31IEWi3Pp3DcM1eWmF1WAmyuxesgxgzIbQTN4TGpiqkNabQbszsZtA6yo72UnYdrGrqlB+tbIlcJMc9BYVjoiNEdXaaGHJt7VJCCNV4k5FicqCRcTfV3MZKK2ZTqUhe8ps8hYcA5W+Tj+YNHASMAt1zLUeT8oSgBtNBFW76W9Cx7gqVnyTFFlzT85LdIFRjm3ZDuFSvVcKVVNyiSgfXbjkUaKrI5aAUUxUfsZMI+HhJX5ptalXhEJPOUpaL/elQsa7UR0zZMQEqXW2zrDzRa/lWj/TB9WvL2iiRw01SGHUoo+2UFRk2J86NBR+AHX/TOeOEdzyyQYzdduP24kpl9wXeQ+rkwdj1anVb3mqy/jJF1QViPYbQ0bAzbpuNXKHr+xlk1v58kWBkT0UDszbL3cVY7lb9iV4ih11puCd7aSxppElsQxi1dLXfFGNRX8JChHVeDrXCCgWh4/f8CLkdRAWw4tTKDgD3RiDcnDtFUk+1slCeLpzJxscNHHK7RFBxVt6bW9B3AHJvutSmOR5XMyeCbvD24G9ofXvC18GF355qd6/U060YoB6JSaPEKv2M1Rlp1sf7BdO3ox+btAR6WsScPI09rZRKWA2RuB5F7KrvqwbOEm/qQcDa8zW93fA6mUyHut2kKEoUze1vGnSkUfjkG6BPjSOXNFW286kzNtEtA4cIWYp3vtoF085uzFCJN3aCnBJhVPKbwYXJsdgdGRbl0utqc/P3yMnxXLgWUzKMBPLiR8KF3q0QRxF2DFXsdfZ+F1SkO9khtrzdt6shvppX1YLgk3V0E5/CTzWv1fJBXfFjKO3O2igk3W27r9xSOpowXLOEQaorRTwPKwfzIRJ0ysWFGKZRwkWaMbQoOO6NtduF7TCt1gdk4tc6ExXeSDPePYcNnbwQ7SGLMlSk5I7pLLCtvOobgiouiEnhGwlrnUYh0bUEnUFA0gzLZRQmIb7A8+UhVqiOFCN1g8hZAsQX2glW/ElnqCOxM0ICd7SV6oQhaMCFLttDbqGG10PAWAXXbg2WIt2Ai2zB4lUvW4Wq6zn4VkCKyYWJFQ4FOt1Yx2jdk1HYtROlHRmcFjgHPRen/n6x7Z6lNPOmFMDihLOiYocv+X1u3UgLsuCDoxoOB4G+FgKVh4j6KrghGhu6t8izUV0K7oO4zkZmVSYHCjO2zfUSYgflCnVcCYvUQFvJeYTzu3cIlw2/knxQbB1ykx0Nk9rYOaNrM3XXFBv1HOFOrNFXarrBCQDmfqR0sVyw+Bm3VCK5pbbST1zc7QnWNvWBGTFpGrCgR+0IcRWlghwy8rn6inHV1qN5SA2qHcaG5eEKL7c7nN9z4apgYbCF3/jrg7LRjiWM7tH2hLDHyFqzgdazvUd0UiatFTLBa/faHdajlDcb/riLHMI8tn1/uaZYIEi3HanwlkMyV/XaZEcB5ts2IO8oRPIBxJ5j65o5W3zp9Jg5KD2HlA0N5bHchGgXOjHLbzpcXFd3kc1HQmzIW6yA9irDBAYqTsOxPzsmcjJWJarTDqcLyzFcbppk7Bwov5mofr1btkI4rH1X7mjKjZO7VRCYry1drhwn31q9lx5schwJ7sxtwfpCR0Iwce62ooefLdlMJyNU6es1UCEz773WdzPX0HxTlm++Uq5ynduXjZvczi4OF0wOWlBNRFGHuNuKlpGjg3X76LaipLjwPP3ME6RXSiblQdeoXQoRIxcrLtmAIjNGbLk/oU7TH27SUoxNZqyck2/p5unMKNfm4l26GgB0rrN2Y+HsOSJCqkTu8i0LmqEKSAHwX47F14SiRic2liK5VtMx0pAxqUPNgsOGTvysJ5QtXN1kUb3BN44lSOfU13EctaZ2A7x4XNGseBAa93I+hj0dqGK3NgGHeOTx1ApYekOWCQOyRGp6xz/pZakbKHVB8x4tZL7vls4eH5ejDPb52pC4aGPkm2h9dPUK6nYjDSnOkbnbZbMnVyMqaS6O4FnO52h/VG+lhy27BI+YrKzbe6PRZnE93y+8PMqU6OwPJXc5wxKR6biv3u52Zh+oCgBA1nUhcZXrqL5H/fmUanROSclqYHFvcNpRX0Ut7WFUelkpJt/k0dAzAYMh9V1DDgrJuCu8RjpwlwV1IaKYwoJ93OE6SC1yEhpFXavTBfNj0vJv52nE7t5A7yh15UE4anrhsBd4CA5W4nioKuEm+9vLOKUSUZu2rkIIVos1v2F9jC75CWSTf/BsF62rXqkuPRrDGHpH5fMJdoQjuR7WrYvg2t3nrezqewjBusvOR9Kj2y79deHbJLXJchtGqDPlV+MBNaMDYLsd32rr8mCkFxklHF4xJrT1hdM5GKQg8a1N1m9OhJkWPpWuRwO9pCdTtku4Nh2SV5TSliGRJDQkdNoVHpQF3527Gh3xhHev8abV9/GxZs4S1SjEoeMw9SaXZAUHXodYJwjF8VC7DJLNHCbDzVku95kuZlx+3XF6tSNP7hRdLSJY8cyJuxzOkm50Hpc6ZWo2l4jQR3wUj+OVzXpTqLFKAVukpunaoW22l4PFpT6ilaSSQFncWRmZeZCjbottpnWai9KCUFnNBjkjNI9UdyqjG2WcrqfA8RnrFKDQuhyC8dJyq11Qpoa/3+ptbudNvIR7bUrWbHMbmmMZlXy8Mk2vTQ2uc6YVXNlKd65zh0jPeqOEtdlaOJh03Nr3sWKIybrzgdrcaCggDLG/r7aHpXaqM7/o7TNTdWR/3E46JhV4Kd8qG2q9Cc2CW6bhe9+sWQtOyTxkqtWRsdj1OtndcMkePfWgZmMNNhVd5AcJwJTcy66eNhLrpr+0AIvJDl936jU1lqFcEC10JO3W5nOxz5fodswpJXNyf6VxGneRVtq+MEATY2ihvdpgtUOtISSomDsD1Vu5rkR/c6pwDL7dGgIh4G5ldGJnZuv26MmmUpo0hrVVF1xxtFjts+iAHaYbopxhxhjF6raXPMvn7ERnQQ56WwIp71DK9kOMuOyax8NThq5Tfm+v8HN37UNq0kX+NGwjAJs3G19h/uWgtF5uoEyNjREcYTTttCkr0FLjwcOOco9DNpw2EYLJZm6Iqw7NciPBuOxMprLBazqyHPPj9uL1rR/y1EURNefOno5W0W+os3Puo5QNTGVUAp/w2Qq2+apWSK3fnaHbtTm2UD6ZS0SJmXqtDI7bb1GtW9Iauh/2llKLBXpt0xWRnOnxbFzasXT20CRx6364ijyN+AO5tLsTQWX1iTkOd4Qt/DOCrWr33iDDemQgDrNXNytosNziIcjS3WOTXRzNR7KrU7UenfctlEqXfWaMrioEtlHo9G7bTpWHZNmmEgQpr8LbtEPPYjl46L6rK1/xBOaejvzRz4KtzSjRUb/EBdHxrXosxd2qUu77dXrzzxxv5tStLdIhgnAPQgTq4odjX6c5eiguFCWQfKp1Ba/DY9d705LJEj4xI7Z3dWlXWWWhwaK2HeALWtepAx1RdJBculMV3g3qtdXFeyXK8ok4n7keSnH7BnnN0fKoSE1Mqup5lVyy5HiAdwyTzMcjf/vb24e3347g3v6rV8PmA5n/Z+dCzyOcr2+FPI4Ufdv79Fjr03+pyd8/vNVuDPR4nnQ1aRe+Doj+dM718S8OB+dJ0/Pdqq9Hwc9D7tYO5xeL3+Lc65q2nr40Rfp4AwTMcLpmfiexmV9bdcH3709An+uAiyiu/S9t8aX2W3D1Nr8tOL/U4Xux3X79Gb6O+j68ea/Xjb6gBP7Fr8vZstd7BMAg9B1+R9/+8X8Bahe2ivgtAAA= -->
