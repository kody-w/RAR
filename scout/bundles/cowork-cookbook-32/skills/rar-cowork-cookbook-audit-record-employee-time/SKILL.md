---
name: "rar-cowork-cookbook-audit-record-employee-time"
description: "Audits record employee time records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_record_employee_time", "rar_sha256": "b0efe0c777205a4c27989b1236886daa6e22082eeae32186f9a2fda63b4a9767", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_record_employee_time_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-record-employee-time:64ffdedda57bfc3e0f5cb76c6a8ad613fc27113e37a104081232541dd6da9182", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_record_employee_time`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_record_employee_time_agent.py` is
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

Record employee time Completeness Audit — Audits record employee time records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-record-employee-time
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_record_employee_time_agent.py` and embedded as the fenced Python below (sha256 b0efe0c777205a4c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_record_employee_time_agent.py` first:

```bash
python3 audit_record_employee_time_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_record_employee_time_agent.py   # or on stdin
python3 audit_record_employee_time_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record employee time Completeness Audit — Audits record employee time records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-record-employee-time
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_record_employee_time',
    "version": '2.0.0',
    "display_name": 'Record employee time Completeness Audit',
    "description": 'Audits record employee time records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-record-employee-time',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-record-employee-time',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f7dc6e2d17c60c67',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/record-employee-time'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-record-employee-time', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditRecordEmployeeTime(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditRecordEmployeeTime'
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
    print(AuditRecordEmployeeTime().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
