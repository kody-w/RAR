---
name: "rar-cowork-cookbook-ppt-exec-budget-workforce"
description: "Builds a read-only executive PowerPoint deck on budget workforce status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_budget_workforce", "rar_sha256": "a96c3e8a0f04231f40d46cab81dc1d9ec5c65d3a8bff296a86bb26443b829745", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
