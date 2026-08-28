---
name: "rar-cowork-cookbook-report-record-life-events"
description: "Builds a structured summary report of record life events activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_record_life_events", "rar_sha256": "1c101960babca3a7551ea32d030f82b9507ddc0164361be33b6db1b74e23d114", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_record_life_events`. The original RAPP
agent is preserved byte-for-byte in `report_record_life_events_agent.py` and in the RCI capsule.

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
