---
name: "rar-cowork-cookbook-bulk-update-plan-worker-retirement"
description: "Applies a bulk field update across plan worker retirement records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_worker_retirement", "rar_sha256": "7f3d4500e958776de15b663f1058a9fd400d42bcd259a24789e5b93249b7aa62", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_plan_worker_retirement`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_plan_worker_retirement_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_plan_worker_retirement_agent.py` and embedded as the fenced Python below (sha256 7f3d4500e958776d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_plan_worker_retirement_agent.py` first:

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
    "version": '2.0.1',
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
