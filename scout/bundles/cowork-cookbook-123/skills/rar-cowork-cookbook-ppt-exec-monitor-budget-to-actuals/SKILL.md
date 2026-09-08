---
name: "rar-cowork-cookbook-ppt-exec-monitor-budget-to-actuals"
description: "Builds a read-only executive PowerPoint deck on budget-to-actuals from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_budget_to_actuals", "rar_sha256": "3b0f3c9fa8759b5367cf369d12e7750fc64d53f19ba35971c9c9c4f69854b4dc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
