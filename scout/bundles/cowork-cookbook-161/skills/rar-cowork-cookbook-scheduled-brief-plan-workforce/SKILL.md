---
name: "rar-cowork-cookbook-scheduled-brief-plan-workforce"
description: "Schedulable morning-brief email summarizing plan workforce for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_workforce", "rar_sha256": "8dedbbf5fd94b33941f33e4a19df9bc8f8c64a9fc4389c95ffdff19312ad25a7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_plan_workforce`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_plan_workforce_agent.py` and in the RCI capsule.

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

Plan workforce Scheduled Email Brief — Schedulable morning-brief email summarizing plan workforce for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-workforce
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_plan_workforce_agent.py` and embedded as the fenced Python below (sha256 8dedbbf5fd94b339…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_plan_workforce_agent.py` first:

```bash
python3 scheduled_brief_plan_workforce_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_plan_workforce_agent.py   # or on stdin
python3 scheduled_brief_plan_workforce_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan workforce Scheduled Email Brief — Schedulable morning-brief email summarizing plan workforce for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-workforce
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_plan_workforce',
    "version": '2.0.0',
    "display_name": 'Plan workforce Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing plan workforce for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-plan-workforce',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-plan-workforce',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '58eb8ea1e0c7f701',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/plan-workforce'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-plan-workforce', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefPlanWorkforce(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPlanWorkforce'
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
    print(ScheduledBriefPlanWorkforce().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
