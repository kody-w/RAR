---
name: "rar-cowork-cookbook-audit-maintain-open-service-requests"
description: "Audits maintain open service requests records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_maintain_open_service_requests", "rar_sha256": "fb160a5a2353162fbb7879e1d9e8110e713df6bb0cd8881347b2ce84614193aa", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_maintain_open_service_requests`. The original RAPP
agent is preserved byte-for-byte in `audit_maintain_open_service_requests_agent.py` and in the RCI capsule.

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

Maintain open service requests Completeness Audit — Audits maintain open service requests records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-maintain-open-service-requests
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_maintain_open_service_requests_agent.py` and embedded as the fenced Python below (sha256 fb160a5a2353162f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_maintain_open_service_requests_agent.py` first:

```bash
python3 audit_maintain_open_service_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_maintain_open_service_requests_agent.py   # or on stdin
python3 audit_maintain_open_service_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain open service requests Completeness Audit — Audits maintain open service requests records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-maintain-open-service-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_maintain_open_service_requests',
    "version": '2.0.0',
    "display_name": 'Maintain open service requests Completeness Audit',
    "description": 'Audits maintain open service requests records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-maintain-open-service-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-maintain-open-service-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1827097505563b96',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/maintain-open-service-requests'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/audit-maintain-open-service-requests', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditMaintainOpenServiceRequests(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditMaintainOpenServiceRequests'
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
    print(AuditMaintainOpenServiceRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
