---
name: "rar-cowork-cookbook-audit-implement-process-governance"
description: "Audits implement process governance records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_implement_process_governance", "rar_sha256": "1281397cb133b512cad685cd913603b4ee1052fdc56bc7df423112d4fe4dfc5b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_implement_process_governance`. The original RAPP
agent is preserved byte-for-byte in `audit_implement_process_governance_agent.py` and in the RCI capsule.

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

Implement process governance Completeness Audit — Audits implement process governance records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-implement-process-governance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_implement_process_governance_agent.py` and embedded as the fenced Python below (sha256 1281397cb133b512…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_implement_process_governance_agent.py` first:

```bash
python3 audit_implement_process_governance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_implement_process_governance_agent.py   # or on stdin
python3 audit_implement_process_governance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement process governance Completeness Audit — Audits implement process governance records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-implement-process-governance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_implement_process_governance',
    "version": '2.0.1',
    "display_name": 'Implement process governance Completeness Audit',
    "description": 'Audits implement process governance records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-implement-process-governance',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-implement-process-governance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a31359a2132581f4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-03', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/implement-process-governance'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-implement-process-governance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.556, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditImplementProcessGovernance(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditImplementProcessGovernance'
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
    print(AuditImplementProcessGovernance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
