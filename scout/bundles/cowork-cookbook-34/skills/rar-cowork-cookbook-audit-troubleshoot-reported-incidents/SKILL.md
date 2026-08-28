---
name: "rar-cowork-cookbook-audit-troubleshoot-reported-incidents"
description: "Audits troubleshoot reported incidents records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_troubleshoot_reported_incidents", "rar_sha256": "15ff61694de13e141819ed327ee375fa2ee13993f6aecd2550d8b50f6e7c2cf4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_troubleshoot_reported_incidents`. The original RAPP
agent is preserved byte-for-byte in `audit_troubleshoot_reported_incidents_agent.py` and in the RCI capsule.

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

Troubleshoot reported incidents Completeness Audit — Audits troubleshoot reported incidents records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-troubleshoot-reported-incidents
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_troubleshoot_reported_incidents_agent.py` and embedded as the fenced Python below (sha256 15ff61694de13e14…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_troubleshoot_reported_incidents_agent.py` first:

```bash
python3 audit_troubleshoot_reported_incidents_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_troubleshoot_reported_incidents_agent.py   # or on stdin
python3 audit_troubleshoot_reported_incidents_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Troubleshoot reported incidents Completeness Audit — Audits troubleshoot reported incidents records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-troubleshoot-reported-incidents
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_troubleshoot_reported_incidents',
    "version": '2.0.1',
    "display_name": 'Troubleshoot reported incidents Completeness Audit',
    "description": 'Audits troubleshoot reported incidents records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-troubleshoot-reported-incidents',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-troubleshoot-reported-incidents',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5a6f789abfeb615d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-04', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/troubleshoot-reported-incidents'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-troubleshoot-reported-incidents', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditTroubleshootReportedIncidents(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditTroubleshootReportedIncidents'
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
    print(AuditTroubleshootReportedIncidents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
