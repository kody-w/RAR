---
name: "rar-cowork-cookbook-audit-develop-chart-of-accounts-strategy"
description: "Audits develop chart of accounts strategy records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_chart_of_accounts_strategy", "rar_sha256": "efb490240a03a16ed2bc4a50879f154ff983f66c90c4905a7ec6b2624077f765", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
