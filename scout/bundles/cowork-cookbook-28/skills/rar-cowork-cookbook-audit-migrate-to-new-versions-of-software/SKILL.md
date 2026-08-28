---
name: "rar-cowork-cookbook-audit-migrate-to-new-versions-of-software"
description: "Audits migrate to new versions of software records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_migrate_to_new_versions_of_software", "rar_sha256": "17ea1cd3997abbc4458625a9183c0ef8d8a2af2ca2465b6760ac5e6c9295bd0b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_migrate_to_new_versions_of_software_agent.py` and embedded as the fenced Python below (sha256 17ea1cd3997abbc4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_migrate_to_new_versions_of_software_agent.py` first:

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
    "version": '2.0.1',
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
