---
name: "rar-cowork-cookbook-audit-estimate-project-contracts"
description: "Audits estimate project contracts records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_estimate_project_contracts", "rar_sha256": "6a23f7f7671ceb2382a69aa11ae2dc7932e51d2f466238bb59adb382e0a74b08", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_estimate_project_contracts_agent.py` and embedded as the fenced Python below (sha256 6a23f7f7671ceb23…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_estimate_project_contracts_agent.py` first:

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
    "version": '2.0.1',
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
