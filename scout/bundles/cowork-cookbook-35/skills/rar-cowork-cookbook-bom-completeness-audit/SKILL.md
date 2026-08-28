---
name: "rar-cowork-cookbook-bom-completeness-audit"
description: "Audits active BOMs for missing components, expired versions, and items that are obsolete."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bom_completeness_audit", "rar_sha256": "1391ef31c56ca86c0f6d4198c1ec90b6cbf7e21b8a9acff91d6223765a9d24e8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bom_completeness_audit_agent.py` and embedded as the fenced Python below (sha256 1391ef31c56ca86c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bom_completeness_audit_agent.py` first:

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
    "version": '2.0.0',
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
