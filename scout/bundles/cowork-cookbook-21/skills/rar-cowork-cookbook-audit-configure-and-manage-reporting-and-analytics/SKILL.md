---
name: "rar-cowork-cookbook-audit-configure-and-manage-reporting-and-analytics"
description: "Audits configure and manage reporting and analytics records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_configure_and_manage_reporting_and_analytics", "rar_sha256": "a173221b84582d03922dea044bd4e37bd0dc905f52914854bfe34ee8767967fd", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_configure_and_manage_reporting_and_analytics`. The original RAPP
agent is preserved byte-for-byte in `audit_configure_and_manage_reporting_and_analytics_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_configure_and_manage_reporting_and_analytics_agent.py` and embedded as the fenced Python below (sha256 a173221b84582d03…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_configure_and_manage_reporting_and_analytics_agent.py` first:

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
    "version": '2.0.1',
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
