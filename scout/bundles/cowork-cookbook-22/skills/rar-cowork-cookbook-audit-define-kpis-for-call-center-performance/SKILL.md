---
name: "rar-cowork-cookbook-audit-define-kpis-for-call-center-performance"
description: "Audits define KPIs for call center performance records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_kpis_for_call_center_performance", "rar_sha256": "00d85df12a6778b8234a0f0043c189a1e1c70ac2839438bdfa3548fffb70a883", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_define_kpis_for_call_center_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-define-kpis-for-call-center-performance:c20901004fe1111930b452cc19409adcc982761d16aa861771310ea7f5430268", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_define_kpis_for_call_center_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_define_kpis_for_call_center_performance_agent.py` is
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

Define KPIs for call center performance Completeness Audit — Audits define KPIs for call center performance records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-kpis-for-call-center-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_kpis_for_call_center_performance_agent.py` and embedded as the fenced Python below (sha256 00d85df12a6778b8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_kpis_for_call_center_performance_agent.py` first:

```bash
python3 audit_define_kpis_for_call_center_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_kpis_for_call_center_performance_agent.py   # or on stdin
python3 audit_define_kpis_for_call_center_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define KPIs for call center performance Completeness Audit — Audits define KPIs for call center performance records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-kpis-for-call-center-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_kpis_for_call_center_performance',
    "version": '2.0.0',
    "display_name": 'Define KPIs for call center performance Completeness Audit',
    "description": 'Audits define KPIs for call center performance records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-define-kpis-for-call-center-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-kpis-for-call-center-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c9cfc4ed357308d1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-kpis-for-call-center-performance'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/audit-define-kpis-for-call-center-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditDefineKpisForCallCenterPerformance(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineKpisForCallCenterPerformance'
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
    print(AuditDefineKpisForCallCenterPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
