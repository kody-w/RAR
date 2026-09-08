---
name: "rar-cowork-cookbook-adaptive-card-conduct-upsell-cross-sell-or-repeat-sale-prompt"
description: "Generates a read-only Adaptive Card JSON file visualizing upsell/cross-sell/repeat-sale prompt status from Dynamics 365 ERP, with KPI tiles, RAG row, and action buttons; call when you need an embeddable status card."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_conduct_upsell_cross_sell_or_repeat_sale_prompt", "rar_sha256": "3d9b82454db6dc6747ed7da8542277baca80f18a227eb9520bf1bedf19fd6cad", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
