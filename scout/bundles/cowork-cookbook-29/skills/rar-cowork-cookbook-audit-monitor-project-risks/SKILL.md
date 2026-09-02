---
name: "rar-cowork-cookbook-audit-monitor-project-risks"
description: "Audits monitor project risks records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_monitor_project_risks", "rar_sha256": "cb21c37d83e0dc77939a3ef239a321770a633454312c0e02b1fda1655c87f09f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_monitor_project_risks_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-monitor-project-risks:5a51c742693260244bfd9f98f9d8fa1dc6dede1560dd047d5fd0e782f1ae8dae", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_monitor_project_risks`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_monitor_project_risks_agent.py` is
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

Monitor project risks Completeness Audit — Audits monitor project risks records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-monitor-project-risks
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_monitor_project_risks_agent.py` and embedded as the fenced Python below (sha256 cb21c37d83e0dc77…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_monitor_project_risks_agent.py` first:

```bash
python3 audit_monitor_project_risks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_monitor_project_risks_agent.py   # or on stdin
python3 audit_monitor_project_risks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor project risks Completeness Audit — Audits monitor project risks records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-monitor-project-risks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_monitor_project_risks',
    "version": '2.0.0',
    "display_name": 'Monitor project risks Completeness Audit',
    "description": 'Audits monitor project risks records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-monitor-project-risks',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-monitor-project-risks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2991b81293d1d7ef',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/analyze-project-performance/monitor-project-risks'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/audit-monitor-project-risks', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditMonitorProjectRisks(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditMonitorProjectRisks'
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
    print(AuditMonitorProjectRisks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
