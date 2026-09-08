---
name: "rar-cowork-cookbook-ppt-exec-monitor-human-capital-expenses"
description: "Builds a read-only executive PowerPoint deck on human capital expenses from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_human_capital_expenses", "rar_sha256": "2fcaed209d17ec80f738a3a220822f77157f8596a95155798557b31f7598011f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
