---
name: "rar-cowork-cookbook-audit-estimate-project-contracts"
description: "Audits estimate project contracts records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_estimate_project_contracts", "rar_sha256": "9291ad2563ae0a20df5ea6e33fa820dce555fef852dd444417bf79c0a5958da6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_estimate_project_contracts`. The original RAPP
agent is preserved byte-for-byte in `audit_estimate_project_contracts_agent.py` and in the RCI capsule.

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

Estimate project contracts Completeness Audit — Audits estimate project contracts records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-estimate-project-contracts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_estimate_project_contracts_agent.py` and embedded as the fenced Python below (sha256 9291ad2563ae0a20…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_estimate_project_contracts_agent.py` first:

```bash
python3 audit_estimate_project_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_estimate_project_contracts_agent.py   # or on stdin
python3 audit_estimate_project_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Estimate project contracts Completeness Audit — Audits estimate project contracts records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-estimate-project-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_estimate_project_contracts',
    "version": '2.0.0',
    "display_name": 'Estimate project contracts Completeness Audit',
    "description": 'Audits estimate project contracts records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-estimate-project-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-estimate-project-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '50308aa446e84715',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/estimate-project-contracts'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/audit-estimate-project-contracts', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditEstimateProjectContracts(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditEstimateProjectContracts'
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
    print(AuditEstimateProjectContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
