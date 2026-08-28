---
name: "rar-cowork-cookbook-audit-process-project-change-requests"
description: "Audits process project change requests records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_process_project_change_requests", "rar_sha256": "ff551b361cc1a57cf5a9b1bfc1cc21b5487a9dec869bca8b34f3b78022b2c4cd", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_process_project_change_requests`. The original RAPP
agent is preserved byte-for-byte in `audit_process_project_change_requests_agent.py` and in the RCI capsule.

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

Process project change requests Completeness Audit — Audits process project change requests records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-project-change-requests
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_process_project_change_requests_agent.py` and embedded as the fenced Python below (sha256 ff551b361cc1a57c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_process_project_change_requests_agent.py` first:

```bash
python3 audit_process_project_change_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_process_project_change_requests_agent.py   # or on stdin
python3 audit_process_project_change_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process project change requests Completeness Audit — Audits process project change requests records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-project-change-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_process_project_change_requests',
    "version": '2.0.1',
    "display_name": 'Process project change requests Completeness Audit',
    "description": 'Audits process project change requests records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-process-project-change-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-process-project-change-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '28c9dbee38784100',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/process-project-change-requests'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/audit-process-project-change-requests', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditProcessProjectChangeRequests(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditProcessProjectChangeRequests'
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
    print(AuditProcessProjectChangeRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
