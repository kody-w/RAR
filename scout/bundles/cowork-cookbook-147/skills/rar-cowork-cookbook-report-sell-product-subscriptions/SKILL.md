---
name: "rar-cowork-cookbook-report-sell-product-subscriptions"
description: "Builds a structured summary report of sell product subscriptions activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_sell_product_subscriptions", "rar_sha256": "c7849078647ff537b70bb8903016a7c850e36eb77843a98d9ebbe85e03a63950", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_sell_product_subscriptions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-sell-product-subscriptions:045f4c12f6474dd175dfc098ef94721ec1bb1f13bf523eb6b96852c618f95513", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_sell_product_subscriptions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_sell_product_subscriptions_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
