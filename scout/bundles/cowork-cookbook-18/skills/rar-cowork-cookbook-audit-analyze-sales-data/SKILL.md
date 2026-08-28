---
name: "rar-cowork-cookbook-audit-analyze-sales-data"
description: "Audits analyze sales data records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_sales_data", "rar_sha256": "30309535cf8944842601633086423b7fb98b5139b3e4534a0e19696eb48e2d25", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_sales_data_agent.py` and embedded as the fenced Python below (sha256 30309535cf894484…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_sales_data_agent.py` first:

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
    "version": '2.0.0',
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
