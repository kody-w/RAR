---
name: "rar-cowork-cookbook-audit-process-supplier-invoices"
description: "Audits process supplier invoices records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_process_supplier_invoices", "rar_sha256": "009124bc35ee6e803de149f85c27ff5f933f263b8e7b7a8c968e0f31c0525568", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_process_supplier_invoices_agent.py` and embedded as the fenced Python below (sha256 009124bc35ee6e80…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_process_supplier_invoices_agent.py` first:

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
    "version": '2.0.0',
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
