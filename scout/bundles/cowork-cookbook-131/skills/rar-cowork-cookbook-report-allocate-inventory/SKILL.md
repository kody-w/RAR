---
name: "rar-cowork-cookbook-report-allocate-inventory"
description: "Builds a structured summary report of allocate inventory activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_allocate_inventory", "rar_sha256": "5989f9d4de6b4f702724b86a78ad4ffb9552f3c070dba2cdaa242b10112a7e40", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_allocate_inventory`. The original RAPP
agent is preserved byte-for-byte in `report_allocate_inventory_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_allocate_inventory_agent.py` and embedded as the fenced Python below (sha256 5989f9d4de6b4f70…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_allocate_inventory_agent.py` first:

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
    "version": '2.0.1',
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
