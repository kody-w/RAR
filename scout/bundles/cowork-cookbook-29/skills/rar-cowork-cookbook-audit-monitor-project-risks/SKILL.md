---
name: "rar-cowork-cookbook-audit-monitor-project-risks"
description: "Audits monitor project risks records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_monitor_project_risks", "rar_sha256": "cb21c37d83e0dc77939a3ef239a321770a633454312c0e02b1fda1655c87f09f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_monitor_project_risks`. The original RAPP
agent is preserved byte-for-byte in `audit_monitor_project_risks_agent.py` and in the RCI capsule.

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
