---
name: "rar-cowork-cookbook-report-define-operating-hours"
description: "Builds a structured summary report of define operating hours activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_operating_hours", "rar_sha256": "97be3aa7d198390e67391aaee67aefddcf2de79d418e6916f1b29b1d211963ba", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_operating_hours`. The original RAPP
agent is preserved byte-for-byte in `report_define_operating_hours_agent.py` and in the RCI capsule.

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
