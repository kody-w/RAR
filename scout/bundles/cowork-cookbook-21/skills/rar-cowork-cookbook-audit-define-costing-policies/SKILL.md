---
name: "rar-cowork-cookbook-audit-define-costing-policies"
description: "Audits define costing policies records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_costing_policies", "rar_sha256": "0443e8d8ab45475a3245a6fea6f6d59b900d6a13d73bd220c5e89d61a09a04be", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_define_costing_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-define-costing-policies:7007c3490956ad06cd5b7621d510f412fe7b90330911fc6b301778a2260820ee", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_define_costing_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_define_costing_policies_agent.py` is
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

Define costing policies Completeness Audit — Audits define costing policies records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-costing-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_costing_policies_agent.py` and embedded as the fenced Python below (sha256 0443e8d8ab45475a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_costing_policies_agent.py` first:

```bash
python3 audit_define_costing_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_costing_policies_agent.py   # or on stdin
python3 audit_define_costing_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define costing policies Completeness Audit — Audits define costing policies records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-costing-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_costing_policies',
    "version": '2.0.0',
    "display_name": 'Define costing policies Completeness Audit',
    "description": 'Audits define costing policies records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-define-costing-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-costing-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b9021fd9bed64061',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/define-costing-policies'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-define-costing-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditDefineCostingPolicies(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineCostingPolicies'
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
    print(AuditDefineCostingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
