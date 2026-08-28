---
name: "rar-cowork-cookbook-audit-evaluate-supplier-bids"
description: "Audits evaluate supplier bids records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_evaluate_supplier_bids", "rar_sha256": "4df2102e7ae79a1152cb163c4a0f0e25027823cbf870b65730d29e5de7deb619", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_evaluate_supplier_bids_agent.py` and embedded as the fenced Python below (sha256 4df2102e7ae79a11…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_evaluate_supplier_bids_agent.py` first:

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
    "version": '2.0.0',
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
