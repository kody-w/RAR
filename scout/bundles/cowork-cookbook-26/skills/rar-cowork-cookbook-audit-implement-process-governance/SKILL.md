---
name: "rar-cowork-cookbook-audit-implement-process-governance"
description: "Audits implement process governance records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_implement_process_governance", "rar_sha256": "72854e1589df2791f3600aa40891644d6c3cf287dc71db3dfa36f1a100d90395", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_implement_process_governance_agent.py` and embedded as the fenced Python below (sha256 72854e1589df2791…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_implement_process_governance_agent.py` first:

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
    "version": '2.0.0',
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
