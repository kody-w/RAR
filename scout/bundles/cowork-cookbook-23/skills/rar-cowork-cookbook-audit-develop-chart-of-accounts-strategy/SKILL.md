---
name: "rar-cowork-cookbook-audit-develop-chart-of-accounts-strategy"
description: "Audits develop chart of accounts strategy records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_chart_of_accounts_strategy", "rar_sha256": "5d90f7b59ca5ef7570634921ae8da77463fa32cf70a483840d097a9e93a5eaf0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_develop_chart_of_accounts_strategy`. The original RAPP
agent is preserved byte-for-byte in `audit_develop_chart_of_accounts_strategy_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_chart_of_accounts_strategy_agent.py` and embedded as the fenced Python below (sha256 5d90f7b59ca5ef75…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_chart_of_accounts_strategy_agent.py` first:

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
    "version": '2.0.1',
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
