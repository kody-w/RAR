---
name: "rar-cowork-cookbook-audit-define-agent-skill-sets"
description: "Audits define agent skill sets records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_agent_skill_sets", "rar_sha256": "d1aa6d64676ed18cbceff938839f5d2ba4e2a9dedaabadf2e752c607a9946d2f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_define_agent_skill_sets`. The original RAPP
agent is preserved byte-for-byte in `audit_define_agent_skill_sets_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_agent_skill_sets_agent.py` and embedded as the fenced Python below (sha256 d1aa6d64676ed18c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_agent_skill_sets_agent.py` first:

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
    "version": '2.0.1',
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
