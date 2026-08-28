---
name: "rar-cowork-cookbook-report-identify-business-continuity-risks"
description: "Builds a structured summary report of identify business continuity risks activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_identify_business_continuity_risks", "rar_sha256": "12190d3db1f8c1038dbb7a770ca06f89d20c3a1701f530eff289403cab575e5f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_identify_business_continuity_risks`. The original RAPP
agent is preserved byte-for-byte in `report_identify_business_continuity_risks_agent.py` and in the RCI capsule.

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
