---
name: "rar-cowork-cookbook-audit-consume-resources"
description: "Audits consume resources records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_consume_resources", "rar_sha256": "95b546ba288e84db3477ec284397b916cb9fefb8a886d501d78827b19a7400ed", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_consume_resources_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-consume-resources:d83f1e0b5303f183697214ab46cfbba3364f4c555680ad7c3483350a368f5fde", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_consume_resources`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_consume_resources_agent.py` is
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

Consume resources Completeness Audit — Audits consume resources records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-consume-resources
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_consume_resources_agent.py` and embedded as the fenced Python below (sha256 95b546ba288e84db…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_consume_resources_agent.py` first:

```bash
python3 audit_consume_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_consume_resources_agent.py   # or on stdin
python3 audit_consume_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Consume resources Completeness Audit — Audits consume resources records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-consume-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_consume_resources',
    "version": '2.0.0',
    "display_name": 'Consume resources Completeness Audit',
    "description": 'Audits consume resources records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-consume-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-consume-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '576054b7cbd21f15',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/consume-resources'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/audit-consume-resources', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditConsumeResources(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditConsumeResources'
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
    print(AuditConsumeResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
