---
name: "rar-cowork-cookbook-audit-produce-assets"
description: "Audits produce assets records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_produce_assets", "rar_sha256": "d021772905ba08da76701038ad537e83251f0fb3ad20fa91ef8392df7b67f511", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_produce_assets`. The original RAPP
agent is preserved byte-for-byte in `audit_produce_assets_agent.py` and in the RCI capsule.

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

Produce assets Completeness Audit — Audits produce assets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-produce-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_produce_assets_agent.py` and embedded as the fenced Python below (sha256 d021772905ba08da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_produce_assets_agent.py` first:

```bash
python3 audit_produce_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_produce_assets_agent.py   # or on stdin
python3 audit_produce_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Produce assets Completeness Audit — Audits produce assets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-produce-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_produce_assets',
    "version": '2.0.1',
    "display_name": 'Produce assets Completeness Audit',
    "description": 'Audits produce assets records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-produce-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-produce-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c67e75c7e751805e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/produce-assets'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/audit-produce-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditProduceAssets(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditProduceAssets'
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
    print(AuditProduceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
