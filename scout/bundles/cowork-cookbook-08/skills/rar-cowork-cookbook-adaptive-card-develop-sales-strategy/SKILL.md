---
name: "rar-cowork-cookbook-adaptive-card-develop-sales-strategy"
description: "Generates a read-only Adaptive Card JSON file summarizing develop sales strategy status from Dynamics 365 ERP for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_sales_strategy", "rar_sha256": "c97a63c552ba8ec888862cb16f6badc5444f58d2fda88f19a3342aaf01b4f965", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_sales_strategy`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_sales_strategy_agent.py` and in the RCI capsule.

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

Develop sales strategy Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing develop sales strategy status from Dynamics 365 ERP for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-sales-strategy
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
      "description": "The 2-3 action buttons to place on the card.",
      "type": "string"
    },
    "as_of_date": {
      "description": "Snapshot date used in the card timestamp and output filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_count": {
      "description": "How many KPI tiles to include (3-5), each with current value and trend arrow.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to report on (e.g. USMF).",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-sales-strategy-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_sales_strategy_agent.py` and embedded as the fenced Python below (sha256 c97a63c552ba8ec8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_sales_strategy_agent.py` first:

```bash
python3 adaptive_card_develop_sales_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_sales_strategy_agent.py   # or on stdin
python3 adaptive_card_develop_sales_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop sales strategy Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing develop sales strategy status from Dynamics 365 ERP for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-sales-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_sales_strategy',
    "version": '3.0.2',
    "display_name": 'Develop sales strategy Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing develop sales strategy status from Dynamics 365 ERP for a given legal entity, with KPI tiles, a RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-develop-sales-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-sales-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2cea04b11c968b1c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-sales-strategy'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/adaptive-card-develop-sales-strategy', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'as_of_date': 'Snapshot date used in the card timestamp and output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'legal_entity': 'D365 F&SCM legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-sales-strategy-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical develop sales strategy status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-develop-sales-strategy-2026-05-24-card.json' that visualizes the current state of develop sales strategy. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current develop sales strategy KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing develop sales strategy status from Dynamics 365 ERP for a given legal entity, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of develop sales strategy status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 F&SCM legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Snapshot date used in the card timestamp and output filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-sales-strategy-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of develop sales strategy status for Teams, Outlook, or a dashboard, without changing any D365 data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDevelopSalesStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopSalesStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Snapshot date used in the card timestamp and output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-sales-strategy-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardDevelopSalesStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
