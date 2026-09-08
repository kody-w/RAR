---
name: "rar-cowork-cookbook-adaptive-card-conduct-upsell-cross-sell-or-repeat-sale-prompt"
description: "Generates a read-only Adaptive Card JSON file visualizing upsell/cross-sell/repeat-sale prompt status from Dynamics 365 ERP, with KPI tiles, RAG row, and action buttons; call when you need an embeddable status card."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_conduct_upsell_cross_sell_or_repeat_sale_prompt", "rar_sha256": "3d9b82454db6dc6747ed7da8542277baca80f18a227eb9520bf1bedf19fd6cad", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_conduct_upsell_cross_sell_or_repeat_sale_prompt`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py` and in the RCI capsule.

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

Conduct upsell, cross sell or repeat sale prompt Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing upsell/cross-sell/repeat-sale prompt status from Dynamics 365 ERP, with KPI tiles, RAG row, and action buttons; call when you need an embeddable status card.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-conduct-upsell-cross-sell-or-repeat-sale-prompt
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
    "as_of_date": {
      "description": "Date used for the card timestamp and file name.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-...-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py` and embedded as the fenced Python below (sha256 3d9b82454db6dc67…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py` first:

```bash
python3 adaptive_card_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py   # or on stdin
python3 adaptive_card_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct upsell, cross sell or repeat sale prompt Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing upsell/cross-sell/repeat-sale prompt status from Dynamics 365 ERP, with KPI tiles, RAG row, and action buttons; call when you need an embeddable status card.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-conduct-upsell-cross-sell-or-repeat-sale-prompt
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_conduct_upsell_cross_sell_or_repeat_sale_prompt',
    "version": '3.0.2',
    "display_name": 'Conduct upsell, cross sell or repeat sale prompt Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing upsell/cross-sell/repeat-sale prompt status from Dynamics 365 ERP, with KPI tiles, RAG row, and action buttons; call when you need an embeddable status card.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-conduct-upsell-cross-sell-or-repeat-sale-prompt',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-conduct-upsell-cross-sell-or-repeat-sale-prompt',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b5e27618f25a3172',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/conduct-upsell-cross-sell-or-repeat-sale-prompt'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/adaptive-card-conduct-upsell-cross-sell-or-repeat-sale-prompt', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the card timestamp and file name.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-...-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical conduct upsell, cross sell or repeat sale prompt status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-conduct-upsell-cross-sell-or-repeat-sale-prompt-2026-05-24-card.json' that visualizes the current state of conduct upsell, cross sell or repeat sale prompt. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current conduct upsell, cross sell or repeat sale prompt KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing upsell/cross-sell/repeat-sale prompt status from Dynamics 365 ERP, with KPI tiles, RAG row, and action buttons; call when you need an embeddable status card.', 'example_request': 'Make an Adaptive Card JSON for upsell/cross-sell status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-...-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and file name.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you want a Teams/Outlook-ready Adaptive Card snapshot of upsell, cross-sell or repeat-sale prompt status from D365 F&SCM, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardConductUpsellCrossSellOrRepeatSalePrompt(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardConductUpsellCrossSellOrRepeatSalePrompt'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the card timestamp and file name.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-...-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardConductUpsellCrossSellOrRepeatSalePrompt().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
