---
name: "rar-cowork-cookbook-audit-evaluate-supplier-bids"
description: "Audits evaluate supplier bids records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_evaluate_supplier_bids", "rar_sha256": "0cc665ac8b5b6a7696f5369032f91407c3b5be49d038cf622874c876e40f1473", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_evaluate_supplier_bids`. The original RAPP
agent is preserved byte-for-byte in `audit_evaluate_supplier_bids_agent.py` and in the RCI capsule.

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

Evaluate supplier bids Completeness Audit — Audits evaluate supplier bids records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-evaluate-supplier-bids
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_evaluate_supplier_bids_agent.py` and embedded as the fenced Python below (sha256 0cc665ac8b5b6a76…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_evaluate_supplier_bids_agent.py` first:

```bash
python3 audit_evaluate_supplier_bids_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_evaluate_supplier_bids_agent.py   # or on stdin
python3 audit_evaluate_supplier_bids_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Evaluate supplier bids Completeness Audit — Audits evaluate supplier bids records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-evaluate-supplier-bids
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_evaluate_supplier_bids',
    "version": '2.0.1',
    "display_name": 'Evaluate supplier bids Completeness Audit',
    "description": 'Audits evaluate supplier bids records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-evaluate-supplier-bids',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-evaluate-supplier-bids',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4f0f8e7502a889c5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/evaluate-supplier-bids'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/audit-evaluate-supplier-bids', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditEvaluateSupplierBids(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditEvaluateSupplierBids'
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
    print(AuditEvaluateSupplierBids().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
