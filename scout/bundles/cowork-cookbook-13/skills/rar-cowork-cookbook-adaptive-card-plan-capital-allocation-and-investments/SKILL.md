---
name: "rar-cowork-cookbook-adaptive-card-plan-capital-allocation-and-investments"
description: "Generates a read-only Adaptive Card JSON file summarizing capital allocation and investment status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_plan_capital_allocation_and_investments", "rar_sha256": "83f328970c397d038613a6912b976825430c543deff0368a88ea84a4d1b35d54", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_plan_capital_allocation_and_investments`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_plan_capital_allocation_and_investments_agent.py` and in the RCI capsule.

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

Plan capital allocation and investments Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing capital allocation and investment status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-plan-capital-allocation-and-investments
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
    "action_buttons": {
      "description": "The 2-3 action buttons and their target links to include on the card.",
      "type": "string"
    },
    "as_of_date": {
      "description": "Snapshot date used in the card header timestamp and output filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_selection": {
      "description": "Which 3-5 capital allocation KPIs to show as tiles with trend arrows.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on (recipe default: USMF).",
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
      "description": "Name of the generated Adaptive Card JSON file.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_plan_capital_allocation_and_investments_agent.py` and embedded as the fenced Python below (sha256 83f328970c397d03…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_plan_capital_allocation_and_investments_agent.py` first:

```bash
python3 adaptive_card_plan_capital_allocation_and_investments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_plan_capital_allocation_and_investments_agent.py   # or on stdin
python3 adaptive_card_plan_capital_allocation_and_investments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan capital allocation and investments Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing capital allocation and investment status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-plan-capital-allocation-and-investments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_plan_capital_allocation_and_investments',
    "version": '3.0.2',
    "display_name": 'Plan capital allocation and investments Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing capital allocation and investment status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-plan-capital-allocation-and-investments',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-plan-capital-allocation-and-investments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ba368a911a1a4acd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/plan-capital-allocation-and-investments'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/adaptive-card-plan-capital-allocation-and-investments', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons and their target links to include on the card.', 'as_of_date': 'Snapshot date used in the card header timestamp and output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_selection': 'Which 3-5 capital allocation KPIs to show as tiles with trend arrows.', 'legal_entity': 'D365 legal entity to report on (recipe default: USMF).', 'output_filename': 'Name of the generated Adaptive Card JSON file.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical plan capital allocation and investments status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-plan-capital-allocation-and-investments-2026-05-24-card.json' that visualizes the current state of plan capital allocation and investments. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current plan capital allocation and investments KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing capital allocation and investment status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing our capital allocation and investment status in USMF for Teams.', 'inputs': [{'description': 'D365 legal entity to report on (recipe default: USMF).', 'name': 'legal_entity'}, {'description': 'Snapshot date used in the card header timestamp and output filename.', 'name': 'as_of_date'}, {'description': 'Name of the generated Adaptive Card JSON file.', 'name': 'output_filename'}, {'description': 'Which 3-5 capital allocation KPIs to show as tiles with trend arrows.', 'name': 'kpi_selection'}, {'description': 'The 2-3 action buttons and their target links to include on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an embeddable Adaptive Card snapshot of capital allocation and investment status for Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardPlanCapitalAllocationAndInvestments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardPlanCapitalAllocationAndInvestments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons and their target links to include on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Snapshot date used in the card header timestamp and output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_selection': {'description': 'Which 3-5 capital allocation KPIs to show as tiles with trend arrows.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (recipe default: USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the generated Adaptive Card JSON file.', 'type': 'string'}},
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
    print(AdaptiveCardPlanCapitalAllocationAndInvestments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
