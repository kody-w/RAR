---
name: "rar-cowork-cookbook-report-furlough-workers"
description: "Builds a read-only furlough workers summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_furlough_workers", "rar_sha256": "f0369a257c04ef1ad4789b36fb12fcadf3d54c8dbab1ef281824339b07016407", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1: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 -->
