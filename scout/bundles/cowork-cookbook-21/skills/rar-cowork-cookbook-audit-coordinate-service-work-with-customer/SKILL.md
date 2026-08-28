---
name: "rar-cowork-cookbook-audit-coordinate-service-work-with-customer"
description: "Audits coordinate service work with customer records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_coordinate_service_work_with_customer", "rar_sha256": "50351fc14b4eb86dc528303ee84510b0966f606343d6f102e7e81be26398a53f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_coordinate_service_work_with_customer`. The original RAPP
agent is preserved byte-for-byte in `audit_coordinate_service_work_with_customer_agent.py` and in the RCI capsule.

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
