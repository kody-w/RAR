---
name: "rar-cowork-cookbook-audit-monitor-system-performance-and-health"
description: "Audits monitor system performance and health records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_monitor_system_performance_and_health", "rar_sha256": "a3ebf51d86fce5607dddba7b1b8cbbb5fe45d0765ba59af0748e501065a826f1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_monitor_system_performance_and_health_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-monitor-system-performance-and-health:5bcf98be05bcae2fc57ef14a57a2cca92334c9bfbedd86e1f5ed5cff06199924", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_monitor_system_performance_and_health`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_monitor_system_performance_and_health_agent.py` is
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

Monitor system performance and health Completeness Audit — Audits monitor system performance and health records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-monitor-system-performance-and-health
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_monitor_system_performance_and_health_agent.py` and embedded as the fenced Python below (sha256 a3ebf51d86fce560…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_monitor_system_performance_and_health_agent.py` first:

```bash
python3 audit_monitor_system_performance_and_health_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_monitor_system_performance_and_health_agent.py   # or on stdin
python3 audit_monitor_system_performance_and_health_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor system performance and health Completeness Audit — Audits monitor system performance and health records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-monitor-system-performance-and-health
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_monitor_system_performance_and_health',
    "version": '2.0.0',
    "display_name": 'Monitor system performance and health Completeness Audit',
    "description": 'Audits monitor system performance and health records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-monitor-system-performance-and-health',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-monitor-system-performance-and-health',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cf8688db3a3b027e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-04', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/monitor-system-performance-and-health'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-monitor-system-performance-and-health', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditMonitorSystemPerformanceAndHealth(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditMonitorSystemPerformanceAndHealth'
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
    print(AuditMonitorSystemPerformanceAndHealth().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
