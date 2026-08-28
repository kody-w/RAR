---
name: "rar-cowork-cookbook-audit-insure-assets"
description: "Audits insure assets records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_insure_assets", "rar_sha256": "dd64589168f30e2fde80576fae97d79d4cfab722d5ff7ab131401b484acdb3cb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_insure_assets`. The original RAPP
agent is preserved byte-for-byte in `audit_insure_assets_agent.py` and in the RCI capsule.

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

Insure assets Completeness Audit — Audits insure assets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-insure-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_insure_assets_agent.py` and embedded as the fenced Python below (sha256 dd64589168f30e2f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_insure_assets_agent.py` first:

```bash
python3 audit_insure_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_insure_assets_agent.py   # or on stdin
python3 audit_insure_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Insure assets Completeness Audit — Audits insure assets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-insure-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_insure_assets',
    "version": '2.0.1',
    "display_name": 'Insure assets Completeness Audit',
    "description": 'Audits insure assets records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-insure-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-insure-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '05d7a5efc476e910',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/insure-assets'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/audit-insure-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.556, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditInsureAssets(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditInsureAssets'
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
    print(AuditInsureAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
