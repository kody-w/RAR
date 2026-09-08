---
name: "rar-cowork-cookbook-report-conduct-training"
description: "Builds a read-only conduct training summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_conduct_training", "rar_sha256": "51f9d3e105cd378f935fa1e516ce60e24f8acc8b1837b17dd956a4a00c9adef2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
