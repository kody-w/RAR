---
name: "rar-cowork-cookbook-audit-develop-budgets"
description: "Audits develop budgets records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_budgets", "rar_sha256": "3a0291a746a37eb3a42707054fdd1a7100a1a17c66bca3ddf0a79c694fe44170", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_develop_budgets`. The original RAPP
agent is preserved byte-for-byte in `audit_develop_budgets_agent.py` and in the RCI capsule.

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

Develop budgets Completeness Audit — Audits develop budgets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_budgets_agent.py` and embedded as the fenced Python below (sha256 3a0291a746a37eb3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_budgets_agent.py` first:

```bash
python3 audit_develop_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_budgets_agent.py   # or on stdin
python3 audit_develop_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop budgets Completeness Audit — Audits develop budgets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_budgets',
    "version": '2.0.0',
    "display_name": 'Develop budgets Completeness Audit',
    "description": 'Audits develop budgets records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-develop-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f66daeab2a0ff1c7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/develop-budgets'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/audit-develop-budgets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditDevelopBudgets(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopBudgets'
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
    print(AuditDevelopBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
