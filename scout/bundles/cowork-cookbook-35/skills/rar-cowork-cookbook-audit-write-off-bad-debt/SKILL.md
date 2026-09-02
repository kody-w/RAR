---
name: "rar-cowork-cookbook-audit-write-off-bad-debt"
description: "Audits write off bad debt records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_write_off_bad_debt", "rar_sha256": "a6ad6cd5911266ccd2c028c467bace1f35bf7aabdac93d3afe764afd60850544", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_write_off_bad_debt_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-write-off-bad-debt:457b2b3cdb735250da0fdbfb36b8967aeb66b18a0720fc038b1297f4c973a7cb", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_write_off_bad_debt`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_write_off_bad_debt_agent.py` is
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

Write off bad debt Completeness Audit — Audits write off bad debt records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-write-off-bad-debt
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_write_off_bad_debt_agent.py` and embedded as the fenced Python below (sha256 a6ad6cd5911266cc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_write_off_bad_debt_agent.py` first:

```bash
python3 audit_write_off_bad_debt_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_write_off_bad_debt_agent.py   # or on stdin
python3 audit_write_off_bad_debt_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Write off bad debt Completeness Audit — Audits write off bad debt records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-write-off-bad-debt
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_write_off_bad_debt',
    "version": '2.0.0',
    "display_name": 'Write off bad debt Completeness Audit',
    "description": 'Audits write off bad debt records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-write-off-bad-debt',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-write-off-bad-debt',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fc3771795ac91f18',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/write-off-bad-debt'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/audit-write-off-bad-debt', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditWriteOffBadDebt(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditWriteOffBadDebt'
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
    print(AuditWriteOffBadDebt().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
