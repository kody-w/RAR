---
name: "rar-cowork-cookbook-audit-implement-the-disaster-recovery-plan"
description: "Audits implement the disaster recovery plan records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_implement_the_disaster_recovery_plan", "rar_sha256": "786b8d7eb61883e3f4cd050612659a547c98a95bf8b06fdcea9c8b6312a47919", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_implement_the_disaster_recovery_plan_agent.py` and embedded as the fenced Python below (sha256 786b8d7eb61883e3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_implement_the_disaster_recovery_plan_agent.py` first:

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
    "version": '2.0.1',
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
