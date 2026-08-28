---
name: "rar-cowork-cookbook-audit-identify-production-resources"
description: "Audits identify production resources records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_identify_production_resources", "rar_sha256": "0e1a694cdcae5e26bc6d942bf8a487af8542fc2fb35e8d49d74bb0d83ba0506a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_identify_production_resources_agent.py` and embedded as the fenced Python below (sha256 0e1a694cdcae5e26…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_identify_production_resources_agent.py` first:

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
    "version": '2.0.0',
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
