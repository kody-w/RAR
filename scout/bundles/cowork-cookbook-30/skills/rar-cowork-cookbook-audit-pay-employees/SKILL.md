---
name: "rar-cowork-cookbook-audit-pay-employees"
description: "Audits pay employees records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_pay_employees", "rar_sha256": "92374eb569a4920a7b95080cd54f4c3e0525c9261f8d87e86f1dd086d661a92b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_pay_employees_agent.py` and embedded as the fenced Python below (sha256 92374eb569a4920a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_pay_employees_agent.py` first:

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
    "version": '2.0.0',
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
