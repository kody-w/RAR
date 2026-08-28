---
name: "rar-cowork-cookbook-audit-record-asset-lease-right-of-use"
description: "Audits record asset lease right-of-use records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_record_asset_lease_right_of_use", "rar_sha256": "7b8f1c2203250220ae3fbb28d4f7485722d73e3937f3de9860e3c96e9f8f44fd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_record_asset_lease_right_of_use`. The original RAPP
agent is preserved byte-for-byte in `audit_record_asset_lease_right_of_use_agent.py` and in the RCI capsule.

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
