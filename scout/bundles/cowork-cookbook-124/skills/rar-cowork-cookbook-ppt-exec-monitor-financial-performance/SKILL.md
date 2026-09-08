---
name: "rar-cowork-cookbook-ppt-exec-monitor-financial-performance"
description: "Builds a read-only executive PowerPoint deck on financial performance from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_financial_performance", "rar_sha256": "98bf10b19af30517b23002069df077fde5475d829c00be43d8971fab55010ec4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_monitor_financial_performance`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_monitor_financial_performance_agent.py` and in the RCI capsule.

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

Monitor financial performance Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on financial performance from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-financial-performance
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
      "description": "D365 legal entity to report on (e.g. USMF).",
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
      "description": "Target .pptx filename, e.g. ppt-exec-monitor-financial-performance-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period to compare against for the trend chart.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_monitor_financial_performance_agent.py` and embedded as the fenced Python below (sha256 98bf10b19af30517…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_monitor_financial_performance_agent.py` first:

```bash
python3 ppt_exec_monitor_financial_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_monitor_financial_performance_agent.py   # or on stdin
python3 ppt_exec_monitor_financial_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor financial performance Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on financial performance from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-financial-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_monitor_financial_performance',
    "version": '3.0.3',
    "display_name": 'Monitor financial performance Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on financial performance from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-monitor-financial-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-monitor-financial-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '17cde7e709aa096e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/monitor-financial-performance'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/ppt-exec-monitor-financial-performance', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g. USMF).', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-monitor-financial-performance-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period to compare against for the trend chart.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for monitor financial performance reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on monitor financial performance for a 15-minute monthly review. Produce 'ppt-exec-monitor-financial-performance-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads monitor financial performance data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on financial performance from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': "Build an executive PowerPoint on financial performance for USMF for this month's 15-minute review.", 'inputs': [{'description': 'D365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Reporting period and prior period to compare against for the trend chart.', 'name': 'review_period'}, {'description': 'Target .pptx filename, e.g. ppt-exec-monitor-financial-performance-2026-05-24.pptx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a 15-minute monthly financial performance review deck generated from D365 ERP data without modifying any records.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecMonitorFinancialPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMonitorFinancialPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-monitor-financial-performance-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period to compare against for the trend chart.', 'type': 'string'}},
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
    print(PptExecMonitorFinancialPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
