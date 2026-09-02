---
name: "rar-cowork-cookbook-audit-plan-service-operations"
description: "Audits plan service operations records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_service_operations", "rar_sha256": "dc13b6b34eb220f1bb2e55c652ba2345edd833827a94e8c96dbea4505b39b67f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_plan_service_operations_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-plan-service-operations:ca336736d2a65a9ea598e05b73d0cfb83a6f13cfca27dea10fcc010496edd145", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_plan_service_operations`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_plan_service_operations_agent.py` is
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

Plan service operations Completeness Audit — Audits plan service operations records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-service-operations
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_plan_service_operations_agent.py` and embedded as the fenced Python below (sha256 dc13b6b34eb220f1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_plan_service_operations_agent.py` first:

```bash
python3 audit_plan_service_operations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_plan_service_operations_agent.py   # or on stdin
python3 audit_plan_service_operations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan service operations Completeness Audit — Audits plan service operations records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-service-operations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_plan_service_operations',
    "version": '2.0.0',
    "display_name": 'Plan service operations Completeness Audit',
    "description": 'Audits plan service operations records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-plan-service-operations',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-plan-service-operations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ee13b3cc6d7fa02f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-service-operations'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/audit-plan-service-operations', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditPlanServiceOperations(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPlanServiceOperations'
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
    print(AuditPlanServiceOperations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
