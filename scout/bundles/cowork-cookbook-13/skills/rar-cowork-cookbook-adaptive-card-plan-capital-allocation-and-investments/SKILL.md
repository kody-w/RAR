---
name: "rar-cowork-cookbook-adaptive-card-plan-capital-allocation-and-investments"
description: "Generates a read-only Adaptive Card JSON file summarizing capital allocation and investment status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_plan_capital_allocation_and_investments", "rar_sha256": "83f328970c397d038613a6912b976825430c543deff0368a88ea84a4d1b35d54", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
