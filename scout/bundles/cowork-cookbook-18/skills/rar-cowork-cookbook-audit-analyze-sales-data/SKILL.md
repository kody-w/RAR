---
name: "rar-cowork-cookbook-audit-analyze-sales-data"
description: "Audits analyze sales data records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_sales_data", "rar_sha256": "bac214d5d2e51b12565966a5c14bf0f2afb475ad7a3dd14933ce72f11c1b93c7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_analyze_sales_data`. The original RAPP
agent is preserved byte-for-byte in `audit_analyze_sales_data_agent.py` and in the RCI capsule.

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

Analyze sales data Completeness Audit — Audits analyze sales data records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-sales-data
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_sales_data_agent.py` and embedded as the fenced Python below (sha256 bac214d5d2e51b12…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_sales_data_agent.py` first:

```bash
python3 audit_analyze_sales_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_analyze_sales_data_agent.py   # or on stdin
python3 audit_analyze_sales_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze sales data Completeness Audit — Audits analyze sales data records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-sales-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_analyze_sales_data',
    "version": '2.0.1',
    "display_name": 'Analyze sales data Completeness Audit',
    "description": 'Audits analyze sales data records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-analyze-sales-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-analyze-sales-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '813c00fb048f2527',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/analyze-sales/analyze-sales-data'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/audit-analyze-sales-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditAnalyzeSalesData(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAnalyzeSalesData'
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
    print(AuditAnalyzeSalesData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
