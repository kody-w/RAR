---
name: "rar-cowork-cookbook-audit-manage-project-communications"
description: "Audits manage project communications records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_project_communications", "rar_sha256": "73fa62ccfa57de3e1b2a0b1a31c21203f166592820f888edb2f6f060c05ce47d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_manage_project_communications`. The original RAPP
agent is preserved byte-for-byte in `audit_manage_project_communications_agent.py` and in the RCI capsule.

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
