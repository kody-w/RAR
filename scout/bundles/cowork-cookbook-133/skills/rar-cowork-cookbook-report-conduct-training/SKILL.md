---
name: "rar-cowork-cookbook-report-conduct-training"
description: "Builds a read-only conduct training summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_conduct_training", "rar_sha256": "51f9d3e105cd378f935fa1e516ce60e24f8acc8b1837b17dd956a4a00c9adef2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_conduct_training`. The original RAPP
agent is preserved byte-for-byte in `report_conduct_training_agent.py` and in the RCI capsule.

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

Conduct training Summary Report — Builds a read-only conduct training summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-conduct-training
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
      "description": "Dimensions to break down by, such as department, category, or responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to report on (e.g. USMF).",
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
      "description": "Name of the Excel workbook to produce, e.g. report-conduct-training-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_conduct_training_agent.py` and embedded as the fenced Python below (sha256 51f9d3e105cd378f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_conduct_training_agent.py` first:

```bash
python3 report_conduct_training_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_conduct_training_agent.py   # or on stdin
python3 report_conduct_training_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct training Summary Report — Builds a read-only conduct training summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-conduct-training
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_conduct_training',
    "version": '3.0.3',
    "display_name": 'Conduct training Summary Report',
    "description": 'Builds a read-only conduct training summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-conduct-training',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-conduct-training',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e1f123c9d3a41c17',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/conduct-training'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-conduct-training', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions to break down by, such as department, category, or responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-conduct-training-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where conduct training stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of conduct training for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-conduct-training-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads conduct training records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only conduct training summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a conduct training summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions to break down by, such as department, category, or responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-conduct-training-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a conduct training summary report from Dynamics 365 ERP data with totals, breakdowns, and a top-10-by-value list, without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportConductTraining(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportConductTraining'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions to break down by, such as department, category, or responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-conduct-training-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportConductTraining().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
