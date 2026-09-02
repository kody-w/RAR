---
name: "rar-cowork-cookbook-bulk-update-develop-a-disaster-recovery-plan"
description: "Applies a bulk field update across develop a disaster recovery plan records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_a_disaster_recovery_plan", "rar_sha256": "f1975161d4148b7fd0c488b6c96b9fb0107264cabeb9fa917a00b894f8d430e0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_develop_a_disaster_recovery_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-develop-a-disaster-recovery-plan:702e4d94f27cce154a7fa6c9283ced698496883a355ec9edc6511ac1e4a1dcb9", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_develop_a_disaster_recovery_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_develop_a_disaster_recovery_plan_agent.py` is
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

Develop a disaster recovery plan Bulk Field Update — Applies a bulk field update across develop a disaster recovery plan records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-a-disaster-recovery-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_a_disaster_recovery_plan_agent.py` and embedded as the fenced Python below (sha256 f1975161d4148b7f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_a_disaster_recovery_plan_agent.py` first:

```bash
python3 bulk_update_develop_a_disaster_recovery_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_develop_a_disaster_recovery_plan_agent.py   # or on stdin
python3 bulk_update_develop_a_disaster_recovery_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop a disaster recovery plan Bulk Field Update — Applies a bulk field update across develop a disaster recovery plan records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-a-disaster-recovery-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_develop_a_disaster_recovery_plan',
    "version": '2.0.0',
    "display_name": 'Develop a disaster recovery plan Bulk Field Update',
    "description": 'Applies a bulk field update across develop a disaster recovery plan records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-develop-a-disaster-recovery-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-develop-a-disaster-recovery-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6c336ff9fa34a3ec',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/develop-a-disaster-recovery-plan'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-develop-a-disaster-recovery-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateDevelopADisasterRecoveryPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDevelopADisasterRecoveryPlan'
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
    print(BulkUpdateDevelopADisasterRecoveryPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
