---
name: "rar-cowork-cookbook-audit-pick-goods"
description: "Audits pick goods records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_pick_goods", "rar_sha256": "cfd3bd5627e0400f907aed0e86c227288e77c72ae2754bfe81d0fc2c6d7cb912", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_pick_goods`. The original RAPP
agent is preserved byte-for-byte in `audit_pick_goods_agent.py` and in the RCI capsule.

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

Pick goods Completeness Audit — Audits pick goods records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-pick-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_pick_goods_agent.py` and embedded as the fenced Python below (sha256 cfd3bd5627e0400f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_pick_goods_agent.py` first:

```bash
python3 audit_pick_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_pick_goods_agent.py   # or on stdin
python3 audit_pick_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pick goods Completeness Audit — Audits pick goods records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-pick-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_pick_goods',
    "version": '2.0.1',
    "display_name": 'Pick goods Completeness Audit',
    "description": 'Audits pick goods records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-pick-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-pick-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '04a531393048f71a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/pick-goods'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/audit-pick-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditPickGoods(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPickGoods'
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
    print(AuditPickGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
