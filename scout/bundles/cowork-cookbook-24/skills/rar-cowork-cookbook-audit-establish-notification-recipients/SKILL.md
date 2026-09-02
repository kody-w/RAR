---
name: "rar-cowork-cookbook-audit-establish-notification-recipients"
description: "Audits establish notification recipients records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_establish_notification_recipients", "rar_sha256": "ac835e0c1d0b7d22a248b4397f9fecbfa57e74805f8ad7be0afdabaf7cbccebe", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_establish_notification_recipients_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-establish-notification-recipients:84ad84ed3190e38423bbc0dee7484169248acc28a9eb240bab236e827325616c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_establish_notification_recipients`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_establish_notification_recipients_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_establish_notification_recipients_agent.py` and embedded as the fenced Python below (sha256 ac835e0c1d0b7d22…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_establish_notification_recipients_agent.py` first:

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
    "version": '2.0.0',
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
