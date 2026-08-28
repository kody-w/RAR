---
name: "rar-cowork-cookbook-audit-issue-purchase-orders"
description: "Audits issue purchase orders records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_issue_purchase_orders", "rar_sha256": "85bd953ff912c813ace5fced3eda41ba06c4a88678346aa7ed7deecc64330ddb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_issue_purchase_orders`. The original RAPP
agent is preserved byte-for-byte in `audit_issue_purchase_orders_agent.py` and in the RCI capsule.

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

Issue purchase orders Completeness Audit — Audits issue purchase orders records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-issue-purchase-orders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_issue_purchase_orders_agent.py` and embedded as the fenced Python below (sha256 85bd953ff912c813…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_issue_purchase_orders_agent.py` first:

```bash
python3 audit_issue_purchase_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_issue_purchase_orders_agent.py   # or on stdin
python3 audit_issue_purchase_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue purchase orders Completeness Audit — Audits issue purchase orders records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-issue-purchase-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_issue_purchase_orders',
    "version": '2.0.1',
    "display_name": 'Issue purchase orders Completeness Audit',
    "description": 'Audits issue purchase orders records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-issue-purchase-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-issue-purchase-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd5fa878ebc906e98',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/issue-purchase-orders'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/audit-issue-purchase-orders', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditIssuePurchaseOrders(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditIssuePurchaseOrders'
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
    print(AuditIssuePurchaseOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
