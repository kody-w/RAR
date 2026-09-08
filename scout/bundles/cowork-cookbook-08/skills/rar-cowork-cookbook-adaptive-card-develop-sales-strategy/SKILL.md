---
name: "rar-cowork-cookbook-adaptive-card-develop-sales-strategy"
description: "Generates a read-only Adaptive Card JSON file summarizing develop sales strategy status from Dynamics 365 ERP for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_sales_strategy", "rar_sha256": "c97a63c552ba8ec888862cb16f6badc5444f58d2fda88f19a3342aaf01b4f965", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
