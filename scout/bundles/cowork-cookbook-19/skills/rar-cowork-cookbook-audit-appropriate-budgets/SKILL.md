---
name: "rar-cowork-cookbook-audit-appropriate-budgets"
description: "Audits appropriate budgets records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_appropriate_budgets", "rar_sha256": "9e5eecf813c43941a9ca01f37e6fe30c3b3dc0b7c7772fe899a7c13a1e447012", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_appropriate_budgets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-appropriate-budgets:03723e8bc22b85d3400cba902a9afd726648be507dbbb2fa6601a89d722d4f28", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_appropriate_budgets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_appropriate_budgets_agent.py` is
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
