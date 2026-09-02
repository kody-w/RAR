---
name: "rar-cowork-cookbook-audit-identify-service-trends"
description: "Audits identify service trends records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_identify_service_trends", "rar_sha256": "ad6b7e78f47baf97cdb65bd253d8389364dd11ecd417b1f446020e97daacd847", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_identify_service_trends_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-identify-service-trends:6d04b6fa014a45693186554da11e592fd7e4cd3532a5f7f8a1b476550c04db72", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_identify_service_trends`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_identify_service_trends_agent.py` is
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

Identify service trends Completeness Audit — Audits identify service trends records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-identify-service-trends
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_identify_service_trends_agent.py` and embedded as the fenced Python below (sha256 ad6b7e78f47baf97…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_identify_service_trends_agent.py` first:

```bash
python3 audit_identify_service_trends_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_identify_service_trends_agent.py   # or on stdin
python3 audit_identify_service_trends_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify service trends Completeness Audit — Audits identify service trends records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-identify-service-trends
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_identify_service_trends',
    "version": '2.0.0',
    "display_name": 'Identify service trends Completeness Audit',
    "description": 'Audits identify service trends records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-identify-service-trends',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-identify-service-trends',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8acfa90e72d44c7c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/analyze-service-performance/identify-service-trends'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/audit-identify-service-trends', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditIdentifyServiceTrends(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditIdentifyServiceTrends'
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
    print(AuditIdentifyServiceTrends().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
