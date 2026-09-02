---
name: "rar-cowork-cookbook-vendor-master-cleanup"
description: "Identifies duplicate, incomplete, or inactive vendors in the master record and proposes a cleanup plan."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/vendor_master_cleanup", "rar_sha256": "e35db88e2b480e9fc65cf124389bd28c1148750d116ce79201593f5779c51b4b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "vendor_master_cleanup_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/vendor-master-cleanup:6f59959de4c3b14d5bd6afac282f1cea709aa2664a05d026a60b464fa01cb6ad", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/vendor_master_cleanup`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `vendor_master_cleanup_agent.py` is
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

Vendor Master Cleanup Report — Identifies duplicate, incomplete, or inactive vendors in the master record and proposes a cleanup plan.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/vendor-master-cleanup
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vendor_master_cleanup_agent.py` and embedded as the fenced Python below (sha256 e35db88e2b480e9f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vendor_master_cleanup_agent.py` first:

```bash
python3 vendor_master_cleanup_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 vendor_master_cleanup_agent.py   # or on stdin
python3 vendor_master_cleanup_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Vendor Master Cleanup Report — Identifies duplicate, incomplete, or inactive vendors in the master record and proposes a cleanup plan.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/vendor-master-cleanup
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/vendor_master_cleanup',
    "version": '2.0.0',
    "display_name": 'Vendor Master Cleanup Report',
    "description": 'Identifies duplicate, incomplete, or inactive vendors in the master record and proposes a cleanup plan.',
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
        "upstream_slug": 'vendor-master-cleanup',
        "upstream_url": 'https://coworkcookbook.com/recipes/vendor-master-cleanup',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8cc312cdb130b37c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/vendor-master-cleanup', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.286, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class VendorMasterCleanup(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'VendorMasterCleanup'
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
    print(VendorMasterCleanup().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
