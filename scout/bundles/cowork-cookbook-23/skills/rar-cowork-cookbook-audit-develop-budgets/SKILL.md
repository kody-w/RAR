---
name: "rar-cowork-cookbook-audit-develop-budgets"
description: "Audits develop budgets records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_budgets", "rar_sha256": "65e39f2f87092d09393f055919c95903e2a8e5de82aac6b6f4f84eee564d2a27", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_budgets_agent.py` and embedded as the fenced Python below (sha256 65e39f2f87092d09…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_budgets_agent.py` first:

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
    "version": '2.0.1',
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
