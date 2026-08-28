---
name: "rar-cowork-cookbook-report-allocate-service-parts-inventory"
description: "Builds a structured summary report of allocate service parts inventory activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_allocate_service_parts_inventory", "rar_sha256": "be6964647986e1e62c37322a122c6923923b122e89cdb040a4521b098c24c55e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
