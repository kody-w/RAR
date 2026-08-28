---
name: "rar-cowork-cookbook-audit-stage-inventory"
description: "Audits stage inventory records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_stage_inventory", "rar_sha256": "ada5208f911cf27d42ac41490e234b124a65609307d52add159e6b659b422b13", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_stage_inventory_agent.py` and embedded as the fenced Python below (sha256 ada5208f911cf27d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_stage_inventory_agent.py` first:

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
    "version": '2.0.0',
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
