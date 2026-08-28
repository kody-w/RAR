---
name: "rar-cowork-cookbook-audit-track-and-analyze-software-licenses"
description: "Audits track and analyze software licenses records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_track_and_analyze_software_licenses", "rar_sha256": "2d0d38662482940f48196c251539c2c064c1a37a06005316b35762d4118d325a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_track_and_analyze_software_licenses`. The original RAPP
agent is preserved byte-for-byte in `audit_track_and_analyze_software_licenses_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_track_and_analyze_software_licenses_agent.py` and embedded as the fenced Python below (sha256 2d0d38662482940f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_track_and_analyze_software_licenses_agent.py` first:

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
    "version": '2.0.1',
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
