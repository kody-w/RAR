---
name: "rar-cowork-cookbook-vendor-master-cleanup"
description: "Identifies duplicate, incomplete, or inactive vendors in the master record and proposes a cleanup plan."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/vendor_master_cleanup", "rar_sha256": "e35db88e2b480e9fc65cf124389bd28c1148750d116ce79201593f5779c51b4b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/vendor_master_cleanup`. The original RAPP
agent is preserved byte-for-byte in `vendor_master_cleanup_agent.py` and in the RCI capsule.

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
