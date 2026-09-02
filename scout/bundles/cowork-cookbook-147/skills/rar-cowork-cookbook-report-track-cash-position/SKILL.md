---
name: "rar-cowork-cookbook-report-track-cash-position"
description: "Builds a structured summary report of track cash position activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_track_cash_position", "rar_sha256": "62060e402fda8a1c638acbcab19881b096fe9023b86e59cae08c2b52933cdfd6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_track_cash_position_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-track-cash-position:e017d421771762daaeff571008c8b73ce9ed182e4e3cf96c3b20170b4d9d2b76", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_track_cash_position`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_track_cash_position_agent.py` is
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

Track cash position Summary Report — Builds a structured summary report of track cash position activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-track-cash-position
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_track_cash_position_agent.py` and embedded as the fenced Python below (sha256 62060e402fda8a1c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_track_cash_position_agent.py` first:

```bash
python3 report_track_cash_position_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_track_cash_position_agent.py   # or on stdin
python3 report_track_cash_position_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track cash position Summary Report — Builds a structured summary report of track cash position activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-track-cash-position
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_track_cash_position',
    "version": '2.0.0',
    "display_name": 'Track cash position Summary Report',
    "description": 'Builds a structured summary report of track cash position activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-track-cash-position',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-track-cash-position',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b1fcdda37f6b7311',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/track-cash-position'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/report-track-cash-position', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ReportTrackCashPosition(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportTrackCashPosition'
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
    print(ReportTrackCashPosition().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
