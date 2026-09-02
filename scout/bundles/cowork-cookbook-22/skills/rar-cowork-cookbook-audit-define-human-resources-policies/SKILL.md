---
name: "rar-cowork-cookbook-audit-define-human-resources-policies"
description: "Audits define human resources policies records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_human_resources_policies", "rar_sha256": "da5a0a9d16f665a3e6a52919bf8581e4f45edd05bfe5516a1768b4bfda2a22ab", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_define_human_resources_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-define-human-resources-policies:254bc7511656a4fdb31cad36520860eebb459d356984e17fac4d7e606d3305e7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_define_human_resources_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_define_human_resources_policies_agent.py` is
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

Define human resources policies Completeness Audit — Audits define human resources policies records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-human-resources-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_human_resources_policies_agent.py` and embedded as the fenced Python below (sha256 da5a0a9d16f665a3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_human_resources_policies_agent.py` first:

```bash
python3 audit_define_human_resources_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_human_resources_policies_agent.py   # or on stdin
python3 audit_define_human_resources_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define human resources policies Completeness Audit — Audits define human resources policies records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-human-resources-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_human_resources_policies',
    "version": '2.0.0',
    "display_name": 'Define human resources policies Completeness Audit',
    "description": 'Audits define human resources policies records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-define-human-resources-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-human-resources-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c56ca562d432f324',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/define-human-resources-policies'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-define-human-resources-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditDefineHumanResourcesPolicies(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineHumanResourcesPolicies'
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
    print(AuditDefineHumanResourcesPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
