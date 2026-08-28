---
name: "rar-cowork-cookbook-audit-identify-production-resources"
description: "Audits identify production resources records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_identify_production_resources", "rar_sha256": "c096a0c50dcf413157c6ec036a543329eae5f1c75e934ebb2b0171aab359456a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_identify_production_resources`. The original RAPP
agent is preserved byte-for-byte in `audit_identify_production_resources_agent.py` and in the RCI capsule.

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

Identify production resources Completeness Audit — Audits identify production resources records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-identify-production-resources
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_identify_production_resources_agent.py` and embedded as the fenced Python below (sha256 c096a0c50dcf4131…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_identify_production_resources_agent.py` first:

```bash
python3 audit_identify_production_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_identify_production_resources_agent.py   # or on stdin
python3 audit_identify_production_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify production resources Completeness Audit — Audits identify production resources records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-identify-production-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_identify_production_resources',
    "version": '2.0.1',
    "display_name": 'Identify production resources Completeness Audit',
    "description": 'Audits identify production resources records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-identify-production-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-identify-production-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e06117323376824c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/identify-production-resources'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/audit-identify-production-resources', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditIdentifyProductionResources(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditIdentifyProductionResources'
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
    print(AuditIdentifyProductionResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
