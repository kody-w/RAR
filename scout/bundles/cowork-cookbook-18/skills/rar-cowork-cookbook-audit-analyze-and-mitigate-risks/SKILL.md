---
name: "rar-cowork-cookbook-audit-analyze-and-mitigate-risks"
description: "Audits analyze and mitigate risks records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_and_mitigate_risks", "rar_sha256": "f65cb0b73a62274eeb48f79123d3f0838796d0e6c83d9a1c997eb889e8ed81d6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_analyze_and_mitigate_risks_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-analyze-and-mitigate-risks:51f908b34ca430c00de23b748120e64b720d970d1910b69628de8b1dc561d4ff", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_analyze_and_mitigate_risks`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_analyze_and_mitigate_risks_agent.py` is
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

Analyze and mitigate risks Completeness Audit — Audits analyze and mitigate risks records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-and-mitigate-risks
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_and_mitigate_risks_agent.py` and embedded as the fenced Python below (sha256 f65cb0b73a62274e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_and_mitigate_risks_agent.py` first:

```bash
python3 audit_analyze_and_mitigate_risks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_analyze_and_mitigate_risks_agent.py   # or on stdin
python3 audit_analyze_and_mitigate_risks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze and mitigate risks Completeness Audit — Audits analyze and mitigate risks records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-and-mitigate-risks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_analyze_and_mitigate_risks',
    "version": '2.0.0',
    "display_name": 'Analyze and mitigate risks Completeness Audit',
    "description": 'Audits analyze and mitigate risks records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-analyze-and-mitigate-risks',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-analyze-and-mitigate-risks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9f56d347112895c7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/analyze-and-mitigate-risks'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/audit-analyze-and-mitigate-risks', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditAnalyzeAndMitigateRisks(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAnalyzeAndMitigateRisks'
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
    print(AuditAnalyzeAndMitigateRisks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
