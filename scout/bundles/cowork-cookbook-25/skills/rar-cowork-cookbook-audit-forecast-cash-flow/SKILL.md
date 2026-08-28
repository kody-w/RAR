---
name: "rar-cowork-cookbook-audit-forecast-cash-flow"
description: "Audits forecast cash flow records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_forecast_cash_flow", "rar_sha256": "5c2cf0f0f891030a1f5160595ddd9488af620ff0eac6775e9adb186061a793fd", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_forecast_cash_flow`. The original RAPP
agent is preserved byte-for-byte in `audit_forecast_cash_flow_agent.py` and in the RCI capsule.

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

Forecast cash flow Completeness Audit — Audits forecast cash flow records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-forecast-cash-flow
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_forecast_cash_flow_agent.py` and embedded as the fenced Python below (sha256 5c2cf0f0f891030a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_forecast_cash_flow_agent.py` first:

```bash
python3 audit_forecast_cash_flow_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_forecast_cash_flow_agent.py   # or on stdin
python3 audit_forecast_cash_flow_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast cash flow Completeness Audit — Audits forecast cash flow records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-forecast-cash-flow
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_forecast_cash_flow',
    "version": '2.0.1',
    "display_name": 'Forecast cash flow Completeness Audit',
    "description": 'Audits forecast cash flow records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'audit-forecast-cash-flow',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-forecast-cash-flow',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9973d8fee01e764b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/forecast-cash-flow'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-forecast-cash-flow', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditForecastCashFlow(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditForecastCashFlow'
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
    print(AuditForecastCashFlow().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
