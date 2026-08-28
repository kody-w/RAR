---
name: "rar-cowork-cookbook-audit-monitor-project-risks"
description: "Audits monitor project risks records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_monitor_project_risks", "rar_sha256": "a36e40a35bc78bce93a95f205e4f150ee34674608103f26826fccca45886f350", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_monitor_project_risks_agent.py` and embedded as the fenced Python below (sha256 a36e40a35bc78bce…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_monitor_project_risks_agent.py` first:

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
    "version": '2.0.1',
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
