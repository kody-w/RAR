---
name: "rar-cowork-cookbook-audit-develop-leave-and-absence-policies"
description: "Audits develop leave and absence policies records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_leave_and_absence_policies", "rar_sha256": "606fb1be5d6de0889972ee322b4574e5779ab3599dff728b8f66d1c2a3e73d6d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_develop_leave_and_absence_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-develop-leave-and-absence-policies:4c2cf7f628b68a5073d937a1a9010f32e70cd57566d9de2bc7bf2024f33b1b94", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_develop_leave_and_absence_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_develop_leave_and_absence_policies_agent.py` is
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

Develop leave and absence policies Completeness Audit — Audits develop leave and absence policies records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-leave-and-absence-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_leave_and_absence_policies_agent.py` and embedded as the fenced Python below (sha256 606fb1be5d6de088…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_leave_and_absence_policies_agent.py` first:

```bash
python3 audit_develop_leave_and_absence_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_leave_and_absence_policies_agent.py   # or on stdin
python3 audit_develop_leave_and_absence_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop leave and absence policies Completeness Audit — Audits develop leave and absence policies records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-leave-and-absence-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_leave_and_absence_policies',
    "version": '2.0.0',
    "display_name": 'Develop leave and absence policies Completeness Audit',
    "description": 'Audits develop leave and absence policies records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-develop-leave-and-absence-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-leave-and-absence-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '90daad5bfa490e56',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/develop-leave-and-absence-policies'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-develop-leave-and-absence-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditDevelopLeaveAndAbsencePolicies(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopLeaveAndAbsencePolicies'
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
    print(AuditDevelopLeaveAndAbsencePolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
