---
name: "rar-cowork-cookbook-audit-develop-chart-of-accounts-strategy"
description: "Audits develop chart of accounts strategy records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_chart_of_accounts_strategy", "rar_sha256": "efb490240a03a16ed2bc4a50879f154ff983f66c90c4905a7ec6b2624077f765", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_develop_chart_of_accounts_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-develop-chart-of-accounts-strategy:a200505dca2c134bfaec54d4aae5bf34154e269f13ff37c16660188ff2290a27", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_develop_chart_of_accounts_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_develop_chart_of_accounts_strategy_agent.py` is
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

Develop chart of accounts strategy Completeness Audit — Audits develop chart of accounts strategy records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-chart-of-accounts-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_chart_of_accounts_strategy_agent.py` and embedded as the fenced Python below (sha256 efb490240a03a16e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_chart_of_accounts_strategy_agent.py` first:

```bash
python3 audit_develop_chart_of_accounts_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_chart_of_accounts_strategy_agent.py   # or on stdin
python3 audit_develop_chart_of_accounts_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop chart of accounts strategy Completeness Audit — Audits develop chart of accounts strategy records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-chart-of-accounts-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_chart_of_accounts_strategy',
    "version": '2.0.0',
    "display_name": 'Develop chart of accounts strategy Completeness Audit',
    "description": 'Audits develop chart of accounts strategy records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-develop-chart-of-accounts-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-chart-of-accounts-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '061468a81229a353',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-chart-of-accounts-strategy'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-develop-chart-of-accounts-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditDevelopChartOfAccountsStrategy(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopChartOfAccountsStrategy'
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
    print(AuditDevelopChartOfAccountsStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
