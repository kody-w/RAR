---
name: "rar-cowork-cookbook-audit-process-supplier-invoices"
description: "Audits process supplier invoices records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_process_supplier_invoices", "rar_sha256": "009124bc35ee6e803de149f85c27ff5f933f263b8e7b7a8c968e0f31c0525568", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_process_supplier_invoices_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-process-supplier-invoices:c52a83dedb60d3dcbc662fba6e77e1fe06c5f8bf9e010cd68dbc04f7368facfe", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_process_supplier_invoices`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_process_supplier_invoices_agent.py` is
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
