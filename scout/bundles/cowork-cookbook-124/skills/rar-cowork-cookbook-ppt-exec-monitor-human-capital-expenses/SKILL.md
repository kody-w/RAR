---
name: "rar-cowork-cookbook-ppt-exec-monitor-human-capital-expenses"
description: "Builds a read-only executive PowerPoint deck on human capital expenses from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_human_capital_expenses", "rar_sha256": "2fcaed209d17ec80f738a3a220822f77157f8596a95155798557b31f7598011f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_monitor_human_capital_expenses`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_monitor_human_capital_expenses_agent.py` and in the RCI capsule.

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

Monitor human capital expenses Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on human capital expenses from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-human-capital-expenses
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
      "description": "D365 legal entity to report on, e.g. USMF.",
      "type": "string"
    },
    "meeting_length": {
      "description": "Length of the review the deck must fit, e.g. 15 minutes.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-monitor-human-capital-expenses-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and cadence for the review, e.g. monthly with prior-period comparison.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_monitor_human_capital_expenses_agent.py` and embedded as the fenced Python below (sha256 2fcaed209d17ec80…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_monitor_human_capital_expenses_agent.py` first:

```bash
python3 ppt_exec_monitor_human_capital_expenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_monitor_human_capital_expenses_agent.py   # or on stdin
python3 ppt_exec_monitor_human_capital_expenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor human capital expenses Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on human capital expenses from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-human-capital-expenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_monitor_human_capital_expenses',
    "version": '3.0.3',
    "display_name": 'Monitor human capital expenses Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on human capital expenses from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-monitor-human-capital-expenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-monitor-human-capital-expenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b30cd688fc18a307',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/monitor-human-capital-expenses'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/ppt-exec-monitor-human-capital-expenses', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'meeting_length': 'Length of the review the deck must fit, e.g. 15 minutes.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-monitor-human-capital-expenses-2026-05-24.pptx.', 'review_period': 'Reporting period and cadence for the review, e.g. monthly with prior-period comparison.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for monitor human capital expenses reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on monitor human capital expenses for a 15-minute monthly review. Produce 'ppt-exec-monitor-human-capital-expenses-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads monitor human capital expenses data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on human capital expenses from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build the monthly human capital expense exec deck for USMF from D365 — 15-minute review, with speaker notes.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-monitor-human-capital-expenses-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and cadence for the review, e.g. monthly with prior-period comparison.', 'name': 'review_period'}, {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'name': 'meeting_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready human capital expense deck for a short monthly review, sourced from D365 F&SCM without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecMonitorHumanCapitalExpenses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMonitorHumanCapitalExpenses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'meeting_length': {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-monitor-human-capital-expenses-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and cadence for the review, e.g. monthly with prior-period comparison.', 'type': 'string'}},
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
    print(PptExecMonitorHumanCapitalExpenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
