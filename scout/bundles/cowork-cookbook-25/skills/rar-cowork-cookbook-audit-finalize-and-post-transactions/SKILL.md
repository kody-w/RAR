---
name: "rar-cowork-cookbook-audit-finalize-and-post-transactions"
description: "Audits finalize and post transactions records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_finalize_and_post_transactions", "rar_sha256": "60771174cc7876eab0db22638f939f9d55174c303f99116cd4e7d6c0c7cd0109", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_finalize_and_post_transactions_agent.py` and embedded as the fenced Python below (sha256 60771174cc7876ea…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_finalize_and_post_transactions_agent.py` first:

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
    "version": '2.0.0',
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
