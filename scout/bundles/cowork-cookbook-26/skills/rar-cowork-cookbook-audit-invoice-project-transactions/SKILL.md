---
name: "rar-cowork-cookbook-audit-invoice-project-transactions"
description: "Audits invoice project transactions records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_invoice_project_transactions", "rar_sha256": "8fb2cc8b44b7419a9a55188e1fd1e8724a5a3caae5c3f32075421cf37c50f864", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_invoice_project_transactions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-invoice-project-transactions:f31277f401d1befbe06f32bbe9cdaafabea4dd729b1da2fadbb4508f75628805", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_invoice_project_transactions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_invoice_project_transactions_agent.py` is
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
