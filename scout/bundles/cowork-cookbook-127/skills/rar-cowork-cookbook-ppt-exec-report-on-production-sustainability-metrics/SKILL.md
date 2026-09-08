---
name: "rar-cowork-cookbook-ppt-exec-report-on-production-sustainability-metrics"
description: "Builds a read-only executive PowerPoint deck on production sustainability metrics from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_report_on_production_sustainability_metrics", "rar_sha256": "f13d5f88829ca98355b539cd2e39748dc11f07c4ccde89b94611a2178b76d65f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_report_on_production_sustainability_metrics`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_report_on_production_sustainability_metrics_agent.py` and in the RCI capsule.

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

Report on production sustainability metrics Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on production sustainability metrics from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-report-on-production-sustainability-metrics
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to report on, e.g. USMF.",
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
      "description": "Target .pptx filename, e.g. ppt-exec-report-on-production-sustainability-metrics-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend comparison (monthly review cadence).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_report_on_production_sustainability_metrics_agent.py` and embedded as the fenced Python below (sha256 f13d5f88829ca983…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_report_on_production_sustainability_metrics_agent.py` first:

```bash
python3 ppt_exec_report_on_production_sustainability_metrics_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_report_on_production_sustainability_metrics_agent.py   # or on stdin
python3 ppt_exec_report_on_production_sustainability_metrics_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report on production sustainability metrics Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on production sustainability metrics from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-report-on-production-sustainability-metrics
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_report_on_production_sustainability_metrics',
    "version": '3.0.3',
    "display_name": 'Report on production sustainability metrics Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on production sustainability metrics from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-report-on-production-sustainability-metrics',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-report-on-production-sustainability-metrics',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'db9cb4ce8da1fe86',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/analyze-production-operations/report-on-production-sustainability-metrics'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/ppt-exec-report-on-production-sustainability-metrics', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-report-on-production-sustainability-metrics-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend comparison (monthly review cadence).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for report on production sustainability metrics reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on report on production sustainability metrics for a 15-minute monthly review. Produce 'ppt-exec-report-on-production-sustainability-metrics-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads report on production sustainability metrics data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on production sustainability metrics from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes.', 'example_request': "Build an executive PowerPoint on production sustainability metrics for USMF for this month's review.", 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-report-on-production-sustainability-metrics-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend comparison (monthly review cadence).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready sustainability metrics deck for a 15-minute monthly review, sourced from Dynamics 365 ERP without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecReportOnProductionSustainabilityMetrics(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecReportOnProductionSustainabilityMetrics'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-report-on-production-sustainability-metrics-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend comparison (monthly review cadence).', 'type': 'string'}},
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
    print(PptExecReportOnProductionSustainabilityMetrics().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
