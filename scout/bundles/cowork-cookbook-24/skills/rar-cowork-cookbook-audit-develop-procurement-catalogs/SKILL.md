---
name: "rar-cowork-cookbook-audit-develop-procurement-catalogs"
description: "Audits develop procurement catalogs records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_procurement_catalogs", "rar_sha256": "9b7b5e8d6bb3e597dd5acff351546b0dad8f3f77814c563ef863629971645ca7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_develop_procurement_catalogs`. The original RAPP
agent is preserved byte-for-byte in `audit_develop_procurement_catalogs_agent.py` and in the RCI capsule.

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
