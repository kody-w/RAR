---
name: "rar-cowork-cookbook-audit-analyze-asset-leases"
description: "Audits analyze asset leases records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_asset_leases", "rar_sha256": "c6e12789c9c4381cc2c8fec2dfa6555051c475ee63880a78841068b661a05295", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_analyze_asset_leases_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-analyze-asset-leases:cca9a80425adad2e27de1cc3936a67bb497315982cbfe828679b57003217308c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_analyze_asset_leases`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_analyze_asset_leases_agent.py` is
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

Analyze asset leases Completeness Audit — Audits analyze asset leases records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-asset-leases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_asset_leases_agent.py` and embedded as the fenced Python below (sha256 c6e12789c9c4381c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_asset_leases_agent.py` first:

```bash
python3 audit_analyze_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_analyze_asset_leases_agent.py   # or on stdin
python3 audit_analyze_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze asset leases Completeness Audit — Audits analyze asset leases records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_analyze_asset_leases',
    "version": '2.0.0',
    "display_name": 'Analyze asset leases Completeness Audit',
    "description": 'Audits analyze asset leases records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-analyze-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-analyze-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5fe5c8ea0b1d0c27',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/analyze-asset-leases'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/audit-analyze-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditAnalyzeAssetLeases(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAnalyzeAssetLeases'
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
    print(AuditAnalyzeAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
