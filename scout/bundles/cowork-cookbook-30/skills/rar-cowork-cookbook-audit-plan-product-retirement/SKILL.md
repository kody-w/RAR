---
name: "rar-cowork-cookbook-audit-plan-product-retirement"
description: "Audits plan product retirement records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_product_retirement", "rar_sha256": "27768fea67662245cee9afeee7e7ebbf5625b4e9ea009ab35d352e6b3b482e54", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_plan_product_retirement`. The original RAPP
agent is preserved byte-for-byte in `audit_plan_product_retirement_agent.py` and in the RCI capsule.

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
