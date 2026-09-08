---
name: "rar-cowork-cookbook-report-create-and-track-service-level-agreements"
description: "Builds a read-only summary report of service level agreement activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_create_and_track_service_level_agreements", "rar_sha256": "ec4afbb6e79fb4b34d28e6a81a34409f4f23b528133d1853f209b0b36979ca48", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_create_and_track_service_level_agreements`. The original RAPP
agent is preserved byte-for-byte in `report_create_and_track_service_level_agreements_agent.py` and in the RCI capsule.

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

Create and track service level agreements Summary Report — Builds a read-only summary report of service level agreement activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-create-and-track-service-level-agreements
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
      "description": "Dynamics 365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-create-and-track-service-level-agreements-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_create_and_track_service_level_agreements_agent.py` and embedded as the fenced Python below (sha256 ec4afbb6e79fb4b3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_create_and_track_service_level_agreements_agent.py` first:

```bash
python3 report_create_and_track_service_level_agreements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_create_and_track_service_level_agreements_agent.py   # or on stdin
python3 report_create_and_track_service_level_agreements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create and track service level agreements Summary Report — Builds a read-only summary report of service level agreement activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-create-and-track-service-level-agreements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_create_and_track_service_level_agreements',
    "version": '3.0.3',
    "display_name": 'Create and track service level agreements Summary Report',
    "description": 'Builds a read-only summary report of service level agreement activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-create-and-track-service-level-agreements',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-create-and-track-service-level-agreements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b40625ed62ab1485',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/create-and-track-service-level-agreements'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/report-create-and-track-service-level-agreements', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-create-and-track-service-level-agreements-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where create and track service level agreements stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of create and track service level agreements for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-create-and-track-service-level-agreements-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads create and track service level agreements records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of service level agreement activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': "Build an SLA summary report from D365 for USMF's latest posted period as an Excel file with Summary, Detail, and Top10 sheets.", 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-create-and-track-service-level-agreements-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write SLA activity summary from Dynamics 365 ERP with totals, dimension breakdowns, and a Top 10 by value list as an Excel file.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportCreateAndTrackServiceLevelAgreements(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportCreateAndTrackServiceLevelAgreements'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-create-and-track-service-level-agreements-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportCreateAndTrackServiceLevelAgreements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
