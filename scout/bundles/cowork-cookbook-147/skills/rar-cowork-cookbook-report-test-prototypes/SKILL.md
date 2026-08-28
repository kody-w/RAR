---
name: "rar-cowork-cookbook-report-test-prototypes"
description: "Builds a structured summary report of test prototypes activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_test_prototypes", "rar_sha256": "727771c3182c86859be479d1e86e5242333ea6cf2f2aebd3593170f469a66d54", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_test_prototypes_agent.py` and embedded as the fenced Python below (sha256 727771c3182c8685…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_test_prototypes_agent.py` first:

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
    "version": '2.0.0',
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
