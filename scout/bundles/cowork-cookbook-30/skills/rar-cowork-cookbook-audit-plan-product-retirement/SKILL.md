---
name: "rar-cowork-cookbook-audit-plan-product-retirement"
description: "Audits plan product retirement records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_product_retirement", "rar_sha256": "f090670ebb5b69f8fa31a8f544c660ee4184deda49ade2336029c670c0c1f092", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_plan_product_retirement_agent.py` and embedded as the fenced Python below (sha256 f090670ebb5b69f8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_plan_product_retirement_agent.py` first:

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
    "version": '2.0.1',
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
