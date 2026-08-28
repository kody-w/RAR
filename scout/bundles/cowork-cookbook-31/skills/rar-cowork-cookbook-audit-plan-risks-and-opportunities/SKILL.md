---
name: "rar-cowork-cookbook-audit-plan-risks-and-opportunities"
description: "Audits plan risks and opportunities records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_risks_and_opportunities", "rar_sha256": "20aa1575fd78e3da6dee837c1047263678951444427dffc96cb4e7d493aa0347", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_plan_risks_and_opportunities`. The original RAPP
agent is preserved byte-for-byte in `audit_plan_risks_and_opportunities_agent.py` and in the RCI capsule.

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

Plan risks and opportunities Completeness Audit — Audits plan risks and opportunities records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-risks-and-opportunities
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_plan_risks_and_opportunities_agent.py` and embedded as the fenced Python below (sha256 20aa1575fd78e3da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_plan_risks_and_opportunities_agent.py` first:

```bash
python3 audit_plan_risks_and_opportunities_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_plan_risks_and_opportunities_agent.py   # or on stdin
python3 audit_plan_risks_and_opportunities_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan risks and opportunities Completeness Audit — Audits plan risks and opportunities records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-risks-and-opportunities
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_plan_risks_and_opportunities',
    "version": '2.0.1',
    "display_name": 'Plan risks and opportunities Completeness Audit',
    "description": 'Audits plan risks and opportunities records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-plan-risks-and-opportunities',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-plan-risks-and-opportunities',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '93fafe02a36a79da',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-risks-and-opportunities'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/audit-plan-risks-and-opportunities', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditPlanRisksAndOpportunities(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPlanRisksAndOpportunities'
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
    print(AuditPlanRisksAndOpportunities().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
