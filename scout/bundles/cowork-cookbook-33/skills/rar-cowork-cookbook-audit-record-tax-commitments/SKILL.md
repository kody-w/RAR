---
name: "rar-cowork-cookbook-audit-record-tax-commitments"
description: "Audits record tax commitments records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_record_tax_commitments", "rar_sha256": "68daaf9b759e0647b694cdca447228592b7f9659c4b34324a0af4633aeb0e3c5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_record_tax_commitments`. The original RAPP
agent is preserved byte-for-byte in `audit_record_tax_commitments_agent.py` and in the RCI capsule.

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

Record tax commitments Completeness Audit — Audits record tax commitments records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-record-tax-commitments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_record_tax_commitments_agent.py` and embedded as the fenced Python below (sha256 68daaf9b759e0647…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_record_tax_commitments_agent.py` first:

```bash
python3 audit_record_tax_commitments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_record_tax_commitments_agent.py   # or on stdin
python3 audit_record_tax_commitments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record tax commitments Completeness Audit — Audits record tax commitments records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-record-tax-commitments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_record_tax_commitments',
    "version": '2.0.0',
    "display_name": 'Record tax commitments Completeness Audit',
    "description": 'Audits record tax commitments records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-record-tax-commitments',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-record-tax-commitments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '52b0daa1ddfb1f3f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/record-tax-commitments'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-record-tax-commitments', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditRecordTaxCommitments(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditRecordTaxCommitments'
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
    print(AuditRecordTaxCommitments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
