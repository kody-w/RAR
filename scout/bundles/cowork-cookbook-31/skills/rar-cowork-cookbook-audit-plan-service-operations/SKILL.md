---
name: "rar-cowork-cookbook-audit-plan-service-operations"
description: "Audits plan service operations records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_service_operations", "rar_sha256": "dc13b6b34eb220f1bb2e55c652ba2345edd833827a94e8c96dbea4505b39b67f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_plan_service_operations`. The original RAPP
agent is preserved byte-for-byte in `audit_plan_service_operations_agent.py` and in the RCI capsule.

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

Plan service operations Completeness Audit — Audits plan service operations records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-service-operations
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_plan_service_operations_agent.py` and embedded as the fenced Python below (sha256 dc13b6b34eb220f1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_plan_service_operations_agent.py` first:

```bash
python3 audit_plan_service_operations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_plan_service_operations_agent.py   # or on stdin
python3 audit_plan_service_operations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan service operations Completeness Audit — Audits plan service operations records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-service-operations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_plan_service_operations',
    "version": '2.0.0',
    "display_name": 'Plan service operations Completeness Audit',
    "description": 'Audits plan service operations records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-plan-service-operations',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-plan-service-operations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ee13b3cc6d7fa02f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-service-operations'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/audit-plan-service-operations', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditPlanServiceOperations(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPlanServiceOperations'
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
    print(AuditPlanServiceOperations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
