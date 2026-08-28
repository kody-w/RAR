---
name: "rar-cowork-cookbook-audit-implement-compliance-controls-and-measures"
description: "Audits implement compliance controls and measures records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_implement_compliance_controls_and_measures", "rar_sha256": "e9f2ac0ea922f0027b983a4057e934d0ee84ebd59e4f4e6ffec34d4ba1b8b703", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_implement_compliance_controls_and_measures_agent.py` and embedded as the fenced Python below (sha256 e9f2ac0ea922f002…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_implement_compliance_controls_and_measures_agent.py` first:

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
    "version": '2.0.0',
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
