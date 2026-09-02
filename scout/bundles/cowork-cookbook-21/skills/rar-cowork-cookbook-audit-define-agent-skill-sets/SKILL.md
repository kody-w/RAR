---
name: "rar-cowork-cookbook-audit-define-agent-skill-sets"
description: "Audits define agent skill sets records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_agent_skill_sets", "rar_sha256": "a2853f82222eb6c3dc6115b53f3226bc7f79595a18230eb4eee02262fe585b36", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_define_agent_skill_sets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-define-agent-skill-sets:dc38be46560505b288b11917c81ec813abb38f31249cfc9543b0029376a80f77", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_define_agent_skill_sets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_define_agent_skill_sets_agent.py` is
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

Define agent skill sets Completeness Audit — Audits define agent skill sets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-agent-skill-sets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_agent_skill_sets_agent.py` and embedded as the fenced Python below (sha256 a2853f82222eb6c3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_agent_skill_sets_agent.py` first:

```bash
python3 audit_define_agent_skill_sets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_agent_skill_sets_agent.py   # or on stdin
python3 audit_define_agent_skill_sets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define agent skill sets Completeness Audit — Audits define agent skill sets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-agent-skill-sets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_agent_skill_sets',
    "version": '2.0.0',
    "display_name": 'Define agent skill sets Completeness Audit',
    "description": 'Audits define agent skill sets records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-define-agent-skill-sets',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-agent-skill-sets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a9f76b34f5f5f58d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-agent-skill-sets'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/audit-define-agent-skill-sets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditDefineAgentSkillSets(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineAgentSkillSets'
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
    print(AuditDefineAgentSkillSets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
