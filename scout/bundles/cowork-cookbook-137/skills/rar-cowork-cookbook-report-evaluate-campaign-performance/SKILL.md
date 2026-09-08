---
name: "rar-cowork-cookbook-report-evaluate-campaign-performance"
description: "Builds a read-only campaign performance summary from Dynamics 365 F&SCM for a legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_evaluate_campaign_performance", "rar_sha256": "ca679d3b5cbb477482e8493d5d6269cbafbc92d91cdb39f44876858b9c17b16c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
