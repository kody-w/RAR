---
name: "rar-cowork-cookbook-audit-implement-the-disaster-recovery-plan"
description: "Audits implement the disaster recovery plan records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_implement_the_disaster_recovery_plan", "rar_sha256": "cd387e7d4caa694d106eaa4833df3192d7269f6e54c25e2276e9d00ea6328bde", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_implement_the_disaster_recovery_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-implement-the-disaster-recovery-plan:da313939f1bef1a278d8e2e6e857cf99828ec3c1d9c2b3d6b7c0bbcd90ec0875", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_implement_the_disaster_recovery_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_implement_the_disaster_recovery_plan_agent.py` is
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

Implement the disaster recovery plan Completeness Audit — Audits implement the disaster recovery plan records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-implement-the-disaster-recovery-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_implement_the_disaster_recovery_plan_agent.py` and embedded as the fenced Python below (sha256 cd387e7d4caa694d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_implement_the_disaster_recovery_plan_agent.py` first:

```bash
python3 audit_implement_the_disaster_recovery_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_implement_the_disaster_recovery_plan_agent.py   # or on stdin
python3 audit_implement_the_disaster_recovery_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement the disaster recovery plan Completeness Audit — Audits implement the disaster recovery plan records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-implement-the-disaster-recovery-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_implement_the_disaster_recovery_plan',
    "version": '2.0.0',
    "display_name": 'Implement the disaster recovery plan Completeness Audit',
    "description": 'Audits implement the disaster recovery plan records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-implement-the-disaster-recovery-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-implement-the-disaster-recovery-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8d61c97db21d4117',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-03', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/implement-the-disaster-recovery-plan'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-implement-the-disaster-recovery-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditImplementTheDisasterRecoveryPlan(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditImplementTheDisasterRecoveryPlan'
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
    print(AuditImplementTheDisasterRecoveryPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
