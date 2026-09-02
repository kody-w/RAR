---
name: "rar-cowork-cookbook-audit-plan-service-demand"
description: "Audits plan service demand records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_service_demand", "rar_sha256": "3ab88bdbd385b634df008cf9b82fb934130bb4c05cfd21f41312c58c5aeb8f5f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_plan_service_demand_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-plan-service-demand:d9206b711777089b7468280704c4b2ec5b20b954f03f0d9ba4b00369ac791c70", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_plan_service_demand`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_plan_service_demand_agent.py` is
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

Plan service demand Completeness Audit — Audits plan service demand records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-service-demand
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_plan_service_demand_agent.py` and embedded as the fenced Python below (sha256 3ab88bdbd385b634…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_plan_service_demand_agent.py` first:

```bash
python3 audit_plan_service_demand_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_plan_service_demand_agent.py   # or on stdin
python3 audit_plan_service_demand_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan service demand Completeness Audit — Audits plan service demand records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-service-demand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_plan_service_demand',
    "version": '2.0.0',
    "display_name": 'Plan service demand Completeness Audit',
    "description": 'Audits plan service demand records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-plan-service-demand',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-plan-service-demand',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fd2ef82b9eb4b48d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/plan-service-demand'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/audit-plan-service-demand', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditPlanServiceDemand(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPlanServiceDemand'
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
    print(AuditPlanServiceDemand().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
