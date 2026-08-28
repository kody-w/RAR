---
name: "rar-cowork-cookbook-report-scrap-defective-production"
description: "Builds a structured summary report of scrap defective production activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_scrap_defective_production", "rar_sha256": "905934cb705579195ec69bcf002d2dfab32f0badb464a82ba7c3088aa19ac898", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_scrap_defective_production`. The original RAPP
agent is preserved byte-for-byte in `report_scrap_defective_production_agent.py` and in the RCI capsule.

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

Scrap defective production Summary Report — Builds a structured summary report of scrap defective production activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-scrap-defective-production
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_scrap_defective_production_agent.py` and embedded as the fenced Python below (sha256 905934cb70557919…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_scrap_defective_production_agent.py` first:

```bash
python3 report_scrap_defective_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_scrap_defective_production_agent.py   # or on stdin
python3 report_scrap_defective_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Scrap defective production Summary Report — Builds a structured summary report of scrap defective production activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-scrap-defective-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_scrap_defective_production',
    "version": '2.0.1',
    "display_name": 'Scrap defective production Summary Report',
    "description": 'Builds a structured summary report of scrap defective production activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-scrap-defective-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-scrap-defective-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '645169e56274e9c4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/scrap-defective-production'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/report-scrap-defective-production', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportScrapDefectiveProduction(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportScrapDefectiveProduction'
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
    print(ReportScrapDefectiveProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
