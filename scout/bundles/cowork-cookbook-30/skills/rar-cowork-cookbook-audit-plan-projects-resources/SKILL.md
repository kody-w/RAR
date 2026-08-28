---
name: "rar-cowork-cookbook-audit-plan-projects-resources"
description: "Audits plan projects resources records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_projects_resources", "rar_sha256": "7369ce7fe1ae5f8bdb43db714fe90814de5d6c24291837d51b75e110db31519d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_plan_projects_resources`. The original RAPP
agent is preserved byte-for-byte in `audit_plan_projects_resources_agent.py` and in the RCI capsule.

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
