---
name: "rar-cowork-cookbook-audit-plan-risks-and-opportunities"
description: "Audits plan risks and opportunities records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_risks_and_opportunities", "rar_sha256": "7d3ed4344ee79401ba40eeb181255c651ba523a32191ca8492a884ec1380d26e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_plan_risks_and_opportunities_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-plan-risks-and-opportunities:e2a45e8f320ef7035ebb03c3758e15992afcca0de85994f72dbb2ec53b61ba04", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_plan_risks_and_opportunities`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_plan_risks_and_opportunities_agent.py` is
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
