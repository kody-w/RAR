---
name: "rar-cowork-cookbook-audit-return-goods-to-vendor"
description: "Audits return goods to vendor records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_return_goods_to_vendor", "rar_sha256": "fa131ee0e2465086329bdaf61426408a4ad6db1e51821257dec4394429c55a4b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_return_goods_to_vendor_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-return-goods-to-vendor:01043ed48ac2bf0fd1e5c5bd7792a640c41ebfdd1dd6dabaea0db207239ad7c3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_return_goods_to_vendor`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_return_goods_to_vendor_agent.py` is
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

Return goods to vendor Completeness Audit — Audits return goods to vendor records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-return-goods-to-vendor
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_return_goods_to_vendor_agent.py` and embedded as the fenced Python below (sha256 fa131ee0e2465086…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_return_goods_to_vendor_agent.py` first:

```bash
python3 audit_return_goods_to_vendor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_return_goods_to_vendor_agent.py   # or on stdin
python3 audit_return_goods_to_vendor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Return goods to vendor Completeness Audit — Audits return goods to vendor records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-return-goods-to-vendor
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_return_goods_to_vendor',
    "version": '2.0.0',
    "display_name": 'Return goods to vendor Completeness Audit',
    "description": 'Audits return goods to vendor records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-return-goods-to-vendor',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-return-goods-to-vendor',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '057a28c1f691deff',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/return-goods-to-vendor'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/audit-return-goods-to-vendor', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditReturnGoodsToVendor(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditReturnGoodsToVendor'
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
    print(AuditReturnGoodsToVendor().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
