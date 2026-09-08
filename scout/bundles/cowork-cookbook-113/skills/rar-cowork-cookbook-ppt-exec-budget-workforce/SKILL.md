---
name: "rar-cowork-cookbook-ppt-exec-budget-workforce"
description: "Builds a read-only executive PowerPoint deck on budget workforce status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_budget_workforce", "rar_sha256": "a96c3e8a0f04231f40d46cab81dc1d9ec5c65d3a8bff296a86bb26443b829745", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_budget_workforce`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_budget_workforce_agent.py` and in the RCI capsule.

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

Budget workforce Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on budget workforce status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-budget-workforce
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-budget-workforce-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend chart, e.g. monthly review as of 2026-05-24.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_budget_workforce_agent.py` and embedded as the fenced Python below (sha256 a96c3e8a0f04231f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_budget_workforce_agent.py` first:

```bash
python3 ppt_exec_budget_workforce_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_budget_workforce_agent.py   # or on stdin
python3 ppt_exec_budget_workforce_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Budget workforce Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on budget workforce status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-budget-workforce
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_budget_workforce',
    "version": '3.0.3',
    "display_name": 'Budget workforce Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on budget workforce status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-budget-workforce',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-budget-workforce',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'da6d1e7fa0df9097',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/budget-workforce'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/ppt-exec-budget-workforce', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'meeting_length': 'Length of the review the deck must fit, e.g. 15 minutes.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-budget-workforce-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend chart, e.g. monthly review as of 2026-05-24.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for budget workforce reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on budget workforce for a 15-minute monthly review. Produce 'ppt-exec-budget-workforce-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads budget workforce data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on budget workforce status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': "Build the executive budget workforce PowerPoint deck from D365 USMF for this month's 15-minute review.", 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-budget-workforce-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend chart, e.g. monthly review as of 2026-05-24.', 'name': 'review_period'}, {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'name': 'meeting_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready budget workforce deck for a short monthly review, sourced from D365 F&SCM without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecBudgetWorkforce(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecBudgetWorkforce'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'meeting_length': {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-budget-workforce-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend chart, e.g. monthly review as of 2026-05-24.', 'type': 'string'}},
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
    print(PptExecBudgetWorkforce().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
