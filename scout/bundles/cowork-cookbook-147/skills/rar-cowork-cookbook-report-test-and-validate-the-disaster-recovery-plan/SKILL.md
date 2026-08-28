---
name: "rar-cowork-cookbook-report-test-and-validate-the-disaster-recovery-plan"
description: "Builds a structured summary report of test and validate the disaster recovery plan activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_test_and_validate_the_disaster_recovery_plan", "rar_sha256": "ac416a223c3b0d6773492d3dfc593f93ae4385d62a165b63b4cee547b22dd162", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_test_and_validate_the_disaster_recovery_plan_agent.py` and embedded as the fenced Python below (sha256 ac416a223c3b0d67…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_test_and_validate_the_disaster_recovery_plan_agent.py` first:

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
    "version": '2.0.1',
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
