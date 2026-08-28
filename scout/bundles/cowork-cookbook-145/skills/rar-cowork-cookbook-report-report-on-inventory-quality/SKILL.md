---
name: "rar-cowork-cookbook-report-report-on-inventory-quality"
description: "Builds a structured summary report of report on inventory quality activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_report_on_inventory_quality", "rar_sha256": "72d88de0e18f37702cbd0d536474cc7c62b765702b39c79a8daded48f38210bb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_report_on_inventory_quality_agent.py` and embedded as the fenced Python below (sha256 72d88de0e18f3770…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_report_on_inventory_quality_agent.py` first:

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
    "version": '2.0.0',
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
