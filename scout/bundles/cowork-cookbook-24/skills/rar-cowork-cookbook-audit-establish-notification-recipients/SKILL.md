---
name: "rar-cowork-cookbook-audit-establish-notification-recipients"
description: "Audits establish notification recipients records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_establish_notification_recipients", "rar_sha256": "ac835e0c1d0b7d22a248b4397f9fecbfa57e74805f8ad7be0afdabaf7cbccebe", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
