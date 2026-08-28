---
name: "rar-cowork-cookbook-audit-consume-resources"
description: "Audits consume resources records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_consume_resources", "rar_sha256": "b987c554f0f5237aec39dbf6e70d0b7155ebb6bf8031b4995e50dfe71e25322b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_consume_resources`. The original RAPP
agent is preserved byte-for-byte in `audit_consume_resources_agent.py` and in the RCI capsule.

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

Consume resources Completeness Audit — Audits consume resources records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-consume-resources
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_consume_resources_agent.py` and embedded as the fenced Python below (sha256 b987c554f0f5237a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_consume_resources_agent.py` first:

```bash
python3 audit_consume_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_consume_resources_agent.py   # or on stdin
python3 audit_consume_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Consume resources Completeness Audit — Audits consume resources records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-consume-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_consume_resources',
    "version": '2.0.1',
    "display_name": 'Consume resources Completeness Audit',
    "description": 'Audits consume resources records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-consume-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-consume-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '576054b7cbd21f15',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/consume-resources'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/audit-consume-resources', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditConsumeResources(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditConsumeResources'
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
    print(AuditConsumeResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
