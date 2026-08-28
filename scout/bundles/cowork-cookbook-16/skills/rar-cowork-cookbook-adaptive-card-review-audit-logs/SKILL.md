---
name: "rar-cowork-cookbook-adaptive-card-review-audit-logs"
description: "Produces a reusable Adaptive Card JSON snapshot of review audit logs status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_review_audit_logs", "rar_sha256": "a0b50b13b8bb1619cb2e956376f11b1aa0cca5835e4b4fa6cb8e9c62e976fd1a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_review_audit_logs_agent.py` and embedded as the fenced Python below (sha256 a0b50b13b8bb1619…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_review_audit_logs_agent.py` first:

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
    "version": '2.0.1',
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
