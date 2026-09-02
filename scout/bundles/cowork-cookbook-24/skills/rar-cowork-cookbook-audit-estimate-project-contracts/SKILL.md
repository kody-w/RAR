---
name: "rar-cowork-cookbook-audit-estimate-project-contracts"
description: "Audits estimate project contracts records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_estimate_project_contracts", "rar_sha256": "9291ad2563ae0a20df5ea6e33fa820dce555fef852dd444417bf79c0a5958da6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_estimate_project_contracts_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-estimate-project-contracts:d48356b6ea1cf391640646b92dbbc0c3569d9329f1ad9862b11531b68cba09cd", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_estimate_project_contracts`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_estimate_project_contracts_agent.py` is
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

Estimate project contracts Completeness Audit — Audits estimate project contracts records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-estimate-project-contracts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_estimate_project_contracts_agent.py` and embedded as the fenced Python below (sha256 9291ad2563ae0a20…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_estimate_project_contracts_agent.py` first:

```bash
python3 audit_estimate_project_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_estimate_project_contracts_agent.py   # or on stdin
python3 audit_estimate_project_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Estimate project contracts Completeness Audit — Audits estimate project contracts records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-estimate-project-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_estimate_project_contracts',
    "version": '2.0.0',
    "display_name": 'Estimate project contracts Completeness Audit',
    "description": 'Audits estimate project contracts records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-estimate-project-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-estimate-project-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '50308aa446e84715',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/estimate-project-contracts'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/audit-estimate-project-contracts', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditEstimateProjectContracts(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditEstimateProjectContracts'
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
    print(AuditEstimateProjectContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
