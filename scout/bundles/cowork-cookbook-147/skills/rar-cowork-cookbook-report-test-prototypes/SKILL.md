---
name: "rar-cowork-cookbook-report-test-prototypes"
description: "Builds a structured summary report of test prototypes activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_test_prototypes", "rar_sha256": "b618cfce45f9b2abf08d3de66027aed8269fddd2c2f445392a10f6e5e5d62dc0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_test_prototypes`. The original RAPP
agent is preserved byte-for-byte in `report_test_prototypes_agent.py` and in the RCI capsule.

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

Test prototypes Summary Report — Builds a structured summary report of test prototypes activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-test-prototypes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_test_prototypes_agent.py` and embedded as the fenced Python below (sha256 b618cfce45f9b2ab…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_test_prototypes_agent.py` first:

```bash
python3 report_test_prototypes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_test_prototypes_agent.py   # or on stdin
python3 report_test_prototypes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Test prototypes Summary Report — Builds a structured summary report of test prototypes activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-test-prototypes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_test_prototypes',
    "version": '2.0.1',
    "display_name": 'Test prototypes Summary Report',
    "description": 'Builds a structured summary report of test prototypes activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-test-prototypes',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-test-prototypes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b4672b37774457e0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/test-prototypes'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/report-test-prototypes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportTestPrototypes(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportTestPrototypes'
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
    print(ReportTestPrototypes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
