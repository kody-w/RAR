---
name: "rar-cowork-cookbook-ppt-exec-report-on-production-sustainability-metrics"
description: "Builds a read-only executive PowerPoint deck on production sustainability metrics from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_report_on_production_sustainability_metrics", "rar_sha256": "f13d5f88829ca98355b539cd2e39748dc11f07c4ccde89b94611a2178b76d65f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
