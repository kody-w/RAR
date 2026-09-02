---
name: "rar-cowork-cookbook-audit-analyze-sourcing-effectiveness"
description: "Audits analyze sourcing effectiveness records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_sourcing_effectiveness", "rar_sha256": "afe9495b0d3555fe2877d9001660e1f6c0bcfc1da93743b8aabdb2a4c325b65d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_analyze_sourcing_effectiveness_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-analyze-sourcing-effectiveness:726e5d905d2072017c9fe6c538fb329677a1fde361895081943bd038e8f96133", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_analyze_sourcing_effectiveness`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_analyze_sourcing_effectiveness_agent.py` is
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
