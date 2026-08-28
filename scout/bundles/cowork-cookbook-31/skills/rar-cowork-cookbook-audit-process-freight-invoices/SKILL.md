---
name: "rar-cowork-cookbook-audit-process-freight-invoices"
description: "Audits process freight invoices records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_process_freight_invoices", "rar_sha256": "e0a6e9ac66f10d196e599756220cad33b53417eda29ed3746ca1b52f92f4e3f5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_process_freight_invoices`. The original RAPP
agent is preserved byte-for-byte in `audit_process_freight_invoices_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_process_freight_invoices_agent.py` and embedded as the fenced Python below (sha256 e0a6e9ac66f10d19…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_process_freight_invoices_agent.py` first:

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
    "version": '2.0.1',
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
