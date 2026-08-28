---
name: "rar-cowork-cookbook-audit-asses-worker-performance"
description: "Audits asses worker performance records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_asses_worker_performance", "rar_sha256": "05c36eee21555aa98f256a8ce24f3b6a58085318e084b9b3be009f7f8feacd37", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_asses_worker_performance`. The original RAPP
agent is preserved byte-for-byte in `audit_asses_worker_performance_agent.py` and in the RCI capsule.

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
