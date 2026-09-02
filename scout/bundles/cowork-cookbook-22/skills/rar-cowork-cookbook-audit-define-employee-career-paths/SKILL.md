---
name: "rar-cowork-cookbook-audit-define-employee-career-paths"
description: "Audits define employee career paths records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_employee_career_paths", "rar_sha256": "b539a37888dc94a6cdf2730d074584ff8f3e1c238b494e67c7e2f103a91f908c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_define_employee_career_paths_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-define-employee-career-paths:d9146dbfbab519650159c54d47dab30b1ba37b11ffa6e0226e9c647874193d9e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_define_employee_career_paths`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_define_employee_career_paths_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_employee_career_paths_agent.py` and embedded as the fenced Python below (sha256 b539a37888dc94a6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_employee_career_paths_agent.py` first:

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
    "version": '2.0.0',
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
