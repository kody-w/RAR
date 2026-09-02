---
name: "rar-cowork-cookbook-audit-conduct-a-business-impact-analysis"
description: "Audits conduct a business impact analysis records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_conduct_a_business_impact_analysis", "rar_sha256": "618429668a37fbfe2c04a96a7cf756b8eeb94909bcdeb696e0d7c0d6ea3fd9ac", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_conduct_a_business_impact_analysis_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-conduct-a-business-impact-analysis:45d97ec9485bd4a109d60a60c50206bd3aede9b015f0a6c9b431b81de248af32", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_conduct_a_business_impact_analysis`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_conduct_a_business_impact_analysis_agent.py` is
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
