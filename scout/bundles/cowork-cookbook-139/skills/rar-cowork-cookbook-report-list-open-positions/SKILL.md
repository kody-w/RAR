---
name: "rar-cowork-cookbook-report-list-open-positions"
description: "Builds a read-only summary report of open positions from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_list_open_positions", "rar_sha256": "3ff6d7d1f14edc697b5a239776e9b0a63fa4ac4c970eefe7ec86ac1cf75205d6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
