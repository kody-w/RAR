---
name: "rar-cowork-cookbook-audit-monitor-regulatory-compliance"
description: "Audits monitor regulatory compliance records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_monitor_regulatory_compliance", "rar_sha256": "8eae62b9d210c459c31e4dd3538de47a476fcf05d30587ec87c8ee79c215e1cb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_monitor_regulatory_compliance_agent.py` and embedded as the fenced Python below (sha256 8eae62b9d210c459…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_monitor_regulatory_compliance_agent.py` first:

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
    "version": '2.0.0',
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
