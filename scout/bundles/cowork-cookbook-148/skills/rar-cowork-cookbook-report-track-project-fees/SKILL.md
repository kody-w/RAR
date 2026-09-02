---
name: "rar-cowork-cookbook-report-track-project-fees"
description: "Builds a structured summary report of track project fees activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_track_project_fees", "rar_sha256": "5fa5ba2dc740c53fc274edc9f7e2ca1e5b27888186511e159a2ba35bc1ba5be4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_track_project_fees_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-track-project-fees:2c5c739d3e7988c9c78a301dc0ac3d9332774c16e95c60f4e7aa4015b6650e84", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_track_project_fees`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_track_project_fees_agent.py` is
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

Track project fees Summary Report — Builds a structured summary report of track project fees activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-track-project-fees
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_track_project_fees_agent.py` and embedded as the fenced Python below (sha256 5fa5ba2dc740c53f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_track_project_fees_agent.py` first:

```bash
python3 report_track_project_fees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_track_project_fees_agent.py   # or on stdin
python3 report_track_project_fees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track project fees Summary Report — Builds a structured summary report of track project fees activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-track-project-fees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_track_project_fees',
    "version": '2.0.0',
    "display_name": 'Track project fees Summary Report',
    "description": 'Builds a structured summary report of track project fees activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-track-project-fees',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-track-project-fees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bbafbdd5773904f3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/track-project-fees'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-track-project-fees', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportTrackProjectFees(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportTrackProjectFees'
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
    print(ReportTrackProjectFees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
