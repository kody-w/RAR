---
name: "rar-cowork-cookbook-audit-plan-projects-resources"
description: "Audits plan projects resources records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_projects_resources", "rar_sha256": "7369ce7fe1ae5f8bdb43db714fe90814de5d6c24291837d51b75e110db31519d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_plan_projects_resources_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-plan-projects-resources:433dbfb1e92b89c56911437521c5dd9d68c8927ebeedf6c1c38b6963edc1ad04", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_plan_projects_resources`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_plan_projects_resources_agent.py` is
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

Plan projects resources Completeness Audit — Audits plan projects resources records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-projects-resources
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_plan_projects_resources_agent.py` and embedded as the fenced Python below (sha256 7369ce7fe1ae5f8b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_plan_projects_resources_agent.py` first:

```bash
python3 audit_plan_projects_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_plan_projects_resources_agent.py   # or on stdin
python3 audit_plan_projects_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan projects resources Completeness Audit — Audits plan projects resources records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-projects-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_plan_projects_resources',
    "version": '2.0.0',
    "display_name": 'Plan projects resources Completeness Audit',
    "description": 'Audits plan projects resources records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-plan-projects-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-plan-projects-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cbcec43c82deb947',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/plan-projects-resources'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/audit-plan-projects-resources', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditPlanProjectsResources(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPlanProjectsResources'
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
    print(AuditPlanProjectsResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
