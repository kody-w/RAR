---
name: "rar-cowork-cookbook-bom-completeness-audit"
description: "Audits active BOMs for missing components, expired versions, and items that are obsolete."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bom_completeness_audit", "rar_sha256": "ddc0ef63bda93ead91cbbb25116d6b3389aee0ffd89837a68c7f56663e308f64", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bom_completeness_audit`. The original RAPP
agent is preserved byte-for-byte in `bom_completeness_audit_agent.py` and in the RCI capsule.

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

BOM Completeness Audit — Audits active BOMs for missing components, expired versions, and items that are obsolete.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bom-completeness-audit
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bom_completeness_audit_agent.py` and embedded as the fenced Python below (sha256 ddc0ef63bda93ead…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bom_completeness_audit_agent.py` first:

```bash
python3 bom_completeness_audit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bom_completeness_audit_agent.py   # or on stdin
python3 bom_completeness_audit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
BOM Completeness Audit — Audits active BOMs for missing components, expired versions, and items that are obsolete.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bom-completeness-audit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bom_completeness_audit',
    "version": '2.0.1',
    "display_name": 'BOM Completeness Audit',
    "description": 'Audits active BOMs for missing components, expired versions, and items that are obsolete.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bom-completeness-audit',
        "upstream_url": 'https://coworkcookbook.com/recipes/bom-completeness-audit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6d2f831e34b92f83',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/bom-completeness-audit', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class BomCompletenessAudit(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BomCompletenessAudit'
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
    print(BomCompletenessAudit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
