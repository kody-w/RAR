---
name: "rar-cowork-cookbook-audit-merge-cases"
description: "Audits merge cases records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_merge_cases", "rar_sha256": "6a7276c2b800be4db8a078e331107f8b238bb7c61fd0e20027ffacdb4aa9ce43", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_merge_cases_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-merge-cases:f77e62cc2550b3192eb4458bb7ea6411b46e377c13504bed2555b5ee7dc6aeae", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_merge_cases`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_merge_cases_agent.py` is
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

Merge cases Completeness Audit — Audits merge cases records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-merge-cases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_merge_cases_agent.py` and embedded as the fenced Python below (sha256 6a7276c2b800be4d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_merge_cases_agent.py` first:

```bash
python3 audit_merge_cases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_merge_cases_agent.py   # or on stdin
python3 audit_merge_cases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Merge cases Completeness Audit — Audits merge cases records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-merge-cases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_merge_cases',
    "version": '2.0.0',
    "display_name": 'Merge cases Completeness Audit',
    "description": 'Audits merge cases records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-merge-cases',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-merge-cases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '40d16db423886e8f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/merge-cases'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/audit-merge-cases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditMergeCases(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditMergeCases'
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
    print(AuditMergeCases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
