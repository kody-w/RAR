---
name: "rar-cowork-cookbook-audit-monitor-system-performance-and-health"
description: "Audits monitor system performance and health records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_monitor_system_performance_and_health", "rar_sha256": "936144fb795ba21bc1a742c8439fb888fb1d59cdeba1c76ac5803824a7e867d1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_monitor_system_performance_and_health_agent.py` and embedded as the fenced Python below (sha256 936144fb795ba21b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_monitor_system_performance_and_health_agent.py` first:

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
    "version": '2.0.1',
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
