---
name: "rar-cowork-cookbook-audit-allocate-budgets"
description: "Audits allocate budgets records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_allocate_budgets", "rar_sha256": "cd980aa8395eeaac8259b7ed8a8ae4b638454fd16612909db1ae561d286a42d1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_allocate_budgets_agent.py` and embedded as the fenced Python below (sha256 cd980aa8395eeaac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_allocate_budgets_agent.py` first:

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
    "version": '2.0.1',
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
