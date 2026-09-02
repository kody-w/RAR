---
name: "rar-cowork-cookbook-report-record-life-events"
description: "Builds a structured summary report of record life events activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_record_life_events", "rar_sha256": "1c101960babca3a7551ea32d030f82b9507ddc0164361be33b6db1b74e23d114", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_record_life_events_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-record-life-events:897d27e565c2ce88c8abeef0122bbce8b00011a51f117d00d76e54a1a7438225", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_record_life_events`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_record_life_events_agent.py` is
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

Record life events Summary Report — Builds a structured summary report of record life events activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-record-life-events
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_record_life_events_agent.py` and embedded as the fenced Python below (sha256 1c101960babca3a7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_record_life_events_agent.py` first:

```bash
python3 report_record_life_events_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_record_life_events_agent.py   # or on stdin
python3 report_record_life_events_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record life events Summary Report — Builds a structured summary report of record life events activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-record-life-events
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_record_life_events',
    "version": '2.0.0',
    "display_name": 'Record life events Summary Report',
    "description": 'Builds a structured summary report of record life events activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-record-life-events',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-record-life-events',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '537b6f7ea42d87f6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/record-life-events'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-record-life-events', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportRecordLifeEvents(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportRecordLifeEvents'
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
    print(ReportRecordLifeEvents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
