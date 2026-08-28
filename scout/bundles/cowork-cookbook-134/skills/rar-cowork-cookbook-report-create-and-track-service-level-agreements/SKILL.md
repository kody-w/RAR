---
name: "rar-cowork-cookbook-report-create-and-track-service-level-agreements"
description: "Builds a structured summary report of create and track service level agreements activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_create_and_track_service_level_agreements", "rar_sha256": "ff2df6d1a5ecf3a04ef4f27fbcacada861034f3599bb8d85bc5a90e304644062", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
