---
name: "rar-cowork-cookbook-report-identify-business-continuity-risks"
description: "Builds a structured summary report of identify business continuity risks activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_identify_business_continuity_risks", "rar_sha256": "12190d3db1f8c1038dbb7a770ca06f89d20c3a1701f530eff289403cab575e5f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_identify_business_continuity_risks_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-identify-business-continuity-risks:3379373c973eccd3bd33d61bc1bf3d9e8909261a589c76d77fb8dc2b402452ca", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_identify_business_continuity_risks`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_identify_business_continuity_risks_agent.py` is
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

Identify business continuity risks Summary Report — Builds a structured summary report of identify business continuity risks activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-identify-business-continuity-risks
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_identify_business_continuity_risks_agent.py` and embedded as the fenced Python below (sha256 12190d3db1f8c103…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_identify_business_continuity_risks_agent.py` first:

```bash
python3 report_identify_business_continuity_risks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_identify_business_continuity_risks_agent.py   # or on stdin
python3 report_identify_business_continuity_risks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify business continuity risks Summary Report — Builds a structured summary report of identify business continuity risks activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-identify-business-continuity-risks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_identify_business_continuity_risks',
    "version": '2.0.0',
    "display_name": 'Identify business continuity risks Summary Report',
    "description": 'Builds a structured summary report of identify business continuity risks activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-identify-business-continuity-risks',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-identify-business-continuity-risks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '55173d5db73adba5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/identify-business-continuity-risks'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-identify-business-continuity-risks', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportIdentifyBusinessContinuityRisks(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportIdentifyBusinessContinuityRisks'
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
    print(ReportIdentifyBusinessContinuityRisks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
