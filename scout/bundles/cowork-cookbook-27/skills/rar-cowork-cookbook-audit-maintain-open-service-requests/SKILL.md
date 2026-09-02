---
name: "rar-cowork-cookbook-audit-maintain-open-service-requests"
description: "Audits maintain open service requests records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_maintain_open_service_requests", "rar_sha256": "fb160a5a2353162fbb7879e1d9e8110e713df6bb0cd8881347b2ce84614193aa", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_maintain_open_service_requests_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-maintain-open-service-requests:3415217183928dfebe73f7c13cfe090d5d18e60b2016ae36d73bc6b6a8eb4f91", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_maintain_open_service_requests`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_maintain_open_service_requests_agent.py` is
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
