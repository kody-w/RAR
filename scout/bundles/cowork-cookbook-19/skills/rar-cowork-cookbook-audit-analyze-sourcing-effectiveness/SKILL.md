---
name: "rar-cowork-cookbook-audit-analyze-sourcing-effectiveness"
description: "Audits analyze sourcing effectiveness records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_sourcing_effectiveness", "rar_sha256": "afe9495b0d3555fe2877d9001660e1f6c0bcfc1da93743b8aabdb2a4c325b65d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_sourcing_effectiveness_agent.py` and embedded as the fenced Python below (sha256 afe9495b0d3555fe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_sourcing_effectiveness_agent.py` first:

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
    "version": '2.0.0',
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
