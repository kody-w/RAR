---
name: "rar-cowork-cookbook-audit-analyze-asset-leases"
description: "Audits analyze asset leases records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_asset_leases", "rar_sha256": "c6e12789c9c4381cc2c8fec2dfa6555051c475ee63880a78841068b661a05295", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_analyze_asset_leases`. The original RAPP
agent is preserved byte-for-byte in `audit_analyze_asset_leases_agent.py` and in the RCI capsule.

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

Analyze asset leases Completeness Audit — Audits analyze asset leases records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-asset-leases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_asset_leases_agent.py` and embedded as the fenced Python below (sha256 c6e12789c9c4381c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_asset_leases_agent.py` first:

```bash
python3 audit_analyze_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_analyze_asset_leases_agent.py   # or on stdin
python3 audit_analyze_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze asset leases Completeness Audit — Audits analyze asset leases records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_analyze_asset_leases',
    "version": '2.0.0',
    "display_name": 'Analyze asset leases Completeness Audit',
    "description": 'Audits analyze asset leases records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-analyze-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-analyze-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5fe5c8ea0b1d0c27',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/analyze-asset-leases'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/audit-analyze-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditAnalyzeAssetLeases(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAnalyzeAssetLeases'
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
    print(AuditAnalyzeAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
