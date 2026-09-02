---
name: "rar-cowork-cookbook-audit-develop-procurement-catalogs"
description: "Audits develop procurement catalogs records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_procurement_catalogs", "rar_sha256": "9b7b5e8d6bb3e597dd5acff351546b0dad8f3f77814c563ef863629971645ca7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_develop_procurement_catalogs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-develop-procurement-catalogs:0618d2c74818003ec7cb780a77882dd9b29029065072d50e47038eef540a1a89", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_develop_procurement_catalogs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_develop_procurement_catalogs_agent.py` is
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

Develop procurement catalogs Completeness Audit — Audits develop procurement catalogs records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-procurement-catalogs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_procurement_catalogs_agent.py` and embedded as the fenced Python below (sha256 9b7b5e8d6bb3e597…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_procurement_catalogs_agent.py` first:

```bash
python3 audit_develop_procurement_catalogs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_procurement_catalogs_agent.py   # or on stdin
python3 audit_develop_procurement_catalogs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop procurement catalogs Completeness Audit — Audits develop procurement catalogs records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-procurement-catalogs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_procurement_catalogs',
    "version": '2.0.0',
    "display_name": 'Develop procurement catalogs Completeness Audit',
    "description": 'Audits develop procurement catalogs records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-develop-procurement-catalogs',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-procurement-catalogs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cc7aeac7b745342c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/develop-procurement-catalogs'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/audit-develop-procurement-catalogs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditDevelopProcurementCatalogs(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopProcurementCatalogs'
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
    print(AuditDevelopProcurementCatalogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
