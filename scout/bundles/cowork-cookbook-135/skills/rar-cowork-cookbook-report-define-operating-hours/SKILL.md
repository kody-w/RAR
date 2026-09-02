---
name: "rar-cowork-cookbook-report-define-operating-hours"
description: "Builds a structured summary report of define operating hours activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_operating_hours", "rar_sha256": "97be3aa7d198390e67391aaee67aefddcf2de79d418e6916f1b29b1d211963ba", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_define_operating_hours_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-define-operating-hours:872707239f19402f128664ea01090dbeb4571438e3e8f4f4c843e78c1e7127c6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_define_operating_hours`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_define_operating_hours_agent.py` is
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

Define operating hours Summary Report — Builds a structured summary report of define operating hours activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-operating-hours
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_operating_hours_agent.py` and embedded as the fenced Python below (sha256 97be3aa7d198390e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_operating_hours_agent.py` first:

```bash
python3 report_define_operating_hours_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_operating_hours_agent.py   # or on stdin
python3 report_define_operating_hours_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define operating hours Summary Report — Builds a structured summary report of define operating hours activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-operating-hours
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_operating_hours',
    "version": '2.0.0',
    "display_name": 'Define operating hours Summary Report',
    "description": 'Builds a structured summary report of define operating hours activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-define-operating-hours',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-operating-hours',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'eda323bd08f19fe4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-operating-hours'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/report-define-operating-hours', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.286, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportDefineOperatingHours(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineOperatingHours'
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
    print(ReportDefineOperatingHours().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
