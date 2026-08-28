---
name: "rar-cowork-cookbook-report-create-and-track-service-level-agreements"
description: "Builds a structured summary report of create and track service level agreements activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_create_and_track_service_level_agreements", "rar_sha256": "de3f308f88bff982258b839900850d66fa52358d8aa021e86d482871b5a27f5a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_create_and_track_service_level_agreements`. The original RAPP
agent is preserved byte-for-byte in `report_create_and_track_service_level_agreements_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_create_and_track_service_level_agreements_agent.py` and embedded as the fenced Python below (sha256 de3f308f88bff982…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_create_and_track_service_level_agreements_agent.py` first:

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
    "version": '2.0.1',
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
