---
name: "rar-cowork-cookbook-report-scrap-defective-production"
description: "Builds a structured summary report of scrap defective production activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_scrap_defective_production", "rar_sha256": "64b1908f6270f17d4dd3f4999a090f9c2d975b92c7c829f29b302a2ec1ad6c09", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_scrap_defective_production_agent.py` and embedded as the fenced Python below (sha256 64b1908f6270f17d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_scrap_defective_production_agent.py` first:

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
    "version": '2.0.0',
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
