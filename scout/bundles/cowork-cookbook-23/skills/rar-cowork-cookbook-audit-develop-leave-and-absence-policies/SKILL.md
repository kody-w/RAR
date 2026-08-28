---
name: "rar-cowork-cookbook-audit-develop-leave-and-absence-policies"
description: "Audits develop leave and absence policies records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_leave_and_absence_policies", "rar_sha256": "606fb1be5d6de0889972ee322b4574e5779ab3599dff728b8f66d1c2a3e73d6d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_develop_leave_and_absence_policies`. The original RAPP
agent is preserved byte-for-byte in `audit_develop_leave_and_absence_policies_agent.py` and in the RCI capsule.

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
