---
name: "rar-cowork-cookbook-fixed-asset-register-audit"
description: "Audits the fixed asset register for missing fields, inconsistent depreciation profiles, and assets due for retirement."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/fixed_asset_register_audit", "rar_sha256": "6ed6542ca6929599ac160e485c6925697c9a379baffd621e592b9ce94923f1fe", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "fixed_asset_register_audit_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/fixed-asset-register-audit:2e29f03d26fc939632fad03949a01e4faae563e2e729299f1b6f696e7a02fe5e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/fixed_asset_register_audit`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `fixed_asset_register_audit_agent.py` is
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
