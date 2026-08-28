---
name: "rar-cowork-cookbook-audit-define-costing-policies"
description: "Audits define costing policies records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_costing_policies", "rar_sha256": "0443e8d8ab45475a3245a6fea6f6d59b900d6a13d73bd220c5e89d61a09a04be", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_costing_policies_agent.py` and embedded as the fenced Python below (sha256 0443e8d8ab45475a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_costing_policies_agent.py` first:

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
    "version": '2.0.0',
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
