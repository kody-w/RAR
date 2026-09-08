---
name: "rar-cowork-cookbook-adaptive-card-load-goods-for-shipping"
description: "Generates a read-only Adaptive Card JSON file visualizing load goods for shipping status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_load_goods_for_shipping", "rar_sha256": "2bcd64512ca64617c223255529ba7394a02163679d79d8d7090222f83becf2dc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_load_goods_for_shipping`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_load_goods_for_shipping_agent.py` and in the RCI capsule.

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

Load goods for shipping Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing load goods for shipping status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-load-goods-for-shipping
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
      "description": "Which 2-3 action buttons the card should offer.",
      "type": "string"
    },
    "as_of_date": {
      "description": "Date used for the card timestamp and output filename.",
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
      "description": "Name of the Adaptive Card JSON file to produce.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_load_goods_for_shipping_agent.py` and embedded as the fenced Python below (sha256 2bcd64512ca64617…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_load_goods_for_shipping_agent.py` first:

```bash
python3 adaptive_card_load_goods_for_shipping_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_load_goods_for_shipping_agent.py   # or on stdin
python3 adaptive_card_load_goods_for_shipping_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Load goods for shipping Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing load goods for shipping status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-load-goods-for-shipping
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_load_goods_for_shipping',
    "version": '3.0.2',
    "display_name": 'Load goods for shipping Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing load goods for shipping status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-load-goods-for-shipping',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-load-goods-for-shipping',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7765f4457b7d2e66',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/load-goods-for-shipping'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/adaptive-card-load-goods-for-shipping', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'Which 2-3 action buttons the card should offer.', 'as_of_date': 'Date used for the card timestamp and output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical load goods for shipping status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-load-goods-for-shipping-2026-05-24-card.json' that visualizes the current state of load goods for shipping. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current load goods for shipping KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing load goods for shipping status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of load goods for shipping status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date used for the card timestamp and output filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'Which 2-3 action buttons the card should offer.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of D365 load goods for shipping status to embed in Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardLoadGoodsForShipping(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardLoadGoodsForShipping'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'Which 2-3 action buttons the card should offer.', 'type': 'string'}, 'as_of_date': {'description': 'Date used for the card timestamp and output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce.', 'type': 'string'}},
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
    print(AdaptiveCardLoadGoodsForShipping().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
