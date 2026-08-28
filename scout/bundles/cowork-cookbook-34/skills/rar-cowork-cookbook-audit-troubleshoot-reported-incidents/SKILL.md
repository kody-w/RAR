---
name: "rar-cowork-cookbook-audit-troubleshoot-reported-incidents"
description: "Audits troubleshoot reported incidents records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_troubleshoot_reported_incidents", "rar_sha256": "46e44fb0e00692e7112f42c3facbd4cb5e5b0a01b605952f543ee0bc5f2b4303", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_troubleshoot_reported_incidents_agent.py` and embedded as the fenced Python below (sha256 46e44fb0e00692e7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_troubleshoot_reported_incidents_agent.py` first:

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
    "version": '2.0.0',
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
