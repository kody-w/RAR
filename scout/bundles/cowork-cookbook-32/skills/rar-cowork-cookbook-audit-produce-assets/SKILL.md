---
name: "rar-cowork-cookbook-audit-produce-assets"
description: "Audits produce assets records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_produce_assets", "rar_sha256": "31d620124172ffe72e72e6193f374d1ac02b097530cc749d90cfabd065c1d6f7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_produce_assets_agent.py` and embedded as the fenced Python below (sha256 31d620124172ffe7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_produce_assets_agent.py` first:

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
    "version": '2.0.0',
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
