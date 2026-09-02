---
name: "rar-cowork-cookbook-audit-migrate-to-new-versions-of-software"
description: "Audits migrate to new versions of software records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_migrate_to_new_versions_of_software", "rar_sha256": "d83974780ea585c6fbcf4dbba6d93a79be5d9d0f9dedc613701774dfeef9eda0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_migrate_to_new_versions_of_software_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-migrate-to-new-versions-of-software:65a538f29164840ab70a07be2386182b56a25dd8d69f5b6e73cd653f6c883aeb", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_migrate_to_new_versions_of_software`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_migrate_to_new_versions_of_software_agent.py` is
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

Migrate to new versions of software Completeness Audit — Audits migrate to new versions of software records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-migrate-to-new-versions-of-software
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_migrate_to_new_versions_of_software_agent.py` and embedded as the fenced Python below (sha256 d83974780ea585c6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_migrate_to_new_versions_of_software_agent.py` first:

```bash
python3 audit_migrate_to_new_versions_of_software_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_migrate_to_new_versions_of_software_agent.py   # or on stdin
python3 audit_migrate_to_new_versions_of_software_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Migrate to new versions of software Completeness Audit — Audits migrate to new versions of software records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-migrate-to-new-versions-of-software
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_migrate_to_new_versions_of_software',
    "version": '2.0.0',
    "display_name": 'Migrate to new versions of software Completeness Audit',
    "description": 'Audits migrate to new versions of software records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-migrate-to-new-versions-of-software',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-migrate-to-new-versions-of-software',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'df6391e6aee74112',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-03', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/migrate-to-new-versions-of-software'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-migrate-to-new-versions-of-software', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditMigrateToNewVersionsOfSoftware(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditMigrateToNewVersionsOfSoftware'
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
    print(AuditMigrateToNewVersionsOfSoftware().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
