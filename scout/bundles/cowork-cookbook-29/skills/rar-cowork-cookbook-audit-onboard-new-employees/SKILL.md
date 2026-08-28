---
name: "rar-cowork-cookbook-audit-onboard-new-employees"
description: "Audits onboard new employees records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_onboard_new_employees", "rar_sha256": "5e996bcefe35bba48d4b6fba6fd8560ed5b11e5be14d8f343ed1a49bd3ab05b8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_onboard_new_employees`. The original RAPP
agent is preserved byte-for-byte in `audit_onboard_new_employees_agent.py` and in the RCI capsule.

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

Onboard new employees Completeness Audit — Audits onboard new employees records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-onboard-new-employees
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_onboard_new_employees_agent.py` and embedded as the fenced Python below (sha256 5e996bcefe35bba4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_onboard_new_employees_agent.py` first:

```bash
python3 audit_onboard_new_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_onboard_new_employees_agent.py   # or on stdin
python3 audit_onboard_new_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard new employees Completeness Audit — Audits onboard new employees records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-onboard-new-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_onboard_new_employees',
    "version": '2.0.1',
    "display_name": 'Onboard new employees Completeness Audit',
    "description": 'Audits onboard new employees records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-onboard-new-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-onboard-new-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a25eeee8249c0223',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/onboard-new-employees'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-onboard-new-employees', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditOnboardNewEmployees(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditOnboardNewEmployees'
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
    print(AuditOnboardNewEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
