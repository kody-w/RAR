---
name: "rar-cowork-cookbook-audit-process-change-requests"
description: "Audits process change requests records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_process_change_requests", "rar_sha256": "5940aeda5867dff8286f95e68efeac5e0d31ce84bc5fb287d97bd93a613cf8ca", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_process_change_requests_agent.py` and embedded as the fenced Python below (sha256 5940aeda5867dff8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_process_change_requests_agent.py` first:

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
    "version": '2.0.0',
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
