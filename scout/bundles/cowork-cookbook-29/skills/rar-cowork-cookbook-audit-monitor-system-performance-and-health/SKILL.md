---
name: "rar-cowork-cookbook-audit-monitor-system-performance-and-health"
description: "Audits monitor system performance and health records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_monitor_system_performance_and_health", "rar_sha256": "a3ebf51d86fce5607dddba7b1b8cbbb5fe45d0765ba59af0748e501065a826f1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_monitor_system_performance_and_health`. The original RAPP
agent is preserved byte-for-byte in `audit_monitor_system_performance_and_health_agent.py` and in the RCI capsule.

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
