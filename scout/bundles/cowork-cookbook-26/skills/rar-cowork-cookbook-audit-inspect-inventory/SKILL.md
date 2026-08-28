---
name: "rar-cowork-cookbook-audit-inspect-inventory"
description: "Audits inspect inventory records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_inspect_inventory", "rar_sha256": "8b34f9e934a84d58035318f79ff4e3da0a30e393f96d5b007ea2c1e036304e04", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_inspect_inventory`. The original RAPP
agent is preserved byte-for-byte in `audit_inspect_inventory_agent.py` and in the RCI capsule.

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

Inspect inventory Completeness Audit — Audits inspect inventory records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-inspect-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_inspect_inventory_agent.py` and embedded as the fenced Python below (sha256 8b34f9e934a84d58…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_inspect_inventory_agent.py` first:

```bash
python3 audit_inspect_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_inspect_inventory_agent.py   # or on stdin
python3 audit_inspect_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Inspect inventory Completeness Audit — Audits inspect inventory records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-inspect-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_inspect_inventory',
    "version": '2.0.1',
    "display_name": 'Inspect inventory Completeness Audit',
    "description": 'Audits inspect inventory records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-inspect-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-inspect-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1cb18180c3de7867',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/inspect-inventory'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/audit-inspect-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.6, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance', 'word:inspect'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditInspectInventory(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditInspectInventory'
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
    print(AuditInspectInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
