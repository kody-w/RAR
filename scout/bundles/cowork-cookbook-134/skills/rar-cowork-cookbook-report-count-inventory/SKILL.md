---
name: "rar-cowork-cookbook-report-count-inventory"
description: "Builds a structured summary report of count inventory activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_count_inventory", "rar_sha256": "135ed43a82f3180d74980a7cc59b44b63de68a2ec593d30d7fec2d7b1be8bee7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_count_inventory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-count-inventory:61f69a2fc973d343759f710839a6cc2e931f8a1a0e345d844946d24423c7cc01", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_count_inventory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_count_inventory_agent.py` is
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

Count inventory Summary Report — Builds a structured summary report of count inventory activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-count-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_count_inventory_agent.py` and embedded as the fenced Python below (sha256 135ed43a82f3180d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_count_inventory_agent.py` first:

```bash
python3 report_count_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_count_inventory_agent.py   # or on stdin
python3 report_count_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Count inventory Summary Report — Builds a structured summary report of count inventory activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-count-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_count_inventory',
    "version": '2.0.0',
    "display_name": 'Count inventory Summary Report',
    "description": 'Builds a structured summary report of count inventory activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-count-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-count-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cb370b93b0c800a2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/count-inventory'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/report-count-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportCountInventory(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportCountInventory'
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
    print(ReportCountInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
