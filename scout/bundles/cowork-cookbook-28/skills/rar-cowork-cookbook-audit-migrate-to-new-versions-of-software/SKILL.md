---
name: "rar-cowork-cookbook-audit-migrate-to-new-versions-of-software"
description: "Audits migrate to new versions of software records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_migrate_to_new_versions_of_software", "rar_sha256": "d83974780ea585c6fbcf4dbba6d93a79be5d9d0f9dedc613701774dfeef9eda0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_migrate_to_new_versions_of_software`. The original RAPP
agent is preserved byte-for-byte in `audit_migrate_to_new_versions_of_software_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

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
