---
name: "rar-cowork-cookbook-audit-analyze-inventory-levels"
description: "Audits analyze inventory levels records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_inventory_levels", "rar_sha256": "49ae307a307ca8de74d9000abf2897f952856e7350750b7b7a813700aaf704bf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_analyze_inventory_levels`. The original RAPP
agent is preserved byte-for-byte in `audit_analyze_inventory_levels_agent.py` and in the RCI capsule.

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
