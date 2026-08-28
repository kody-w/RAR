---
name: "rar-cowork-cookbook-audit-plan-asset-leases"
description: "Audits plan asset leases records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_asset_leases", "rar_sha256": "643ed33c9e37e00529b90f21f858e75f60b92ee6ad0af85c45de49cc17b3cce4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_plan_asset_leases`. The original RAPP
agent is preserved byte-for-byte in `audit_plan_asset_leases_agent.py` and in the RCI capsule.

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

Plan asset leases Completeness Audit — Audits plan asset leases records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-asset-leases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_plan_asset_leases_agent.py` and embedded as the fenced Python below (sha256 643ed33c9e37e005…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_plan_asset_leases_agent.py` first:

```bash
python3 audit_plan_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_plan_asset_leases_agent.py   # or on stdin
python3 audit_plan_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan asset leases Completeness Audit — Audits plan asset leases records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_plan_asset_leases',
    "version": '2.0.1',
    "display_name": 'Plan asset leases Completeness Audit',
    "description": 'Audits plan asset leases records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-plan-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-plan-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1886312d97607e39',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/plan-asset-leases'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/audit-plan-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditPlanAssetLeases(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPlanAssetLeases'
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
    print(AuditPlanAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
