---
name: "rar-cowork-cookbook-audit-implement-the-disaster-recovery-plan"
description: "Audits implement the disaster recovery plan records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_implement_the_disaster_recovery_plan", "rar_sha256": "cd387e7d4caa694d106eaa4833df3192d7269f6e54c25e2276e9d00ea6328bde", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_implement_the_disaster_recovery_plan`. The original RAPP
agent is preserved byte-for-byte in `audit_implement_the_disaster_recovery_plan_agent.py` and in the RCI capsule.

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
