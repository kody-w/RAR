---
name: "rar-cowork-cookbook-audit-onboard-new-suppliers"
description: "Audits onboard new suppliers records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_onboard_new_suppliers", "rar_sha256": "09c344921f1ede7563dcde2ca0e598f2ca81f3a071ff654b2d889f9dacce02f3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_onboard_new_suppliers_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-onboard-new-suppliers:0e0b2a4ce210f8fe8fd2a9ce445e18b47d7a37d8a0a2c259439478d1475eccc7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_onboard_new_suppliers`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_onboard_new_suppliers_agent.py` is
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

Onboard new suppliers Completeness Audit — Audits onboard new suppliers records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-onboard-new-suppliers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_onboard_new_suppliers_agent.py` and embedded as the fenced Python below (sha256 09c344921f1ede75…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_onboard_new_suppliers_agent.py` first:

```bash
python3 audit_onboard_new_suppliers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_onboard_new_suppliers_agent.py   # or on stdin
python3 audit_onboard_new_suppliers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard new suppliers Completeness Audit — Audits onboard new suppliers records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-onboard-new-suppliers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_onboard_new_suppliers',
    "version": '2.0.0',
    "display_name": 'Onboard new suppliers Completeness Audit',
    "description": 'Audits onboard new suppliers records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-onboard-new-suppliers',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-onboard-new-suppliers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f5847536a7e1154d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/onboard-new-suppliers'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/audit-onboard-new-suppliers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditOnboardNewSuppliers(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditOnboardNewSuppliers'
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
    print(AuditOnboardNewSuppliers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
