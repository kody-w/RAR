---
name: "rar-cowork-cookbook-audit-identify-service-trends"
description: "Audits identify service trends records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_identify_service_trends", "rar_sha256": "194deabf507734ffd06c6b28ea8c0e116c72274a87ebc1a14d7855381bed232a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_identify_service_trends_agent.py` and embedded as the fenced Python below (sha256 194deabf507734ff…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_identify_service_trends_agent.py` first:

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
    "version": '2.0.1',
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
