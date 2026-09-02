---
name: "rar-cowork-cookbook-audit-audit-regulatory-compliance"
description: "Audits audit regulatory compliance records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_audit_regulatory_compliance", "rar_sha256": "3a915f97829bb77230e4965b888130af93d2a0df242f193ef760d96fd960a9cb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_audit_regulatory_compliance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-audit-regulatory-compliance:380cad76712913aec2191eb0f6a03ae92f74cb4b46c3fe8115eedcd23464b211", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_audit_regulatory_compliance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_audit_regulatory_compliance_agent.py` is
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

Audit regulatory compliance Completeness Audit — Audits audit regulatory compliance records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-audit-regulatory-compliance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_audit_regulatory_compliance_agent.py` and embedded as the fenced Python below (sha256 3a915f97829bb772…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_audit_regulatory_compliance_agent.py` first:

```bash
python3 audit_audit_regulatory_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_audit_regulatory_compliance_agent.py   # or on stdin
python3 audit_audit_regulatory_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Audit regulatory compliance Completeness Audit — Audits audit regulatory compliance records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-audit-regulatory-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_audit_regulatory_compliance',
    "version": '2.0.0',
    "display_name": 'Audit regulatory compliance Completeness Audit',
    "description": 'Audits audit regulatory compliance records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-audit-regulatory-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-audit-regulatory-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ef7e1f9165d7c161',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/audit-regulatory-compliance'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/audit-audit-regulatory-compliance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditAuditRegulatoryCompliance(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAuditRegulatoryCompliance'
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
    print(AuditAuditRegulatoryCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
