---
name: "rar-cowork-cookbook-audit-plan-risks-and-opportunities"
description: "Audits plan risks and opportunities records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_risks_and_opportunities", "rar_sha256": "7d3ed4344ee79401ba40eeb181255c651ba523a32191ca8492a884ec1380d26e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_plan_risks_and_opportunities_agent.py` and embedded as the fenced Python below (sha256 7d3ed4344ee79401…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_plan_risks_and_opportunities_agent.py` first:

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
    "version": '2.0.0',
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
