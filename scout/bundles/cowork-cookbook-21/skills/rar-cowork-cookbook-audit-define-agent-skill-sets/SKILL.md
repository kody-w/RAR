---
name: "rar-cowork-cookbook-audit-define-agent-skill-sets"
description: "Audits define agent skill sets records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_agent_skill_sets", "rar_sha256": "a2853f82222eb6c3dc6115b53f3226bc7f79595a18230eb4eee02262fe585b36", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
