---
name: "rar-cowork-cookbook-report-identify-continuous-improvement-opportunities"
description: "Builds a read-only summary report of continuous improvement opportunities from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_identify_continuous_improvement_opportunities", "rar_sha256": "b9620c1e4cd488307ade6b19701a3676c86e25b2c45f698c03f71b7f573452d3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_identify_continuous_improvement_opportunities`. The original RAPP
agent is preserved byte-for-byte in `report_identify_continuous_improvement_opportunities_agent.py` and in the RCI capsule.

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

Identify continuous improvement opportunities Summary Report — Builds a read-only summary report of continuous improvement opportunities from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-identify-continuous-improvement-opportunities
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
      "description": "D365 legal entity to report on (default USMF).",
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
      "description": "Name of the Excel workbook to produce, e.g. report-identify-continuous-improvement-opportunities-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to cover; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_identify_continuous_improvement_opportunities_agent.py` and embedded as the fenced Python below (sha256 b9620c1e4cd48830…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_identify_continuous_improvement_opportunities_agent.py` first:

```bash
python3 report_identify_continuous_improvement_opportunities_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_identify_continuous_improvement_opportunities_agent.py   # or on stdin
python3 report_identify_continuous_improvement_opportunities_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify continuous improvement opportunities Summary Report — Builds a read-only summary report of continuous improvement opportunities from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-identify-continuous-improvement-opportunities
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_identify_continuous_improvement_opportunities',
    "version": '3.0.3',
    "display_name": 'Identify continuous improvement opportunities Summary Report',
    "description": 'Builds a read-only summary report of continuous improvement opportunities from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-identify-continuous-improvement-opportunities',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-identify-continuous-improvement-opportunities',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7296d869eb565a3d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/analyze-production-operations/identify-continuous-improvement-opportunities'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/report-identify-continuous-improvement-opportunities', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (default USMF).', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-identify-continuous-improvement-opportunities-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where identify continuous improvement opportunities stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of identify continuous improvement opportunities for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-identify-continuous-improvement-opportunities-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads identify continuous improvement opportunities records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of continuous improvement opportunities from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a continuous improvement opportunities summary report from D365 USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on (default USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-identify-continuous-improvement-opportunities-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals/trends/breakdown report of continuous improvement opportunities from D365 ERP data, delivered as an Excel workbook. No data is modified.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportIdentifyContinuousImprovementOpportunities(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportIdentifyContinuousImprovementOpportunities'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-identify-continuous-improvement-opportunities-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportIdentifyContinuousImprovementOpportunities().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
