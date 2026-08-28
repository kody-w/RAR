---
name: "rar-cowork-cookbook-report-allocate-inventory"
description: "Builds a structured summary report of allocate inventory activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_allocate_inventory", "rar_sha256": "2eaa29da24b2c94779fc32975afeb26cfd4773c66c1e4df94d90f8be714a898c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
