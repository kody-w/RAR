---
name: "rar-cowork-cookbook-audit-monitor-regulatory-compliance"
description: "Audits monitor regulatory compliance records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_monitor_regulatory_compliance", "rar_sha256": "8eae62b9d210c459c31e4dd3538de47a476fcf05d30587ec87c8ee79c215e1cb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_monitor_regulatory_compliance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-monitor-regulatory-compliance:80b041eb8b4947f04b0f3c77722e4eb4eebb201416b1bb6e0662b9ffad6a75a8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_monitor_regulatory_compliance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_monitor_regulatory_compliance_agent.py` is
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
