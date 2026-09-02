---
name: "rar-cowork-cookbook-report-allocate-inventory"
description: "Builds a structured summary report of allocate inventory activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_allocate_inventory", "rar_sha256": "2eaa29da24b2c94779fc32975afeb26cfd4773c66c1e4df94d90f8be714a898c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_allocate_inventory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-allocate-inventory:50ada4602eea64e6f91cc9d09896c4818884e13dd40236e3384b4298eaa21076", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_allocate_inventory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_allocate_inventory_agent.py` is
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

Allocate inventory Summary Report — Builds a structured summary report of allocate inventory activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-allocate-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_allocate_inventory_agent.py` and embedded as the fenced Python below (sha256 2eaa29da24b2c947…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_allocate_inventory_agent.py` first:

```bash
python3 report_allocate_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_allocate_inventory_agent.py   # or on stdin
python3 report_allocate_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate inventory Summary Report — Builds a structured summary report of allocate inventory activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-allocate-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_allocate_inventory',
    "version": '2.0.0',
    "display_name": 'Allocate inventory Summary Report',
    "description": 'Builds a structured summary report of allocate inventory activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-allocate-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-allocate-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'afc3a02f14945209',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/allocate-inventory'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/report-allocate-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportAllocateInventory(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportAllocateInventory'
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
    print(ReportAllocateInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
