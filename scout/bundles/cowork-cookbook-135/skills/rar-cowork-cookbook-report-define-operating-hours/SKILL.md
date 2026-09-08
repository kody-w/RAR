---
name: "rar-cowork-cookbook-report-define-operating-hours"
description: "Builds a read-only Excel summary report of define operating hours activity from Dynamics 365 F&SCM for a given legal entity and posted period, with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_operating_hours", "rar_sha256": "b0dad0a90a57e0be2c6f0e6bfc621263ac00f14320dc5975426ece8e6091e433", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_operating_hours`. The original RAPP
agent is preserved byte-for-byte in `report_define_operating_hours_agent.py` and in the RCI capsule.

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

Define operating hours Summary Report — Builds a read-only Excel summary report of define operating hours activity from Dynamics 365 F&SCM for a given legal entity and posted period, with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-operating-hours
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
      "description": "Excel workbook name, e.g. report-define-operating-hours-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to summarize; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_operating_hours_agent.py` and embedded as the fenced Python below (sha256 b0dad0a90a57e0be…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_operating_hours_agent.py` first:

```bash
python3 report_define_operating_hours_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_operating_hours_agent.py   # or on stdin
python3 report_define_operating_hours_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define operating hours Summary Report — Builds a read-only Excel summary report of define operating hours activity from Dynamics 365 F&SCM for a given legal entity and posted period, with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-operating-hours
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_operating_hours',
    "version": '3.0.3',
    "display_name": 'Define operating hours Summary Report',
    "description": 'Builds a read-only Excel summary report of define operating hours activity from Dynamics 365 F&SCM for a given legal entity and posted period, with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-define-operating-hours',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-operating-hours',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '31f97c942743f266',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-operating-hours'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/report-define-operating-hours', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Excel workbook name, e.g. report-define-operating-hours-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where define operating hours stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of define operating hours for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-define-operating-hours-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define operating hours records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only Excel summary report of define operating hours activity from Dynamics 365 F&SCM for a given legal entity and posted period, with Summary, Detail, and Top10 sheets.', 'example_request': "Build a define operating hours summary report for USMF's latest posted period as an Excel workbook with Summary, Detail, and Top10 sheets.", 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Excel workbook name, e.g. report-define-operating-hours-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write D365 ERP summary report of define operating hours with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDefineOperatingHours(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineOperatingHours'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. report-define-operating-hours-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportDefineOperatingHours().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
