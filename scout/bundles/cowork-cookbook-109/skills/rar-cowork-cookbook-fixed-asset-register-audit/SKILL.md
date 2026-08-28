---
name: "rar-cowork-cookbook-fixed-asset-register-audit"
description: "Audits the fixed asset register for missing fields, inconsistent depreciation profiles, and assets due for retirement."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/fixed_asset_register_audit", "rar_sha256": "6ed6542ca6929599ac160e485c6925697c9a379baffd621e592b9ce94923f1fe", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `fixed_asset_register_audit_agent.py` and embedded as the fenced Python below (sha256 6ed6542ca6929599…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `fixed_asset_register_audit_agent.py` first:

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
    "version": '2.0.0',
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
