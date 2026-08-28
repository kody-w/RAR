---
name: "rar-cowork-cookbook-audit-manage-financial-risks"
description: "Audits manage financial risks records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_financial_risks", "rar_sha256": "b205e8c5eb201c7d906a80dfc7d077e8cef1f3a4648e7109d982f88d4d5a65bc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_manage_financial_risks`. The original RAPP
agent is preserved byte-for-byte in `audit_manage_financial_risks_agent.py` and in the RCI capsule.

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
