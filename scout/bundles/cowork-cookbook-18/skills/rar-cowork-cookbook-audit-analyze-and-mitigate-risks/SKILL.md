---
name: "rar-cowork-cookbook-audit-analyze-and-mitigate-risks"
description: "Audits analyze and mitigate risks records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_and_mitigate_risks", "rar_sha256": "f65cb0b73a62274eeb48f79123d3f0838796d0e6c83d9a1c997eb889e8ed81d6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_analyze_and_mitigate_risks`. The original RAPP
agent is preserved byte-for-byte in `audit_analyze_and_mitigate_risks_agent.py` and in the RCI capsule.

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
