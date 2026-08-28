---
name: "rar-cowork-cookbook-audit-label-received-goods"
description: "Audits label received goods records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_label_received_goods", "rar_sha256": "2a9d4f9bcc1800aaf2d7a52b41198debe380df6b2ee3cb906f2122637508376f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_label_received_goods_agent.py` and embedded as the fenced Python below (sha256 2a9d4f9bcc1800aa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_label_received_goods_agent.py` first:

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
    "version": '2.0.1',
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
