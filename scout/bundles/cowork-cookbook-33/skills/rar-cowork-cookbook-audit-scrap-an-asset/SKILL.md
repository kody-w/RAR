---
name: "rar-cowork-cookbook-audit-scrap-an-asset"
description: "Audits scrap an asset records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_scrap_an_asset", "rar_sha256": "4c65e9e1a2b9de45144929a1cd24acbdf66613aab9b65bc4375d20db4b9ceec1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_scrap_an_asset_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-scrap-an-asset:99a170ebe2779b86e1598bc85d2633a55065b5186d7da27ddafb19f44d00559f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_scrap_an_asset`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_scrap_an_asset_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_scrap_an_asset_agent.py` and embedded as the fenced Python below (sha256 4c65e9e1a2b9de45…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_scrap_an_asset_agent.py` first:

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
    "version": '2.0.0',
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
