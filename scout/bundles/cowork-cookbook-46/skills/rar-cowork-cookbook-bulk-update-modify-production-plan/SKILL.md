---
name: "rar-cowork-cookbook-bulk-update-modify-production-plan"
description: "Applies a bulk field update across modify production plan records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_modify_production_plan", "rar_sha256": "03edfa94ed654ec6253359d593b4612dfe51ab88d9083caaa800f20e8e4304f6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_modify_production_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-modify-production-plan:60728b38e60a74916e300babd67fe8be57fe02fd78c1a05fafebd3def44d8cc0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_modify_production_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_modify_production_plan_agent.py` is
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

Modify production plan Bulk Field Update — Applies a bulk field update across modify production plan records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-modify-production-plan
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_modify_production_plan_agent.py` and embedded as the fenced Python below (sha256 03edfa94ed654ec6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_modify_production_plan_agent.py` first:

```bash
python3 bulk_update_modify_production_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_modify_production_plan_agent.py   # or on stdin
python3 bulk_update_modify_production_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Modify production plan Bulk Field Update — Applies a bulk field update across modify production plan records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-modify-production-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_modify_production_plan',
    "version": '2.0.0',
    "display_name": 'Modify production plan Bulk Field Update',
    "description": 'Applies a bulk field update across modify production plan records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-modify-production-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-modify-production-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '943e16fabaa17b82',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/modify-production-plan'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/bulk-update-modify-production-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateModifyProductionPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateModifyProductionPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(BulkUpdateModifyProductionPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
