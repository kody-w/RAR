---
name: "rar-cowork-cookbook-vendor-master-cleanup"
description: "Identifies duplicate, incomplete, or inactive vendors in the master record and proposes a cleanup plan."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/vendor_master_cleanup", "rar_sha256": "6d2739c00e099c5c3bfc9e396297c37e80841229a70b3224ebde87826a5c8ef5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vendor_master_cleanup_agent.py` and embedded as the fenced Python below (sha256 6d2739c00e099c5c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vendor_master_cleanup_agent.py` first:

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
    "version": '2.0.1',
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
