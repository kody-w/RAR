---
name: "rar-cowork-cookbook-audit-issue-purchase-orders"
description: "Audits issue purchase orders records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_issue_purchase_orders", "rar_sha256": "1c3d4ed03c50af539e0a4a7bcbc27184240d0fe5b8f12c7877b3c90be8fcf48c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_issue_purchase_orders_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-issue-purchase-orders:bed541bd7500af0e65ae56a789551b76f183dd74b17119430544e406a974e738", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_issue_purchase_orders`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_issue_purchase_orders_agent.py` is
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

Issue purchase orders Completeness Audit — Audits issue purchase orders records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-issue-purchase-orders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_issue_purchase_orders_agent.py` and embedded as the fenced Python below (sha256 1c3d4ed03c50af53…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_issue_purchase_orders_agent.py` first:

```bash
python3 audit_issue_purchase_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_issue_purchase_orders_agent.py   # or on stdin
python3 audit_issue_purchase_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue purchase orders Completeness Audit — Audits issue purchase orders records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-issue-purchase-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_issue_purchase_orders',
    "version": '2.0.0',
    "display_name": 'Issue purchase orders Completeness Audit',
    "description": 'Audits issue purchase orders records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-issue-purchase-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-issue-purchase-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd5fa878ebc906e98',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/issue-purchase-orders'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/audit-issue-purchase-orders', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditIssuePurchaseOrders(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditIssuePurchaseOrders'
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
    print(AuditIssuePurchaseOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
