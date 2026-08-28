---
name: "rar-cowork-cookbook-audit-inspect-inventory"
description: "Audits inspect inventory records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_inspect_inventory", "rar_sha256": "e7f41c594b3df71e9ff1b86013978629aa51d28559203fb016cfe99e0e3fd42b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_inspect_inventory_agent.py` and embedded as the fenced Python below (sha256 e7f41c594b3df71e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_inspect_inventory_agent.py` first:

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
    "version": '2.0.0',
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
