---
name: "rar-cowork-cookbook-bulk-update-plan-worker-retirement"
description: "Applies a bulk field update across plan worker retirement records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_worker_retirement", "rar_sha256": "18c8f1ee5fb1561fad731322354cddbd47ceafb400e69824942a10c87352028f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
