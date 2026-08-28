---
name: "rar-cowork-cookbook-report-allocate-service-parts-inventory"
description: "Builds a structured summary report of allocate service parts inventory activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_allocate_service_parts_inventory", "rar_sha256": "4baf7cbfe438a19e0c2b7cce4a676a86507735fff01bfd944b3e2432dcb1859c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_allocate_service_parts_inventory`. The original RAPP
agent is preserved byte-for-byte in `report_allocate_service_parts_inventory_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_allocate_service_parts_inventory_agent.py` and embedded as the fenced Python below (sha256 4baf7cbfe438a19e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_allocate_service_parts_inventory_agent.py` first:

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
    "version": '2.0.1',
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
