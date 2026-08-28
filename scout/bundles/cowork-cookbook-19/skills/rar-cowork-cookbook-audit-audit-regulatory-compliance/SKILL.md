---
name: "rar-cowork-cookbook-audit-audit-regulatory-compliance"
description: "Audits audit regulatory compliance records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_audit_regulatory_compliance", "rar_sha256": "3a915f97829bb77230e4965b888130af93d2a0df242f193ef760d96fd960a9cb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_audit_regulatory_compliance`. The original RAPP
agent is preserved byte-for-byte in `audit_audit_regulatory_compliance_agent.py` and in the RCI capsule.

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
