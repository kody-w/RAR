---
name: "rar-cowork-cookbook-report-sell-an-asset"
description: "Builds a structured summary report of sell an asset activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_sell_an_asset", "rar_sha256": "174c5ecbf4f2df823b105010d5641147d4815e552d5e98d069d22f0776fce6d6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_sell_an_asset_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-sell-an-asset:61dfa744480b7f0e9d188076002afab4bc401a615b672d89e39e74a089200aa0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_sell_an_asset`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_sell_an_asset_agent.py` is
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

Sell an asset Summary Report — Builds a structured summary report of sell an asset activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-sell-an-asset
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_sell_an_asset_agent.py` and embedded as the fenced Python below (sha256 174c5ecbf4f2df82…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_sell_an_asset_agent.py` first:

```bash
python3 report_sell_an_asset_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_sell_an_asset_agent.py   # or on stdin
python3 report_sell_an_asset_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Sell an asset Summary Report — Builds a structured summary report of sell an asset activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-sell-an-asset
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_sell_an_asset',
    "version": '2.0.0',
    "display_name": 'Sell an asset Summary Report',
    "description": 'Builds a structured summary report of sell an asset activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'report-sell-an-asset',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-sell-an-asset',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0009834f5e59b884',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/sell-an-asset'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/report-sell-an-asset', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ReportSellAnAsset(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportSellAnAsset'
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
    print(ReportSellAnAsset().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
