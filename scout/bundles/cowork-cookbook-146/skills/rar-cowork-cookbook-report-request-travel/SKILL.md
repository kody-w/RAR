---
name: "rar-cowork-cookbook-report-request-travel"
description: "Builds a read-only summary report of travel requests from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_request_travel", "rar_sha256": "881419c80e4a6c07e326aaea59e70893bf0b9275e8c4e8f2b28484c3931815cd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_request_travel`. The original RAPP
agent is preserved byte-for-byte in `report_request_travel_agent.py` and in the RCI capsule.

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

Request travel Summary Report — Builds a read-only summary report of travel requests from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-request-travel
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
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Excel workbook filename, e.g. report-request-travel-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_request_travel_agent.py` and embedded as the fenced Python below (sha256 881419c80e4a6c07…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_request_travel_agent.py` first:

```bash
python3 report_request_travel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_request_travel_agent.py   # or on stdin
python3 report_request_travel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Request travel Summary Report — Builds a read-only summary report of travel requests from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-request-travel
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_request_travel',
    "version": '3.0.3',
    "display_name": 'Request travel Summary Report',
    "description": 'Builds a read-only summary report of travel requests from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-request-travel',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-request-travel',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '010f3b0506ac3857',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/request-travel'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-request-travel', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Excel workbook filename, e.g. report-request-travel-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where request travel stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of request travel for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-request-travel-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads request travel records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of travel requests from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a travel request summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Excel workbook filename, e.g. report-request-travel-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-modification travel request summary from D365 ERP with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportRequestTravel(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportRequestTravel'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook filename, e.g. report-request-travel-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportRequestTravel().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
