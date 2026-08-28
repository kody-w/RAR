---
name: "rar-cowork-cookbook-audit-implement-compliance-controls-and-measures"
description: "Audits implement compliance controls and measures records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_implement_compliance_controls_and_measures", "rar_sha256": "5d26a161109b26f0c8705909d6b19c41774f08f2a782beb9dc6cf10245ce04ff", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_implement_compliance_controls_and_measures`. The original RAPP
agent is preserved byte-for-byte in `audit_implement_compliance_controls_and_measures_agent.py` and in the RCI capsule.

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

Implement compliance controls and measures Completeness Audit — Audits implement compliance controls and measures records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-implement-compliance-controls-and-measures
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_implement_compliance_controls_and_measures_agent.py` and embedded as the fenced Python below (sha256 5d26a161109b26f0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_implement_compliance_controls_and_measures_agent.py` first:

```bash
python3 audit_implement_compliance_controls_and_measures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_implement_compliance_controls_and_measures_agent.py   # or on stdin
python3 audit_implement_compliance_controls_and_measures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement compliance controls and measures Completeness Audit — Audits implement compliance controls and measures records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-implement-compliance-controls-and-measures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_implement_compliance_controls_and_measures',
    "version": '2.0.1',
    "display_name": 'Implement compliance controls and measures Completeness Audit',
    "description": 'Audits implement compliance controls and measures records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-implement-compliance-controls-and-measures',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-implement-compliance-controls-and-measures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8999ee3a6068edfe',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-03', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/implement-compliance-controls-and-measures'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-implement-compliance-controls-and-measures', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditImplementComplianceControlsAndMeasures(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditImplementComplianceControlsAndMeasures'
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
    print(AuditImplementComplianceControlsAndMeasures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
