---
name: "rar-cowork-cookbook-audit-manage-supplier-risk"
description: "Audits manage supplier risk records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_supplier_risk", "rar_sha256": "0c07aecbbc754ee9a61c3c5ad6530a8f4698043dc8ed26f087605a8dd3d7b04e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_manage_supplier_risk_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-manage-supplier-risk:7e4311cf585b21296ed859e57b2abcc41e0cf61e3d8b4cd971b18292b347953f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_manage_supplier_risk`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_manage_supplier_risk_agent.py` is
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

Manage supplier risk Completeness Audit — Audits manage supplier risk records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-supplier-risk
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_supplier_risk_agent.py` and embedded as the fenced Python below (sha256 0c07aecbbc754ee9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_supplier_risk_agent.py` first:

```bash
python3 audit_manage_supplier_risk_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_manage_supplier_risk_agent.py   # or on stdin
python3 audit_manage_supplier_risk_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage supplier risk Completeness Audit — Audits manage supplier risk records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-supplier-risk
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_manage_supplier_risk',
    "version": '2.0.0',
    "display_name": 'Manage supplier risk Completeness Audit',
    "description": 'Audits manage supplier risk records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-manage-supplier-risk',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-manage-supplier-risk',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e31bd677b88997ae',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/manage-supplier-risk'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/audit-manage-supplier-risk', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditManageSupplierRisk(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditManageSupplierRisk'
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
    print(AuditManageSupplierRisk().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
