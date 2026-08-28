---
name: "rar-cowork-cookbook-audit-pick-goods"
description: "Audits pick goods records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_pick_goods", "rar_sha256": "75e466c3ff6b58477b911ca60396812555f7b9cfcae7e9889edec759b935b6e1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_pick_goods`. The original RAPP
agent is preserved byte-for-byte in `audit_pick_goods_agent.py` and in the RCI capsule.

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
