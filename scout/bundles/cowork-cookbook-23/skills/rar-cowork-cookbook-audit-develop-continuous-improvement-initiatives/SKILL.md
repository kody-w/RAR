---
name: "rar-cowork-cookbook-audit-develop-continuous-improvement-initiatives"
description: "Audits develop continuous improvement initiatives records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_continuous_improvement_initiatives", "rar_sha256": "c94392fd958f17a91ad2e53f437ac3f31619162a84fb4a1066bb63b8e91397b8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_develop_continuous_improvement_initiatives`. The original RAPP
agent is preserved byte-for-byte in `audit_develop_continuous_improvement_initiatives_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_continuous_improvement_initiatives_agent.py` and embedded as the fenced Python below (sha256 c94392fd958f17a9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_continuous_improvement_initiatives_agent.py` first:

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
    "version": '2.0.1',
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
