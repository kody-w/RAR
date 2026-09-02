---
name: "rar-cowork-cookbook-audit-pay-employees"
description: "Audits pay employees records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_pay_employees", "rar_sha256": "92374eb569a4920a7b95080cd54f4c3e0525c9261f8d87e86f1dd086d661a92b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_pay_employees_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-pay-employees:bd7f24c455d7286d0ec73f099e5e7b029e5ed2c5b3be14f99d47cc0e5ff43b16", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_pay_employees`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_pay_employees_agent.py` is
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

Pay employees Completeness Audit — Audits pay employees records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-pay-employees
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_pay_employees_agent.py` and embedded as the fenced Python below (sha256 92374eb569a4920a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_pay_employees_agent.py` first:

```bash
python3 audit_pay_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_pay_employees_agent.py   # or on stdin
python3 audit_pay_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pay employees Completeness Audit — Audits pay employees records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-pay-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_pay_employees',
    "version": '2.0.0',
    "display_name": 'Pay employees Completeness Audit',
    "description": 'Audits pay employees records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-pay-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-pay-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd82163f2d0fcfd87',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/pay-employees'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-pay-employees', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditPayEmployees(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPayEmployees'
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
    print(AuditPayEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
