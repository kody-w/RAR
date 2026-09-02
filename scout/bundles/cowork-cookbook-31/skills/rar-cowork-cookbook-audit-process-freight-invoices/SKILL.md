---
name: "rar-cowork-cookbook-audit-process-freight-invoices"
description: "Audits process freight invoices records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_process_freight_invoices", "rar_sha256": "8459abecd6fc7e6dfaeccaf979eb32c96e1a4399716389f5614ac4468880dc92", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_process_freight_invoices_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-process-freight-invoices:66154bc306c80bdc7a6d0ef8813c5042fe4e254c587f90fa1e0039aa836e7747", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_process_freight_invoices`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_process_freight_invoices_agent.py` is
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

Process freight invoices Completeness Audit — Audits process freight invoices records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-freight-invoices
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_process_freight_invoices_agent.py` and embedded as the fenced Python below (sha256 8459abecd6fc7e6d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_process_freight_invoices_agent.py` first:

```bash
python3 audit_process_freight_invoices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_process_freight_invoices_agent.py   # or on stdin
python3 audit_process_freight_invoices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process freight invoices Completeness Audit — Audits process freight invoices records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-freight-invoices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_process_freight_invoices',
    "version": '2.0.0',
    "display_name": 'Process freight invoices Completeness Audit',
    "description": 'Audits process freight invoices records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-process-freight-invoices',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-process-freight-invoices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a65d62bbf9b4eaa1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/process-freight-invoices'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/audit-process-freight-invoices', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditProcessFreightInvoices(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditProcessFreightInvoices'
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
    print(AuditProcessFreightInvoices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
