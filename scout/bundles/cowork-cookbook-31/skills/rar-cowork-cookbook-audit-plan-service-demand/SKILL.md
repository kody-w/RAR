---
name: "rar-cowork-cookbook-audit-plan-service-demand"
description: "Audits plan service demand records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_service_demand", "rar_sha256": "3ab88bdbd385b634df008cf9b82fb934130bb4c05cfd21f41312c58c5aeb8f5f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_plan_service_demand_agent.py` and embedded as the fenced Python below (sha256 3ab88bdbd385b634…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_plan_service_demand_agent.py` first:

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
    "version": '2.0.0',
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
