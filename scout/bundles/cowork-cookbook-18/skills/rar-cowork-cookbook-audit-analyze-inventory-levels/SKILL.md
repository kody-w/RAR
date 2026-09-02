---
name: "rar-cowork-cookbook-audit-analyze-inventory-levels"
description: "Audits analyze inventory levels records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_inventory_levels", "rar_sha256": "49ae307a307ca8de74d9000abf2897f952856e7350750b7b7a813700aaf704bf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_analyze_inventory_levels_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-analyze-inventory-levels:d82d6cb5f8bc3403398760382a8d23bec96370bf51168f50489b0736d594f117", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_analyze_inventory_levels`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_analyze_inventory_levels_agent.py` is
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

Analyze inventory levels Completeness Audit — Audits analyze inventory levels records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-inventory-levels
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_inventory_levels_agent.py` and embedded as the fenced Python below (sha256 49ae307a307ca8de…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_inventory_levels_agent.py` first:

```bash
python3 audit_analyze_inventory_levels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_analyze_inventory_levels_agent.py   # or on stdin
python3 audit_analyze_inventory_levels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze inventory levels Completeness Audit — Audits analyze inventory levels records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-inventory-levels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_analyze_inventory_levels',
    "version": '2.0.0',
    "display_name": 'Analyze inventory levels Completeness Audit',
    "description": 'Audits analyze inventory levels records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-analyze-inventory-levels',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-analyze-inventory-levels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b2a74e65298afbf7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/analyze-warehouse-operations/analyze-inventory-levels'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/audit-analyze-inventory-levels', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditAnalyzeInventoryLevels(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAnalyzeInventoryLevels'
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
    print(AuditAnalyzeInventoryLevels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
