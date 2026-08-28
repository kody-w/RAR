---
name: "rar-cowork-cookbook-report-pack-goods"
description: "Builds a structured summary report of pack goods activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_pack_goods", "rar_sha256": "d37d46156b3277bb7e5bfe4e9eae22821091217d94ad54898ed2217c2735d2a2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_pack_goods`. The original RAPP
agent is preserved byte-for-byte in `report_pack_goods_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_pack_goods_agent.py` and embedded as the fenced Python below (sha256 d37d46156b3277bb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_pack_goods_agent.py` first:

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
    "version": '2.0.1',
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
