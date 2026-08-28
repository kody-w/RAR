---
name: "rar-cowork-cookbook-audit-stage-inventory"
description: "Audits stage inventory records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_stage_inventory", "rar_sha256": "6b455098c28ef0cccbe982a0f007b2c244c5cd0af14c64c7b64a25dbfc83fadf", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_stage_inventory`. The original RAPP
agent is preserved byte-for-byte in `audit_stage_inventory_agent.py` and in the RCI capsule.

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

Stage inventory Completeness Audit — Audits stage inventory records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-stage-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_stage_inventory_agent.py` and embedded as the fenced Python below (sha256 6b455098c28ef0cc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_stage_inventory_agent.py` first:

```bash
python3 audit_stage_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_stage_inventory_agent.py   # or on stdin
python3 audit_stage_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Stage inventory Completeness Audit — Audits stage inventory records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-stage-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_stage_inventory',
    "version": '2.0.1',
    "display_name": 'Stage inventory Completeness Audit',
    "description": 'Audits stage inventory records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-stage-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-stage-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b391605f21c609e6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/stage-inventory'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/audit-stage-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditStageInventory(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditStageInventory'
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
    print(AuditStageInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
