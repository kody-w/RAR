---
name: "rar-cowork-cookbook-audit-record-asset-lease-right-of-use"
description: "Audits record asset lease right-of-use records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_record_asset_lease_right_of_use", "rar_sha256": "7b8f1c2203250220ae3fbb28d4f7485722d73e3937f3de9860e3c96e9f8f44fd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_record_asset_lease_right_of_use_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-record-asset-lease-right-of-use:f02ab5496c2b4e9f6da00f18091f3a78719b3fecfc3aa8f8fb577f1b05f9de74", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_record_asset_lease_right_of_use`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_record_asset_lease_right_of_use_agent.py` is
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

Record asset lease right-of-use Completeness Audit — Audits record asset lease right-of-use records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-record-asset-lease-right-of-use
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_record_asset_lease_right_of_use_agent.py` and embedded as the fenced Python below (sha256 7b8f1c2203250220…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_record_asset_lease_right_of_use_agent.py` first:

```bash
python3 audit_record_asset_lease_right_of_use_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_record_asset_lease_right_of_use_agent.py   # or on stdin
python3 audit_record_asset_lease_right_of_use_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record asset lease right-of-use Completeness Audit — Audits record asset lease right-of-use records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-record-asset-lease-right-of-use
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_record_asset_lease_right_of_use',
    "version": '2.0.0',
    "display_name": 'Record asset lease right-of-use Completeness Audit',
    "description": 'Audits record asset lease right-of-use records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-record-asset-lease-right-of-use',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-record-asset-lease-right-of-use',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'af059344dbb3f189',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/record-asset-lease-right-of-use'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/audit-record-asset-lease-right-of-use', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditRecordAssetLeaseRightOfUse(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditRecordAssetLeaseRightOfUse'
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
    print(AuditRecordAssetLeaseRightOfUse().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
