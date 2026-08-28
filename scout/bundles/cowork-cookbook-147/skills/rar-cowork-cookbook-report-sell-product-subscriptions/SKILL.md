---
name: "rar-cowork-cookbook-report-sell-product-subscriptions"
description: "Builds a structured summary report of sell product subscriptions activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_sell_product_subscriptions", "rar_sha256": "08ed5b80ea2b62343378bafdacb03aed8ac44a6c1d4dbb1ed1503168be5474ee", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_sell_product_subscriptions`. The original RAPP
agent is preserved byte-for-byte in `report_sell_product_subscriptions_agent.py` and in the RCI capsule.

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

Sell product subscriptions Summary Report — Builds a structured summary report of sell product subscriptions activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-sell-product-subscriptions
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_sell_product_subscriptions_agent.py` and embedded as the fenced Python below (sha256 08ed5b80ea2b6234…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_sell_product_subscriptions_agent.py` first:

```bash
python3 report_sell_product_subscriptions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_sell_product_subscriptions_agent.py   # or on stdin
python3 report_sell_product_subscriptions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Sell product subscriptions Summary Report — Builds a structured summary report of sell product subscriptions activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-sell-product-subscriptions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_sell_product_subscriptions',
    "version": '2.0.1',
    "display_name": 'Sell product subscriptions Summary Report',
    "description": 'Builds a structured summary report of sell product subscriptions activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-sell-product-subscriptions',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-sell-product-subscriptions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cdc7fa29d5fc2fa9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/sell-product-subscriptions'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/report-sell-product-subscriptions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportSellProductSubscriptions(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportSellProductSubscriptions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
    print(ReportSellProductSubscriptions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
