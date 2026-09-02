---
name: "rar-cowork-cookbook-audit-pick-goods"
description: "Audits pick goods records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_pick_goods", "rar_sha256": "75e466c3ff6b58477b911ca60396812555f7b9cfcae7e9889edec759b935b6e1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_pick_goods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-pick-goods:68ab000a557c783eb2bd79fd36459c0a601a0f5a04e8b4a4d7d19d50a0f23995", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_pick_goods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_pick_goods_agent.py` is
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

Pick goods Completeness Audit — Audits pick goods records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-pick-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_pick_goods_agent.py` and embedded as the fenced Python below (sha256 75e466c3ff6b5847…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_pick_goods_agent.py` first:

```bash
python3 audit_pick_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_pick_goods_agent.py   # or on stdin
python3 audit_pick_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pick goods Completeness Audit — Audits pick goods records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-pick-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_pick_goods',
    "version": '2.0.0',
    "display_name": 'Pick goods Completeness Audit',
    "description": 'Audits pick goods records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-pick-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-pick-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '04a531393048f71a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/pick-goods'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/audit-pick-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditPickGoods(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPickGoods'
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
    print(AuditPickGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
