---
name: "rar-cowork-cookbook-scheduled-brief-plan-workforce"
description: "Schedulable morning-brief email summarizing plan workforce for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_workforce", "rar_sha256": "54d022a3b9a5806f6f40245fa8dae8d7bfc4bff95747b64be4741a9e8c9ae8e9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_plan_workforce_agent.py` and embedded as the fenced Python below (sha256 54d022a3b9a5806f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_plan_workforce_agent.py` first:

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
    "version": '2.0.1',
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
