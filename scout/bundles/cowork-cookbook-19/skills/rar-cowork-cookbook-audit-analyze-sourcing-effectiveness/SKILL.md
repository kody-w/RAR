---
name: "rar-cowork-cookbook-audit-analyze-sourcing-effectiveness"
description: "Audits analyze sourcing effectiveness records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_sourcing_effectiveness", "rar_sha256": "0e61e093dc9ee571b87c9f13c4537e00ff5b0e1bfa7de50aa1f75f779afb1946", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_analyze_sourcing_effectiveness`. The original RAPP
agent is preserved byte-for-byte in `audit_analyze_sourcing_effectiveness_agent.py` and in the RCI capsule.

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

Analyze sourcing effectiveness Completeness Audit — Audits analyze sourcing effectiveness records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-sourcing-effectiveness
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_sourcing_effectiveness_agent.py` and embedded as the fenced Python below (sha256 0e61e093dc9ee571…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_sourcing_effectiveness_agent.py` first:

```bash
python3 audit_analyze_sourcing_effectiveness_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_analyze_sourcing_effectiveness_agent.py   # or on stdin
python3 audit_analyze_sourcing_effectiveness_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze sourcing effectiveness Completeness Audit — Audits analyze sourcing effectiveness records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-sourcing-effectiveness
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_analyze_sourcing_effectiveness',
    "version": '2.0.1',
    "display_name": 'Analyze sourcing effectiveness Completeness Audit',
    "description": 'Audits analyze sourcing effectiveness records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-analyze-sourcing-effectiveness',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-analyze-sourcing-effectiveness',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c07f03214ac55278',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/analyze-sourcing-effectiveness'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/audit-analyze-sourcing-effectiveness', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditAnalyzeSourcingEffectiveness(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAnalyzeSourcingEffectiveness'
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
    print(AuditAnalyzeSourcingEffectiveness().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
