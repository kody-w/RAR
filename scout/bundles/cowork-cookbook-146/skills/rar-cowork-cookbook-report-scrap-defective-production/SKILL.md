---
name: "rar-cowork-cookbook-report-scrap-defective-production"
description: "Builds a read-only scrap defective production summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_scrap_defective_production", "rar_sha256": "917fd92fbb832b5fe2532db4ded79c420dc78573396edaca3c149db650ca3b79", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
