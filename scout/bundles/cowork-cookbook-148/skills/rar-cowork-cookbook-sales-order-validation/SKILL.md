---
name: "rar-cowork-cookbook-sales-order-validation"
description: "Validates open sales orders against policy: pricing, credit, customer status, delivery terms."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/sales_order_validation", "rar_sha256": "be0e513ff706e8300aa10663fef35038d721149f9593c973126f3dca576ecca3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/sales_order_validation`. The original RAPP
agent is preserved byte-for-byte in `sales_order_validation_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `sales_order_validation_agent.py` and embedded as the fenced Python below (sha256 be0e513ff706e830…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `sales_order_validation_agent.py` first:

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
    "version": '2.0.1',
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
