---
name: "rar-cowork-cookbook-audit-consume-resources"
description: "Audits consume resources records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_consume_resources", "rar_sha256": "95b546ba288e84db3477ec284397b916cb9fefb8a886d501d78827b19a7400ed", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_consume_resources_agent.py` and embedded as the fenced Python below (sha256 95b546ba288e84db…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_consume_resources_agent.py` first:

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
    "version": '2.0.0',
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
