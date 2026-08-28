---
name: "rar-cowork-cookbook-audit-test-and-validate-the-business-continuity-plan"
description: "Audits test and validate the business continuity plan records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_test_and_validate_the_business_continuity_plan", "rar_sha256": "b48b80a30883eee53cd27f64a976f85afb025318a4da0c1c6e32f201143fb617", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_test_and_validate_the_business_continuity_plan`. The original RAPP
agent is preserved byte-for-byte in `audit_test_and_validate_the_business_continuity_plan_agent.py` and in the RCI capsule.

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
