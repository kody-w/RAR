---
name: "rar-cowork-cookbook-user-access-review-audit"
description: "Audits Dynamics 365 user accounts for segregation-of-duties conflicts, inactive accounts with active role assignments, and roles granted without recent login."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/user_access_review_audit", "rar_sha256": "d274d9c1c300ae5f3e8eafe595379d5d50ec69b4b4e4a112785cbd3d17bb130e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "user_access_review_audit_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/user-access-review-audit:fc2e9bd43d13877c7be066cf365f3cb8d7509dc7fbee478f6ccbcfaa678374e5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/user_access_review_audit`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `user_access_review_audit_agent.py` is
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

User Access Review & SoD Audit — Audits Dynamics 365 user accounts for segregation-of-duties conflicts, inactive accounts with active role assignments, and roles granted without recent login.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/user-access-review-audit
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `user_access_review_audit_agent.py` and embedded as the fenced Python below (sha256 d274d9c1c300ae5f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `user_access_review_audit_agent.py` first:

```bash
python3 user_access_review_audit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 user_access_review_audit_agent.py   # or on stdin
python3 user_access_review_audit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
User Access Review & SoD Audit — Audits Dynamics 365 user accounts for segregation-of-duties conflicts, inactive accounts with active role assignments, and roles granted without recent login.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/user-access-review-audit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/user_access_review_audit',
    "version": '2.0.0',
    "display_name": 'User Access Review & SoD Audit',
    "description": 'Audits Dynamics 365 user accounts for segregation-of-duties conflicts, inactive accounts with active role assignments, and roles granted without recent login.',
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
        "upstream_slug": 'user-access-review-audit',
        "upstream_url": 'https://coworkcookbook.com/recipes/user-access-review-audit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '37bcf4aff678f487',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/user-access-review-audit', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Email'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:audit', 'word:review'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class UserAccessReviewAudit(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'UserAccessReviewAudit'
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
    print(UserAccessReviewAudit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
