---
name: "rar-cowork-cookbook-audit-forecast-demand"
description: "Audits forecast demand records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_forecast_demand", "rar_sha256": "ecf4ad3901a981b7887a78d3fd2c892487855862eb1b3eba0bb473bc233d2c37", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_forecast_demand`. The original RAPP
agent is preserved byte-for-byte in `audit_forecast_demand_agent.py` and in the RCI capsule.

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
