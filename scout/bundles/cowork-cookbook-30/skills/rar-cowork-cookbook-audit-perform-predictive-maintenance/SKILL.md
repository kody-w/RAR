---
name: "rar-cowork-cookbook-audit-perform-predictive-maintenance"
description: "Audits perform predictive maintenance records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_perform_predictive_maintenance", "rar_sha256": "389c27b29f73995945986bb5e4aa4cfe1c80b4525aadc7aa39047c6d09c9ebc7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_perform_predictive_maintenance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-perform-predictive-maintenance:59287f9c34313aede7caf295673277f11ca5d0456882f8a2eba145f561d45947", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_perform_predictive_maintenance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_perform_predictive_maintenance_agent.py` is
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
