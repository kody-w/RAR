---
name: "rar-cowork-cookbook-report-put-away-received-goods"
description: "Builds a structured summary report of put away received goods activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_put_away_received_goods", "rar_sha256": "91a357609f8f1489fbf0c576a3627c9a4f262c6001370cc4294d3da49e3c67c5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_put_away_received_goods_agent.py` and embedded as the fenced Python below (sha256 91a357609f8f1489…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_put_away_received_goods_agent.py` first:

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
    "version": '2.0.0',
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
