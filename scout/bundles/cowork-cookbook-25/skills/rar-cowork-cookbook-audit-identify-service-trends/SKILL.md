---
name: "rar-cowork-cookbook-audit-identify-service-trends"
description: "Audits identify service trends records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_identify_service_trends", "rar_sha256": "ad6b7e78f47baf97cdb65bd253d8389364dd11ecd417b1f446020e97daacd847", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_identify_service_trends`. The original RAPP
agent is preserved byte-for-byte in `audit_identify_service_trends_agent.py` and in the RCI capsule.

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
