---
name: "rar-cowork-cookbook-audit-process-customer-payments"
description: "Audits process customer payments records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_process_customer_payments", "rar_sha256": "da21d9f3a3ba07c47b45f92b4c992fe465bd748830c2f27f1d289864926149c1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
