---
name: "rar-cowork-cookbook-audit-monitor-financial-performance"
description: "Audits monitor financial performance records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_monitor_financial_performance", "rar_sha256": "4d9b6e13a8e57b9b4bdb685aa9054cb9f99fa27e9e0500d9e6bb411a8c2e5f72", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_monitor_financial_performance`. The original RAPP
agent is preserved byte-for-byte in `audit_monitor_financial_performance_agent.py` and in the RCI capsule.

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

Monitor financial performance Completeness Audit — Audits monitor financial performance records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-monitor-financial-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_monitor_financial_performance_agent.py` and embedded as the fenced Python below (sha256 4d9b6e13a8e57b9b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_monitor_financial_performance_agent.py` first:

```bash
python3 audit_monitor_financial_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_monitor_financial_performance_agent.py   # or on stdin
python3 audit_monitor_financial_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor financial performance Completeness Audit — Audits monitor financial performance records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-monitor-financial-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_monitor_financial_performance',
    "version": '2.0.0',
    "display_name": 'Monitor financial performance Completeness Audit',
    "description": 'Audits monitor financial performance records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-monitor-financial-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-monitor-financial-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a3a8042de954d9a9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/monitor-financial-performance'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/audit-monitor-financial-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditMonitorFinancialPerformance(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditMonitorFinancialPerformance'
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
    print(AuditMonitorFinancialPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
