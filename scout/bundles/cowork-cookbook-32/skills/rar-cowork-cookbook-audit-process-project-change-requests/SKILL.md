---
name: "rar-cowork-cookbook-audit-process-project-change-requests"
description: "Audits process project change requests records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_process_project_change_requests", "rar_sha256": "b7b2d5daec4da30b7ce23fd73f27a81a0905ac88440b7306a7e76f5c826343d0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_process_project_change_requests_agent.py` and embedded as the fenced Python below (sha256 b7b2d5daec4da30b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_process_project_change_requests_agent.py` first:

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
    "version": '2.0.0',
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
