---
name: "rar-cowork-cookbook-report-report-on-inventory-quality"
description: "Builds a structured summary report of report on inventory quality activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_report_on_inventory_quality", "rar_sha256": "72d88de0e18f37702cbd0d536474cc7c62b765702b39c79a8daded48f38210bb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_report_on_inventory_quality_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-report-on-inventory-quality:297707ba30f8c29694308fcd9d17b4d220a4f3aee47dae05fba51cd05e737e6b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_report_on_inventory_quality`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_report_on_inventory_quality_agent.py` is
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
