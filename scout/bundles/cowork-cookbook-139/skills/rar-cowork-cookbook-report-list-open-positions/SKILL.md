---
name: "rar-cowork-cookbook-report-list-open-positions"
description: "Builds a read-only summary report of open positions from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_list_open_positions", "rar_sha256": "3ff6d7d1f14edc697b5a239776e9b0a63fa4ac4c970eefe7ec86ac1cf75205d6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_list_open_positions`. The original RAPP
agent is preserved byte-for-byte in `report_list_open_positions_agent.py` and in the RCI capsule.

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

List open positions Summary Report — Builds a read-only summary report of open positions from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-list-open-positions
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
      "description": "Excel workbook filename, e.g. report-list-open-positions-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_list_open_positions_agent.py` and embedded as the fenced Python below (sha256 3ff6d7d1f14edc69…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_list_open_positions_agent.py` first:

```bash
python3 report_list_open_positions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_list_open_positions_agent.py   # or on stdin
python3 report_list_open_positions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
List open positions Summary Report — Builds a read-only summary report of open positions from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-list-open-positions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_list_open_positions',
    "version": '3.0.3',
    "display_name": 'List open positions Summary Report',
    "description": 'Builds a read-only summary report of open positions from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-list-open-positions',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-list-open-positions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8b55dda5024c16cb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/list-open-positions'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-list-open-positions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Excel workbook filename, e.g. report-list-open-positions-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where list open positions stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of list open positions for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-list-open-positions-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads list open positions records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of open positions from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build an open positions summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Excel workbook filename, e.g. report-list-open-positions-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an open-positions summary report from D365 ERP with totals, by-dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportListOpenPositions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportListOpenPositions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook filename, e.g. report-list-open-positions-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportListOpenPositions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
