---
name: "rar-cowork-cookbook-audit-budget-workforce"
description: "Audits budget workforce records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_budget_workforce", "rar_sha256": "06a38d701e50a941d4de4d086d97642d0f0d16b290565f70831e37435c09b9e4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_budget_workforce_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-budget-workforce:c1a1a94f2a13e53083d787d7fa271bc304d8394acacc24cb35be3d87c8a25440", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_budget_workforce`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_budget_workforce_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_budget_workforce_agent.py` and embedded as the fenced Python below (sha256 06a38d701e50a941…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_budget_workforce_agent.py` first:

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
    "version": '2.0.0',
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
