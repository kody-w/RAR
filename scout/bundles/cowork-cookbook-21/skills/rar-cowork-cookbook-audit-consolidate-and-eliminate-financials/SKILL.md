---
name: "rar-cowork-cookbook-audit-consolidate-and-eliminate-financials"
description: "Audits consolidate and eliminate financials records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_consolidate_and_eliminate_financials", "rar_sha256": "814d470de06d684d5c1b330b748492699dfaab53b41058e831cde09859e9bb25", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_consolidate_and_eliminate_financials`. The original RAPP
agent is preserved byte-for-byte in `audit_consolidate_and_eliminate_financials_agent.py` and in the RCI capsule.

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

Consolidate and eliminate financials Completeness Audit — Audits consolidate and eliminate financials records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-consolidate-and-eliminate-financials
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_consolidate_and_eliminate_financials_agent.py` and embedded as the fenced Python below (sha256 814d470de06d684d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_consolidate_and_eliminate_financials_agent.py` first:

```bash
python3 audit_consolidate_and_eliminate_financials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_consolidate_and_eliminate_financials_agent.py   # or on stdin
python3 audit_consolidate_and_eliminate_financials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Consolidate and eliminate financials Completeness Audit — Audits consolidate and eliminate financials records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-consolidate-and-eliminate-financials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_consolidate_and_eliminate_financials',
    "version": '2.0.1',
    "display_name": 'Consolidate and eliminate financials Completeness Audit',
    "description": 'Audits consolidate and eliminate financials records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-consolidate-and-eliminate-financials',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-consolidate-and-eliminate-financials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0ec9840f8ea69c87',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/consolidate-and-eliminate-financials'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-consolidate-and-eliminate-financials', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditConsolidateAndEliminateFinancials(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditConsolidateAndEliminateFinancials'
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
    print(AuditConsolidateAndEliminateFinancials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
