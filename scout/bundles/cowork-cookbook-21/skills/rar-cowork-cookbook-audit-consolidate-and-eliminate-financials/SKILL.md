---
name: "rar-cowork-cookbook-audit-consolidate-and-eliminate-financials"
description: "Audits consolidate and eliminate financials records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_consolidate_and_eliminate_financials", "rar_sha256": "6964711aa692de3abfc84fb989ae34a461863af5d63e00e8204b6a583449d291", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_consolidate_and_eliminate_financials_agent.py` and embedded as the fenced Python below (sha256 6964711aa692de3a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_consolidate_and_eliminate_financials_agent.py` first:

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
    "version": '2.0.0',
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
