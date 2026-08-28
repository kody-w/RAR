---
name: "rar-cowork-cookbook-audit-define-employee-career-paths"
description: "Audits define employee career paths records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_employee_career_paths", "rar_sha256": "011bacfe1fe3f90792abdb532b6c371b22ad0b12d6859bd56db5ef4b5afbd8e5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_define_employee_career_paths`. The original RAPP
agent is preserved byte-for-byte in `audit_define_employee_career_paths_agent.py` and in the RCI capsule.

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

Define employee career paths Completeness Audit — Audits define employee career paths records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-employee-career-paths
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_employee_career_paths_agent.py` and embedded as the fenced Python below (sha256 011bacfe1fe3f907…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_employee_career_paths_agent.py` first:

```bash
python3 audit_define_employee_career_paths_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_employee_career_paths_agent.py   # or on stdin
python3 audit_define_employee_career_paths_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define employee career paths Completeness Audit — Audits define employee career paths records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-employee-career-paths
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_employee_career_paths',
    "version": '2.0.1',
    "display_name": 'Define employee career paths Completeness Audit',
    "description": 'Audits define employee career paths records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-define-employee-career-paths',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-employee-career-paths',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '47f10fa6afbac9ee',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/define-employee-career-paths'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-define-employee-career-paths', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditDefineEmployeeCareerPaths(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineEmployeeCareerPaths'
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
    print(AuditDefineEmployeeCareerPaths().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
