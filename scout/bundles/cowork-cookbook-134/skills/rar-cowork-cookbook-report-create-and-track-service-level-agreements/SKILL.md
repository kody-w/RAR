---
name: "rar-cowork-cookbook-report-create-and-track-service-level-agreements"
description: "Builds a read-only summary report of service level agreement activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_create_and_track_service_level_agreements", "rar_sha256": "ec4afbb6e79fb4b34d28e6a81a34409f4f23b528133d1853f209b0b36979ca48", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
