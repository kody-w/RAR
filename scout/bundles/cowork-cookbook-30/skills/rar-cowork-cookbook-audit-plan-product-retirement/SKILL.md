---
name: "rar-cowork-cookbook-audit-plan-product-retirement"
description: "Audits plan product retirement records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_product_retirement", "rar_sha256": "27768fea67662245cee9afeee7e7ebbf5625b4e9ea009ab35d352e6b3b482e54", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_plan_product_retirement_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-plan-product-retirement:90ae5b1dd4a73536c9011cb99e544d8a991334dc922b8f095e86231d7a887171", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_plan_product_retirement`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_plan_product_retirement_agent.py` is
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

Plan product retirement Completeness Audit — Audits plan product retirement records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-product-retirement
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_plan_product_retirement_agent.py` and embedded as the fenced Python below (sha256 27768fea67662245…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_plan_product_retirement_agent.py` first:

```bash
python3 audit_plan_product_retirement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_plan_product_retirement_agent.py   # or on stdin
python3 audit_plan_product_retirement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan product retirement Completeness Audit — Audits plan product retirement records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-product-retirement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_plan_product_retirement',
    "version": '2.0.0',
    "display_name": 'Plan product retirement Completeness Audit',
    "description": 'Audits plan product retirement records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-plan-product-retirement',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-plan-product-retirement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b70ee1edd192358a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/retire-products/plan-product-retirement'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/audit-plan-product-retirement', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditPlanProductRetirement(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPlanProductRetirement'
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
    print(AuditPlanProductRetirement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
