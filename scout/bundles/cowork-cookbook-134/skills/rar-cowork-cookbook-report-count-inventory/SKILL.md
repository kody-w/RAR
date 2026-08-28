---
name: "rar-cowork-cookbook-report-count-inventory"
description: "Builds a structured summary report of count inventory activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_count_inventory", "rar_sha256": "135ed43a82f3180d74980a7cc59b44b63de68a2ec593d30d7fec2d7b1be8bee7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_count_inventory`. The original RAPP
agent is preserved byte-for-byte in `report_count_inventory_agent.py` and in the RCI capsule.

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
