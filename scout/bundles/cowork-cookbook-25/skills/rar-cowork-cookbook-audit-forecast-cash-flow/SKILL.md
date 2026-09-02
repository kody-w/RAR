---
name: "rar-cowork-cookbook-audit-forecast-cash-flow"
description: "Audits forecast cash flow records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_forecast_cash_flow", "rar_sha256": "36ed5d139bf28ffd912b5a70b302a90d555a94c2714ac9c62613b1a3999a10a6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_forecast_cash_flow_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-forecast-cash-flow:915ed162f12ea2f9b43ffd261a840ce1059de51ef2cbf009b473f1daee84ce99", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_forecast_cash_flow`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_forecast_cash_flow_agent.py` is
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

Forecast cash flow Completeness Audit — Audits forecast cash flow records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-forecast-cash-flow
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_forecast_cash_flow_agent.py` and embedded as the fenced Python below (sha256 36ed5d139bf28ffd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_forecast_cash_flow_agent.py` first:

```bash
python3 audit_forecast_cash_flow_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_forecast_cash_flow_agent.py   # or on stdin
python3 audit_forecast_cash_flow_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast cash flow Completeness Audit — Audits forecast cash flow records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-forecast-cash-flow
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_forecast_cash_flow',
    "version": '2.0.0',
    "display_name": 'Forecast cash flow Completeness Audit',
    "description": 'Audits forecast cash flow records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-forecast-cash-flow',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-forecast-cash-flow',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9973d8fee01e764b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/forecast-cash-flow'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-forecast-cash-flow', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditForecastCashFlow(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditForecastCashFlow'
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
    print(AuditForecastCashFlow().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
