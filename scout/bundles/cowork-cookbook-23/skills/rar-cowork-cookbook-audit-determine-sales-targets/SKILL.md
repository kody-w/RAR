---
name: "rar-cowork-cookbook-audit-determine-sales-targets"
description: "Audits determine sales targets records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_determine_sales_targets", "rar_sha256": "d745e42aa59db3850641fa1eb468789e9228c581ac9533de9c254bfbca5eccaf", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_determine_sales_targets`. The original RAPP
agent is preserved byte-for-byte in `audit_determine_sales_targets_agent.py` and in the RCI capsule.

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

Determine sales targets Completeness Audit — Audits determine sales targets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-determine-sales-targets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_determine_sales_targets_agent.py` and embedded as the fenced Python below (sha256 d745e42aa59db385…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_determine_sales_targets_agent.py` first:

```bash
python3 audit_determine_sales_targets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_determine_sales_targets_agent.py   # or on stdin
python3 audit_determine_sales_targets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Determine sales targets Completeness Audit — Audits determine sales targets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-determine-sales-targets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_determine_sales_targets',
    "version": '2.0.1',
    "display_name": 'Determine sales targets Completeness Audit',
    "description": 'Audits determine sales targets records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'audit-determine-sales-targets',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-determine-sales-targets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b4437a045ed395fd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/determine-sales-targets'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/audit-determine-sales-targets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditDetermineSalesTargets(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDetermineSalesTargets'
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
    print(AuditDetermineSalesTargets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
