---
name: "rar-cowork-cookbook-report-test-and-validate-the-disaster-recovery-plan"
description: "Builds a structured summary report of test and validate the disaster recovery plan activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_test_and_validate_the_disaster_recovery_plan", "rar_sha256": "68ed0b053676ca2bb87f9d14e0ab653d7ff70f37c75d0bccdbdfac83876207cf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_test_and_validate_the_disaster_recovery_plan`. The original RAPP
agent is preserved byte-for-byte in `report_test_and_validate_the_disaster_recovery_plan_agent.py` and in the RCI capsule.

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

Test and validate the disaster recovery plan Summary Report — Builds a structured summary report of test and validate the disaster recovery plan activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-test-and-validate-the-disaster-recovery-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_test_and_validate_the_disaster_recovery_plan_agent.py` and embedded as the fenced Python below (sha256 68ed0b053676ca2b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_test_and_validate_the_disaster_recovery_plan_agent.py` first:

```bash
python3 report_test_and_validate_the_disaster_recovery_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_test_and_validate_the_disaster_recovery_plan_agent.py   # or on stdin
python3 report_test_and_validate_the_disaster_recovery_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Test and validate the disaster recovery plan Summary Report — Builds a structured summary report of test and validate the disaster recovery plan activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-test-and-validate-the-disaster-recovery-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_test_and_validate_the_disaster_recovery_plan',
    "version": '2.0.0',
    "display_name": 'Test and validate the disaster recovery plan Summary Report',
    "description": 'Builds a structured summary report of test and validate the disaster recovery plan activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-test-and-validate-the-disaster-recovery-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-test-and-validate-the-disaster-recovery-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0820da01225043dc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/test-and-validate-the-disaster-recovery-plan'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-test-and-validate-the-disaster-recovery-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.25, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportTestAndValidateTheDisasterRecoveryPlan(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportTestAndValidateTheDisasterRecoveryPlan'
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
    print(ReportTestAndValidateTheDisasterRecoveryPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
