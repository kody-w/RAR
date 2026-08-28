---
name: "rar-cowork-cookbook-audit-conduct-a-business-impact-analysis"
description: "Audits conduct a business impact analysis records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_conduct_a_business_impact_analysis", "rar_sha256": "f890808631ff00b8256c4c044fae1b3fa6d54a08c422d8166258a15da406f466", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_conduct_a_business_impact_analysis`. The original RAPP
agent is preserved byte-for-byte in `audit_conduct_a_business_impact_analysis_agent.py` and in the RCI capsule.

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

Conduct a business impact analysis Completeness Audit — Audits conduct a business impact analysis records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-conduct-a-business-impact-analysis
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_conduct_a_business_impact_analysis_agent.py` and embedded as the fenced Python below (sha256 f890808631ff00b8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_conduct_a_business_impact_analysis_agent.py` first:

```bash
python3 audit_conduct_a_business_impact_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_conduct_a_business_impact_analysis_agent.py   # or on stdin
python3 audit_conduct_a_business_impact_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct a business impact analysis Completeness Audit — Audits conduct a business impact analysis records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-conduct-a-business-impact-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_conduct_a_business_impact_analysis',
    "version": '2.0.1',
    "display_name": 'Conduct a business impact analysis Completeness Audit',
    "description": 'Audits conduct a business impact analysis records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-conduct-a-business-impact-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-conduct-a-business-impact-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c79cf39eadf3364c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/conduct-a-business-impact-analysis'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-conduct-a-business-impact-analysis', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditConductABusinessImpactAnalysis(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditConductABusinessImpactAnalysis'
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
    print(AuditConductABusinessImpactAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
