---
name: "rar-cowork-cookbook-audit-identify-production-resources"
description: "Audits identify production resources records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_identify_production_resources", "rar_sha256": "0e1a694cdcae5e26bc6d942bf8a487af8542fc2fb35e8d49d74bb0d83ba0506a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_identify_production_resources_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-identify-production-resources:1f3a5f473fe41ada240e32442bfa465c0001fa67a54620106dbf7d50588b5193", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_identify_production_resources`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_identify_production_resources_agent.py` is
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

Identify production resources Completeness Audit — Audits identify production resources records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-identify-production-resources
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_identify_production_resources_agent.py` and embedded as the fenced Python below (sha256 0e1a694cdcae5e26…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_identify_production_resources_agent.py` first:

```bash
python3 audit_identify_production_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_identify_production_resources_agent.py   # or on stdin
python3 audit_identify_production_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify production resources Completeness Audit — Audits identify production resources records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-identify-production-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_identify_production_resources',
    "version": '2.0.0',
    "display_name": 'Identify production resources Completeness Audit',
    "description": 'Audits identify production resources records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-identify-production-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-identify-production-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e06117323376824c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/identify-production-resources'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/audit-identify-production-resources', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditIdentifyProductionResources(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditIdentifyProductionResources'
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
    print(AuditIdentifyProductionResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
