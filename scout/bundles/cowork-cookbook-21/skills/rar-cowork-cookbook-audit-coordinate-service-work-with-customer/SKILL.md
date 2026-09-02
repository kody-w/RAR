---
name: "rar-cowork-cookbook-audit-coordinate-service-work-with-customer"
description: "Audits coordinate service work with customer records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_coordinate_service_work_with_customer", "rar_sha256": "50351fc14b4eb86dc528303ee84510b0966f606343d6f102e7e81be26398a53f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_coordinate_service_work_with_customer_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-coordinate-service-work-with-customer:e7f8e2477ef58806787f4fbfc981d215e757c008cda8851d3e9ebd4c642c41f6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_coordinate_service_work_with_customer`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_coordinate_service_work_with_customer_agent.py` is
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

Coordinate service work with customer Completeness Audit — Audits coordinate service work with customer records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-coordinate-service-work-with-customer
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_coordinate_service_work_with_customer_agent.py` and embedded as the fenced Python below (sha256 50351fc14b4eb86d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_coordinate_service_work_with_customer_agent.py` first:

```bash
python3 audit_coordinate_service_work_with_customer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_coordinate_service_work_with_customer_agent.py   # or on stdin
python3 audit_coordinate_service_work_with_customer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Coordinate service work with customer Completeness Audit — Audits coordinate service work with customer records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-coordinate-service-work-with-customer
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_coordinate_service_work_with_customer',
    "version": '2.0.0',
    "display_name": 'Coordinate service work with customer Completeness Audit',
    "description": 'Audits coordinate service work with customer records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-coordinate-service-work-with-customer',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-coordinate-service-work-with-customer',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cd8116ca1f4d874a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/coordinate-service-work-with-customer'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/audit-coordinate-service-work-with-customer', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.556, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditCoordinateServiceWorkWithCustomer(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditCoordinateServiceWorkWithCustomer'
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
    print(AuditCoordinateServiceWorkWithCustomer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
