---
name: "rar-cowork-cookbook-report-evaluate-campaign-performance"
description: "Builds a read-only campaign performance summary from Dynamics 365 F&SCM for a legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_evaluate_campaign_performance", "rar_sha256": "ca679d3b5cbb477482e8493d5d6269cbafbc92d91cdb39f44876858b9c17b16c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_evaluate_campaign_performance`. The original RAPP
agent is preserved byte-for-byte in `report_evaluate_campaign_performance_agent.py` and in the RCI capsule.

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

Evaluate campaign performance Summary Report — Builds a read-only campaign performance summary from Dynamics 365 F&SCM for a legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-evaluate-campaign-performance
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
      "description": "Dimensions to break out by where applicable: department, category, responsible owner.",
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
      "description": "Excel workbook filename, e.g. report-evaluate-campaign-performance-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_evaluate_campaign_performance_agent.py` and embedded as the fenced Python below (sha256 ca679d3b5cbb4774…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_evaluate_campaign_performance_agent.py` first:

```bash
python3 report_evaluate_campaign_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_evaluate_campaign_performance_agent.py   # or on stdin
python3 report_evaluate_campaign_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Evaluate campaign performance Summary Report — Builds a read-only campaign performance summary from Dynamics 365 F&SCM for a legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-evaluate-campaign-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_evaluate_campaign_performance',
    "version": '3.0.3',
    "display_name": 'Evaluate campaign performance Summary Report',
    "description": 'Builds a read-only campaign performance summary from Dynamics 365 F&SCM for a legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-evaluate-campaign-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-evaluate-campaign-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '70d69b8af96014a2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/evaluate-campaign-performance'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/report-evaluate-campaign-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions to break out by where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Excel workbook filename, e.g. report-evaluate-campaign-performance-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where evaluate campaign performance stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of evaluate campaign performance for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-evaluate-campaign-performance-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads evaluate campaign performance records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only campaign performance summary from Dynamics 365 F&SCM for a legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a campaign performance summary report for USMF from the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Excel workbook filename, e.g. report-evaluate-campaign-performance-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions to break out by where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary report of campaign performance activity from D365 ERP with totals, dimension breakdowns, and a top-10-by-value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportEvaluateCampaignPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportEvaluateCampaignPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions to break out by where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook filename, e.g. report-evaluate-campaign-performance-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportEvaluateCampaignPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
