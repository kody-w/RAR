---
name: "rar-cowork-cookbook-audit-conduct-current-state-analysis"
description: "Audits conduct current state analysis records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_conduct_current_state_analysis", "rar_sha256": "b203070b9e71395b6dc2107d14375c79343be03ddb60d785faa6f3dcdfc2a394", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_conduct_current_state_analysis_agent.py` and embedded as the fenced Python below (sha256 b203070b9e71395b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_conduct_current_state_analysis_agent.py` first:

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
    "version": '2.0.0',
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
