---
name: "rar-cowork-cookbook-sales-order-validation"
description: "Validates open sales orders against policy: pricing, credit, customer status, delivery terms."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/sales_order_validation", "rar_sha256": "bb8d0dfd8674a39fa2e8f3b14616b168f209445bdc870d6c54d5cca7015c0e63", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "sales_order_validation_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/sales-order-validation:9827fd485a83dd20616790561fcd6b8f1f076071f251c5cd9c6b4a8ee261cfe7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/sales_order_validation`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `sales_order_validation_agent.py` is
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

Sales Order Compliance Check — Validates open sales orders against policy: pricing, credit, customer status, delivery terms.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/sales-order-validation
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `sales_order_validation_agent.py` and embedded as the fenced Python below (sha256 bb8d0dfd8674a39f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `sales_order_validation_agent.py` first:

```bash
python3 sales_order_validation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 sales_order_validation_agent.py   # or on stdin
python3 sales_order_validation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Sales Order Compliance Check — Validates open sales orders against policy: pricing, credit, customer status, delivery terms.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/sales-order-validation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/sales_order_validation',
    "version": '2.0.0',
    "display_name": 'Sales Order Compliance Check',
    "description": 'Validates open sales orders against policy: pricing, credit, customer status, delivery terms.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'sales-order-validation',
        "upstream_url": 'https://coworkcookbook.com/recipes/sales-order-validation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4e4ccc9ad4063bc5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/sales-order-validation', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.556, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:check', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class SalesOrderValidation(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'SalesOrderValidation'
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
    print(SalesOrderValidation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
