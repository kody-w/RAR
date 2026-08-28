---
name: "rar-cowork-cookbook-audit-budget-workforce"
description: "Audits budget workforce records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_budget_workforce", "rar_sha256": "ed5a15fc9c83495b25b3181fa1d48c48d487a902c11ce9e7cfe12d975546f80e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_budget_workforce`. The original RAPP
agent is preserved byte-for-byte in `audit_budget_workforce_agent.py` and in the RCI capsule.

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

Budget workforce Completeness Audit — Audits budget workforce records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-budget-workforce
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_budget_workforce_agent.py` and embedded as the fenced Python below (sha256 ed5a15fc9c83495b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_budget_workforce_agent.py` first:

```bash
python3 audit_budget_workforce_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_budget_workforce_agent.py   # or on stdin
python3 audit_budget_workforce_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Budget workforce Completeness Audit — Audits budget workforce records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-budget-workforce
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_budget_workforce',
    "version": '2.0.1',
    "display_name": 'Budget workforce Completeness Audit',
    "description": 'Audits budget workforce records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-budget-workforce',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-budget-workforce',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7e3cd745b27bce66',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/budget-workforce'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-budget-workforce', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditBudgetWorkforce(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditBudgetWorkforce'
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
    print(AuditBudgetWorkforce().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
