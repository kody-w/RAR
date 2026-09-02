---
name: "rar-cowork-cookbook-audit-process-project-change-requests"
description: "Audits process project change requests records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_process_project_change_requests", "rar_sha256": "b7b2d5daec4da30b7ce23fd73f27a81a0905ac88440b7306a7e76f5c826343d0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_process_project_change_requests_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-process-project-change-requests:f5830ad6d585739e6f0a1c25ca2d2fb5f451af17e4bc440a3870f8d966c2ecea", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_process_project_change_requests`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_process_project_change_requests_agent.py` is
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

Process project change requests Completeness Audit — Audits process project change requests records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-project-change-requests
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_process_project_change_requests_agent.py` and embedded as the fenced Python below (sha256 b7b2d5daec4da30b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_process_project_change_requests_agent.py` first:

```bash
python3 audit_process_project_change_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_process_project_change_requests_agent.py   # or on stdin
python3 audit_process_project_change_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process project change requests Completeness Audit — Audits process project change requests records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-project-change-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_process_project_change_requests',
    "version": '2.0.0',
    "display_name": 'Process project change requests Completeness Audit',
    "description": 'Audits process project change requests records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-process-project-change-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-process-project-change-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '28c9dbee38784100',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/process-project-change-requests'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/audit-process-project-change-requests', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditProcessProjectChangeRequests(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditProcessProjectChangeRequests'
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
    print(AuditProcessProjectChangeRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
