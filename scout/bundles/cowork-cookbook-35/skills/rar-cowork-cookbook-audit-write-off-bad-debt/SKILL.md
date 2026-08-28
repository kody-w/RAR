---
name: "rar-cowork-cookbook-audit-write-off-bad-debt"
description: "Audits write off bad debt records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_write_off_bad_debt", "rar_sha256": "a6ad6cd5911266ccd2c028c467bace1f35bf7aabdac93d3afe764afd60850544", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_write_off_bad_debt`. The original RAPP
agent is preserved byte-for-byte in `audit_write_off_bad_debt_agent.py` and in the RCI capsule.

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
