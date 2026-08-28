---
name: "rar-cowork-cookbook-audit-develop-procurement-catalogs"
description: "Audits develop procurement catalogs records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_procurement_catalogs", "rar_sha256": "1dac1e404dba6c8729c4cb52c475e2d088c4c1f3296ae21a428f44abd7a60ae2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_procurement_catalogs_agent.py` and embedded as the fenced Python below (sha256 1dac1e404dba6c87…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_procurement_catalogs_agent.py` first:

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
    "version": '2.0.1',
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
