---
name: "rar-cowork-cookbook-audit-define-kpis-for-call-center-performance"
description: "Audits define KPIs for call center performance records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_kpis_for_call_center_performance", "rar_sha256": "f09aa246ec5efa877b7aeb5ba392e2216b081f5bcae9e889c4aa8de34724dd97", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_define_kpis_for_call_center_performance`. The original RAPP
agent is preserved byte-for-byte in `audit_define_kpis_for_call_center_performance_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_kpis_for_call_center_performance_agent.py` and embedded as the fenced Python below (sha256 f09aa246ec5efa87…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_kpis_for_call_center_performance_agent.py` first:

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
    "version": '2.0.1',
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
