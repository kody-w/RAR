---
name: "rar-cowork-cookbook-report-create-and-track-service-level-agreements"
description: "Builds a structured summary report of create and track service level agreements activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_create_and_track_service_level_agreements", "rar_sha256": "ff2df6d1a5ecf3a04ef4f27fbcacada861034f3599bb8d85bc5a90e304644062", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_create_and_track_service_level_agreements_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-create-and-track-service-level-agreements:13078a4f9cbc1bf48b5a958a663bd3af9a91222cc886543cdec254e98e3a2562", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_create_and_track_service_level_agreements`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_create_and_track_service_level_agreements_agent.py` is
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

Create and track service level agreements Summary Report — Builds a structured summary report of create and track service level agreements activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-create-and-track-service-level-agreements
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_create_and_track_service_level_agreements_agent.py` and embedded as the fenced Python below (sha256 ff2df6d1a5ecf3a0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_create_and_track_service_level_agreements_agent.py` first:

```bash
python3 report_create_and_track_service_level_agreements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_create_and_track_service_level_agreements_agent.py   # or on stdin
python3 report_create_and_track_service_level_agreements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create and track service level agreements Summary Report — Builds a structured summary report of create and track service level agreements activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-create-and-track-service-level-agreements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_create_and_track_service_level_agreements',
    "version": '2.0.0',
    "display_name": 'Create and track service level agreements Summary Report',
    "description": 'Builds a structured summary report of create and track service level agreements activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-create-and-track-service-level-agreements',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-create-and-track-service-level-agreements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cbe057ce9150cf2c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/create-and-track-service-level-agreements'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/report-create-and-track-service-level-agreements', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportCreateAndTrackServiceLevelAgreements(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportCreateAndTrackServiceLevelAgreements'
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
    print(ReportCreateAndTrackServiceLevelAgreements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
