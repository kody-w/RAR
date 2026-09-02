---
name: "rar-cowork-cookbook-report-revalue-inventory"
description: "Builds a structured summary report of revalue inventory activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_revalue_inventory", "rar_sha256": "0f2502bb12e6fdb4843ecbfe70693ed5153fb035b045181edc4dabaa1b143b8c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_revalue_inventory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-revalue-inventory:54954504489c1dab96744fb389eddad620b6f91b70101600bb1a5ad74b591475", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_revalue_inventory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_revalue_inventory_agent.py` is
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

Revalue inventory Summary Report — Builds a structured summary report of revalue inventory activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-revalue-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_revalue_inventory_agent.py` and embedded as the fenced Python below (sha256 0f2502bb12e6fdb4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_revalue_inventory_agent.py` first:

```bash
python3 report_revalue_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_revalue_inventory_agent.py   # or on stdin
python3 report_revalue_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Revalue inventory Summary Report — Builds a structured summary report of revalue inventory activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-revalue-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_revalue_inventory',
    "version": '2.0.0',
    "display_name": 'Revalue inventory Summary Report',
    "description": 'Builds a structured summary report of revalue inventory activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-revalue-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-revalue-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e070fe8201d890ad',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/revalue-inventory'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/report-revalue-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ReportRevalueInventory(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportRevalueInventory'
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
    print(ReportRevalueInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
