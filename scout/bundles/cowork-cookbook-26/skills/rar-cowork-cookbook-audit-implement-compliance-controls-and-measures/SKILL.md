---
name: "rar-cowork-cookbook-audit-implement-compliance-controls-and-measures"
description: "Audits implement compliance controls and measures records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_implement_compliance_controls_and_measures", "rar_sha256": "e9f2ac0ea922f0027b983a4057e934d0ee84ebd59e4f4e6ffec34d4ba1b8b703", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_implement_compliance_controls_and_measures_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-implement-compliance-controls-and-measures:f6f9cbcbfb6939c3f40e19cbe2ea2db9fd16a01aa7371737d8c8844cb6b98554", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_implement_compliance_controls_and_measures`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_implement_compliance_controls_and_measures_agent.py` is
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
