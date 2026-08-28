---
name: "rar-cowork-cookbook-audit-perform-service-tasks"
description: "Audits perform service tasks records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_perform_service_tasks", "rar_sha256": "ad0881568b7ab3535038f2b1cc564cd23421461237f42c74a96a4a897561112a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_perform_service_tasks`. The original RAPP
agent is preserved byte-for-byte in `audit_perform_service_tasks_agent.py` and in the RCI capsule.

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

Perform service tasks Completeness Audit — Audits perform service tasks records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-perform-service-tasks
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_perform_service_tasks_agent.py` and embedded as the fenced Python below (sha256 ad0881568b7ab353…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_perform_service_tasks_agent.py` first:

```bash
python3 audit_perform_service_tasks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_perform_service_tasks_agent.py   # or on stdin
python3 audit_perform_service_tasks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform service tasks Completeness Audit — Audits perform service tasks records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-perform-service-tasks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_perform_service_tasks',
    "version": '2.0.0',
    "display_name": 'Perform service tasks Completeness Audit',
    "description": 'Audits perform service tasks records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-perform-service-tasks',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-perform-service-tasks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0b7e3ed2c596d569',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/perform-service-tasks'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/audit-perform-service-tasks', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditPerformServiceTasks(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPerformServiceTasks'
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
    print(AuditPerformServiceTasks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
