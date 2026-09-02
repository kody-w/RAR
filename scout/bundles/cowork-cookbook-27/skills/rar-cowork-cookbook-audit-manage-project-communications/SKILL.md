---
name: "rar-cowork-cookbook-audit-manage-project-communications"
description: "Audits manage project communications records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_project_communications", "rar_sha256": "73fa62ccfa57de3e1b2a0b1a31c21203f166592820f888edb2f6f060c05ce47d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_manage_project_communications_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-manage-project-communications:826db4878c4e072afda203b408143b8e5e36af21cb4b77e144a81482439e5ca3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_manage_project_communications`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_manage_project_communications_agent.py` is
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

Manage project communications Completeness Audit — Audits manage project communications records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-project-communications
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_project_communications_agent.py` and embedded as the fenced Python below (sha256 73fa62ccfa57de3e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_project_communications_agent.py` first:

```bash
python3 audit_manage_project_communications_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_manage_project_communications_agent.py   # or on stdin
python3 audit_manage_project_communications_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage project communications Completeness Audit — Audits manage project communications records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-project-communications
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_manage_project_communications',
    "version": '2.0.0',
    "display_name": 'Manage project communications Completeness Audit',
    "description": 'Audits manage project communications records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-manage-project-communications',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-manage-project-communications',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd5e75fd737b5b78d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/manage-project-communications'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/audit-manage-project-communications', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditManageProjectCommunications(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditManageProjectCommunications'
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
    print(AuditManageProjectCommunications().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
