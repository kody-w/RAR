---
name: "rar-cowork-cookbook-report-pack-goods"
description: "Builds a structured summary report of pack goods activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_pack_goods", "rar_sha256": "a4d79dec13e6997064271c022dbded6acc59c2065dd8ddba0d8533b01e4fa409", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
