---
name: "rar-cowork-cookbook-audit-inspect-inventory"
description: "Audits inspect inventory records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_inspect_inventory", "rar_sha256": "e7f41c594b3df71e9ff1b86013978629aa51d28559203fb016cfe99e0e3fd42b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_inspect_inventory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-inspect-inventory:6d154cc0e901f600a8fbb1b57b0270ad78587472dc99bef662ee984c47b31fb2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_inspect_inventory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_inspect_inventory_agent.py` is
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
