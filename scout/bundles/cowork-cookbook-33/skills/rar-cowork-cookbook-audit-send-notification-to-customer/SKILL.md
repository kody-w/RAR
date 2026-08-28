---
name: "rar-cowork-cookbook-audit-send-notification-to-customer"
description: "Audits send notification to customer records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_send_notification_to_customer", "rar_sha256": "cbc8b02b908eab3087423d623d0264b0096664ffd98caf99700743fd9b27dfba", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_send_notification_to_customer_agent.py` and embedded as the fenced Python below (sha256 cbc8b02b908eab30…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_send_notification_to_customer_agent.py` first:

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
    "version": '2.0.0',
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
