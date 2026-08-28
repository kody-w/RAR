---
name: "rar-cowork-cookbook-audit-return-goods-to-vendor"
description: "Audits return goods to vendor records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_return_goods_to_vendor", "rar_sha256": "fa131ee0e2465086329bdaf61426408a4ad6db1e51821257dec4394429c55a4b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_return_goods_to_vendor`. The original RAPP
agent is preserved byte-for-byte in `audit_return_goods_to_vendor_agent.py` and in the RCI capsule.

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
