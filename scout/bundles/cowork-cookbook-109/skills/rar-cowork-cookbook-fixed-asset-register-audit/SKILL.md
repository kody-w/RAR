---
name: "rar-cowork-cookbook-fixed-asset-register-audit"
description: "Audits the fixed asset register for missing fields, inconsistent depreciation profiles, and assets due for retirement."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/fixed_asset_register_audit", "rar_sha256": "4af834188f2a1a4faa274599e7d4e94275f3c665193e048894bfa41dd0527c4b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/fixed_asset_register_audit`. The original RAPP
agent is preserved byte-for-byte in `fixed_asset_register_audit_agent.py` and in the RCI capsule.

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

Fixed Asset Register Audit — Audits the fixed asset register for missing fields, inconsistent depreciation profiles, and assets due for retirement.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/fixed-asset-register-audit
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `fixed_asset_register_audit_agent.py` and embedded as the fenced Python below (sha256 4af834188f2a1a4f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `fixed_asset_register_audit_agent.py` first:

```bash
python3 fixed_asset_register_audit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 fixed_asset_register_audit_agent.py   # or on stdin
python3 fixed_asset_register_audit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Fixed Asset Register Audit — Audits the fixed asset register for missing fields, inconsistent depreciation profiles, and assets due for retirement.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/fixed-asset-register-audit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/fixed_asset_register_audit',
    "version": '2.0.1',
    "display_name": 'Fixed Asset Register Audit',
    "description": 'Audits the fixed asset register for missing fields, inconsistent depreciation profiles, and assets due for retirement.',
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
        "upstream_slug": 'fixed-asset-register-audit',
        "upstream_url": 'https://coworkcookbook.com/recipes/fixed-asset-register-audit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '39d63ed89c228565',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/fixed-asset-register-audit', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.429, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:audit'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class FixedAssetRegisterAudit(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'FixedAssetRegisterAudit'
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
    print(FixedAssetRegisterAudit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
