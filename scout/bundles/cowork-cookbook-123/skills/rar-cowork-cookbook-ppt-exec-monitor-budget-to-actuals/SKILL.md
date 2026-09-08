---
name: "rar-cowork-cookbook-ppt-exec-monitor-budget-to-actuals"
description: "Builds a read-only executive PowerPoint deck on budget-to-actuals from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_budget_to_actuals", "rar_sha256": "3b0f3c9fa8759b5367cf369d12e7750fc64d53f19ba35971c9c9c4f69854b4dc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_monitor_budget_to_actuals`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_monitor_budget_to_actuals_agent.py` and in the RCI capsule.

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

Monitor budget to actuals Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on budget-to-actuals from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-budget-to-actuals
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-monitor-budget-to-actuals-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend comparison, e.g. the current month vs prior month.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_monitor_budget_to_actuals_agent.py` and embedded as the fenced Python below (sha256 3b0f3c9fa8759b53…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_monitor_budget_to_actuals_agent.py` first:

```bash
python3 ppt_exec_monitor_budget_to_actuals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_monitor_budget_to_actuals_agent.py   # or on stdin
python3 ppt_exec_monitor_budget_to_actuals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor budget to actuals Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on budget-to-actuals from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-budget-to-actuals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_monitor_budget_to_actuals',
    "version": '3.0.3',
    "display_name": 'Monitor budget to actuals Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on budget-to-actuals from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'ppt-exec-monitor-budget-to-actuals',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-monitor-budget-to-actuals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7a038e4f9b4f5b57',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/monitor-budget-to-actuals'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-monitor-budget-to-actuals', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-monitor-budget-to-actuals-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend comparison, e.g. the current month vs prior month.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for monitor budget to actuals reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on monitor budget to actuals for a 15-minute monthly review. Produce 'ppt-exec-monitor-budget-to-actuals-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads monitor budget to actuals data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on budget-to-actuals from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': "Build the executive budget-to-actuals PowerPoint deck for USMF for this month's 15-minute review.", 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-monitor-budget-to-actuals-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend comparison, e.g. the current month vs prior month.', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a monthly 15-minute budget vs actuals review deck generated from Dynamics 365 F&SCM without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecMonitorBudgetToActuals(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMonitorBudgetToActuals'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-monitor-budget-to-actuals-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend comparison, e.g. the current month vs prior month.', 'type': 'string'}},
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
    print(PptExecMonitorBudgetToActuals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
