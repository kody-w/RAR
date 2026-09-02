---
name: "rar-cowork-cookbook-audit-analyze-worker-performance"
description: "Audits analyze worker performance records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_worker_performance", "rar_sha256": "6829b968e8a219f61797849303ae671e210a1583287a1828fa04f83c7b9622ff", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_analyze_worker_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-analyze-worker-performance:c0df0fed8c924b909d12a0b5ff8d4e755bbfa766d4a11aa009ae4b7cb98eb913", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_analyze_worker_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_analyze_worker_performance_agent.py` is
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
