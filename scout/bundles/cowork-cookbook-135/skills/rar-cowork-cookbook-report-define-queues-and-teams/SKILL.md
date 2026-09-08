---
name: "rar-cowork-cookbook-report-define-queues-and-teams"
description: "Generates a read-only summary report of queues and teams activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_queues_and_teams", "rar_sha256": "c19ad6a4191396a8b0da1c1d958b1c775de7cfb16ca6de57d516d6fc13d03551", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_queues_and_teams`. The original RAPP
agent is preserved byte-for-byte in `report_define_queues_and_teams_agent.py` and in the RCI capsule.

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

Define queues and teams Summary Report — Generates a read-only summary report of queues and teams activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-queues-and-teams
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
      "description": "Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to report against, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-define-queues-and-teams-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to cover; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_queues_and_teams_agent.py` and embedded as the fenced Python below (sha256 c19ad6a4191396a8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_queues_and_teams_agent.py` first:

```bash
python3 report_define_queues_and_teams_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_queues_and_teams_agent.py   # or on stdin
python3 report_define_queues_and_teams_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define queues and teams Summary Report — Generates a read-only summary report of queues and teams activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-queues-and-teams
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_queues_and_teams',
    "version": '3.0.3',
    "display_name": 'Define queues and teams Summary Report',
    "description": 'Generates a read-only summary report of queues and teams activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-define-queues-and-teams',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-queues-and-teams',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7544ec186fab0c0d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-queues-and-teams'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/report-define-queues-and-teams', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-define-queues-and-teams-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where define queues and teams stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of define queues and teams for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-define-queues-and-teams-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define queues and teams records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only summary report of queues and teams activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': "Build a queues and teams summary report for USMF's latest posted period as an Excel workbook with a Top 10 sheet.", 'inputs': [{'description': 'Dynamics 365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available in the tenant.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-define-queues-and-teams-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-modify Dynamics 365 ERP summary report of queues and teams with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDefineQueuesAndTeams(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineQueuesAndTeams'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-define-queues-and-teams-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportDefineQueuesAndTeams().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
