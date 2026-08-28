---
name: "rar-cowork-cookbook-audit-monitor-financial-performance"
description: "Audits monitor financial performance records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_monitor_financial_performance", "rar_sha256": "00fdbdb4b6a9022134876023a39ccac5af25ff84df33c841edfffa1ec3031ccc", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_monitor_financial_performance_agent.py` and embedded as the fenced Python below (sha256 00fdbdb4b6a90221…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_monitor_financial_performance_agent.py` first:

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
    "version": '2.0.1',
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
