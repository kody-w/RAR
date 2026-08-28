---
name: "rar-cowork-cookbook-audit-onboard-new-employees"
description: "Audits onboard new employees records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_onboard_new_employees", "rar_sha256": "af3a795f5c1c5d53d868a79017c8d75e55748a364ee4f3997e13880551fcaea2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_onboard_new_employees_agent.py` and embedded as the fenced Python below (sha256 af3a795f5c1c5d53…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_onboard_new_employees_agent.py` first:

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
    "version": '2.0.0',
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
