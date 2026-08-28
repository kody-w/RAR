---
name: "rar-cowork-cookbook-audit-record-tax-commitments"
description: "Audits record tax commitments records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_record_tax_commitments", "rar_sha256": "cc54c4d7e6ffed351e9bba4aa0188c1eb37e63565a86e818c9ddeec5607497f8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_record_tax_commitments_agent.py` and embedded as the fenced Python below (sha256 cc54c4d7e6ffed35…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_record_tax_commitments_agent.py` first:

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
    "version": '2.0.1',
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
