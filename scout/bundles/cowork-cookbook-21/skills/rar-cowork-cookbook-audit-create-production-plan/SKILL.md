---
name: "rar-cowork-cookbook-audit-create-production-plan"
description: "Audits create production plan records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_create_production_plan", "rar_sha256": "da25b67d47f7122e422aa7fc10c84815d1052367ba460c0ac574d21aa6540cf8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_create_production_plan`. The original RAPP
agent is preserved byte-for-byte in `audit_create_production_plan_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_create_production_plan_agent.py` and embedded as the fenced Python below (sha256 da25b67d47f7122e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_create_production_plan_agent.py` first:

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
    "version": '2.0.1',
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
