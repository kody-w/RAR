---
name: "rar-cowork-cookbook-audit-define-leasing-policies"
description: "Audits define leasing policies records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_leasing_policies", "rar_sha256": "35bda3ecf59bafea48615e03a97da22ffac60f4be318fbfcf2ce7c2cc1f89db1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_define_leasing_policies`. The original RAPP
agent is preserved byte-for-byte in `audit_define_leasing_policies_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_leasing_policies_agent.py` and embedded as the fenced Python below (sha256 35bda3ecf59bafea…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_leasing_policies_agent.py` first:

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
    "version": '2.0.1',
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
