---
name: "rar-cowork-cookbook-adaptive-card-review-audit-logs"
description: "Produces a reusable Adaptive Card JSON snapshot of review audit logs status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_review_audit_logs", "rar_sha256": "72aa7e8715187a0b9d26804af1802e059936faf4194df4331b6def50c2ae55ec", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_review_audit_logs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-review-audit-logs:010f7151581468b8acd55e9d09ff3c4d012b24a4c0642859faa4f24916d86312", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_review_audit_logs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_review_audit_logs_agent.py` is
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

Review audit logs Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of review audit logs status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-review-audit-logs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_review_audit_logs_agent.py` and embedded as the fenced Python below (sha256 72aa7e8715187a0b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_review_audit_logs_agent.py` first:

```bash
python3 adaptive_card_review_audit_logs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_review_audit_logs_agent.py   # or on stdin
python3 adaptive_card_review_audit_logs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Review audit logs Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of review audit logs status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-review-audit-logs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_review_audit_logs',
    "version": '2.0.0',
    "display_name": 'Review audit logs Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of review audit logs status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-review-audit-logs',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-review-audit-logs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cb986a3b2f516f59',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/review-audit-logs'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-review-audit-logs', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['word:audit', 'word:review'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AdaptiveCardReviewAuditLogs(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardReviewAuditLogs'
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
    print(AdaptiveCardReviewAuditLogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
