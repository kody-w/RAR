---
name: "rar-cowork-cookbook-audit-analyze-order-management-processes"
description: "Audits analyze order management processes records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_order_management_processes", "rar_sha256": "8598e4c49a70fa8271b628ba63333bb604901a4f0efdeefe3ffc5a0696b67ecc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_analyze_order_management_processes_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-analyze-order-management-processes:1ba32d2e5a8836ccc2b4b816ee564195b78468e9f3cc6150739ee898091f8e02", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_analyze_order_management_processes`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_analyze_order_management_processes_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_order_management_processes_agent.py` and embedded as the fenced Python below (sha256 8598e4c49a70fa82…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_order_management_processes_agent.py` first:

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
    "version": '2.0.0',
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
