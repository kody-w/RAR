---
name: "rar-cowork-cookbook-audit-define-leasing-policies"
description: "Audits define leasing policies records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_leasing_policies", "rar_sha256": "95083dece24cc3cd581927eadd4117cf19971527826fe0141f67aaeee6f9d965", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_define_leasing_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-define-leasing-policies:403c76fd2de9384fa04af3af4a9bdf8146c3a68704aefc83dd05fe2d01cd1bdf", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_define_leasing_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_define_leasing_policies_agent.py` is
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

Define leasing policies Completeness Audit — Audits define leasing policies records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-leasing-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_leasing_policies_agent.py` and embedded as the fenced Python below (sha256 95083dece24cc3cd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_leasing_policies_agent.py` first:

```bash
python3 audit_define_leasing_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_leasing_policies_agent.py   # or on stdin
python3 audit_define_leasing_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define leasing policies Completeness Audit — Audits define leasing policies records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-leasing-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_leasing_policies',
    "version": '2.0.0',
    "display_name": 'Define leasing policies Completeness Audit',
    "description": 'Audits define leasing policies records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'audit-define-leasing-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-leasing-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3808fd541868ad13',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/define-leasing-policies'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/audit-define-leasing-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditDefineLeasingPolicies(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineLeasingPolicies'
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
    print(AuditDefineLeasingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
