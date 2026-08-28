---
name: "rar-cowork-cookbook-audit-appropriate-budgets"
description: "Audits appropriate budgets records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_appropriate_budgets", "rar_sha256": "76d7092b26937a62b435c77e665824ac3808161c925615048ff13d38f7f960e8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_appropriate_budgets`. The original RAPP
agent is preserved byte-for-byte in `audit_appropriate_budgets_agent.py` and in the RCI capsule.

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

Appropriate budgets Completeness Audit — Audits appropriate budgets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-appropriate-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_appropriate_budgets_agent.py` and embedded as the fenced Python below (sha256 76d7092b26937a62…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_appropriate_budgets_agent.py` first:

```bash
python3 audit_appropriate_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_appropriate_budgets_agent.py   # or on stdin
python3 audit_appropriate_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Appropriate budgets Completeness Audit — Audits appropriate budgets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-appropriate-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_appropriate_budgets',
    "version": '2.0.1',
    "display_name": 'Appropriate budgets Completeness Audit',
    "description": 'Audits appropriate budgets records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-appropriate-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-appropriate-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '408e0714ec63e932',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/appropriate-budgets'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-appropriate-budgets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditAppropriateBudgets(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAppropriateBudgets'
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
    print(AuditAppropriateBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
