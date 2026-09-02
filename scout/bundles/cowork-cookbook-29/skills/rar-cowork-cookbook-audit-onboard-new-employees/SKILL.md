---
name: "rar-cowork-cookbook-audit-onboard-new-employees"
description: "Audits onboard new employees records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_onboard_new_employees", "rar_sha256": "af3a795f5c1c5d53d868a79017c8d75e55748a364ee4f3997e13880551fcaea2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_onboard_new_employees_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-onboard-new-employees:bb84a3bceaae04f5c2639794b77f16533d9f81e0b0bd9cb6a083231113a4c4fd", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_onboard_new_employees`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_onboard_new_employees_agent.py` is
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

Onboard new employees Completeness Audit — Audits onboard new employees records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-onboard-new-employees
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_onboard_new_employees_agent.py` and embedded as the fenced Python below (sha256 af3a795f5c1c5d53…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_onboard_new_employees_agent.py` first:

```bash
python3 audit_onboard_new_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_onboard_new_employees_agent.py   # or on stdin
python3 audit_onboard_new_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard new employees Completeness Audit — Audits onboard new employees records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-onboard-new-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_onboard_new_employees',
    "version": '2.0.0',
    "display_name": 'Onboard new employees Completeness Audit',
    "description": 'Audits onboard new employees records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-onboard-new-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-onboard-new-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a25eeee8249c0223',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/onboard-new-employees'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-onboard-new-employees', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditOnboardNewEmployees(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditOnboardNewEmployees'
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
    print(AuditOnboardNewEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
