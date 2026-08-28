---
name: "rar-cowork-cookbook-audit-manage-sales-order-changes"
description: "Audits manage sales order changes records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_sales_order_changes", "rar_sha256": "06e8e773594a545c80234542cb5e724784c72d2f645f739004585427a02a1358", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_sales_order_changes_agent.py` and embedded as the fenced Python below (sha256 06e8e773594a545c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_sales_order_changes_agent.py` first:

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
    "version": '2.0.0',
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
