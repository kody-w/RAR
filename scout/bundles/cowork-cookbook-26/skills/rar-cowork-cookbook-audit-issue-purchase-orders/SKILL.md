---
name: "rar-cowork-cookbook-audit-issue-purchase-orders"
description: "Audits issue purchase orders records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_issue_purchase_orders", "rar_sha256": "1c3d4ed03c50af539e0a4a7bcbc27184240d0fe5b8f12c7877b3c90be8fcf48c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_issue_purchase_orders_agent.py` and embedded as the fenced Python below (sha256 1c3d4ed03c50af53…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_issue_purchase_orders_agent.py` first:

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
    "version": '2.0.0',
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
