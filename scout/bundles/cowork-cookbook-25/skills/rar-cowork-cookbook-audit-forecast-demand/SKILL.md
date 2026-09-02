---
name: "rar-cowork-cookbook-audit-forecast-demand"
description: "Audits forecast demand records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_forecast_demand", "rar_sha256": "ecf4ad3901a981b7887a78d3fd2c892487855862eb1b3eba0bb473bc233d2c37", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_forecast_demand_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-forecast-demand:e7397bcf3dc0ea72c07e25dd54a9f036eb305944d06d8f03a8d77a0088822931", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_forecast_demand`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_forecast_demand_agent.py` is
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

Forecast demand Completeness Audit — Audits forecast demand records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-forecast-demand
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_forecast_demand_agent.py` and embedded as the fenced Python below (sha256 ecf4ad3901a981b7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_forecast_demand_agent.py` first:

```bash
python3 audit_forecast_demand_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_forecast_demand_agent.py   # or on stdin
python3 audit_forecast_demand_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast demand Completeness Audit — Audits forecast demand records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-forecast-demand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_forecast_demand',
    "version": '2.0.0',
    "display_name": 'Forecast demand Completeness Audit',
    "description": 'Audits forecast demand records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-forecast-demand',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-forecast-demand',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bd2e99e6f607814f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/forecast-demand'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/audit-forecast-demand', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.556, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditForecastDemand(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditForecastDemand'
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
    print(AuditForecastDemand().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
