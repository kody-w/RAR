---
name: "rar-cowork-cookbook-audit-return-goods-to-vendor"
description: "Audits return goods to vendor records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_return_goods_to_vendor", "rar_sha256": "d7eb721b4bc07aced57793c6a0f18fe6810b754ecdbbe125a8df3637d5e5986d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_return_goods_to_vendor_agent.py` and embedded as the fenced Python below (sha256 d7eb721b4bc07ace…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_return_goods_to_vendor_agent.py` first:

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
    "version": '2.0.1',
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
