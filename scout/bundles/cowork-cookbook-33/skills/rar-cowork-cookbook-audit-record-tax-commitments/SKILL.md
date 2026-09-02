---
name: "rar-cowork-cookbook-audit-record-tax-commitments"
description: "Audits record tax commitments records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_record_tax_commitments", "rar_sha256": "68daaf9b759e0647b694cdca447228592b7f9659c4b34324a0af4633aeb0e3c5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_record_tax_commitments_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-record-tax-commitments:a2fa968dd0fe4f0411aecb78b48e6e007f49103f7a711615222b6604855d4a11", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_record_tax_commitments`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_record_tax_commitments_agent.py` is
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
