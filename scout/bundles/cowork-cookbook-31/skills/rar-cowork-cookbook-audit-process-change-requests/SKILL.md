---
name: "rar-cowork-cookbook-audit-process-change-requests"
description: "Audits process change requests records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_process_change_requests", "rar_sha256": "5940aeda5867dff8286f95e68efeac5e0d31ce84bc5fb287d97bd93a613cf8ca", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_process_change_requests_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-process-change-requests:ea6137293fce46f0b6b43c548f78c73a9486f2c76758b534f9834a0df7fc1ea2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_process_change_requests`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_process_change_requests_agent.py` is
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

Process change requests Completeness Audit — Audits process change requests records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-change-requests
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_process_change_requests_agent.py` and embedded as the fenced Python below (sha256 5940aeda5867dff8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_process_change_requests_agent.py` first:

```bash
python3 audit_process_change_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_process_change_requests_agent.py   # or on stdin
python3 audit_process_change_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process change requests Completeness Audit — Audits process change requests records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-change-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_process_change_requests',
    "version": '2.0.0',
    "display_name": 'Process change requests Completeness Audit',
    "description": 'Audits process change requests records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-process-change-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-process-change-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6cf88f43316b4a84',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/process-change-requests'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/audit-process-change-requests', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditProcessChangeRequests(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditProcessChangeRequests'
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
    print(AuditProcessChangeRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
