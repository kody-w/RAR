---
name: "rar-cowork-cookbook-report-request-travel"
description: "Builds a read-only summary report of travel requests from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_request_travel", "rar_sha256": "881419c80e4a6c07e326aaea59e70893bf0b9275e8c4e8f2b28484c3931815cd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
