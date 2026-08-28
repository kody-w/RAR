---
name: "rar-cowork-cookbook-adaptive-card-review-audit-logs"
description: "Produces a reusable Adaptive Card JSON snapshot of review audit logs status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_review_audit_logs", "rar_sha256": "72aa7e8715187a0b9d26804af1802e059936faf4194df4331b6def50c2ae55ec", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_review_audit_logs`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_review_audit_logs_agent.py` and in the RCI capsule.

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
