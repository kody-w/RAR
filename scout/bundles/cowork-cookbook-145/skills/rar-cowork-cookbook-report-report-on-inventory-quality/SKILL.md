---
name: "rar-cowork-cookbook-report-report-on-inventory-quality"
description: "Builds a structured summary report of report on inventory quality activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_report_on_inventory_quality", "rar_sha256": "daf422d624433b7662fee4c06d7dc1fd21a76560ffd28c4b545e892a5c02a4f0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_report_on_inventory_quality`. The original RAPP
agent is preserved byte-for-byte in `report_report_on_inventory_quality_agent.py` and in the RCI capsule.

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

Report on inventory quality Summary Report — Builds a structured summary report of report on inventory quality activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-report-on-inventory-quality
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_report_on_inventory_quality_agent.py` and embedded as the fenced Python below (sha256 daf422d624433b76…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_report_on_inventory_quality_agent.py` first:

```bash
python3 report_report_on_inventory_quality_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_report_on_inventory_quality_agent.py   # or on stdin
python3 report_report_on_inventory_quality_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report on inventory quality Summary Report — Builds a structured summary report of report on inventory quality activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-report-on-inventory-quality
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_report_on_inventory_quality',
    "version": '2.0.1',
    "display_name": 'Report on inventory quality Summary Report',
    "description": 'Builds a structured summary report of report on inventory quality activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-report-on-inventory-quality',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-report-on-inventory-quality',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '828154e995679fde',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/analyze-warehouse-operations/report-on-inventory-quality'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/report-report-on-inventory-quality', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportReportOnInventoryQuality(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportReportOnInventoryQuality'
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
    print(ReportReportOnInventoryQuality().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
