---
name: "rar-cowork-cookbook-audit-plan-service-demand"
description: "Audits plan service demand records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_service_demand", "rar_sha256": "480272e32fca56968dbc292f798011e04b05854440c0f9ec96ad7dd3df343dd8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_plan_service_demand`. The original RAPP
agent is preserved byte-for-byte in `audit_plan_service_demand_agent.py` and in the RCI capsule.

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

Plan service demand Completeness Audit — Audits plan service demand records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-service-demand
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_plan_service_demand_agent.py` and embedded as the fenced Python below (sha256 480272e32fca5696…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_plan_service_demand_agent.py` first:

```bash
python3 audit_plan_service_demand_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_plan_service_demand_agent.py   # or on stdin
python3 audit_plan_service_demand_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan service demand Completeness Audit — Audits plan service demand records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-service-demand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_plan_service_demand',
    "version": '2.0.1',
    "display_name": 'Plan service demand Completeness Audit',
    "description": 'Audits plan service demand records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-plan-service-demand',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-plan-service-demand',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fd2ef82b9eb4b48d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/plan-service-demand'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/audit-plan-service-demand', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditPlanServiceDemand(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPlanServiceDemand'
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
    print(AuditPlanServiceDemand().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
