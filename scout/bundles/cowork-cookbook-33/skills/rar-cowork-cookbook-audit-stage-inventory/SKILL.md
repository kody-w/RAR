---
name: "rar-cowork-cookbook-audit-stage-inventory"
description: "Audits stage inventory records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_stage_inventory", "rar_sha256": "ada5208f911cf27d42ac41490e234b124a65609307d52add159e6b659b422b13", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_stage_inventory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-stage-inventory:235b6c6d68632f70d30c63b0e8f20a19fe9d143fdf34da3d458e5cba111b4c96", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_stage_inventory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_stage_inventory_agent.py` is
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
