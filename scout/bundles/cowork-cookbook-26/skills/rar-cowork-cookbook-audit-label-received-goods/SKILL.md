---
name: "rar-cowork-cookbook-audit-label-received-goods"
description: "Audits label received goods records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_label_received_goods", "rar_sha256": "0c1a1cd39f38ddc7bb77c5a272c89d18b92075439249aba1adfdbb4af57298d7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_label_received_goods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-label-received-goods:036c941b7be8f302be2ddfd80cf2509e6d365ac1486ca0fb629a36a495a4ecbb", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_label_received_goods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_label_received_goods_agent.py` is
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

Label received goods Completeness Audit — Audits label received goods records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-label-received-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_label_received_goods_agent.py` and embedded as the fenced Python below (sha256 0c1a1cd39f38ddc7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_label_received_goods_agent.py` first:

```bash
python3 audit_label_received_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_label_received_goods_agent.py   # or on stdin
python3 audit_label_received_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Label received goods Completeness Audit — Audits label received goods records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-label-received-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_label_received_goods',
    "version": '2.0.0',
    "display_name": 'Label received goods Completeness Audit',
    "description": 'Audits label received goods records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-label-received-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-label-received-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9f6de3b89cdd42b1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-inbound-goods/label-received-goods'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/audit-label-received-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditLabelReceivedGoods(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditLabelReceivedGoods'
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
    print(AuditLabelReceivedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
