---
name: "rar-cowork-cookbook-audit-label-received-goods"
description: "Audits label received goods records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_label_received_goods", "rar_sha256": "0c1a1cd39f38ddc7bb77c5a272c89d18b92075439249aba1adfdbb4af57298d7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_label_received_goods`. The original RAPP
agent is preserved byte-for-byte in `audit_label_received_goods_agent.py` and in the RCI capsule.

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
