---
name: "rar-cowork-cookbook-audit-manage-sales-order-changes"
description: "Audits manage sales order changes records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_sales_order_changes", "rar_sha256": "7ecb9cd20f89109dae00de2e9e107bb64ea4deb87e519958668f061e3d667710", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_manage_sales_order_changes`. The original RAPP
agent is preserved byte-for-byte in `audit_manage_sales_order_changes_agent.py` and in the RCI capsule.

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

Manage sales order changes Completeness Audit — Audits manage sales order changes records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-sales-order-changes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_sales_order_changes_agent.py` and embedded as the fenced Python below (sha256 7ecb9cd20f89109d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_sales_order_changes_agent.py` first:

```bash
python3 audit_manage_sales_order_changes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_manage_sales_order_changes_agent.py   # or on stdin
python3 audit_manage_sales_order_changes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage sales order changes Completeness Audit — Audits manage sales order changes records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-sales-order-changes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_manage_sales_order_changes',
    "version": '2.0.1',
    "display_name": 'Manage sales order changes Completeness Audit',
    "description": 'Audits manage sales order changes records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-manage-sales-order-changes',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-manage-sales-order-changes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b84adbe08e19b1c0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/manage-sales-order-changes'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/audit-manage-sales-order-changes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditManageSalesOrderChanges(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditManageSalesOrderChanges'
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
    print(AuditManageSalesOrderChanges().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
