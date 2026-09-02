---
name: "rar-cowork-cookbook-audit-manage-sales-order-changes"
description: "Audits manage sales order changes records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_sales_order_changes", "rar_sha256": "06e8e773594a545c80234542cb5e724784c72d2f645f739004585427a02a1358", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_manage_sales_order_changes_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-manage-sales-order-changes:60fadd7658c1f657c16a602c316da3872a07b82bc20c6a8a9d1fa3ca96fb7d04", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_manage_sales_order_changes`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_manage_sales_order_changes_agent.py` is
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

Manage sales order changes Completeness Audit — Audits manage sales order changes records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-sales-order-changes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_sales_order_changes_agent.py` and embedded as the fenced Python below (sha256 06e8e773594a545c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_sales_order_changes_agent.py` first:

```bash
python3 audit_manage_sales_order_changes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_manage_sales_order_changes_agent.py   # or on stdin
python3 audit_manage_sales_order_changes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage sales order changes Completeness Audit — Audits manage sales order changes records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-sales-order-changes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_manage_sales_order_changes',
    "version": '2.0.0',
    "display_name": 'Manage sales order changes Completeness Audit',
    "description": 'Audits manage sales order changes records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-manage-sales-order-changes',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-manage-sales-order-changes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b84adbe08e19b1c0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/manage-sales-order-changes'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/audit-manage-sales-order-changes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditManageSalesOrderChanges(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditManageSalesOrderChanges'
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
    print(AuditManageSalesOrderChanges().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
