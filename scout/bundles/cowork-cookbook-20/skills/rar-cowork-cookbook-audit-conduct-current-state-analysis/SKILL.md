---
name: "rar-cowork-cookbook-audit-conduct-current-state-analysis"
description: "Audits conduct current state analysis records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_conduct_current_state_analysis", "rar_sha256": "ce21e8b19a9ef6bd66ab95b53903b551814ed616b025fc70bb3e97db80f348c3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_conduct_current_state_analysis`. The original RAPP
agent is preserved byte-for-byte in `audit_conduct_current_state_analysis_agent.py` and in the RCI capsule.

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

Conduct current state analysis Completeness Audit — Audits conduct current state analysis records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-conduct-current-state-analysis
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_conduct_current_state_analysis_agent.py` and embedded as the fenced Python below (sha256 ce21e8b19a9ef6bd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_conduct_current_state_analysis_agent.py` first:

```bash
python3 audit_conduct_current_state_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_conduct_current_state_analysis_agent.py   # or on stdin
python3 audit_conduct_current_state_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct current state analysis Completeness Audit — Audits conduct current state analysis records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-conduct-current-state-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_conduct_current_state_analysis',
    "version": '2.0.1',
    "display_name": 'Conduct current state analysis Completeness Audit',
    "description": 'Audits conduct current state analysis records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-conduct-current-state-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-conduct-current-state-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd40b9115cc24174b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/conduct-current-state-analysis'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/audit-conduct-current-state-analysis', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditConductCurrentStateAnalysis(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditConductCurrentStateAnalysis'
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
    print(AuditConductCurrentStateAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
