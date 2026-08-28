---
name: "rar-cowork-cookbook-audit-test-and-validate-the-business-continuity-plan"
description: "Audits test and validate the business continuity plan records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_test_and_validate_the_business_continuity_plan", "rar_sha256": "2fe7a5633e21f1a9430eab520cc7383b4116f3314cd713dabffbff01e473447d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_test_and_validate_the_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 2fe7a5633e21f1a9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_test_and_validate_the_business_continuity_plan_agent.py` first:

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
    "version": '2.0.1',
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
