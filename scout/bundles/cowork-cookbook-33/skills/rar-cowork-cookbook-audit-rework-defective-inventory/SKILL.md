---
name: "rar-cowork-cookbook-audit-rework-defective-inventory"
description: "Audits rework defective inventory records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_rework_defective_inventory", "rar_sha256": "501abe5afaeded5a276820e2ce9401b6165031b632a555e2a15a3110bab5122a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_rework_defective_inventory`. The original RAPP
agent is preserved byte-for-byte in `audit_rework_defective_inventory_agent.py` and in the RCI capsule.

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

Rework defective inventory Completeness Audit — Audits rework defective inventory records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-rework-defective-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_rework_defective_inventory_agent.py` and embedded as the fenced Python below (sha256 501abe5afaeded5a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_rework_defective_inventory_agent.py` first:

```bash
python3 audit_rework_defective_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_rework_defective_inventory_agent.py   # or on stdin
python3 audit_rework_defective_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Rework defective inventory Completeness Audit — Audits rework defective inventory records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-rework-defective-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_rework_defective_inventory',
    "version": '2.0.1',
    "display_name": 'Rework defective inventory Completeness Audit',
    "description": 'Audits rework defective inventory records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-rework-defective-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-rework-defective-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '44ba930729715ef3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/rework-defective-inventory'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/audit-rework-defective-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditReworkDefectiveInventory(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditReworkDefectiveInventory'
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
    print(AuditReworkDefectiveInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
