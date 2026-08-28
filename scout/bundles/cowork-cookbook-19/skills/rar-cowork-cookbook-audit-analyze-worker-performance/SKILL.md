---
name: "rar-cowork-cookbook-audit-analyze-worker-performance"
description: "Audits analyze worker performance records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_worker_performance", "rar_sha256": "6829b968e8a219f61797849303ae671e210a1583287a1828fa04f83c7b9622ff", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_worker_performance_agent.py` and embedded as the fenced Python below (sha256 6829b968e8a219f6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_worker_performance_agent.py` first:

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
    "version": '2.0.0',
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
