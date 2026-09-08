---
name: "rar-cowork-cookbook-adaptive-card-load-goods-for-shipping"
description: "Generates a read-only Adaptive Card JSON file visualizing load goods for shipping status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_load_goods_for_shipping", "rar_sha256": "2bcd64512ca64617c223255529ba7394a02163679d79d8d7090222f83becf2dc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6abPiRrrmX2HOjRjbV1WFdoma6IgRIAkJtKANJFfHsfZ9QQtIePzfJwVU2e4u3+memC9DnVNAKvPNd32eN4/065s79Endvn1+00O3WvBuUaRJ2C7cKlhs6lvd5uCtzj3wu/Drqm9Tb+jrtnv78BaEnd+mTZ/WFVjOh1XYun3YLdxFG7rBx7oqpgUTuGDCNVxs3DZYiLoiL6K0CBfXtBvcIr2nVbwoajdYxHUddIuobhddkjbNPN71bj+AsbYuF9upcsvU7xYYSSy4/65vpMdcdxED4dWiCGO3WIRVn/bTh8Ut7ZNFAnQI2w+LvSoserBl92GhMfyirW8fHsa5/qz4AljT11X3CdgTjm7ZgIlvn3/++4e3FHx++/zrm1+4HRh6+2rJbMgBaMzPCnN1q7/UBQIKF7x9fmsm4NEKfG/CFihZgqEgjBavbz92YRF9WPznf+Y3t427nz5/qRav15e3+Z82VIs+CRd97XZ9GCx8t3G9tACWfVowxc2dOuDffmir2dMdCEgVf3qu/F1S3Sz+Nl/78bnJpzjsf/zyVjdzhIDVX95+WgDvfXlrh/nzp1lK8+NPn4r6FrY//vS7nG7wstDvZ2FA60/vr+8vsWDi71PTaPGuq+zmtVcb+mkTAuF/sG9+PVV/iXu55P05+ce6+bD4vuTZnr8BfZ8p5wG53xcLfABWvn3K6rT68bVHW4MMcSs//PGnvxLrJ6GfF2nX/0tyf34KfibYjy+X/PThEb6/L6CXbd9k/vW2DUiYf8cSMP3rdt8c9VeyH5H9B9FFWoHy/BrL74r73gLob4uf/9K2/2rBh0X05W0bFqBqWtcrws+LXx8p8vMPwe+DP/z9NyD6/yhGr4fWf0h4L90qjcKuf3//+YfuMfzD33/+YWhAFodu+T60xfdkfs+vj33+5MHXrB//vBbsb1Z5Vd+qxbcaWvxaN/+t/e3TwgI4Fvw+3n1e/LES5xe0mI34uunTBX+oxg7o+gc//vT2G0CfClgzPCBqBp//+I+FlPpt3dVRv9D9eugXIMB9Woaz8kaSdgvwM6NGGwK/dilw7GseyP85wrPGdbT45X/6D1D/6L9Afem+cO3dB8D2PmPx+wOL30Flvn/F4l8+LQwgvG7TOK0A0mqMqn6p3Bgg7rxx04Zd2F4BWHlTH34EKz/OHxZptfjlX5L//hD1qZl+eWBz+kRAbSPM6NcNRfhptvOUAKh/WuUDrgrH0B/ALkXtA5WiJ8YDTeoC8E0/+6TL06JYBCnAF8BZ00M28NvnWdgvv/ziuV3ypXrCNbZ4klm3BBO+qbP4+BHYFhVpnPRfqtBP6sUPv/72w+J/Lf6rVQ/h8x4qoI5XVICGD/YDVTaUYBoIGAgxgJBHVH797eVhIAbQ6ALEMI3S8LkYZGkeBl/dre+YjyhBLrwQOBC4uGzqtp/pMu0/LYRo8U1fsOl8aWaJpO76RRA2YRWElT8BqS4w55snq7pfdCAVuwiQ59CFj11/8Vr3oWIJyt3tf1lIGxVwUl2A/2Y1H5PA4rpKgfu/JcNzHAhpf+gW668iPi3kOS8Xjdu6TdK6rz0i9xmXmclfy4Fwd1GFty/VTMDh7KpHkTzdE89NRuq/Qvrx0Ur4dQkQIei+7h2/GpFgYTwYtP1Sda8CcNs5FD4gBLBpPKTBTAv/45VSXVIPRfDwH9B0lvSKQvCKyiMHD3/RrOjPZuXP/c6XAYURfPH/eWs0m83wvMbyjMFuF6xsaPYzHHNDOIft2UOCDR47P0rv967lKzJ9BegvVZGC3Gqn//Gc+TD6NecJekMLfK4x2kM+yCAQjlnuI8HnhG3buTTcL9VXJgBqLx6wB7QGaACqZU7SrxvOV79qmoCSn7//3hU8EgIEABgOknjRDF4BEiwKw8Bz/RxoNUfsayRBtodzwd6S1E/+ZNXsYZBUQP4CKJGCsgNs8ekbOj+vflX9Twufzc+85NEYDqBG24cAoEc4KziHZI4bUK9/9t/Azs8PIcCMsuln2z1QJcDS52DYhpch7dJ+Du3Tr2EDIPnj/P60dB4NxwYUBnAWSP9mAN59FMycXyVIEKADwAxQP2VaAaoHTnk54SHQLefqB+j66kWfEh/DL4PCR5XNHPV14WzIvGam/WfuutX0R5AwvpcmQF45z3js+4+Z9m23WfYMlB0AO7Dj16vP/uDTk+KfPcTiq9zP/3TA+fHfOwM9SNv8cwJ8XiR933Sfl8sn0X7l2U8AppZPXbtvnPtx5sSPc5F/fBT5gzm/FvmfhD/t/rz49xT8k4hXgXxeIJ/gT/B86fBKsNcL+GPzcW1/xOerXyot/B1JwfZ1CTJsjt4ESP4b7X2dArgvbgHSgMlPGuxm9rwBwn7gPgjFl+qPGT9XHKCVKp4ztKv/gAQP/gfZ/4zcN3oCl6oe7B3MfWMczue1R3104dvnaiiKD28ABcN/7Zw2s1A5Z3Y3H/BADYFOrE/Dx7cn9r2/sG8e+fMx9/SofPQj9g8o+aJDYNaLR+oI0MisZj81s17Pk9rc27ndex29B8BX/yx+C0Zn9gy+ZfBD5lxFAPPLR/G+yvXhrtno727yALyx/+cdlMcHt/i02IYAXIvuj1X00n3uAf5Q7M94gTj5wFMfFsGDyoB6QIHZiTNQuF3+oKjv6pI36Tug2Oo72uzqGwAbgALfuGhG7rTyiwEg0I/YR+Kn74p8sNr7k9W+48WZCv9IfLPQywDw6MMi/BR/Wpi6xH1X7rem/HuRd/tZTlB/nhuCDy/wBe/gIPVh8e1MBBz0OqU+/qhQDeXb55/n89iceY8l8wewBrx9W/Ttzyle+Pb37+n1CPn715D/s3byjLyAmeZ4/VVnAZQHCgSD/72UAZs8WANw76zv7474XZ36cVac1QHq988/bfz6BioJ4FnvvmrpddgA0wHIfuzm1moJEAdsCL4/sQFc+787hryEdIkLOmAgBfX8gMQJBPVdEicRykdRDCUIAl15LoWtcBdGERIjqVUAfuiAglcwiqIRjXmhH6GBD+Q9YeZ9biLTWbFZK7DTR4BU4e+XwVDwsuhpweyub6eeB248Dfv1zSPxOa/xTmCer81yhXghvvTG9rw8E6v0EPemmcpam0hUzI3RyOFLMnOgmzLAm4O9MRw2cz3BnM5roV2dOeYKH5e2sRJVNJDukqlbPOVOIdGT5TjmbX4X8zuxZKmMqBCVX948zePtBik6DbQb6zVZL0W/OfXjqXaKxj9lijQeVia/z6mNMHpLiDaX43nvTht2aDQ93vO+ZxxYBK3O3FKpsJV+GU2hM3eN293MMw04ttQaT3PcwspPSy4vcMfjTtVIRAiF98XVgFch3SfHlmVpzi78BC+PrlvtMVPzLzshk4f1mkvUkbj7V03Ii5Wp01Gk+ZxccZqgNQdpX1tcfikKy3EuFbrG5d2dgJZR1NKwN1QGbRgWtAyjAToEY9fU6a0/WiFreZW4abZV4A8ynAp7Gts0bHXhvcnkLSofuijqBW53ENIR3dIjg7VsEMecZXEul0k75TTZ0T5PlcltdW5a7dkNvtdswfck2Wzd43DzDrjA9PJuEziBQDmOZV81lA4qoj96UEKdy+PREBOe7S+CFMdROVJx6FmStdFOZucdpG29M8hjh5Qbt7HEfI/xoxnwZa9BundgMzQWpMt6vzwUe4FaY/29He/qISzt08nSiTrOVxZrbXL41qvrODVO+prPWxN4uD5tDu12rQQSs1wNdMPC1xsiJinkJgdFV4tgfxF3sBv6DT30o0wawTXXqH1GlZIex82FvtBxsY0clx0m10UlprkJvOhM5b416/OODaEwtS3P3Y4SWzHKzrVIcwshJ4KLXSagboniaurdgHaMuPWUJBkKRd2QsZltYFn3zP7YHtFeYM6t2FpLa69tG4308lN5m9rB88kL3gjHq7OpVHGHu5kymgWaa+cKEk/BYclFGUsUpdBWOLvqhV2aomtk43TK5n6rV+sOu6LJJUphxCGqGiphk5a8w325ybx7PGVh4rg7YrlZD0ITRop5Pef76hIpJTHAd4eq8F61XWR/u2bM+bqMrtAuuhFF35qqHTk7doqi+2q1GejdYbJcvJclHQ28E3dsDnpwUkg2iy9WgbVlEoPetYAZw2Ds3cRyVOhTA6OFNsLpN3fdYINmw7ojIaiuKuUVV1B0Z8hwveVcvSnyRubIQnRcRfDW6da0SEbu1+w2Ube3w2hyN8VdK2GWuTeOp4fr5iDRU3mXaEW52gWxhVMz3F7pMU0qstUMdzrG2VHPc5tB2JzJ4kAVYG4/dqm2OcN7N1hh95OS05tzuD5BliHkonwcW+J0vSzpJEuC8twVdw92Na8jmig5lSqKWpvCP1oeGpukPmZUkkjjmbNdxty1zJqxccNfSWgiVMjl0hz9yxg6TKSF5knbHhLlvlc3IZtT/OYqY5hsa1cLL/uOEYQ9sebUYrSJdC+dccn3XHpsUA/SVqKYBifTWbPMxnOsNA0GZiPDwtmM4RsET7DVb6iCZdg4S5iCpCpka2WIlxQNN/YmrSyPGJ7DwfV8H7HaRQXOu3VXYZUx6mANR27YDpKMbYU1NA3+ljh4TO/uNrALKM62b+KpZKnEDVhCF/yLZOjnwmzStHLG2nILb0T1SKsk/uYjY7HN1g653E81gXr0Hb9JFg/zSLXTcEUiiFMX8mHunDRT2La3XUWkx6qCmQpx2hI7AjdNlX9VmUqzz6GsXZhR3YY7SRfju6P7cRbRBFFfxPMFvuWpOpVOsU3gGt9Jfpza0anftPRQ2Bu/EqHDuLrtD6m4CxPhtA4C0j06ax7LBBQ1mVOH86tI3SnyWIaGPebp3thv+LD2zvWdPNlwIVl108uiHTYsya8dHrNzNj/kytpIJ9FizSBnmUmUqUOt2rLVVGx6Z5q1Y19DLxNEkw+Ji7wUVrggGVvtCHmbhM6CUyvqvcssryfu2pTihGzLDWp42zIT+Qil7MFoyJVSjYec2x7UjoU2lw5K9czY07xycvpuu8lQnheCQtmp2VKjYV+BLvYx6K0Nv4WubQstg9MZQxAKuhbIkgvCCIJ6vaMm97ouywA6yOWG4S/HwzlfDrv8JBa13l9aS88ti8knf3cTRyY7W6ukZC5UgSf+zfMox9J9dhQk3CN2It66YiKfEpUJGoMpYYNPk/2aNXntSMjWgdVsqynN0de4Gk24HaRkzd0xLcnGsv32qqVYpWF3nLHaoru1/p7LUOFk42dCGvyriGi11kYepW5umFYyq7MM60a+Vo74gTxvTJGKuIlnuQY9e0JsxpLgHguPQq2Aj7NdGlUdPSRpdOv8CZS8lIoMIZHlGvFbwgW9ZMonG4GP4HGoW5YpXH7M8WTr8xt9pxFBsr/qZSRfB6lh2sLZcMU1sKjSEs6i3BwOaak3sGIjcXyz2egyHu/IFpHyHUHcDmUXi6lw7uWN68KVeD2mDnQwrDjNJtCzXW6WcjwK5HHI1ZFcahehPQP6amWxtqFqzdxFtkNuxSSs1WlqTqWTEgafl0aq2Hy23SEiihotZTtMueWWt9MGSfYZj5q5smyJiynpdF0VuKG0u5By6HYlXDfXBsZhbUO5KJeEE97dOyfcJ6XbAmTdjWSf5NY+u9BczOzFe1V2e9WSfFkWzrXnEFZjpJKBkBpL83Qp5azehE7FWxMXOJB988my0Gq1SfTc1qBbdeebVTpo4jpmBIvzd0IhQeYuv7PclT9s+Qu9g69LV0hUAWEgeL/cFiierttURcXjuEt8apWichrEZ0NPjWtWqXiPwXZnb7bd/XYr7x6HQ2ym2eN0KDaQ7w7HNaZpdahZ+1PMiRMUnpuJaKoEG4R1odxsGbe24Q1m0YnFxDIzxbrvp+NkaIqhiMdE924queI4XC+dZsJqzdfctayDM6DQtBG1FaGbWsblZbKtONYxA3d0iTiLmgEQrAJNqxbJxDnDj9rRHUTcuq+IJXNzDsJRIi9KopRIasXX0BTgqiVWwm1MbeWa98zUtTC6iff1qVIS4mpU3tHNvTUdVxv2wmqW7qorMXMZOuxWPiL6sUs1w7SkVss8P1tFfA/GYe/oZlBSUNWTyBHam9uDs0xZncRNIvLz3aQNHJNh+g19cBeB324qEYKCYAvBkC8FojFxq50cRhTw5UXYr8JCFtkE9Jf9Rvd55Ch7bL8fll2L+lVEOm7gEwdE64XDytFMiyUH6yCmmclETtoJdAqZoqutkj2JF7dWqaejwWKY6E3kaS0y2uRNTsaOfEo7TUttt+MIAoDdHU8/O6sDx2FDPhWJfBvj6lgKg5vu9sNWTUbPxLsOUQLfU2WdoIoNVijFVY6j7jbYJ6r1EBozM0trCtAdR3kQGQMkh5p4xrZOR+eemIp9obBYttkeNbhYUnh7NQoakqYqxeKg640zwaGMrYoDqQbHkdmWF3lP6DInKEFOHcKBtzGu31zQoloHPrYSzNvlPODExF8HIgda9rWudGtvDONAYCZHaW/D0bUJVneXMWMgTlOud85xzXTGaRMFdNdormGEyAGfLEcQdO0eL491OaSFabPHSNS8zGik/SGyu6n1nIMrFBxxvHA3KeuWq516Zo8FdyHlBhpXmXfZFdEeNHH5Vk0ptKopksp6fSvKlzZwbY4kiSAYUDMDgOVJHSppGkT1gW2gqxCKhmVYBuFKoc5LFiTNYJuKRZ4zp9QKK7kL7J6hDpCAe3k6RjwEuWiDnrgmb73Uva+dzSGuYmxHnLmB9xyIti2m2ttTf9/IkkKKwnko5LXWIj06Hun0rk22DC5tcMaJGQTKr2mQY6obZ9k64deQ2W86HzpceOp0QZJLviG34v6kl/xldVJUx5yYCSSvPZYX7BJMK4MzOSUU4DhhqbuyTuPtPXButkItczHBTkfLuY3uaN09RCaMZb+bJLM7YEQ9LLMA8qqtb15sw2PygkCKa8jnS28gOi7o5TPEcLGdMQ4tXEWpccfUxYvel/cFF0e5AunJDWvJmqGQ04RSGTjexew03pOMQFv0bNOeR3d6FrOnreSb2xT1YIYYzFBnyumUqWfR45UjPE3d6mqE3XlUTlsWa85qyCdLWr6e+I2dJbYQyxu5LGHaEGgVt+2Rwhz/SHiiEicmvY3VU4s3DX3oVnx5GlCBvjojEp/P1sUoydY60JV85w7BRoDOTb2EGthD1oPTtSuRX3o+CJ9CGZVBXCpiNyInsW7w1ZmQG0YSKziM70jnlv2W3hnQCPgyNMIgT0lGAiUZhBAmtrlEpyi1O7pEb8QCnbs1lYX4hjFS/5aqudGkp/X14kk+vmTY8cSlMNoqfehRvXxJGVc9RxMbk2hLMLDo5oJ2uNxRIztHiq8jkrkCqb12rfXd1A35fLXYk1u3CkKQ+slBitFtzAltfc7bY9dQI4RSorbNnnIoj7+j6xUbHOqlmtCgOGyLz1HWieUkXMvXG82PSCcWl+UuztIEOFBFSRp37KVkr/b3ld/zAWo0DsWO3VW5KjiyV7bXFUKOaRXlS0R1UNy5jIGHCXhciceTY5TcfqgE9Ubgkojw5ujFFdpbhgpFauZ3qz3UbkHv3viDhA24a7lhhWOtej5SY1iom72wGpXhdKTolSCzu85IPfi+k50dbSd74QBc0IJMYV14b1OMaGGQj0pqY6sbUI04GWMcVl+6cE0x3HgXItCh62TVX2xwpt6Vt3arocpyfRL4k9wI8pqysyu/XF5zdbnZeDomTIqqItZyZ8T8zXPRWwSpt/QguyQTYDk9hLpLDppDh+lWFXDNParNFVMrZCNqCFkF6H1/rQNYRhHQeHe2Gh9EyShbAkdWcOlDfBuWF+fkKMbq2Hn5yglwRYlXXufHOXp2ouIq8f44eqmxuyfNbgvBipuaV4OHcBb3TYs307DegB6PhCiqa+75PfYPJBHT23t/6crj6BFZ3rktU1XMEeNRUlQgykq94MJj5S7iNF8K1URHshgvNGhoe3G/bHeUBLLg1oydA3CDb9g4VNX7nseCwqFtbGR1AV45bkYxunsptVaO7y6CeAedVpJTyyuaZYe1ygfdXVhVlLQvVjFv09JSMqSq6g60beInrNiceXHXbjRxnwk5V0sZvFoe8VPgA3piw86+qedzkcLXvbtBAsen+tKob2WvCrlhckZ1W3vhAcuOSCZit/OdzVJ0ZyuxJ1U8UhDelJ77/TFcXlDSB/h9DpbY/RhsCPKcanWbKreg9HDhbrvQ7iTDqao4cVSHOy0IzFKFyiNV2ogEY1QU3ymEYx1Uo82V6TeGBgeTfcKz/eTXuHsoHXD66Tl4ylodlnbDCdZu3t3V3f1qoiRcloP1aXLP7bnaOoWzB0lCwusibslljHlx1u7xjUdASJC6w1VUV9hJgjCnPfP9EJk1S7R3ue+3UH7RffheYu5BWXHdfeV5+aDZbjLmXXMLZHtaqU2RETnF7PeXpMRP97Gjkvh0VJf10tnUAWIaPE6zclYJ9SUJmsN26Spd2flMQcV8dT0gSILfIgPNgoRYnmCiONUuFBInkkztcVlC4c48DH6IaYR+P9ygYbdVsHNxkSuurVLILQtVXRNT30dWeCZhXV6tmL4JqbVnGqTrknjrDMmIn2lwBj6k6cFnyqUAT2s5XDfNgFik5CCERbZKrktKgbS7jQCAUO0UAwplhQSAQ9x3NJphW9QybsvpEMvj0W8KZ4usL0l0GsbdeWuLWmku5cvu6mWKsDxM0I3J3GIydgRXH1PKU1egbRnu2bhNjC2k772jGQaqnmSXu8gNCpGRilnkph+m5BEhRnF3AzjanXnQCskJXPnxICdVSHX8JO2Tbnu/BSIAwFXaovxVXe/aeg3L074SOo9Jd9ZS3AZilCZNCY4vCckLd3WPJWRCK6p3RS82hqcAnuPr5larVt+CFu1Asyh6ZTYVhdTJLULXoOQTAvH0/gD6OqxoGpR2/DZSMGRzKRxve1L18e5wdFgiRWvKcj4OCpQ4/DbE0PJ+ri77gM7Fs7I6nhCQfOShW2LJ4XjJknxSmhaSsUMYQGtnl/dE2FmZXk0ho7QmLcbna3fU1bxtOYRP1p4ylEVKcgSkB4IbjAcZYXftMK1cTCnPA1YNxLrUI7hHzubQLLMTBdOEjK+udSgvCWHyETQRJuE+ri/iit3lMUvbvAHOFSUVLumW2o+IB8tQB5+xjY4whEsgw46fqMEyqrOCkYTlhQKGDOaY0+oFOpMEpZy9IVcslEpOYgSz55u4Z1Gx7xyuxG3e3fNK0rsWcb0XqKt6IU+nEqwahwbJkCaEyMOeOuogB4vO1uraUJwuELH20IbwYBBUXHTBSK69NTNOEyyxQseRI2wcVXmCzvH6RspePOo7p+lRWtKDXU3cVdCo0RdJPYc8jpNUExxIJtLvF/dgu6S25Jp61243GdTXLRlCUkN1Lb3q9zRZ3qOV168jcvK2hkfRHHbd1j4FZUce82AVPlSxKaP0ttx504W7ek3oN5wZIDDS+M61WnLyNjjTIjtG14o+yGjbK51zwZgVrqzGM1V4g+piu50subR5JS5872M7b3NAhxUdNPwOFQ9qdz03Erc64HBzXQnIjcQVL1tvKSHYHIX4cLEMSIJvlsas2RXChscKPZ6CXT+RF/6anvWuJyRtxMTrhB4z18hj7xJm8Qqc8fX1wckkckUIVKEdIxhKhrsH+skVtCQ56Coe6+V4N7DMaEO8gLyx3gly40rIeViF6z7k7nIXY4robipTg3GSaZKbe4iptuyvHLakpWh9OSoYYzb31SlpiTqfapm5dPCyu0qwjZ152oUAtZGNHfG2H26jm5IXmiPE+Xxb5W9/e/vw9vu9sLd/7xmz+bbO/7M7SM8bQV8fJnnc6Qvd4PNjr8//pl5///DW+inQ6nm/rCuG+HXT6R/uln38lx4gmEVMzwe4vt4Mft4p7914fsj5La2Coevb6b2ri8dDJWCFN3TzQ5Hd/NysD97/eNPyT+a8zQ8pArPnB7je+/r99UjnY3h+aCQE1NiHr6/x617ih7fg9bTSO8CG97BtZqNfTyYAW7FP8Cf07bf/DancOqSWLgAA -->
