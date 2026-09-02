---
name: "rar-cowork-cookbook-audit-design-warehouse-layout"
description: "Audits design warehouse layout records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_design_warehouse_layout", "rar_sha256": "7b56b9837a26f7584a0ccbde42a912ca3abfbd03123a5d13075c6d06c631d5fc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_design_warehouse_layout_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-design-warehouse-layout:4412b2131eedb997ebaee85bcff55003fc6a6ca9402520472eb699b3f1279ea7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_design_warehouse_layout`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_design_warehouse_layout_agent.py` is
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

Design warehouse layout Completeness Audit — Audits design warehouse layout records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-design-warehouse-layout
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_design_warehouse_layout_agent.py` and embedded as the fenced Python below (sha256 7b56b9837a26f758…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_design_warehouse_layout_agent.py` first:

```bash
python3 audit_design_warehouse_layout_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_design_warehouse_layout_agent.py   # or on stdin
python3 audit_design_warehouse_layout_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Design warehouse layout Completeness Audit — Audits design warehouse layout records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-design-warehouse-layout
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_design_warehouse_layout',
    "version": '2.0.0',
    "display_name": 'Design warehouse layout Completeness Audit',
    "description": 'Audits design warehouse layout records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-design-warehouse-layout',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-design-warehouse-layout',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b827adba283ba279',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-warehouse-operations/design-warehouse-layout'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/audit-design-warehouse-layout', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditDesignWarehouseLayout(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDesignWarehouseLayout'
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
    print(AuditDesignWarehouseLayout().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
