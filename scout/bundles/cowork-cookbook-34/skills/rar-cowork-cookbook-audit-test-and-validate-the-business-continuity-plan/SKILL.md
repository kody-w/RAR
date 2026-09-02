---
name: "rar-cowork-cookbook-audit-test-and-validate-the-business-continuity-plan"
description: "Audits test and validate the business continuity plan records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_test_and_validate_the_business_continuity_plan", "rar_sha256": "b48b80a30883eee53cd27f64a976f85afb025318a4da0c1c6e32f201143fb617", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_test_and_validate_the_business_continuity_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-test-and-validate-the-business-continuity-plan:c31bfb5a521107388d5d0bc8be2d6c85f0c83b401178c397223b952b840b62fc", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_test_and_validate_the_business_continuity_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_test_and_validate_the_business_continuity_plan_agent.py` is
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

Test and validate the business continuity plan Completeness Audit — Audits test and validate the business continuity plan records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-test-and-validate-the-business-continuity-plan
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
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
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
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_test_and_validate_the_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 b48b80a30883eee5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_test_and_validate_the_business_continuity_plan_agent.py` first:

```bash
python3 audit_test_and_validate_the_business_continuity_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_test_and_validate_the_business_continuity_plan_agent.py   # or on stdin
python3 audit_test_and_validate_the_business_continuity_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Test and validate the business continuity plan Completeness Audit — Audits test and validate the business continuity plan records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-test-and-validate-the-business-continuity-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_test_and_validate_the_business_continuity_plan',
    "version": '2.0.0',
    "display_name": 'Test and validate the business continuity plan Completeness Audit',
    "description": 'Audits test and validate the business continuity plan records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'audit-test-and-validate-the-business-continuity-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-test-and-validate-the-business-continuity-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '064a8e9cedaaca59',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-04', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/test-and-validate-the-business-continuity-plan'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-test-and-validate-the-business-continuity-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.545, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance', 'word:validate'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditTestAndValidateTheBusinessContinuityPlan(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditTestAndValidateTheBusinessContinuityPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(AuditTestAndValidateTheBusinessContinuityPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
