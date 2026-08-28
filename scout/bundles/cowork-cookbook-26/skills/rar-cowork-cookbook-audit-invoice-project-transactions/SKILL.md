---
name: "rar-cowork-cookbook-audit-invoice-project-transactions"
description: "Audits invoice project transactions records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_invoice_project_transactions", "rar_sha256": "fe74e4db378bd524ec985a011352916781b06fa3ace9c27f2e7bb4e6759ee4b7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_invoice_project_transactions`. The original RAPP
agent is preserved byte-for-byte in `audit_invoice_project_transactions_agent.py` and in the RCI capsule.

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

Invoice project transactions Completeness Audit — Audits invoice project transactions records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-invoice-project-transactions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_invoice_project_transactions_agent.py` and embedded as the fenced Python below (sha256 fe74e4db378bd524…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_invoice_project_transactions_agent.py` first:

```bash
python3 audit_invoice_project_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_invoice_project_transactions_agent.py   # or on stdin
python3 audit_invoice_project_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Invoice project transactions Completeness Audit — Audits invoice project transactions records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-invoice-project-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_invoice_project_transactions',
    "version": '2.0.1',
    "display_name": 'Invoice project transactions Completeness Audit',
    "description": 'Audits invoice project transactions records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-invoice-project-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-invoice-project-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a4ffafb37f70896b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-financials/invoice-project-transactions'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/audit-invoice-project-transactions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditInvoiceProjectTransactions(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditInvoiceProjectTransactions'
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
    print(AuditInvoiceProjectTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
