---
name: "rar-cowork-cookbook-audit-develop-program-charter"
description: "Audits develop program charter records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_program_charter", "rar_sha256": "41636a364707b4f807320da54e77fcf0d1545d020b0e0434e077bbbb3c96bfe3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_program_charter_agent.py` and embedded as the fenced Python below (sha256 41636a364707b4f8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_program_charter_agent.py` first:

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
    "version": '2.0.0',
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
