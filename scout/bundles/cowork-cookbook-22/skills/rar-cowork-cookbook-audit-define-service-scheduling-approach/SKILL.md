---
name: "rar-cowork-cookbook-audit-define-service-scheduling-approach"
description: "Audits define service scheduling approach records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_service_scheduling_approach", "rar_sha256": "4af186582d574650bf3c21249d6b70940b77f4206380d32f17295d08b021a9d5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_define_service_scheduling_approach`. The original RAPP
agent is preserved byte-for-byte in `audit_define_service_scheduling_approach_agent.py` and in the RCI capsule.

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

Define service scheduling approach Completeness Audit — Audits define service scheduling approach records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-service-scheduling-approach
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_service_scheduling_approach_agent.py` and embedded as the fenced Python below (sha256 4af186582d574650…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_service_scheduling_approach_agent.py` first:

```bash
python3 audit_define_service_scheduling_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_service_scheduling_approach_agent.py   # or on stdin
python3 audit_define_service_scheduling_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define service scheduling approach Completeness Audit — Audits define service scheduling approach records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-service-scheduling-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_service_scheduling_approach',
    "version": '2.0.1',
    "display_name": 'Define service scheduling approach Completeness Audit',
    "description": 'Audits define service scheduling approach records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-define-service-scheduling-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-service-scheduling-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd158c52f5d237ab5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/define-service-scheduling-approach'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/audit-define-service-scheduling-approach', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditDefineServiceSchedulingApproach(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineServiceSchedulingApproach'
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
    print(AuditDefineServiceSchedulingApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
