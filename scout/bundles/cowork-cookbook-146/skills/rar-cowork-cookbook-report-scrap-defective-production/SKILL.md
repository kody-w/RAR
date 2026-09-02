---
name: "rar-cowork-cookbook-report-scrap-defective-production"
description: "Builds a structured summary report of scrap defective production activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_scrap_defective_production", "rar_sha256": "64b1908f6270f17d4dd3f4999a090f9c2d975b92c7c829f29b302a2ec1ad6c09", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_scrap_defective_production_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-scrap-defective-production:52ff0996b109b028a2cfe5c8bbb8c1b1d471cfac3b586e89ee5958dfbedb5f7b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_scrap_defective_production`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_scrap_defective_production_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
