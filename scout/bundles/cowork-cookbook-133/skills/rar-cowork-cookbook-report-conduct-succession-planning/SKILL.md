---
name: "rar-cowork-cookbook-report-conduct-succession-planning"
description: "Generates a read-only conduct succession planning summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_conduct_succession_planning", "rar_sha256": "1e4ad72d267248e4f29de4b3bd100a32ae075f5a768204135f3ad68567391589", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_conduct_succession_planning`. The original RAPP
agent is preserved byte-for-byte in `report_conduct_succession_planning_agent.py` and in the RCI capsule.

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

Conduct succession planning Summary Report — Generates a read-only conduct succession planning summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-conduct-succession-planning
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
      "description": "Name of the Excel workbook to produce, e.g. report-conduct-succession-planning-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_conduct_succession_planning_agent.py` and embedded as the fenced Python below (sha256 1e4ad72d267248e4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_conduct_succession_planning_agent.py` first:

```bash
python3 report_conduct_succession_planning_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_conduct_succession_planning_agent.py   # or on stdin
python3 report_conduct_succession_planning_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct succession planning Summary Report — Generates a read-only conduct succession planning summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-conduct-succession-planning
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_conduct_succession_planning',
    "version": '3.0.3',
    "display_name": 'Conduct succession planning Summary Report',
    "description": 'Generates a read-only conduct succession planning summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-conduct-succession-planning',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-conduct-succession-planning',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1da977895b7c63c0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/offboard-talent/conduct-succession-planning'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-conduct-succession-planning', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-conduct-succession-planning-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where conduct succession planning stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of conduct succession planning for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-conduct-succession-planning-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads conduct succession planning records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only conduct succession planning summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a conduct succession planning summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-conduct-succession-planning-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only succession planning summary with totals, by-dimension breakdowns, and a Top 10 by value list exported to Excel.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportConductSuccessionPlanning(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportConductSuccessionPlanning'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-conduct-succession-planning-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportConductSuccessionPlanning().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
