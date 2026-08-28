---
name: "rar-cowork-cookbook-audit-forecast-demand"
description: "Audits forecast demand records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_forecast_demand", "rar_sha256": "f70e0536133fd896ca1806e35a0d7b21ec75f02af95cbdbdffe3867c4509fce2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_forecast_demand_agent.py` and embedded as the fenced Python below (sha256 f70e0536133fd896…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_forecast_demand_agent.py` first:

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
    "version": '2.0.1',
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
