---
name: "rar-cowork-cookbook-audit-manage-supplier-risk"
description: "Audits manage supplier risk records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_supplier_risk", "rar_sha256": "bb0a8fd0e57df4ba24dad1fe3dfee4ed724c752a0eb096db6d1889ab219dbba0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_manage_supplier_risk`. The original RAPP
agent is preserved byte-for-byte in `audit_manage_supplier_risk_agent.py` and in the RCI capsule.

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

Manage supplier risk Completeness Audit — Audits manage supplier risk records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-supplier-risk
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_supplier_risk_agent.py` and embedded as the fenced Python below (sha256 bb0a8fd0e57df4ba…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_supplier_risk_agent.py` first:

```bash
python3 audit_manage_supplier_risk_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_manage_supplier_risk_agent.py   # or on stdin
python3 audit_manage_supplier_risk_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage supplier risk Completeness Audit — Audits manage supplier risk records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-supplier-risk
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_manage_supplier_risk',
    "version": '2.0.1',
    "display_name": 'Manage supplier risk Completeness Audit',
    "description": 'Audits manage supplier risk records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-manage-supplier-risk',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-manage-supplier-risk',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e31bd677b88997ae',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/manage-supplier-risk'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/audit-manage-supplier-risk', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditManageSupplierRisk(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditManageSupplierRisk'
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
    print(AuditManageSupplierRisk().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
