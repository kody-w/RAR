---
name: "rar-cowork-cookbook-audit-analyze-order-management-processes"
description: "Audits analyze order management processes records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_order_management_processes", "rar_sha256": "161b23d4aa625f65a44869c89f23a0d185e63d70281ca3296126a29cee1d990b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_analyze_order_management_processes`. The original RAPP
agent is preserved byte-for-byte in `audit_analyze_order_management_processes_agent.py` and in the RCI capsule.

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

Analyze order management processes Completeness Audit — Audits analyze order management processes records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-order-management-processes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_order_management_processes_agent.py` and embedded as the fenced Python below (sha256 161b23d4aa625f65…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_order_management_processes_agent.py` first:

```bash
python3 audit_analyze_order_management_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_analyze_order_management_processes_agent.py   # or on stdin
python3 audit_analyze_order_management_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze order management processes Completeness Audit — Audits analyze order management processes records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-order-management-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_analyze_order_management_processes',
    "version": '2.0.1',
    "display_name": 'Analyze order management processes Completeness Audit',
    "description": 'Audits analyze order management processes records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-analyze-order-management-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-analyze-order-management-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '58000345806d3718',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/analyze-order-management-processes'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/audit-analyze-order-management-processes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditAnalyzeOrderManagementProcesses(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAnalyzeOrderManagementProcesses'
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
    print(AuditAnalyzeOrderManagementProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
