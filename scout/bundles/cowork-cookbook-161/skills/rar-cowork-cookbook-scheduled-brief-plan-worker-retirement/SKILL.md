---
name: "rar-cowork-cookbook-scheduled-brief-plan-worker-retirement"
description: "Schedulable morning-brief email summarizing plan worker retirement for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_worker_retirement", "rar_sha256": "e56b2869ccfc5c1397f8abbdcb401e84589b91d4d83bbc765b6205839d9d4d5e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_plan_worker_retirement`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_plan_worker_retirement_agent.py` and in the RCI capsule.

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

Plan worker retirement Scheduled Email Brief — Schedulable morning-brief email summarizing plan worker retirement for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-worker-retirement
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_plan_worker_retirement_agent.py` and embedded as the fenced Python below (sha256 e56b2869ccfc5c13…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_plan_worker_retirement_agent.py` first:

```bash
python3 scheduled_brief_plan_worker_retirement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_plan_worker_retirement_agent.py   # or on stdin
python3 scheduled_brief_plan_worker_retirement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan worker retirement Scheduled Email Brief — Schedulable morning-brief email summarizing plan worker retirement for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-worker-retirement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_plan_worker_retirement',
    "version": '2.0.1',
    "display_name": 'Plan worker retirement Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing plan worker retirement for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-plan-worker-retirement',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-plan-worker-retirement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a89cca683f4e5bf3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/offboard-talent/plan-worker-retirement'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-plan-worker-retirement', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefPlanWorkerRetirement(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPlanWorkerRetirement'
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
    print(ScheduledBriefPlanWorkerRetirement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
