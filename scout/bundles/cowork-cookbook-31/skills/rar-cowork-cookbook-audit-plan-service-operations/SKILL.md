---
name: "rar-cowork-cookbook-audit-plan-service-operations"
description: "Audits plan service operations records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_service_operations", "rar_sha256": "d94792e39ac7c0cf003a5199171dc377dde39e9055f654d3523b34ff6a17b9db", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_plan_service_operations_agent.py` and embedded as the fenced Python below (sha256 d94792e39ac7c0cf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_plan_service_operations_agent.py` first:

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
    "version": '2.0.1',
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
