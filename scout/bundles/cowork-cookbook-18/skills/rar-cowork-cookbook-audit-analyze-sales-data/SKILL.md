---
name: "rar-cowork-cookbook-audit-analyze-sales-data"
description: "Audits analyze sales data records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_sales_data", "rar_sha256": "30309535cf8944842601633086423b7fb98b5139b3e4534a0e19696eb48e2d25", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_analyze_sales_data_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-analyze-sales-data:f50fc871b2f2b6272f0f9c6f1b9efeb46cd04d01dafd8057817c1e7f0171e40b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_analyze_sales_data`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_analyze_sales_data_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
