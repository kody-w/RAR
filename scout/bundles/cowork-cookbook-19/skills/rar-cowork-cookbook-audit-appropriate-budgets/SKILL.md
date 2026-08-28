---
name: "rar-cowork-cookbook-audit-appropriate-budgets"
description: "Audits appropriate budgets records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_appropriate_budgets", "rar_sha256": "9e5eecf813c43941a9ca01f37e6fe30c3b3dc0b7c7772fe899a7c13a1e447012", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_appropriate_budgets`. The original RAPP
agent is preserved byte-for-byte in `audit_appropriate_budgets_agent.py` and in the RCI capsule.

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

Appropriate budgets Completeness Audit — Audits appropriate budgets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-appropriate-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_appropriate_budgets_agent.py` and embedded as the fenced Python below (sha256 9e5eecf813c43941…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_appropriate_budgets_agent.py` first:

```bash
python3 audit_appropriate_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_appropriate_budgets_agent.py   # or on stdin
python3 audit_appropriate_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Appropriate budgets Completeness Audit — Audits appropriate budgets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-appropriate-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_appropriate_budgets',
    "version": '2.0.0',
    "display_name": 'Appropriate budgets Completeness Audit',
    "description": 'Audits appropriate budgets records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-appropriate-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-appropriate-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '408e0714ec63e932',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/appropriate-budgets'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-appropriate-budgets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditAppropriateBudgets(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAppropriateBudgets'
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
    print(AuditAppropriateBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
