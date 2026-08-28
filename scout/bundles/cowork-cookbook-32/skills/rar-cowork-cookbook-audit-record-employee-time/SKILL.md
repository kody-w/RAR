---
name: "rar-cowork-cookbook-audit-record-employee-time"
description: "Audits record employee time records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_record_employee_time", "rar_sha256": "b0efe0c777205a4c27989b1236886daa6e22082eeae32186f9a2fda63b4a9767", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_record_employee_time`. The original RAPP
agent is preserved byte-for-byte in `audit_record_employee_time_agent.py` and in the RCI capsule.

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
