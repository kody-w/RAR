---
name: "rar-cowork-cookbook-audit-plan-training-delivery"
description: "Audits plan training delivery records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_training_delivery", "rar_sha256": "02b105e392ef4c275f64a7d4c00a72d1f7d78067a8e99a56b3de77b144a7c44d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_plan_training_delivery`. The original RAPP
agent is preserved byte-for-byte in `audit_plan_training_delivery_agent.py` and in the RCI capsule.

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
