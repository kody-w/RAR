---
name: "rar-cowork-cookbook-report-track-cash-position"
description: "Builds a structured summary report of track cash position activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_track_cash_position", "rar_sha256": "62060e402fda8a1c638acbcab19881b096fe9023b86e59cae08c2b52933cdfd6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_track_cash_position`. The original RAPP
agent is preserved byte-for-byte in `report_track_cash_position_agent.py` and in the RCI capsule.

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
