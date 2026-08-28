---
name: "rar-cowork-cookbook-audit-define-leasing-policies"
description: "Audits define leasing policies records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_leasing_policies", "rar_sha256": "95083dece24cc3cd581927eadd4117cf19971527826fe0141f67aaeee6f9d965", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
