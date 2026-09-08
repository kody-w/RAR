---
name: "rar-cowork-cookbook-adaptive-card-develop-spend-strategy"
description: "Generates a read-only Adaptive Card JSON file summarizing develop spend strategy status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_spend_strategy", "rar_sha256": "7dd31da628bb2c34cdd0d9005f296bd8eb1134b40b1ed71362b9e777df88783d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_spend_strategy`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_spend_strategy_agent.py` and in the RCI capsule.

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

Develop spend strategy Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing develop spend strategy status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-spend-strategy
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
      "description": "How many KPI tiles to include (3-5).",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-spend-strategy-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_spend_strategy_agent.py` and embedded as the fenced Python below (sha256 7dd31da628bb2c34…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_spend_strategy_agent.py` first:

```bash
python3 adaptive_card_develop_spend_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_spend_strategy_agent.py   # or on stdin
python3 adaptive_card_develop_spend_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop spend strategy Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing develop spend strategy status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-spend-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_spend_strategy',
    "version": '3.0.2',
    "display_name": 'Develop spend strategy Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing develop spend strategy status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-develop-spend-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-spend-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f1d9935fb7286fd5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/develop-spend-strategy'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/adaptive-card-develop-spend-strategy', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'as_of_date': 'Snapshot date used in the card timestamp and output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-spend-strategy-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical develop spend strategy status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-develop-spend-strategy-2026-05-24-card.json' that visualizes the current state of develop spend strategy. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current develop spend strategy KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing develop spend strategy status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card JSON showing develop spend strategy status for USMF as of 2026-05-24.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Snapshot date used in the card timestamp and output filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-spend-strategy-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of develop spend strategy status pulled from Dynamics 365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDevelopSpendStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopSpendStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Snapshot date used in the card timestamp and output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-spend-strategy-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardDevelopSpendStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
