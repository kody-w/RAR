---
name: "rar-cowork-cookbook-audit-perform-service-tasks"
description: "Audits perform service tasks records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_perform_service_tasks", "rar_sha256": "ad0881568b7ab3535038f2b1cc564cd23421461237f42c74a96a4a897561112a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_perform_service_tasks_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-perform-service-tasks:1b22703eb12da801012e22f28c259e0693fce71987420fc8a065912b5298f284", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_perform_service_tasks`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_perform_service_tasks_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
