---
name: "rar-cowork-cookbook-audit-analyze-worker-performance"
description: "Audits analyze worker performance records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_worker_performance", "rar_sha256": "b50ba6598d2558c6c0f98a6cf88c4ffa11d80f66852dbd6e99a639edde6caccf", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_analyze_worker_performance`. The original RAPP
agent is preserved byte-for-byte in `audit_analyze_worker_performance_agent.py` and in the RCI capsule.

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

Analyze worker performance Completeness Audit — Audits analyze worker performance records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-worker-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_worker_performance_agent.py` and embedded as the fenced Python below (sha256 b50ba6598d2558c6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_worker_performance_agent.py` first:

```bash
python3 audit_analyze_worker_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_analyze_worker_performance_agent.py   # or on stdin
python3 audit_analyze_worker_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze worker performance Completeness Audit — Audits analyze worker performance records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-worker-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_analyze_worker_performance',
    "version": '2.0.1',
    "display_name": 'Analyze worker performance Completeness Audit',
    "description": 'Audits analyze worker performance records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-analyze-worker-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-analyze-worker-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '23408aaa4f8277b6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/analyze-worker-performance'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-analyze-worker-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditAnalyzeWorkerPerformance(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAnalyzeWorkerPerformance'
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
    print(AuditAnalyzeWorkerPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
