---
name: "rar-cowork-cookbook-audit-plan-training-delivery"
description: "Audits plan training delivery records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_training_delivery", "rar_sha256": "02b105e392ef4c275f64a7d4c00a72d1f7d78067a8e99a56b3de77b144a7c44d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_plan_training_delivery_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-plan-training-delivery:96b1ac0116551c630cd83898cade7339d5412204b5d976d84a4ce456d1face89", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_plan_training_delivery`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_plan_training_delivery_agent.py` is
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

Plan training delivery Completeness Audit — Audits plan training delivery records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-training-delivery
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_plan_training_delivery_agent.py` and embedded as the fenced Python below (sha256 02b105e392ef4c27…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_plan_training_delivery_agent.py` first:

```bash
python3 audit_plan_training_delivery_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_plan_training_delivery_agent.py   # or on stdin
python3 audit_plan_training_delivery_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan training delivery Completeness Audit — Audits plan training delivery records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-training-delivery
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_plan_training_delivery',
    "version": '2.0.0',
    "display_name": 'Plan training delivery Completeness Audit',
    "description": 'Audits plan training delivery records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-plan-training-delivery',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-plan-training-delivery',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '08f8d19104add6f3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-04', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/plan-training-delivery'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-plan-training-delivery', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditPlanTrainingDelivery(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPlanTrainingDelivery'
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
    print(AuditPlanTrainingDelivery().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
