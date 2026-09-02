---
name: "rar-cowork-cookbook-audit-allocate-budgets"
description: "Audits allocate budgets records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_allocate_budgets", "rar_sha256": "8a55a9ab94ade5e58ed00e53709914d8ac31f3205d81c9f5c5670ff936ef6585", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_allocate_budgets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-allocate-budgets:0e3b4d28953baab87c6f7371ced56d385ab7cbc96456d681755d695a5f9d7d01", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_allocate_budgets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_allocate_budgets_agent.py` is
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
