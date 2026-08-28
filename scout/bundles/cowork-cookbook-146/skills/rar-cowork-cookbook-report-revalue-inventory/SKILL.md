---
name: "rar-cowork-cookbook-report-revalue-inventory"
description: "Builds a structured summary report of revalue inventory activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_revalue_inventory", "rar_sha256": "0f2502bb12e6fdb4843ecbfe70693ed5153fb035b045181edc4dabaa1b143b8c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_revalue_inventory`. The original RAPP
agent is preserved byte-for-byte in `report_revalue_inventory_agent.py` and in the RCI capsule.

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
