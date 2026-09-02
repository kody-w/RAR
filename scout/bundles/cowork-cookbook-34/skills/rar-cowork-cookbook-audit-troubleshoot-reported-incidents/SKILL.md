---
name: "rar-cowork-cookbook-audit-troubleshoot-reported-incidents"
description: "Audits troubleshoot reported incidents records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_troubleshoot_reported_incidents", "rar_sha256": "46e44fb0e00692e7112f42c3facbd4cb5e5b0a01b605952f543ee0bc5f2b4303", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_troubleshoot_reported_incidents_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-troubleshoot-reported-incidents:196aff1d9eccf2f8178b849de4c3737a9d1c6ac643d0accb5d4999a85b6445b0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_troubleshoot_reported_incidents`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_troubleshoot_reported_incidents_agent.py` is
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
