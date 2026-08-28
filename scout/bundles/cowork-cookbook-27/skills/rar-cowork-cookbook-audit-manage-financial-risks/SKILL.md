---
name: "rar-cowork-cookbook-audit-manage-financial-risks"
description: "Audits manage financial risks records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_financial_risks", "rar_sha256": "0ece59c657aac33ba6a76d140097d951e92f2f3dfed752af4d1b1c517cb4126f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_manage_financial_risks`. The original RAPP
agent is preserved byte-for-byte in `audit_manage_financial_risks_agent.py` and in the RCI capsule.

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

Manage financial risks Completeness Audit — Audits manage financial risks records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-financial-risks
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_financial_risks_agent.py` and embedded as the fenced Python below (sha256 0ece59c657aac33b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_financial_risks_agent.py` first:

```bash
python3 audit_manage_financial_risks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_manage_financial_risks_agent.py   # or on stdin
python3 audit_manage_financial_risks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage financial risks Completeness Audit — Audits manage financial risks records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-financial-risks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_manage_financial_risks',
    "version": '2.0.1',
    "display_name": 'Manage financial risks Completeness Audit',
    "description": 'Audits manage financial risks records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-manage-financial-risks',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-manage-financial-risks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd405a999bb6f57ae',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/manage-financial-risks'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/audit-manage-financial-risks', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditManageFinancialRisks(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditManageFinancialRisks'
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
    print(AuditManageFinancialRisks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
