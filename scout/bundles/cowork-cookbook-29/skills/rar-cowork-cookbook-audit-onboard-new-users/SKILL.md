---
name: "rar-cowork-cookbook-audit-onboard-new-users"
description: "Audits onboard new users records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_onboard_new_users", "rar_sha256": "411f42fd0fa1a4da7a1eb620a09cd9bfcd6559cb27827ad2566660273b17a9ff", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_onboard_new_users_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-onboard-new-users:c446a17fb46430e27235cffd960c310170a25a5e5b00b2a5055a7ee6f654a092", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_onboard_new_users`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_onboard_new_users_agent.py` is
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

Onboard new users Completeness Audit — Audits onboard new users records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-onboard-new-users
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_onboard_new_users_agent.py` and embedded as the fenced Python below (sha256 411f42fd0fa1a4da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_onboard_new_users_agent.py` first:

```bash
python3 audit_onboard_new_users_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_onboard_new_users_agent.py   # or on stdin
python3 audit_onboard_new_users_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard new users Completeness Audit — Audits onboard new users records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-onboard-new-users
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_onboard_new_users',
    "version": '2.0.0',
    "display_name": 'Onboard new users Completeness Audit',
    "description": 'Audits onboard new users records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-onboard-new-users',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-onboard-new-users',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '910d3d8f3015fc9f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-04', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/onboard-new-users'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-onboard-new-users', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditOnboardNewUsers(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditOnboardNewUsers'
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
    print(AuditOnboardNewUsers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
