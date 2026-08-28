---
name: "rar-cowork-cookbook-report-put-away-received-goods"
description: "Builds a structured summary report of put away received goods activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_put_away_received_goods", "rar_sha256": "a9f5922e718859c86f5468def89d4a4d5b3240cd50eba0876ff785b958a3051a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_put_away_received_goods`. The original RAPP
agent is preserved byte-for-byte in `report_put_away_received_goods_agent.py` and in the RCI capsule.

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

Put away received goods Summary Report — Builds a structured summary report of put away received goods activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-put-away-received-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_put_away_received_goods_agent.py` and embedded as the fenced Python below (sha256 a9f5922e718859c8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_put_away_received_goods_agent.py` first:

```bash
python3 report_put_away_received_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_put_away_received_goods_agent.py   # or on stdin
python3 report_put_away_received_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Put away received goods Summary Report — Builds a structured summary report of put away received goods activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-put-away-received-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_put_away_received_goods',
    "version": '2.0.1',
    "display_name": 'Put away received goods Summary Report',
    "description": 'Builds a structured summary report of put away received goods activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-put-away-received-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-put-away-received-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8a56ee313cc6b58e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-inbound-goods/put-away-received-goods'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/report-put-away-received-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportPutAwayReceivedGoods(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportPutAwayReceivedGoods'
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
    print(ReportPutAwayReceivedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
