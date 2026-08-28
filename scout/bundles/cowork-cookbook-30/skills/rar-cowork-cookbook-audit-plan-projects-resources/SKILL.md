---
name: "rar-cowork-cookbook-audit-plan-projects-resources"
description: "Audits plan projects resources records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_projects_resources", "rar_sha256": "055d2dcf28ec6cd28c63a736cdb15fe0b16fa227e686fef131f0904da6ceee86", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_plan_projects_resources_agent.py` and embedded as the fenced Python below (sha256 055d2dcf28ec6cd2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_plan_projects_resources_agent.py` first:

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
    "version": '2.0.1',
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
