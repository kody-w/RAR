---
name: "rar-cowork-cookbook-audit-configure-and-manage-reporting-and-analytics"
description: "Audits configure and manage reporting and analytics records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_configure_and_manage_reporting_and_analytics", "rar_sha256": "c401c039e10289d577c5668200d1ba1561ee90745becd4f3477b1892265573a8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_configure_and_manage_reporting_and_analytics_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-configure-and-manage-reporting-and-analytics:7ddc9c531c4e55b885996b43c88b0e5bc3c4fb9f688d9251a757cd6c5afbdb3c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_configure_and_manage_reporting_and_analytics`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_configure_and_manage_reporting_and_analytics_agent.py` is
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

Configure and manage reporting and analytics Completeness Audit — Audits configure and manage reporting and analytics records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-configure-and-manage-reporting-and-analytics
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_configure_and_manage_reporting_and_analytics_agent.py` and embedded as the fenced Python below (sha256 c401c039e10289d5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_configure_and_manage_reporting_and_analytics_agent.py` first:

```bash
python3 audit_configure_and_manage_reporting_and_analytics_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_configure_and_manage_reporting_and_analytics_agent.py   # or on stdin
python3 audit_configure_and_manage_reporting_and_analytics_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage reporting and analytics Completeness Audit — Audits configure and manage reporting and analytics records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-configure-and-manage-reporting-and-analytics
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_configure_and_manage_reporting_and_analytics',
    "version": '2.0.0',
    "display_name": 'Configure and manage reporting and analytics Completeness Audit',
    "description": 'Audits configure and manage reporting and analytics records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-configure-and-manage-reporting-and-analytics',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-configure-and-manage-reporting-and-analytics',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6559c7cc2bc97862',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-reporting-and-analytics'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-configure-and-manage-reporting-and-analytics', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditConfigureAndManageReportingAndAnalytics(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditConfigureAndManageReportingAndAnalytics'
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
    print(AuditConfigureAndManageReportingAndAnalytics().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
