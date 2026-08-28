---
name: "rar-cowork-cookbook-audit-develop-program-charter"
description: "Audits develop program charter records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_program_charter", "rar_sha256": "ebbf3f693693d39a57587691e8481f9bd16008950dd2a8da3058584d07f04e57", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_develop_program_charter`. The original RAPP
agent is preserved byte-for-byte in `audit_develop_program_charter_agent.py` and in the RCI capsule.

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

Develop program charter Completeness Audit — Audits develop program charter records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-program-charter
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_program_charter_agent.py` and embedded as the fenced Python below (sha256 ebbf3f693693d39a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_program_charter_agent.py` first:

```bash
python3 audit_develop_program_charter_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_program_charter_agent.py   # or on stdin
python3 audit_develop_program_charter_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop program charter Completeness Audit — Audits develop program charter records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-program-charter
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_program_charter',
    "version": '2.0.1',
    "display_name": 'Develop program charter Completeness Audit',
    "description": 'Audits develop program charter records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-develop-program-charter',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-program-charter',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8b4695453f491a85',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/develop-project-strategy/develop-program-charter'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/audit-develop-program-charter', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditDevelopProgramCharter(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopProgramCharter'
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
    print(AuditDevelopProgramCharter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
