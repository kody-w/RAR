---
name: "rar-cowork-cookbook-audit-asses-worker-performance"
description: "Audits asses worker performance records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_asses_worker_performance", "rar_sha256": "05c36eee21555aa98f256a8ce24f3b6a58085318e084b9b3be009f7f8feacd37", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_asses_worker_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-asses-worker-performance:c103bcb04e66757b7e1e15ef9d89281af5917244538f3374cdac07daae64b1a2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_asses_worker_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_asses_worker_performance_agent.py` is
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

Asses worker performance Completeness Audit — Audits asses worker performance records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-asses-worker-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_asses_worker_performance_agent.py` and embedded as the fenced Python below (sha256 05c36eee21555aa9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_asses_worker_performance_agent.py` first:

```bash
python3 audit_asses_worker_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_asses_worker_performance_agent.py   # or on stdin
python3 audit_asses_worker_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Asses worker performance Completeness Audit — Audits asses worker performance records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-asses-worker-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_asses_worker_performance',
    "version": '2.0.0',
    "display_name": 'Asses worker performance Completeness Audit',
    "description": 'Audits asses worker performance records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-asses-worker-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-asses-worker-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '58e3fcb4e6fc400e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/asses-worker-performance'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-asses-worker-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditAssesWorkerPerformance(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAssesWorkerPerformance'
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
    print(AuditAssesWorkerPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
