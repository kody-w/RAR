---
name: "rar-cowork-cookbook-audit-finalize-and-post-transactions"
description: "Audits finalize and post transactions records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_finalize_and_post_transactions", "rar_sha256": "4941f8e984cd4f8512a596fbd16f0f0f1da3b6b7c03974ed090bb08bd7cc5eae", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_finalize_and_post_transactions`. The original RAPP
agent is preserved byte-for-byte in `audit_finalize_and_post_transactions_agent.py` and in the RCI capsule.

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

Finalize and post transactions Completeness Audit — Audits finalize and post transactions records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-finalize-and-post-transactions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_finalize_and_post_transactions_agent.py` and embedded as the fenced Python below (sha256 4941f8e984cd4f85…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_finalize_and_post_transactions_agent.py` first:

```bash
python3 audit_finalize_and_post_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_finalize_and_post_transactions_agent.py   # or on stdin
python3 audit_finalize_and_post_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Finalize and post transactions Completeness Audit — Audits finalize and post transactions records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-finalize-and-post-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_finalize_and_post_transactions',
    "version": '2.0.1',
    "display_name": 'Finalize and post transactions Completeness Audit',
    "description": 'Audits finalize and post transactions records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-finalize-and-post-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-finalize-and-post-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '960849d3925b9f07',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/finalize-and-post-transactions'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-finalize-and-post-transactions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditFinalizeAndPostTransactions(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditFinalizeAndPostTransactions'
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
    print(AuditFinalizeAndPostTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
