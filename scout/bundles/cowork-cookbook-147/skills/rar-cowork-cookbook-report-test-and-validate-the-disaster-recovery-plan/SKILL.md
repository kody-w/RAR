---
name: "rar-cowork-cookbook-report-test-and-validate-the-disaster-recovery-plan"
description: "Builds a structured summary report of test and validate the disaster recovery plan activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_test_and_validate_the_disaster_recovery_plan", "rar_sha256": "68ed0b053676ca2bb87f9d14e0ab653d7ff70f37c75d0bccdbdfac83876207cf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_test_and_validate_the_disaster_recovery_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-test-and-validate-the-disaster-recovery-plan:88307d1e773c9751a65eb2d4f7452bf90ef695988f8e8b69527c829f4a418525", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_test_and_validate_the_disaster_recovery_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_test_and_validate_the_disaster_recovery_plan_agent.py` is
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
