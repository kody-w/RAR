---
name: "rar-cowork-cookbook-audit-send-notification-to-customer"
description: "Audits send notification to customer records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_send_notification_to_customer", "rar_sha256": "cbc8b02b908eab3087423d623d0264b0096664ffd98caf99700743fd9b27dfba", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_send_notification_to_customer_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-send-notification-to-customer:4effd85fc6e26134d6c3910fab28b0db95e6553a7deebff2e965b533e64463f2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_send_notification_to_customer`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_send_notification_to_customer_agent.py` is
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
