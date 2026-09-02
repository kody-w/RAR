---
name: "rar-cowork-cookbook-bulk-update-plan-worker-retirement"
description: "Applies a bulk field update across plan worker retirement records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_worker_retirement", "rar_sha256": "18c8f1ee5fb1561fad731322354cddbd47ceafb400e69824942a10c87352028f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_plan_worker_retirement_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-plan-worker-retirement:4defacd9e90952ca9cb5678b61829226c016da88fb36c0e8326183019506316a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_plan_worker_retirement`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_plan_worker_retirement_agent.py` is
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

Plan worker retirement Bulk Field Update — Applies a bulk field update across plan worker retirement records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-worker-retirement
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_plan_worker_retirement_agent.py` and embedded as the fenced Python below (sha256 18c8f1ee5fb1561f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_plan_worker_retirement_agent.py` first:

```bash
python3 bulk_update_plan_worker_retirement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_plan_worker_retirement_agent.py   # or on stdin
python3 bulk_update_plan_worker_retirement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan worker retirement Bulk Field Update — Applies a bulk field update across plan worker retirement records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-worker-retirement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_plan_worker_retirement',
    "version": '2.0.0',
    "display_name": 'Plan worker retirement Bulk Field Update',
    "description": 'Applies a bulk field update across plan worker retirement records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-plan-worker-retirement',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-plan-worker-retirement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '306d4b8ff054086c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/offboard-talent/plan-worker-retirement'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/bulk-update-plan-worker-retirement', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdatePlanWorkerRetirement(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePlanWorkerRetirement'
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
    print(BulkUpdatePlanWorkerRetirement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
