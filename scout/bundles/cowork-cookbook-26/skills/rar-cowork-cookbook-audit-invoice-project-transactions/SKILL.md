---
name: "rar-cowork-cookbook-audit-invoice-project-transactions"
description: "Audits invoice project transactions records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_invoice_project_transactions", "rar_sha256": "8fb2cc8b44b7419a9a55188e1fd1e8724a5a3caae5c3f32075421cf37c50f864", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_invoice_project_transactions_agent.py` and embedded as the fenced Python below (sha256 8fb2cc8b44b7419a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_invoice_project_transactions_agent.py` first:

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
    "version": '2.0.0',
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
