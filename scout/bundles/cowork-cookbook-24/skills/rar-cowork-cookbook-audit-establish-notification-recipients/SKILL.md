---
name: "rar-cowork-cookbook-audit-establish-notification-recipients"
description: "Audits establish notification recipients records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_establish_notification_recipients", "rar_sha256": "00bfd7141876ca031b75e98d918386402b69505e5259c97e2d407efa3469aac5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_establish_notification_recipients`. The original RAPP
agent is preserved byte-for-byte in `audit_establish_notification_recipients_agent.py` and in the RCI capsule.

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

Establish notification recipients Completeness Audit — Audits establish notification recipients records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-establish-notification-recipients
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_establish_notification_recipients_agent.py` and embedded as the fenced Python below (sha256 00bfd7141876ca03…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_establish_notification_recipients_agent.py` first:

```bash
python3 audit_establish_notification_recipients_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_establish_notification_recipients_agent.py   # or on stdin
python3 audit_establish_notification_recipients_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish notification recipients Completeness Audit — Audits establish notification recipients records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-establish-notification-recipients
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_establish_notification_recipients',
    "version": '2.0.1',
    "display_name": 'Establish notification recipients Completeness Audit',
    "description": 'Audits establish notification recipients records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-establish-notification-recipients',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-establish-notification-recipients',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4e70419655041d7a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-03', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/establish-notification-recipients'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-establish-notification-recipients', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditEstablishNotificationRecipients(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditEstablishNotificationRecipients'
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
    print(AuditEstablishNotificationRecipients().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
