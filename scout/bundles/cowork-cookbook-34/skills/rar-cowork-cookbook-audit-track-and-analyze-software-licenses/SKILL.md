---
name: "rar-cowork-cookbook-audit-track-and-analyze-software-licenses"
description: "Audits track and analyze software licenses records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_track_and_analyze_software_licenses", "rar_sha256": "a33d5a6a4b37e9028fab086b9177e87818fdd319b7e9ca58bfb37ec0f7ea7282", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
