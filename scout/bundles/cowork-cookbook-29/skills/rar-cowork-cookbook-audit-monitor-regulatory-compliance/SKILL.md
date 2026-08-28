---
name: "rar-cowork-cookbook-audit-monitor-regulatory-compliance"
description: "Audits monitor regulatory compliance records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_monitor_regulatory_compliance", "rar_sha256": "982a2c905ca199f262510a1ba0a6f922572791708829de5a69722aa3a8755b58", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_monitor_regulatory_compliance`. The original RAPP
agent is preserved byte-for-byte in `audit_monitor_regulatory_compliance_agent.py` and in the RCI capsule.

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

Monitor regulatory compliance Completeness Audit — Audits monitor regulatory compliance records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-monitor-regulatory-compliance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_monitor_regulatory_compliance_agent.py` and embedded as the fenced Python below (sha256 982a2c905ca199f2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_monitor_regulatory_compliance_agent.py` first:

```bash
python3 audit_monitor_regulatory_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_monitor_regulatory_compliance_agent.py   # or on stdin
python3 audit_monitor_regulatory_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor regulatory compliance Completeness Audit — Audits monitor regulatory compliance records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-monitor-regulatory-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_monitor_regulatory_compliance',
    "version": '2.0.1',
    "display_name": 'Monitor regulatory compliance Completeness Audit',
    "description": 'Audits monitor regulatory compliance records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-monitor-regulatory-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-monitor-regulatory-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'db20df2c22f73353',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/monitor-regulatory-compliance'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-monitor-regulatory-compliance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditMonitorRegulatoryCompliance(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditMonitorRegulatoryCompliance'
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
    print(AuditMonitorRegulatoryCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
