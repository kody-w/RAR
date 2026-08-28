---
name: "rar-cowork-cookbook-audit-onboard-new-users"
description: "Audits onboard new users records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_onboard_new_users", "rar_sha256": "dfe194a42ca54e98f19abc5619162c68f914493f96d609514750736980ce809e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_onboard_new_users`. The original RAPP
agent is preserved byte-for-byte in `audit_onboard_new_users_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_onboard_new_users_agent.py` and embedded as the fenced Python below (sha256 dfe194a42ca54e98…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_onboard_new_users_agent.py` first:

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
    "version": '2.0.1',
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
