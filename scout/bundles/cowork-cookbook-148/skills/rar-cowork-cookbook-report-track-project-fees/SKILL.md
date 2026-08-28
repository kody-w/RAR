---
name: "rar-cowork-cookbook-report-track-project-fees"
description: "Builds a structured summary report of track project fees activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_track_project_fees", "rar_sha256": "5fa5ba2dc740c53fc274edc9f7e2ca1e5b27888186511e159a2ba35bc1ba5be4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_track_project_fees`. The original RAPP
agent is preserved byte-for-byte in `report_track_project_fees_agent.py` and in the RCI capsule.

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
