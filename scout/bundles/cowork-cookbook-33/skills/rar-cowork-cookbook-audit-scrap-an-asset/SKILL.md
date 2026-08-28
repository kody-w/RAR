---
name: "rar-cowork-cookbook-audit-scrap-an-asset"
description: "Audits scrap an asset records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_scrap_an_asset", "rar_sha256": "b5586e3d4d8859f863c3c31449c5fbacf7a6f6e48deabdbfe2086bf88a4ce53c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_scrap_an_asset`. The original RAPP
agent is preserved byte-for-byte in `audit_scrap_an_asset_agent.py` and in the RCI capsule.

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

Scrap an asset Completeness Audit — Audits scrap an asset records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-scrap-an-asset
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_scrap_an_asset_agent.py` and embedded as the fenced Python below (sha256 b5586e3d4d8859f8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_scrap_an_asset_agent.py` first:

```bash
python3 audit_scrap_an_asset_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_scrap_an_asset_agent.py   # or on stdin
python3 audit_scrap_an_asset_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Scrap an asset Completeness Audit — Audits scrap an asset records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-scrap-an-asset
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_scrap_an_asset',
    "version": '2.0.1',
    "display_name": 'Scrap an asset Completeness Audit',
    "description": 'Audits scrap an asset records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-scrap-an-asset',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-scrap-an-asset',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '333b1209737f1d37',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/scrap-an-asset'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/audit-scrap-an-asset', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditScrapAnAsset(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditScrapAnAsset'
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
    print(AuditScrapAnAsset().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
