---
name: "rar-cowork-cookbook-report-scrap-defective-production"
description: "Builds a read-only scrap defective production summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_scrap_defective_production", "rar_sha256": "917fd92fbb832b5fe2532db4ded79c420dc78573396edaca3c149db650ca3b79", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_scrap_defective_production`. The original RAPP
agent is preserved byte-for-byte in `report_scrap_defective_production_agent.py` and in the RCI capsule.

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

Scrap defective production Summary Report — Builds a read-only scrap defective production summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-scrap-defective-production
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
      "description": "Excel workbook name, e.g. report-scrap-defective-production-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_scrap_defective_production_agent.py` and embedded as the fenced Python below (sha256 917fd92fbb832b5f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_scrap_defective_production_agent.py` first:

```bash
python3 report_scrap_defective_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_scrap_defective_production_agent.py   # or on stdin
python3 report_scrap_defective_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Scrap defective production Summary Report — Builds a read-only scrap defective production summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-scrap-defective-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_scrap_defective_production',
    "version": '3.0.3',
    "display_name": 'Scrap defective production Summary Report',
    "description": 'Builds a read-only scrap defective production summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-scrap-defective-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-scrap-defective-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bb131e8cecb7a40b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/scrap-defective-production'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/report-scrap-defective-production', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Excel workbook name, e.g. report-scrap-defective-production-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where scrap defective production stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of scrap defective production for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-scrap-defective-production-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads scrap defective production records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only scrap defective production summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a scrap defective production summary for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'name': 'breakdown_dimensions'}, {'description': 'Excel workbook name, e.g. report-scrap-defective-production-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a scrap/defective production summary with totals, dimension breakdowns, and a top-10-by-value list exported to Excel from D365 ERP.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportScrapDefectiveProduction(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportScrapDefectiveProduction'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. report-scrap-defective-production-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportScrapDefectiveProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
