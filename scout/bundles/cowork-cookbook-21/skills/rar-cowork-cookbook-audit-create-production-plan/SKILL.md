---
name: "rar-cowork-cookbook-audit-create-production-plan"
description: "Audits create production plan records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_create_production_plan", "rar_sha256": "c26dd65fb4324a69f5b6d0dbc6daecfb98f45d2322144ecffc91abff968b6d97", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_create_production_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-create-production-plan:ec297faacf0320acd9e9f477359e0cb8a6bb42b815a5cde813ae7505dc2a94e7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_create_production_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_create_production_plan_agent.py` is
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

Create production plan Completeness Audit — Audits create production plan records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-create-production-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_create_production_plan_agent.py` and embedded as the fenced Python below (sha256 c26dd65fb4324a69…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_create_production_plan_agent.py` first:

```bash
python3 audit_create_production_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_create_production_plan_agent.py   # or on stdin
python3 audit_create_production_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create production plan Completeness Audit — Audits create production plan records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-create-production-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_create_production_plan',
    "version": '2.0.0',
    "display_name": 'Create production plan Completeness Audit',
    "description": 'Audits create production plan records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-create-production-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-create-production-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '515745bb20bb5cfe',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/create-production-plan'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/audit-create-production-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditCreateProductionPlan(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditCreateProductionPlan'
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
    print(AuditCreateProductionPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
