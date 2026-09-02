---
name: "rar-cowork-cookbook-audit-manage-financial-risks"
description: "Audits manage financial risks records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_financial_risks", "rar_sha256": "b205e8c5eb201c7d906a80dfc7d077e8cef1f3a4648e7109d982f88d4d5a65bc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_manage_financial_risks_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-manage-financial-risks:5ba40b9a291c6e03e2a8c25c8177d89109c4a0b72e09391b55899b84c53abe1a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_manage_financial_risks`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_manage_financial_risks_agent.py` is
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

Manage financial risks Completeness Audit — Audits manage financial risks records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-financial-risks
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_financial_risks_agent.py` and embedded as the fenced Python below (sha256 b205e8c5eb201c7d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_financial_risks_agent.py` first:

```bash
python3 audit_manage_financial_risks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_manage_financial_risks_agent.py   # or on stdin
python3 audit_manage_financial_risks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage financial risks Completeness Audit — Audits manage financial risks records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-financial-risks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_manage_financial_risks',
    "version": '2.0.0',
    "display_name": 'Manage financial risks Completeness Audit',
    "description": 'Audits manage financial risks records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'audit-manage-financial-risks',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-manage-financial-risks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd405a999bb6f57ae',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/manage-financial-risks'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/audit-manage-financial-risks', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditManageFinancialRisks(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditManageFinancialRisks'
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
    print(AuditManageFinancialRisks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
