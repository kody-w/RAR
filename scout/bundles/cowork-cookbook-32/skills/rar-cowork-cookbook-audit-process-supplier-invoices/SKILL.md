---
name: "rar-cowork-cookbook-audit-process-supplier-invoices"
description: "Audits process supplier invoices records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_process_supplier_invoices", "rar_sha256": "af6a9271b6acf16ac9f438fc4703d21ba85cff160607d70f4222df204ce64784", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_process_supplier_invoices`. The original RAPP
agent is preserved byte-for-byte in `audit_process_supplier_invoices_agent.py` and in the RCI capsule.

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

Process supplier invoices Completeness Audit — Audits process supplier invoices records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-supplier-invoices
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_process_supplier_invoices_agent.py` and embedded as the fenced Python below (sha256 af6a9271b6acf16a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_process_supplier_invoices_agent.py` first:

```bash
python3 audit_process_supplier_invoices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_process_supplier_invoices_agent.py   # or on stdin
python3 audit_process_supplier_invoices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process supplier invoices Completeness Audit — Audits process supplier invoices records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-supplier-invoices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_process_supplier_invoices',
    "version": '2.0.1',
    "display_name": 'Process supplier invoices Completeness Audit',
    "description": 'Audits process supplier invoices records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-process-supplier-invoices',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-process-supplier-invoices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7d0d5d7ef88c8dcc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/process-supplier-invoices'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/audit-process-supplier-invoices', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditProcessSupplierInvoices(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditProcessSupplierInvoices'
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
    print(AuditProcessSupplierInvoices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
