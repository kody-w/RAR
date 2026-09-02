---
name: "rar-cowork-cookbook-audit-evaluate-supplier-bids"
description: "Audits evaluate supplier bids records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_evaluate_supplier_bids", "rar_sha256": "4df2102e7ae79a1152cb163c4a0f0e25027823cbf870b65730d29e5de7deb619", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_evaluate_supplier_bids_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-evaluate-supplier-bids:5b5e0120c2d12f5b0280f5be46177e2617951e387667ef393c386e36e22bbe11", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_evaluate_supplier_bids`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_evaluate_supplier_bids_agent.py` is
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

Evaluate supplier bids Completeness Audit — Audits evaluate supplier bids records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-evaluate-supplier-bids
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_evaluate_supplier_bids_agent.py` and embedded as the fenced Python below (sha256 4df2102e7ae79a11…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_evaluate_supplier_bids_agent.py` first:

```bash
python3 audit_evaluate_supplier_bids_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_evaluate_supplier_bids_agent.py   # or on stdin
python3 audit_evaluate_supplier_bids_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Evaluate supplier bids Completeness Audit — Audits evaluate supplier bids records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-evaluate-supplier-bids
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_evaluate_supplier_bids',
    "version": '2.0.0',
    "display_name": 'Evaluate supplier bids Completeness Audit',
    "description": 'Audits evaluate supplier bids records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-evaluate-supplier-bids',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-evaluate-supplier-bids',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4f0f8e7502a889c5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/evaluate-supplier-bids'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/audit-evaluate-supplier-bids', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditEvaluateSupplierBids(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditEvaluateSupplierBids'
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
    print(AuditEvaluateSupplierBids().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
