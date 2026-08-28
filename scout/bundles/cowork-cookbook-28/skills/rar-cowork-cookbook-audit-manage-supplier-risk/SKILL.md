---
name: "rar-cowork-cookbook-audit-manage-supplier-risk"
description: "Audits manage supplier risk records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_supplier_risk", "rar_sha256": "0c07aecbbc754ee9a61c3c5ad6530a8f4698043dc8ed26f087605a8dd3d7b04e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_supplier_risk_agent.py` and embedded as the fenced Python below (sha256 0c07aecbbc754ee9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_supplier_risk_agent.py` first:

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
    "version": '2.0.0',
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
