---
name: "rar-cowork-cookbook-audit-track-and-analyze-software-licenses"
description: "Audits track and analyze software licenses records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_track_and_analyze_software_licenses", "rar_sha256": "a33d5a6a4b37e9028fab086b9177e87818fdd319b7e9ca58bfb37ec0f7ea7282", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_track_and_analyze_software_licenses_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-track-and-analyze-software-licenses:8d11481c73799faf4387d7ad5b59f9d50f11265704050bacdfcee0fc8302cc3c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_track_and_analyze_software_licenses`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_track_and_analyze_software_licenses_agent.py` is
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

Track and analyze software licenses Completeness Audit — Audits track and analyze software licenses records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-track-and-analyze-software-licenses
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_track_and_analyze_software_licenses_agent.py` and embedded as the fenced Python below (sha256 a33d5a6a4b37e902…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_track_and_analyze_software_licenses_agent.py` first:

```bash
python3 audit_track_and_analyze_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_track_and_analyze_software_licenses_agent.py   # or on stdin
python3 audit_track_and_analyze_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track and analyze software licenses Completeness Audit — Audits track and analyze software licenses records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-track-and-analyze-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_track_and_analyze_software_licenses',
    "version": '2.0.0',
    "display_name": 'Track and analyze software licenses Completeness Audit',
    "description": 'Audits track and analyze software licenses records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-track-and-analyze-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-track-and-analyze-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fad0f2ea517c2e45',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-04', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/track-and-analyze-software-licenses'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-track-and-analyze-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditTrackAndAnalyzeSoftwareLicenses(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditTrackAndAnalyzeSoftwareLicenses'
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
    print(AuditTrackAndAnalyzeSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
