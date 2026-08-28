---
name: "rar-cowork-cookbook-audit-define-service-scheduling-approach"
description: "Audits define service scheduling approach records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_service_scheduling_approach", "rar_sha256": "e121d686bc91c6beb93413269ef06564e63b3602b070cb13525c6f863568045c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_service_scheduling_approach_agent.py` and embedded as the fenced Python below (sha256 e121d686bc91c6be…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_service_scheduling_approach_agent.py` first:

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
    "version": '2.0.0',
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
