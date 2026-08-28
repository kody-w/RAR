---
name: "rar-cowork-cookbook-audit-record-asset-lease-right-of-use"
description: "Audits record asset lease right-of-use records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_record_asset_lease_right_of_use", "rar_sha256": "7612f1b5773babe920a4e659af497262c072c00c92c810d887c715e5ea18b2b7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_record_asset_lease_right_of_use_agent.py` and embedded as the fenced Python below (sha256 7612f1b5773babe9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_record_asset_lease_right_of_use_agent.py` first:

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
    "version": '2.0.1',
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
