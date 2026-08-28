---
name: "rar-cowork-cookbook-audit-process-customer-payments"
description: "Audits process customer payments records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_process_customer_payments", "rar_sha256": "7b61ef743863cb584b21540dd59784ee24ad7babe06ac099c67a344b7284151e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_process_customer_payments`. The original RAPP
agent is preserved byte-for-byte in `audit_process_customer_payments_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_process_customer_payments_agent.py` and embedded as the fenced Python below (sha256 7b61ef743863cb58…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_process_customer_payments_agent.py` first:

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
    "version": '2.0.1',
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
