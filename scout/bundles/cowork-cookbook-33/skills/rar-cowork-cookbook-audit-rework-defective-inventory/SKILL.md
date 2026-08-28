---
name: "rar-cowork-cookbook-audit-rework-defective-inventory"
description: "Audits rework defective inventory records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_rework_defective_inventory", "rar_sha256": "47e6880ec4b802c8e1b89b1fb8d13f901bd8cf0863474bdcf37326fa75ac5f7a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_rework_defective_inventory_agent.py` and embedded as the fenced Python below (sha256 47e6880ec4b802c8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_rework_defective_inventory_agent.py` first:

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
    "version": '2.0.0',
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
