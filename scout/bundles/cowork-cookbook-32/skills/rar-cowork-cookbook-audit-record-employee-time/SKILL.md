---
name: "rar-cowork-cookbook-audit-record-employee-time"
description: "Audits record employee time records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_record_employee_time", "rar_sha256": "4cb5ad858bdcb9d8da3aad688fc18e3b1b0fc1892c58d447369c739a09b887ec", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_record_employee_time_agent.py` and embedded as the fenced Python below (sha256 4cb5ad858bdcb9d8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_record_employee_time_agent.py` first:

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
    "version": '2.0.1',
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
