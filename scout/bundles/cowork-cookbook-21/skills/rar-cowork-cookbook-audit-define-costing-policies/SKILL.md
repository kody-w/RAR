---
name: "rar-cowork-cookbook-audit-define-costing-policies"
description: "Audits define costing policies records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_costing_policies", "rar_sha256": "2a4c0e19579859918fe5dc007861f7c95241fe0af6a39e3202b6ee42b467aa7b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_define_costing_policies`. The original RAPP
agent is preserved byte-for-byte in `audit_define_costing_policies_agent.py` and in the RCI capsule.

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

Define costing policies Completeness Audit — Audits define costing policies records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-costing-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_costing_policies_agent.py` and embedded as the fenced Python below (sha256 2a4c0e1957985991…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_costing_policies_agent.py` first:

```bash
python3 audit_define_costing_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_costing_policies_agent.py   # or on stdin
python3 audit_define_costing_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define costing policies Completeness Audit — Audits define costing policies records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-costing-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_costing_policies',
    "version": '2.0.1',
    "display_name": 'Define costing policies Completeness Audit',
    "description": 'Audits define costing policies records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-define-costing-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-costing-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b9021fd9bed64061',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/define-costing-policies'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-define-costing-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditDefineCostingPolicies(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineCostingPolicies'
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
    print(AuditDefineCostingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
