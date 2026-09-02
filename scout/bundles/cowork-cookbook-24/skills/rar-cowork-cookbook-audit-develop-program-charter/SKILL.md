---
name: "rar-cowork-cookbook-audit-develop-program-charter"
description: "Audits develop program charter records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_program_charter", "rar_sha256": "41636a364707b4f807320da54e77fcf0d1545d020b0e0434e077bbbb3c96bfe3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_develop_program_charter_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-develop-program-charter:0a0ba4ac294e334cf9c932986ab946e23bd9b9f871e6848c8f89072c80f7b4ee", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_develop_program_charter`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_develop_program_charter_agent.py` is
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

Develop program charter Completeness Audit — Audits develop program charter records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-program-charter
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_program_charter_agent.py` and embedded as the fenced Python below (sha256 41636a364707b4f8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_program_charter_agent.py` first:

```bash
python3 audit_develop_program_charter_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_program_charter_agent.py   # or on stdin
python3 audit_develop_program_charter_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop program charter Completeness Audit — Audits develop program charter records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-program-charter
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_program_charter',
    "version": '2.0.0',
    "display_name": 'Develop program charter Completeness Audit',
    "description": 'Audits develop program charter records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-develop-program-charter',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-program-charter',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8b4695453f491a85',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/develop-project-strategy/develop-program-charter'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/audit-develop-program-charter', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditDevelopProgramCharter(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopProgramCharter'
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
    print(AuditDevelopProgramCharter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
