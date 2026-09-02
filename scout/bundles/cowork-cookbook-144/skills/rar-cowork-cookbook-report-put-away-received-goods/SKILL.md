---
name: "rar-cowork-cookbook-report-put-away-received-goods"
description: "Builds a structured summary report of put away received goods activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_put_away_received_goods", "rar_sha256": "91a357609f8f1489fbf0c576a3627c9a4f262c6001370cc4294d3da49e3c67c5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_put_away_received_goods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-put-away-received-goods:4ca7c359ac10930a781e3148ede3da02c1f740cf3a3c664aea69f10594725ec0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_put_away_received_goods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_put_away_received_goods_agent.py` is
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
