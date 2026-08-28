---
name: "rar-cowork-cookbook-audit-conduct-a-business-impact-analysis"
description: "Audits conduct a business impact analysis records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_conduct_a_business_impact_analysis", "rar_sha256": "618429668a37fbfe2c04a96a7cf756b8eeb94909bcdeb696e0d7c0d6ea3fd9ac", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_conduct_a_business_impact_analysis_agent.py` and embedded as the fenced Python below (sha256 618429668a37fbfe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_conduct_a_business_impact_analysis_agent.py` first:

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
    "version": '2.0.0',
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
