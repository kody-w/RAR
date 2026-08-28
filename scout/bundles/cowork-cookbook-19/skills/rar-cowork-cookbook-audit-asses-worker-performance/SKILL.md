---
name: "rar-cowork-cookbook-audit-asses-worker-performance"
description: "Audits asses worker performance records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_asses_worker_performance", "rar_sha256": "609d61f6782798ac812646ee879822fe0fce1dbb565c174a925930568a1aebed", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_asses_worker_performance_agent.py` and embedded as the fenced Python below (sha256 609d61f6782798ac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_asses_worker_performance_agent.py` first:

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
    "version": '2.0.1',
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
