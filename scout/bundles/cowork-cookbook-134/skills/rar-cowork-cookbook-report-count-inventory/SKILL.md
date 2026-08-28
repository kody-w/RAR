---
name: "rar-cowork-cookbook-report-count-inventory"
description: "Builds a structured summary report of count inventory activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_count_inventory", "rar_sha256": "207b3d04e7f091f69a51798598d53324f30b58fd1633867a01a998f9c5ee65ad", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_count_inventory_agent.py` and embedded as the fenced Python below (sha256 207b3d04e7f091f6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_count_inventory_agent.py` first:

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
    "version": '2.0.1',
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
