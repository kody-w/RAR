---
name: "rar-cowork-cookbook-audit-monitor-financial-performance"
description: "Audits monitor financial performance records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_monitor_financial_performance", "rar_sha256": "4d9b6e13a8e57b9b4bdb685aa9054cb9f99fa27e9e0500d9e6bb411a8c2e5f72", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_monitor_financial_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-monitor-financial-performance:a6bcf60307f2b777c1f109a931b0d11870b4714ddf0fc0129e69587efe22e3ac", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_monitor_financial_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_monitor_financial_performance_agent.py` is
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
