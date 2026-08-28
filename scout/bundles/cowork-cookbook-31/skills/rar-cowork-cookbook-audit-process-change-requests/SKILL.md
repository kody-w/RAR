---
name: "rar-cowork-cookbook-audit-process-change-requests"
description: "Audits process change requests records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_process_change_requests", "rar_sha256": "40fd84b7052d824930077d79c24d209274ea6b7c82aafdd4c2d30e8a1434ff70", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_process_change_requests`. The original RAPP
agent is preserved byte-for-byte in `audit_process_change_requests_agent.py` and in the RCI capsule.

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

Process change requests Completeness Audit — Audits process change requests records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-change-requests
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_process_change_requests_agent.py` and embedded as the fenced Python below (sha256 40fd84b7052d8249…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_process_change_requests_agent.py` first:

```bash
python3 audit_process_change_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_process_change_requests_agent.py   # or on stdin
python3 audit_process_change_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process change requests Completeness Audit — Audits process change requests records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-change-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_process_change_requests',
    "version": '2.0.1',
    "display_name": 'Process change requests Completeness Audit',
    "description": 'Audits process change requests records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-process-change-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-process-change-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6cf88f43316b4a84',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/process-change-requests'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/audit-process-change-requests', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditProcessChangeRequests(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditProcessChangeRequests'
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
    print(AuditProcessChangeRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
