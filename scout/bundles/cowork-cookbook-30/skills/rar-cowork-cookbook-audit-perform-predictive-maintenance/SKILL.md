---
name: "rar-cowork-cookbook-audit-perform-predictive-maintenance"
description: "Audits perform predictive maintenance records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_perform_predictive_maintenance", "rar_sha256": "389c27b29f73995945986bb5e4aa4cfe1c80b4525aadc7aa39047c6d09c9ebc7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_perform_predictive_maintenance`. The original RAPP
agent is preserved byte-for-byte in `audit_perform_predictive_maintenance_agent.py` and in the RCI capsule.

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

Perform predictive maintenance Completeness Audit — Audits perform predictive maintenance records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-perform-predictive-maintenance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_perform_predictive_maintenance_agent.py` and embedded as the fenced Python below (sha256 389c27b29f739959…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_perform_predictive_maintenance_agent.py` first:

```bash
python3 audit_perform_predictive_maintenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_perform_predictive_maintenance_agent.py   # or on stdin
python3 audit_perform_predictive_maintenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform predictive maintenance Completeness Audit — Audits perform predictive maintenance records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-perform-predictive-maintenance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_perform_predictive_maintenance',
    "version": '2.0.0',
    "display_name": 'Perform predictive maintenance Completeness Audit',
    "description": 'Audits perform predictive maintenance records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-perform-predictive-maintenance',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-perform-predictive-maintenance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5352bf85e5682180',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/perform-predictive-maintenance'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/audit-perform-predictive-maintenance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditPerformPredictiveMaintenance(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPerformPredictiveMaintenance'
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
    print(AuditPerformPredictiveMaintenance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
