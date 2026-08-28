---
name: "rar-cowork-cookbook-audit-perform-predictive-maintenance"
description: "Audits perform predictive maintenance records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_perform_predictive_maintenance", "rar_sha256": "84f307ab8130b980094a5b11ea42786f3111f4e50b468b1e3d453746d6c53b8d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_perform_predictive_maintenance_agent.py` and embedded as the fenced Python below (sha256 84f307ab8130b980…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_perform_predictive_maintenance_agent.py` first:

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
    "version": '2.0.1',
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
