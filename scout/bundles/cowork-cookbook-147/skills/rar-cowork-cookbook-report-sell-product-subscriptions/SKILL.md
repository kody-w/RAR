---
name: "rar-cowork-cookbook-report-sell-product-subscriptions"
description: "Builds a structured summary report of sell product subscriptions activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_sell_product_subscriptions", "rar_sha256": "c7849078647ff537b70bb8903016a7c850e36eb77843a98d9ebbe85e03a63950", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_sell_product_subscriptions_agent.py` and embedded as the fenced Python below (sha256 c7849078647ff537…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_sell_product_subscriptions_agent.py` first:

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
    "version": '2.0.0',
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
