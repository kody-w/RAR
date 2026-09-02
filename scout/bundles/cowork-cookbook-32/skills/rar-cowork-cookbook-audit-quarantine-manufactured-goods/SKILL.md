---
name: "rar-cowork-cookbook-audit-quarantine-manufactured-goods"
description: "Audits quarantine manufactured goods records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_quarantine_manufactured_goods", "rar_sha256": "607b9c22621b8d617979ce3de3c73c4dc62e0a55a22f27e1591b1e28b16d4c7a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_quarantine_manufactured_goods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-quarantine-manufactured-goods:fae6fc7ed377ae7018b7b27c0b98c57a7932b95de9bb965084de3f60304164dc", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_quarantine_manufactured_goods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_quarantine_manufactured_goods_agent.py` is
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

Quarantine manufactured goods Completeness Audit — Audits quarantine manufactured goods records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-quarantine-manufactured-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_quarantine_manufactured_goods_agent.py` and embedded as the fenced Python below (sha256 607b9c22621b8d61…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_quarantine_manufactured_goods_agent.py` first:

```bash
python3 audit_quarantine_manufactured_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_quarantine_manufactured_goods_agent.py   # or on stdin
python3 audit_quarantine_manufactured_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Quarantine manufactured goods Completeness Audit — Audits quarantine manufactured goods records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-quarantine-manufactured-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_quarantine_manufactured_goods',
    "version": '2.0.0',
    "display_name": 'Quarantine manufactured goods Completeness Audit',
    "description": 'Audits quarantine manufactured goods records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-quarantine-manufactured-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-quarantine-manufactured-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '33dc2e802681d6e5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/quarantine-manufactured-goods'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/audit-quarantine-manufactured-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditQuarantineManufacturedGoods(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditQuarantineManufacturedGoods'
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
    print(AuditQuarantineManufacturedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
