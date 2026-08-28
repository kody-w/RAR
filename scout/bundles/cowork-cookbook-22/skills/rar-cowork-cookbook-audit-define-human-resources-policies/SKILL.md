---
name: "rar-cowork-cookbook-audit-define-human-resources-policies"
description: "Audits define human resources policies records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_human_resources_policies", "rar_sha256": "da5a0a9d16f665a3e6a52919bf8581e4f45edd05bfe5516a1768b4bfda2a22ab", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_define_human_resources_policies`. The original RAPP
agent is preserved byte-for-byte in `audit_define_human_resources_policies_agent.py` and in the RCI capsule.

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
