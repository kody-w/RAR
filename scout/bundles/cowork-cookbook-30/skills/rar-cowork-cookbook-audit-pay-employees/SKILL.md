---
name: "rar-cowork-cookbook-audit-pay-employees"
description: "Audits pay employees records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_pay_employees", "rar_sha256": "a27795bf10b769e0aca5a2db6f0f64d52b81ebb5e331a8d10b0237379afc8cf0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_pay_employees`. The original RAPP
agent is preserved byte-for-byte in `audit_pay_employees_agent.py` and in the RCI capsule.

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

Pay employees Completeness Audit — Audits pay employees records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-pay-employees
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_pay_employees_agent.py` and embedded as the fenced Python below (sha256 a27795bf10b769e0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_pay_employees_agent.py` first:

```bash
python3 audit_pay_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_pay_employees_agent.py   # or on stdin
python3 audit_pay_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pay employees Completeness Audit — Audits pay employees records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-pay-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_pay_employees',
    "version": '2.0.1',
    "display_name": 'Pay employees Completeness Audit',
    "description": 'Audits pay employees records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-pay-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-pay-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd82163f2d0fcfd87',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/pay-employees'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-pay-employees', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditPayEmployees(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPayEmployees'
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
    print(AuditPayEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
