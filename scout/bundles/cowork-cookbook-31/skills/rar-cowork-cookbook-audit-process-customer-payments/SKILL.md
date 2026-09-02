---
name: "rar-cowork-cookbook-audit-process-customer-payments"
description: "Audits process customer payments records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_process_customer_payments", "rar_sha256": "da21d9f3a3ba07c47b45f92b4c992fe465bd748830c2f27f1d289864926149c1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_process_customer_payments_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-process-customer-payments:053e2911aa542ce138d0a1a46dd4f9887880122396aa9e29a8e994508d65773d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_process_customer_payments`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_process_customer_payments_agent.py` is
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

Process customer payments Completeness Audit — Audits process customer payments records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-customer-payments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_process_customer_payments_agent.py` and embedded as the fenced Python below (sha256 da21d9f3a3ba07c4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_process_customer_payments_agent.py` first:

```bash
python3 audit_process_customer_payments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_process_customer_payments_agent.py   # or on stdin
python3 audit_process_customer_payments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer payments Completeness Audit — Audits process customer payments records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-customer-payments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_process_customer_payments',
    "version": '2.0.0',
    "display_name": 'Process customer payments Completeness Audit',
    "description": 'Audits process customer payments records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-process-customer-payments',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-process-customer-payments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '484dc027260ab798',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/process-customer-payments'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/audit-process-customer-payments', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditProcessCustomerPayments(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditProcessCustomerPayments'
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
    print(AuditProcessCustomerPayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
