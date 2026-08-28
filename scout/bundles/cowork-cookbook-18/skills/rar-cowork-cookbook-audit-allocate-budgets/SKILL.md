---
name: "rar-cowork-cookbook-audit-allocate-budgets"
description: "Audits allocate budgets records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_allocate_budgets", "rar_sha256": "8a55a9ab94ade5e58ed00e53709914d8ac31f3205d81c9f5c5670ff936ef6585", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_allocate_budgets`. The original RAPP
agent is preserved byte-for-byte in `audit_allocate_budgets_agent.py` and in the RCI capsule.

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

Allocate budgets Completeness Audit — Audits allocate budgets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-allocate-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_allocate_budgets_agent.py` and embedded as the fenced Python below (sha256 8a55a9ab94ade5e5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_allocate_budgets_agent.py` first:

```bash
python3 audit_allocate_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_allocate_budgets_agent.py   # or on stdin
python3 audit_allocate_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate budgets Completeness Audit — Audits allocate budgets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-allocate-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_allocate_budgets',
    "version": '2.0.0',
    "display_name": 'Allocate budgets Completeness Audit',
    "description": 'Audits allocate budgets records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-allocate-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-allocate-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '687181a90414050a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/allocate-budgets'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-allocate-budgets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditAllocateBudgets(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAllocateBudgets'
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
    print(AuditAllocateBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
