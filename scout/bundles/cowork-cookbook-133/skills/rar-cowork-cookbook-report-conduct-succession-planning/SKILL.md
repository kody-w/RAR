---
name: "rar-cowork-cookbook-report-conduct-succession-planning"
description: "Generates a read-only conduct succession planning summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_conduct_succession_planning", "rar_sha256": "1e4ad72d267248e4f29de4b3bd100a32ae075f5a768204135f3ad68567391589", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
