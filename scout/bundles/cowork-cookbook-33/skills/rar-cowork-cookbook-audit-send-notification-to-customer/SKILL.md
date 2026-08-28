---
name: "rar-cowork-cookbook-audit-send-notification-to-customer"
description: "Audits send notification to customer records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_send_notification_to_customer", "rar_sha256": "14d9906ace690fa10ca806bc4ff2d03f747ef8cc8e28925500c1a7a59ea0be7d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_send_notification_to_customer`. The original RAPP
agent is preserved byte-for-byte in `audit_send_notification_to_customer_agent.py` and in the RCI capsule.

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

Send notification to customer Completeness Audit — Audits send notification to customer records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-send-notification-to-customer
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_send_notification_to_customer_agent.py` and embedded as the fenced Python below (sha256 14d9906ace690fa1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_send_notification_to_customer_agent.py` first:

```bash
python3 audit_send_notification_to_customer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_send_notification_to_customer_agent.py   # or on stdin
python3 audit_send_notification_to_customer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Send notification to customer Completeness Audit — Audits send notification to customer records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-send-notification-to-customer
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_send_notification_to_customer',
    "version": '2.0.1',
    "display_name": 'Send notification to customer Completeness Audit',
    "description": 'Audits send notification to customer records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-send-notification-to-customer',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-send-notification-to-customer',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd619b1b345403e2a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/intake-cases/send-notification-to-customer'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/audit-send-notification-to-customer', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditSendNotificationToCustomer(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditSendNotificationToCustomer'
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
    print(AuditSendNotificationToCustomer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
