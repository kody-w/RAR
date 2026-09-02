---
name: "rar-cowork-cookbook-audit-develop-continuous-improvement-initiatives"
description: "Audits develop continuous improvement initiatives records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_continuous_improvement_initiatives", "rar_sha256": "c9978031e22a86515028a1a9f3800b2b239c111ae4720f6e29ac21ec28e5ffe3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_develop_continuous_improvement_initiatives_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-develop-continuous-improvement-initiatives:6cb9f1fc7d31baad9ffb2493edba887bee72641c4aa70aba8901ee6f360d5f10", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_develop_continuous_improvement_initiatives`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_develop_continuous_improvement_initiatives_agent.py` is
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

Develop continuous improvement initiatives Completeness Audit — Audits develop continuous improvement initiatives records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-continuous-improvement-initiatives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_continuous_improvement_initiatives_agent.py` and embedded as the fenced Python below (sha256 c9978031e22a8651…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_continuous_improvement_initiatives_agent.py` first:

```bash
python3 audit_develop_continuous_improvement_initiatives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_continuous_improvement_initiatives_agent.py   # or on stdin
python3 audit_develop_continuous_improvement_initiatives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop continuous improvement initiatives Completeness Audit — Audits develop continuous improvement initiatives records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-continuous-improvement-initiatives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_continuous_improvement_initiatives',
    "version": '2.0.0',
    "display_name": 'Develop continuous improvement initiatives Completeness Audit',
    "description": 'Audits develop continuous improvement initiatives records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'audit-develop-continuous-improvement-initiatives',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-continuous-improvement-initiatives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e6719447b00e196d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/develop-continuous-improvement-initiatives'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/audit-develop-continuous-improvement-initiatives', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditDevelopContinuousImprovementInitiatives(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopContinuousImprovementInitiatives'
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
    print(AuditDevelopContinuousImprovementInitiatives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
