---
name: "rar-cowork-cookbook-report-allocate-service-parts-inventory"
description: "Builds a structured summary report of allocate service parts inventory activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_allocate_service_parts_inventory", "rar_sha256": "be6964647986e1e62c37322a122c6923923b122e89cdb040a4521b098c24c55e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_allocate_service_parts_inventory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-allocate-service-parts-inventory:b736082cb34734f984d728e79adbba9f3a3efe8981408f2bdc4ec74ffff99c60", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_allocate_service_parts_inventory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_allocate_service_parts_inventory_agent.py` is
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

Allocate service parts inventory Summary Report — Builds a structured summary report of allocate service parts inventory activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-allocate-service-parts-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_allocate_service_parts_inventory_agent.py` and embedded as the fenced Python below (sha256 be6964647986e1e6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_allocate_service_parts_inventory_agent.py` first:

```bash
python3 report_allocate_service_parts_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_allocate_service_parts_inventory_agent.py   # or on stdin
python3 report_allocate_service_parts_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate service parts inventory Summary Report — Builds a structured summary report of allocate service parts inventory activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-allocate-service-parts-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_allocate_service_parts_inventory',
    "version": '2.0.0',
    "display_name": 'Allocate service parts inventory Summary Report',
    "description": 'Builds a structured summary report of allocate service parts inventory activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-allocate-service-parts-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-allocate-service-parts-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a041dbe3db11f663',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/allocate-service-parts-inventory'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/report-allocate-service-parts-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportAllocateServicePartsInventory(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportAllocateServicePartsInventory'
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
    print(ReportAllocateServicePartsInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
