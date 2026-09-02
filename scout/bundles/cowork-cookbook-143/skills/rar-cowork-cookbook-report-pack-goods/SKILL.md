---
name: "rar-cowork-cookbook-report-pack-goods"
description: "Builds a structured summary report of pack goods activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_pack_goods", "rar_sha256": "a4d79dec13e6997064271c022dbded6acc59c2065dd8ddba0d8533b01e4fa409", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_pack_goods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-pack-goods:4f77eb8dac211b4b0b80c5a5e3d38f44c901701f16d977040c1ac3c27d854fe9", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_pack_goods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_pack_goods_agent.py` is
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

Pack goods Summary Report — Builds a structured summary report of pack goods activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-pack-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_pack_goods_agent.py` and embedded as the fenced Python below (sha256 a4d79dec13e69970…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_pack_goods_agent.py` first:

```bash
python3 report_pack_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_pack_goods_agent.py   # or on stdin
python3 report_pack_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pack goods Summary Report — Builds a structured summary report of pack goods activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-pack-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_pack_goods',
    "version": '2.0.0',
    "display_name": 'Pack goods Summary Report',
    "description": 'Builds a structured summary report of pack goods activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-pack-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-pack-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cbea8f9da1e97d66',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/pack-goods'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/report-pack-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportPackGoods(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportPackGoods'
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
    print(ReportPackGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
